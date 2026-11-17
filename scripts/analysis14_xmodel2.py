import os
RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'raw')
# v14: cross-model check of full-text coding (30 random defenses re-coded by claude-sonnet-5-5) and
# full-text adjudication of the 8 screening disagreements found by the cross-model screening check.
import json, csv, re, math
C = {c['id']: c for c in json.load(open(os.path.join(RAW, 'FINAL_CORPUS.json')))}
KEY = json.load(open(os.path.join(RAW, 'xmodel2', 'xmodel2_KEY_ft.json')))
rows = []
for k in (1, 2, 3): rows += list(csv.DictReader(open(os.path.join(RAW, 'xmodel2', 'ft_out_%d.tsv' % k)), delimiter='\t'))
assert len(rows) == 30
def LL(x): return [] if x in (None, '', '-', '?') else [y.strip() for y in re.split(r'[;,]', x) if y.strip() and y.strip() not in ('-', '?')]
def unk(x): return x is None or x.strip() in ('', '?')
def kappa(pairs):
    n = len(pairs)
    if n == 0: return None
    a = sum(x == y for x, y in pairs) / n
    p1 = sum(x for x, _ in pairs) / n; p2 = sum(y for _, y in pairs) / n
    pe = p1 * p2 + (1 - p1) * (1 - p2)
    k = 1.0 if pe == 1 and a == 1 else (a - pe) / (1 - pe) if pe < 1 else 0.0
    return dict(n=n, po=round(a, 2), kappa=round(k, 2), pos_final=sum(x for x, _ in pairs), pos_other=sum(y for _, y in pairs), disagree=sum(x != y for x, y in pairs))
items = {}
def add(name, f, g, cond=lambda c, r: True):
    ps = []
    for r in rows:
        c = C[KEY[r['rid']]]
        if not cond(c, r): continue
        x, y = f(c), g(r)
        if x is None or y is None: continue
        ps.append((int(x), int(y)))
    items[name] = kappa(ps)
for s in 'IPMAOC':
    add('stage:' + s, lambda c, s=s: None if unk(c['ft_stage']) else s in LL(c['ft_stage']), lambda r, s=s: None if unk(r['stage']) else s in LL(r['stage']))
pre = lambda st, m: None if unk(st) else ('A' in LL(st) and (m or '').strip().lower().startswith('pre'))
add('A_pre', lambda c: pre(c['ft_stage'], c['ft_A_mode']), lambda r: pre(r['stage'], r['A_mode']))
for j in ('SEP', 'SELF', 'ML', 'RULE', 'HUMAN'):
    add('judge:' + j, lambda c, j=j: None if unk(c['ft_judge']) else j in LL(c['ft_judge']), lambda r, j=j: None if unk(r['judge']) else j in LL(r['judge']))
llm = lambda x: None if unk(x) else ('SEP' in LL(x) or 'SELF' in LL(x))
add('llm_dependent', lambda c: llm(c['ft_judge']), lambda r: llm(r['judge']))
sraw = lambda j, i: None if unk(j) else ('SEP' in LL(j) and (i or '').strip() == 'RAW')
add('sep_raw', lambda c: sraw(c['ft_judge'], c.get('ft_judge_input')), lambda r: sraw(r['judge'], r['judge_input']))
both_sep = lambda c, r: 'SEP' in LL(c['ft_judge']) and 'SEP' in LL(r['judge']) and (c.get('ft_judge_input') or '') in ('RAW', 'DERIVED', 'TRUSTED') and r['judge_input'].strip() in ('RAW', 'DERIVED', 'TRUSTED')
add('judge_input_RAW|both_SEP', lambda c: c['ft_judge_input'] == 'RAW', lambda r: r['judge_input'].strip() == 'RAW', both_sep)
yn = lambda x: None if unk(x) or x.strip()[0].upper() not in 'YN' else x.strip()[0].upper() == 'Y'
add('adversarial', lambda c: yn(c['ft_adversarial']), lambda r: yn(r['adversarial']))
ad = lambda x: None if unk(x) or x.strip().upper() == 'NA' else x.strip()[0] in '12'
both_adv = lambda c, r: yn(c['ft_adversarial']) and yn(r['adversarial'])
add('adaptive|both_adv', lambda c: ad(c['ft_adaptive']), lambda r: ad(r['adaptive']), both_adv)
for a, b in (('public_bench', 'ft_public_bench'), ('utility', 'ft_utility'), ('overhead', 'ft_overhead'), ('fpr', 'ft_fpr')):
    add(a, lambda c, b=b: yn(c[b]), lambda r, a=a: yn(r[a]))
core = ['stage:A', 'A_pre', 'judge:SEP', 'llm_dependent', 'sep_raw', 'adversarial', 'adaptive|both_adv']
ks = sorted(v['kappa'] for v in items.values() if v and v['pos_final'] + v['pos_other'] > 0)
# share comparison on the same 30 papers
def share(name): v = items[name]; return [v['pos_final'], v['pos_other'], v['n']]
# full-text adjudication of the 8 screening disagreements
ks_ = json.load(open(os.path.join(RAW, 'xmodel', 'KEY_screen.json')))
adj = {}
for m in ('opus', 'sonnet'):
    for r in csv.DictReader(open(os.path.join(RAW, 'xmodel2', 'adj8_out_%s.tsv' % m)), delimiter='\t'):
        adj.setdefault(r['id'], {})[m] = r['decision'].strip().upper()[:3]
exc7 = [i for i in adj if not ks_[i]['final_inc']]; inc1 = [i for i in adj if ks_[i]['final_inc']]
both_inc = [i for i in exc7 if adj[i]['opus'] == 'INC' and adj[i]['sonnet'] == 'INC']
both_exc = [i for i in exc7 if adj[i]['opus'] == 'EXC' and adj[i]['sonnet'] == 'EXC']
split = [i for i in exc7 if i not in both_inc and i not in both_exc]
def wil(k, n, z=1.96):
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n); h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return [round(100 * (c - h) / d, 1), round(100 * (c + h) / d, 1)]
n_exc = sum(not v['final_inc'] for v in ks_.values())
M = json.load(open(os.path.join(RAW, 'MASTER_SCREEN_base.json'))); S = json.load(open(os.path.join(RAW, 'STATS10.json')))
p1_total = sum(m['path'] in ('V2', 'V3') for m in M); p1_inc = sum(1 for c in C.values() if c['route'] == 'V')
# supplementary sample for the adaptive-evaluation item: the 15 remaining defenses coded as adaptively evaluated plus 9 random negatives (seed 20261004)
K2 = json.load(open(os.path.join(RAW, 'xmodel2', 'xmodel2_KEY_ft2.json'))); rows2 = []
for k in (4, 5): rows2 += list(csv.DictReader(open(os.path.join(RAW, 'xmodel2', 'ft_out_%d.tsv' % k)), delimiter='\t'))
assert len(rows2) == 24
pairs = []
for r, key in [(r, KEY) for r in rows] + [(r, K2) for r in rows2]:
    c = C[key[r['rid']]]
    if not (yn(c['ft_adversarial']) and yn(r['adversarial'])): continue
    x, y = ad(c['ft_adaptive']), ad(r['adaptive'])
    if x is None or y is None: continue
    pairs.append((int(x), int(y)))
adp = dict(n=len(pairs), final_pos=sum(x for x, _ in pairs), final_pos_other_pos=sum(x and y for x, y in pairs), final_neg=sum(1 - x for x, _ in pairs), final_neg_other_pos=sum((1 - x) and y for x, y in pairs),
           level_agree_suppl=sum(C[K2[r['rid']]]['ft_adaptive'] == r['adaptive'].strip() for r in rows2), n_suppl=len(rows2), suppl_pos=sum(C[K2[r['rid']]]['ft_adaptive'] in ('1', '2') for r in rows2))
ji = items['judge_input_RAW|both_SEP']
out = dict(model='claude-sonnet-5-5', n=30, seed=20261003, frame=85, items=items, core={k: items[k] for k in core},
           adaptive_all=adp, judge_input_both_sep=ji, all_min=ks[0], all_max=ks[-1], all_median=ks[len(ks) // 2] if len(ks) % 2 else round((ks[len(ks) // 2 - 1] + ks[len(ks) // 2]) / 2, 2), n_items=len(ks),
           adj=dict(n=len(adj), final_exc=len(exc7), both_inc=len(both_inc), both_exc=len(both_exc), split=len(split), final_inc_kept=sum(adj[i]['opus'] == 'INC' and adj[i]['sonnet'] == 'INC' for i in inc1),
                    sample_final_exc=n_exc, miss_pct=round(100 * len(both_inc) / n_exc, 1), miss_ci=wil(len(both_inc), n_exc),
                    path1_candidates=p1_total, path1_included=p1_inc, path1_excluded=p1_total - p1_inc,
                    est=round(len(both_inc) / n_exc * (p1_total - p1_inc)), est_ci=[round(w / 100 * (p1_total - p1_inc)) for w in wil(len(both_inc), n_exc)],
                    hi=len(both_inc) + len(split), hi_pct=round(100 * (len(both_inc) + len(split)) / n_exc, 1), hi_ci=wil(len(both_inc) + len(split), n_exc), hi_est=round((len(both_inc) + len(split)) / n_exc * (p1_total - p1_inc)),
                    hi_est_ci=[round(w / 100 * (p1_total - p1_inc)) for w in wil(len(both_inc) + len(split), n_exc)],
                    share_lo=round(100 * round(len(both_inc) / n_exc * (p1_total - p1_inc)) / p1_inc), share_hi=round(100 * round((len(both_inc) + len(split)) / n_exc * (p1_total - p1_inc)) / p1_inc),
                    split_main_model=[adj[i]['opus'] for i in split],
                    detail={i: adj[i] for i in adj}))
json.dump(out, open(os.path.join(RAW, 'XMODEL14b.json'), 'w'), ensure_ascii=False, indent=1)
for k, v in items.items(): print(k, v)
print({k: out[k] for k in ('all_min', 'all_max', 'all_median', 'n_items')}); print(out['adj']); print(adp)
