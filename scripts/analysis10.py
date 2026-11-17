import os
RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'raw')
# -*- coding: utf-8 -*-
"""Single source of truth for every number reported in the manuscript (v10).
Inputs: MASTER_SCREEN_base.json (pass A), SCREEN_B*.tsv + pb/pb*_B.tsv (pass B), ADJ_SCREEN*.tsv (adjudication),
final_codes.json / FINAL_CORPUS.json (coding), CA/CB*.tsv (abstract dual coding), FT*/FT2* (full text)."""
import json, csv, math, re, collections
from math import comb
import os
W = RAW + os.sep
S = collections.OrderedDict()
def L(s): return [] if s in (None, '', '-', '?') else [x.strip() for x in re.split(r'[;,]', s) if x.strip() and x.strip() not in ('-', '?')]
def wilson(k, n, z=1.96):
    if n == 0: return (None, None)
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n); h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (round(100 * (c - h) / d), round(100 * (c + h) / d))
def pct(k, n): return round(100 * k / n) if n else None
def kappa_bin(a, b):
    n = len(a); po = sum(x == y for x, y in zip(a, b)) / n
    pa = sum(a) / n; pb = sum(b) / n; pe = pa * pb + (1 - pa) * (1 - pb)
    k = (po - pe) / (1 - pe) if pe < 1 else 1.0
    return dict(n=n, po=round(po, 3), kappa=round(k, 2), pabak=round(2 * po - 1, 2), pos1=sum(a), pos2=sum(b))
def fisher(a, b, c, d):  # two-sided Fisher exact for 2x2 [[a,b],[c,d]]
    n = a + b + c + d; r1 = a + b; c1 = a + c
    def p(x): return comb(r1, x) * comb(n - r1, c1 - x) / comb(n, c1)
    p0 = p(a); lo = max(0, c1 - (n - r1)); hi = min(r1, c1)
    return round(sum(p(x) for x in range(lo, hi + 1) if p(x) <= p0 + 1e-12), 3)
def tsv(f): return list(csv.DictReader(open(W + f), delimiter='\t'))

# ---------------- screening ----------------
M = json.load(open(W + 'MASTER_SCREEN_base.json'))
B = {}
for f in ['SCREEN_B.tsv', 'SCREEN_B2.tsv'] + ['pb/pb%d_B.tsv' % i for i in range(1, 7)]:
    for r in tsv(f): B[r['id']] = r
ADJ = {}
for r in tsv('ADJ_SCREEN.tsv'): ADJ[r['id_or_title'].split(' ')[0].rstrip(';')] = (r['final_decision'], r['exc_reason'])
for r in tsv('ADJ_SCREEN2.tsv'): ADJ[r['id']] = (r['final_decision'], r['exc_reason'])
scr = {}
for p in ['ALL', 'V2', 'V3', 'SEC']:
    sub = [m for m in M if p == 'ALL' or m['path'] == p]
    a = [m['A'] == 'INC' for m in sub]; b = [B[m['id']]['decision'] == 'INC' for m in sub]
    k = kappa_bin(a, b); k['AiBe'] = sum(x and not y for x, y in zip(a, b)); k['AeBi'] = sum(y and not x for x, y in zip(a, b)); k['both_inc'] = sum(x and y for x, y in zip(a, b))
    scr[p] = k
S['screen_kappa'] = scr
dis = [m for m in M if m['A'] != B[m['id']]['decision']]
S['screen_disagreements'] = len(dis)
S['dis_not_adj_forwarded']=[m['id'] for m in dis if m['id'] not in ADJ]  # forwarded to eligibility (coding stage)
FINAL = json.load(open(W + 'final_codes.json'))
coding_exc = {i for i, c in FINAL.items() if c['decision'] == 'EXC'}
def screen_final(m):
    if m['id'] in ADJ: return ADJ[m['id']]
    if m['A'] != B[m['id']]['decision']: return ('INC', 'forwarded')
    return (m['A'], m['A_reason'])
fin_scr = {m['id']: screen_final(m) for m in M}
inc_screen = [i for i, (d, _) in fin_scr.items() if d == 'INC']
S['screen_inc'] = len(inc_screen)
S['adj_dis_outcome'] = collections.Counter(fin_scr[m['id']][0] + ('(A)' if fin_scr[m['id']][0] == m['A'] else '(B)') for m in dis)
exc_reasons = collections.Counter(r for i, (d, r) in fin_scr.items() if d == 'EXC')
S['screen_exc'] = len(M) - len(inc_screen); S['screen_exc_reasons'] = dict(exc_reasons.most_common())
S['coding_stage_exc'] = sorted(i for i in coding_exc if i in fin_scr or i.startswith('S'))
S['coding_stage_exc_reasons'] = {i: FINAL[i].get('exc_reason', FINAL[i].get('note', ''))[:60] for i in coding_exc}
# snowball
sb = json.load(open(W + 'pb/snowball13.json'))
S['snowball'] = dict(candidates=len(sb), inc=sum(s['final'] == 'INC' for s in sb), passB_agree=sum(s['final'] == B[s['id']]['decision'] for s in sb))

# ---------------- corpus ----------------
C = json.load(open(W + 'FINAL_CORPUS.json'))
N = len(C); S['N'] = N
S['route'] = dict(collections.Counter(c['route'] for c in C))
S['year'] = dict(sorted(collections.Counter(c['year'] for c in C).items()))
cnt = lambda key, pool: dict(collections.Counter(x for c in pool for x in L(c[key])).most_common())
S['type'] = cnt('type', C); S['actor'] = cnt('actor', C); S['T'] = cnt('T', C); S['viol'] = cnt('viol', C)
S['T5sub'] = cnt('T5sub', [c for c in C if 'T5' in L(c['T'])])
ms = [c for c in C if c['multistage'] == 'Y']
S['multistage'] = dict(n=len(ms), pct=pct(len(ms), N), T6=sum('T6' in L(c['T']) for c in ms), T2=sum('T2' in L(c['T']) for c in ms), both=sum('T6' in L(c['T']) and 'T2' in L(c['T']) for c in ms))
S['T1_USR'] = sum('T1' in L(c['T']) and 'USR' in L(c['actor']) for c in C)
S['only_USR_NON'] = sum(set(L(c['actor'])) <= {'USR', 'NON'} and L(c['actor']) != [] for c in C)
t5b = [c for c in C if 'T5' in L(c['T']) and 'b' in L(c['T5sub'])]
S['T5b_only_USR_NON'] = (sum(set(L(c['actor'])) <= {'USR', 'NON'} for c in t5b), len(t5b))
S['T4_in_C'] = (sum('C' in L(c['viol']) for c in C if 'T4' in L(c['T'])), S['T']['T4'])
emb = [c for c in C if c['embodied'] == 'Y']; S['embodied'] = dict(n=len(emb), A=sum('A' in L(c['type']) for c in emb), B=sum('B' in L(c['type']) for c in emb), D=sum('D' in L(c['type']) for c in emb))
tab1 = {}
for t in ['T1', 'T2', 'T3', 'T4', 'T5', 'T6']:
    tab1[t] = (sum(t in L(c['T']) and bool({'A', 'B'} & set(L(c['type']))) for c in C), sum(t in L(c['T']) and 'D' in L(c['type']) for c in C))
S['tab1'] = tab1
# ---------------- defenses ----------------
D = [c for c in C if 'D' in L(c['type'])]; ND = len(D); S['Ndef'] = ND
S['D'] = cnt('D', D); S['multiD'] = sum(len(L(c['D'])) >= 2 for c in D)
def has(c, k, v): return v in L(c[k])
S['stage'] = cnt('ft_stage', D); S['stage_unknown'] = sum(c['ft_stage'] in ('?', '') for c in D)
nA = S['stage'].get('A', 0); S['A'] = dict(n=nA, pct=pct(nA, ND), ci=wilson(nA, ND))
am = collections.Counter(c['ft_A_mode'] for c in D if has(c, 'ft_stage', 'A')); S['A_mode'] = dict(am)
S['judge'] = cnt('ft_judge', D); S['judge_unknown'] = sum(c['ft_judge'] in ('?', '') for c in D)
llm = [c for c in D if has(c, 'ft_judge', 'SEP') or has(c, 'ft_judge', 'SELF')]
sep = [c for c in D if has(c, 'ft_judge', 'SEP')]; selfonly = [c for c in llm if not has(c, 'ft_judge', 'SEP')]
ex = lambda pool, v: sum(c['ft_judge_exposed'] == v for c in pool)
S['llm'] = dict(n=len(llm), pct=pct(len(llm), ND), ci=wilson(len(llm), ND), exposedY=ex(llm, 'Y'), exposedN=ex(llm, 'N'), exposedQ=sum(c['ft_judge_exposed'] not in ('Y', 'N') for c in llm))
S['llm']['exp_pct_all'] = pct(S['llm']['exposedY'], len(llm)); S['llm']['exp_pct_known'] = pct(S['llm']['exposedY'], S['llm']['exposedY'] + S['llm']['exposedN'])
S['sep'] = dict(n=len(sep), pct=pct(len(sep), ND), ci=wilson(len(sep), ND), exposedY=ex(sep, 'Y'), exposedN=ex(sep, 'N'), exposedQ=sum(c['ft_judge_exposed'] not in ('Y', 'N') for c in sep))
S['sep']['exp_pct'] = pct(S['sep']['exposedY'], len(sep)); S['sep']['exp_ci'] = wilson(S['sep']['exposedY'], len(sep))
S['sep']['exp_pct_known'] = pct(S['sep']['exposedY'], S['sep']['exposedY'] + S['sep']['exposedN'])
S['selfonly'] = dict(n=len(selfonly), exposedY=ex(selfonly, 'Y'))
rule = [c for c in D if has(c, 'ft_judge', 'RULE')]
rl = [c for c in rule if c['ft_policy_src'] in ('LLM', 'MIX')]
S['rule'] = dict(n=len(rule), llm_policy=len(rl), llm_policy_exposed=sum(c['ft_judge_exposed'] == 'Y' for c in rl), llm_policy_titles=[c['title'][:40] for c in rl if c['ft_judge_exposed'] != 'Y'])
nollm = [c for c in D if c not in llm and c not in rl]
S['nollm'] = dict(n=len(nollm), pct=pct(len(nollm), ND), judge_unknown=sum(c['ft_judge'] in ('?', '') for c in nollm))
tab3 = {}
for s_ in ['I', 'P', 'M', 'A', 'O', 'C']:
    sub = [c for c in D if has(c, 'ft_stage', s_)]
    tab3[s_] = [len(sub)] + [sum(has(c, 'ft_judge', j) for c in sub) for j in ['SEP', 'SELF', 'ML', 'RULE', 'HUMAN']]
tab3['ALL'] = [ND] + [S['judge'].get(j, 0) for j in ['SEP', 'SELF', 'ML', 'RULE', 'HUMAN']]
S['tab3'] = tab3
# pre-execution gates
pre = [c for c in D if has(c, 'ft_stage', 'A') and c['ft_A_mode'] == 'pre']
S['pre_gate'] = dict(n=len(pre), llm=sum(c in llm for c in pre), exposed=sum(c['ft_judge_exposed'] == 'Y' for c in pre), llm_exposed=sum(c in llm and c['ft_judge_exposed'] == 'Y' for c in pre))
# strata by path
def stratum(c): return {'V': 'FULL', 'SEC': 'SEC', 'S': 'SNOW'}.get(c['route'], c['route'])
st = {}
for g in ['FULL', 'SEC', 'SNOW']:
    sub = [c for c in D if stratum(c) == g]
    st[g] = dict(n=len(sub), llm=sum(c in llm for c in sub), sep=sum(c in sep for c in sub), rule=sum(c in rule for c in sub), A=sum(has(c, 'ft_stage', 'A') for c in sub),
                 llm_pct=pct(sum(c in llm for c in sub), len(sub)), llm_ci=wilson(sum(c in llm for c in sub), len(sub)))
S['strata_def'] = st
S['strata_corpus'] = dict(collections.Counter(stratum(c) for c in C))
# sensitivity: adversarial defenses only
adv = [c for c in D if c['ft_adversarial'] == 'Y']
advllm = [c for c in adv if c in llm]
S['adv_only'] = dict(n=len(adv), A=sum(has(c, 'ft_stage', 'A') for c in adv), A_pct=pct(sum(has(c, 'ft_stage', 'A') for c in adv), len(adv)), A_ci=wilson(sum(has(c, 'ft_stage', 'A') for c in adv), len(adv)),
                     llm=len(advllm), llm_pct=pct(len(advllm), len(adv)), exposed=sum(c['ft_judge_exposed'] == 'Y' for c in advllm), exp_pct=pct(sum(c['ft_judge_exposed'] == 'Y' for c in advllm), len(advllm)),
                     sep=sum(c in sep for c in adv), sep_exp=sum(c in sep and c['ft_judge_exposed'] == 'Y' for c in adv))
S['nonadv_def'] = ND - len(adv)
# T-wise defenses among adversarial only (for Table 1 note)
S['tab1_def_adv'] = {t: sum(t in L(c['T']) for c in adv) for t in ['T1', 'T2', 'T3', 'T4', 'T5', 'T6']}
# T6 defenses
t6d = [c for c in D if 'T6' in L(c['T'])]
S['T6def'] = dict(n=len(t6d), C=sum(has(c, 'ft_stage', 'C') for c in t6d), rule_C=sum(has(c, 'ft_stage', 'C') and has(c, 'ft_judge', 'RULE') for c in t6d), rule=sum(has(c, 'ft_judge', 'RULE') for c in t6d))
S['C_RULE_all'] = sum(has(c, 'ft_stage', 'C') and has(c, 'ft_judge', 'RULE') for c in D)
# adaptive
known = [c for c in adv if c['ft_adaptive'] in ('0', '1', '2')]
ad = [c for c in known if c['ft_adaptive'] in ('1', '2')]
S['adaptive'] = dict(adv=len(adv), known=len(known), n=len(ad), pct=pct(len(ad), len(known)), ci=wilson(len(ad), len(known)), lvl2=sum(c['ft_adaptive'] == '2' for c in known))
VENUE_MONTH = {('ACL', '2025'): '2025-07', ('ACL', '2026'): '2026-07', ('EMNLP', '2025'): '2025-11', ('Findings-EMNLP', '2025'): '2025-11', ('Findings-ACL', '2026'): '2026-07', ('Findings-ACL', '2025'): '2025-07',
               ('ICML', '2026'): '2026-07', ('ICML', '2025'): '2025-07', ('ICLR', '2026'): '2026-04', ('ICLR', '2025'): '2025-04', ('NeurIPS', '2025'): '2025-12', ('NeurIPS', '2024'): '2024-12'}
def first_public(c):
    v = (c.get('ft_arxiv_v1') or '').strip(); m = re.match(r'(\d{4})-(\d{2})', v)
    if m: return m.group(0), 'v1'
    a = (c.get('ft_arxiv_id') or c.get('arxiv_id') or '').strip(); m = re.match(r'(\d{2})(\d{2})\.\d+', a)
    if m: return '20%s-%s' % m.groups(), 'id'
    return VENUE_MONTH.get((c['venue'], c['year'])), 'venue'
fp = {c['id']: first_public(c) for c in known}
S['fp_source'] = dict(collections.Counter(v[1] for v in fp.values()))
S['fp_missing'] = [c['id'] for c in known if fp[c['id']][0] is None]
bef = [c for c in known if fp[c['id']][0] and fp[c['id']][0] < '2025-03']; aft = [c for c in known if fp[c['id']][0] and fp[c['id']][0] >= '2025-03']
a1, n1 = sum(c in ad for c in bef), len(bef); a2, n2 = sum(c in ad for c in aft), len(aft)
S['adaptive_time'] = dict(before=(a1, n1, pct(a1, n1), wilson(a1, n1)), after=(a2, n2, pct(a2, n2), wilson(a2, n2)), fisher_p=fisher(a1, n1 - a1, a2, n2 - a2))
# evaluation conditions
def yn(c, k): v = c[k].strip().upper(); return 'Y' if v.startswith('Y') else ('N' if v.startswith('N') else '?')
ev = {}
for k in ['ft_public_bench', 'ft_utility', 'ft_overhead', 'ft_fpr']:
    kn = [c for c in D if yn(c, k) in ('Y', 'N')]; y = sum(yn(c, k) == 'Y' for c in kn)
    ev[k[3:]] = (y, len(kn), pct(y, len(kn)), wilson(y, len(kn)))
S['eval'] = ev
S['agentdojo'] = sum('agentdojo' in c['ft_bench'].lower() for c in D)
S['own_env'] = sum('own:' in c['ft_bench'].lower() for c in D)
benches = collections.Counter()
for c in D:
    for b_ in re.split(r'[;,]', c['ft_bench']):
        b_ = b_.strip().lower()
        if b_ and not b_.startswith('own'): benches[re.sub(r'\s*\(.*', '', b_)] += 1
S['bench_top'] = benches.most_common(8)
nm = sorted(int(c['ft_n_models']) for c in D if re.fullmatch(r'\d+', c['ft_n_models'] or ''))
S['n_models'] = dict(known=len(nm), median=(nm[len(nm) // 2] + nm[(len(nm) - 1) // 2]) / 2, one=sum(x == 1 for x in nm), zero=sum(x == 0 for x in nm))
hum = [c for c in D if has(c, 'ft_judge', 'HUMAN') or 'confirm' in c['ft_decisions']]
S['human'] = dict(n=len(hum), burden=sum(c['ft_hitl_burden'].startswith('Y') for c in hum), D6=S['D'].get('D6', 0), D6_burden=sum(c['ft_hitl_burden'].startswith('Y') for c in D if has(c, 'D', 'D6')))
gr = cnt('ft_granularity', D); tr = [c for c in D if has(c, 'ft_granularity', 'TRAJ')]
S['granularity'] = dict(ACTION=gr.get('ACTION', 0), TRAJ=gr.get('TRAJ', 0), both=sum(has(c, 'ft_granularity', 'ACTION') and has(c, 'ft_granularity', 'TRAJ') for c in D), TRAJ_llm=sum(c in llm for c in tr))
# per-D (Table 2 / Table 5)
perD = {}
for dk in ['D1', 'D2', 'D3', 'D4', 'D5', 'D6']:
    sub = [c for c in D if has(c, 'D', dk)]
    perD[dk] = dict(n=len(sub), llm=sum(c in llm for c in sub), llm_policy=sum(c in rl for c in sub), stages=cnt('ft_stage', sub))
S['perD'] = perD
# full text source
def srcclass(c):
    s = c['ft_src'].lower()
    if re.search(r'abstract-only|unreachable|abstract only', s): return 'abstract'
    if 'tdsc' in s and 'partial' in s: return 'partial'
    if 'aclanthology' in s or 'usenix.org/system/files' in s or 'ndss-symposium.org' in s or 'proceedings' in s: return 'published'
    if 'arxiv' in s: return 'arxiv'
    return 'other:' + s[:40]
S['ft_src'] = dict(collections.Counter(srcclass(c) for c in D))
# ---------------- coding reliability ----------------
def load(fs):
    d = {}
    for f in fs:
        for r in tsv(f): d[r['id']] = r
    return d
CA = load(['CA_a.tsv', 'CA_b.tsv', 'pb/CA_new.tsv']); CB = load(['CB_a.tsv', 'CB_b.tsv', 'pb/CB_new.tsv'])
ids = [i for i in CA if i in CB]
both = [i for i in ids if CA[i]['decision'] == 'INC' and CB[i]['decision'] == 'INC']
rel = {}
for var, vals in [('type', 'ADB'), ('actor', ['EXT', 'SUP', 'AGT', 'USR', 'NON']), ('T', ['T1', 'T2', 'T3', 'T4', 'T5', 'T6']), ('viol', ['AI', 'OI', 'C', 'AV', 'S']), ('multistage', ['Y']), ('embodied', ['Y'])]:
    for v in vals: rel[var + ':' + v] = kappa_bin([v in L(CA[i][var]) for i in both], [v in L(CB[i][var]) for i in both])
t5 = [i for i in both if 'T5' in L(CA[i]['T']) and 'T5' in L(CB[i]['T'])]
for v in 'abc': rel['T5sub:' + v] = kappa_bin([v in L(CA[i]['T5sub']) for i in t5], [v in L(CB[i]['T5sub']) for i in t5])
dd = [i for i in both if 'D' in L(CA[i]['type']) and 'D' in L(CB[i]['type'])]
for v in ['D1', 'D2', 'D3', 'D4', 'D5', 'D6']: rel['D:' + v] = kappa_bin([v in L(CA[i]['D']) for i in dd], [v in L(CB[i]['D']) for i in dd])
ks = sorted(r['kappa'] for r in rel.values())
S['rel_abs'] = dict(items=len(rel), min=ks[0], max=ks[-1], median=(ks[len(ks) // 2] + ks[(len(ks) - 1) // 2]) / 2, n_both=len(both), n_dd=len(dd), n_t5=len(t5), n_ids=len(ids),
                    decision=kappa_bin([CA[i]['decision'] == 'INC' for i in ids], [CB[i]['decision'] == 'INC' for i in ids]), detail=rel)
# overrides by adjudication of values on which both coders agreed
F = ['type', 'actor', 'T', 'T5sub', 'viol', 'multistage', 'embodied', 'D']
ov_papers = set(); ov_fields = 0
for i, v in FINAL.items():
    if i not in CA or i not in CB: continue
    for k in F:
        a, b, f = set(L(CA[i][k])), set(L(CB[i][k])), set(L(v[k]))
        if v['decision'] == 'INC' and CA[i]['decision'] == 'INC' and CB[i]['decision'] == 'INC' and a == b and f != a:
            ov_papers.add(i); ov_fields += 1
S['adj_override'] = dict(papers=len(ov_papers), fields=ov_fields, ids=sorted(ov_papers), adjudicated_records=sum(v['source'] == 'adjudicated' for v in FINAL.values()))
S['decision_triples'] = {'/'.join(k): v for k, v in collections.Counter((CA[i]['decision'], CB[i]['decision'], FINAL[i]['decision']) for i in FINAL if i in CA and i in CB).items()}
# full text reliability (sample)
remap = {'C3': 'S02', 'S2': 'S07', 'S3': 'S05', 'S1': 'Q078'}
F1 = {}
for f in ['FT_1.tsv', 'FT_2.tsv', 'FT_3.tsv', 'FT_4.tsv', 'FT_5.tsv', 'FT_6a.tsv', 'FT_6b.tsv']:
    for r in tsv(f): F1[remap.get(r['rid'], r['rid'])] = r
F2 = {}
for f in ['FT2_a.tsv', 'FT2_b.tsv']:
    for r in tsv(f): F2[r['rid']] = r
fids = [i for i in F2 if i in F1]
S['ft_rel_n'] = len(fids)
fr = {}
def binF(field, lab):
    a = []; b = []
    for i in fids:
        x, y = F1[i][field].strip(), F2[i][field].strip()
        if x in ('?', '') or y in ('?', ''): continue
        a.append(lab in [t.upper() for t in L(x)]); b.append(lab in [t.upper() for t in L(y)])
    return kappa_bin(a, b)
for lab in ['I', 'P', 'M', 'A', 'O', 'C']: fr['stage:' + lab] = binF('stage', lab)
for lab in ['SEP', 'SELF', 'ML', 'RULE', 'HUMAN']: fr['judge:' + lab] = binF('judge', lab)
for lab in ['ACTION', 'TRAJ']: fr['granularity:' + lab] = binF('granularity', lab)
fr['decisions:confirm'] = binF('decisions', 'CONFIRM')
def ynF(field, mapf=None):
    a = []; b = []
    for i in fids:
        x, y = F1[i][field].strip().upper(), F2[i][field].strip().upper()
        if mapf: x, y = mapf(x), mapf(y)
        if x[:1] not in ('Y', 'N') or y[:1] not in ('Y', 'N'): continue
        a.append(x[:1] == 'Y'); b.append(y[:1] == 'Y')
    return kappa_bin(a, b)
for f in ['adversarial', 'public_bench', 'utility', 'overhead', 'fpr', 'judge_exposed']: fr[f] = ynF(f)
fr['A_mode:pre'] = ynF('A_mode', lambda v: 'Y' if v == 'PRE' else ('N' if v in ('POST',) else '?'))
fr['policy_src:LLM/MIX'] = ynF('policy_src', lambda v: 'Y' if v in ('LLM', 'MIX') else ('N' if v in ('MAN', 'LEARN', '-') else '?'))
fr['adaptive:any'] = ynF('adaptive', lambda v: 'Y' if v[:1] in '12' else ('N' if v[:1] == '0' else '?'))
nm_pairs = [(F1[i]['n_models'], F2[i]['n_models']) for i in fids if re.fullmatch(r'\d+', F1[i]['n_models'].strip()) and re.fullmatch(r'\d+', F2[i]['n_models'].strip())]
fr['n_models_exact'] = dict(n=len(nm_pairs), agree=sum(x.strip() == y.strip() for x, y in nm_pairs))
S['rel_ft'] = fr
json.dump(S, open(W + 'STATS10.json', 'w'), ensure_ascii=False, indent=1, default=str)
if __name__ == '__main__':
    for k, v in S.items():
        if k in ('rel_abs',): print(k, {a: b for a, b in v.items() if a != 'detail'}); continue
        print(k, ':', v)

# ---------------- PRISMA flow (v10 definition) ----------------
FINALC = {c['id'] for c in C}
bothE = [m for m in M if m['A'] == 'EXC' and B[m['id']]['decision'] == 'EXC']
bothI = [m for m in M if m['A'] == 'INC' and B[m['id']]['decision'] == 'INC']
fwd = [m for m in M if m['A'] != B[m['id']]['decision']] + bothI
elig_exc = [m for m in fwd if m['id'] not in FINALC]
def elig_reason(i):
    if i in ADJ: return ADJ[i][1]
    if i in FINAL: return FINAL[i].get('exc_reason', '?')
    return '?'
P = dict(screened=len(M), both_exc=len(bothE), both_exc_reasons=dict(collections.Counter(m['A_reason'] for m in bothE).most_common()),
         forwarded=len(fwd), both_inc=len(bothI), disagree=len(fwd) - len(bothI),
         elig_excluded=len(elig_exc), elig_exc_reasons=dict(collections.Counter(elig_reason(m['id']) for m in elig_exc).most_common()),
         included_db=sum(m['id'] in FINALC for m in fwd), snowball_inc=sum(c['route'] == 'S' for c in C), total=len(C),
         by_path={p: sum(m['id'] in FINALC for m in fwd if m['path'] == p) for p in ['V2', 'V3', 'SEC']})
S['prisma'] = P
json.dump(S, open(W + 'STATS10.json', 'w'), ensure_ascii=False, indent=1, default=str)
print('PRISMA', P)

# ---------------- v10 round-2 additions ----------------
import random
C = json.load(open(W + 'FINAL_CORPUS.json')); D = [c for c in C if 'D' in L(c['type'])]
sep = [c for c in D if has(c, 'ft_judge', 'SEP')]; selfonly = [c for c in D if has(c, 'ft_judge', 'SELF') and not has(c, 'ft_judge', 'SEP')]
ji = collections.Counter(c.get('ft_judge_input', '?') for c in sep)
S['judge_input'] = dict(n=len(sep), RAW=ji['RAW'], DERIVED=ji['DERIVED'], TRUSTED=ji['TRUSTED'], unknown=ji['?'], raw_pct=pct(ji['RAW'], len(sep)), raw_ci=wilson(ji['RAW'], len(sep)),
                        rawder=ji['RAW'] + ji['DERIVED'], rawder_pct=pct(ji['RAW'] + ji['DERIVED'], len(sep)))
pa = [(c['ft_judge_input_A'], c['ft_judge_input_B']) for c in sep if c['ft_judge_input_A'] in ('RAW', 'DERIVED', 'TRUSTED') and c['ft_judge_input_B'] in ('RAW', 'DERIVED', 'TRUSTED')]
def kcat(a, b):
    n = len(a); po = sum(x == y for x, y in zip(a, b)) / n; cats = set(a) | set(b); pe = sum(a.count(c) / n * b.count(c) / n for c in cats)
    return dict(n=n, po=round(po, 3), kappa=round((po - pe) / (1 - pe), 2))
S['judge_input_rel'] = dict(three=kcat([a for a, b in pa], [b for a, b in pa]), raw=kcat([a == 'RAW' for a, b in pa], [b == 'RAW' for a, b in pa]),
                            disagree=sum(c['ft_judge_input_A'] != c['ft_judge_input_B'] for c in sep))
pre = [c for c in D if has(c, 'ft_stage', 'A') and c['ft_A_mode'] == 'pre']
S['pre_gate2'] = dict(n=len(pre), sep=sum(c in sep for c in pre), sep_raw=sum(c in sep and c.get('ft_judge_input') == 'RAW' for c in pre),
                      sep_der=sum(c in sep and c.get('ft_judge_input') == 'DERIVED' for c in pre), selfonly=sum(c in selfonly for c in pre),
                      rule=sum(has(c, 'ft_judge', 'RULE') for c in pre), rule_only=sum(has(c, 'ft_judge', 'RULE') and not has(c, 'ft_judge', 'SEP') and not has(c, 'ft_judge', 'SELF') for c in pre))
def stratum(c): return {'V': 'FULL', 'SEC': 'SEC', 'S': 'SNOW'}[c['route']]
st2 = {}
for g in ['FULL', 'SEC', 'SNOW']:
    sub = [c for c in D if stratum(c) == g]; adv_ = [c for c in sub if c['ft_adversarial'] == 'Y']; kn = [c for c in adv_ if c['ft_adaptive'] in ('0', '1', '2')]
    ad_ = [c for c in kn if c['ft_adaptive'] in ('1', '2')]; sp_ = [c for c in sub if c in sep]
    pb_ = [c for c in sub if c['ft_public_bench'][:1] in 'YN']
    st2[g] = dict(n=len(sub), A=sum(has(c, 'ft_stage', 'A') for c in sub), A_pct=pct(sum(has(c, 'ft_stage', 'A') for c in sub), len(sub)),
                  sep=len(sp_), sep_raw=sum(c.get('ft_judge_input') == 'RAW' for c in sp_), llm=sum(has(c, 'ft_judge', 'SEP') or has(c, 'ft_judge', 'SELF') for c in sub),
                  rule=sum(has(c, 'ft_judge', 'RULE') for c in sub), adaptive=(len(ad_), len(kn)), adaptive_pct=pct(len(ad_), len(kn)) if kn else None,
                  public=(sum(c['ft_public_bench'].startswith('Y') for c in pb_), len(pb_)))
S['strata2'] = st2
S['path1_def_share'] = pct(st2['FULL']['n'], len(D))
adv = [c for c in D if c['ft_adversarial'] == 'Y']; advsep = [c for c in adv if c in sep]
S['adv_only2'] = dict(n=len(adv), sep=len(advsep), sep_raw=sum(c.get('ft_judge_input') == 'RAW' for c in advsep), sep_raw_pct=pct(sum(c.get('ft_judge_input') == 'RAW' for c in advsep), len(advsep)))
# bootstrap CIs for full-text reliability kappas
def kb(a, b):
    n = len(a); po = sum(x == y for x, y in zip(a, b)) / n; pa_ = sum(a) / n; pb_ = sum(b) / n; pe = pa_ * pb_ + (1 - pa_) * (1 - pb_)
    return (po - pe) / (1 - pe) if pe < 1 else 1.0
def boot(field, lab=None, mapf=None, reps=2000):
    pairs = []
    for i in fids:
        x, y = F1[i][field].strip(), F2[i][field].strip()
        if lab:
            if x in ('?', '') or y in ('?', ''): continue
            pairs.append((lab in [t.upper() for t in L(x)], lab in [t.upper() for t in L(y)]))
        else:
            x, y = mapf(x.upper()), mapf(y.upper())
            if x[:1] not in 'YN' or y[:1] not in 'YN': continue
            pairs.append((x[:1] == 'Y', y[:1] == 'Y'))
    rnd = random.Random(7); ks = []
    for _ in range(reps):
        s = [pairs[rnd.randrange(len(pairs))] for _ in pairs]
        a = [p[0] for p in s]; b = [p[1] for p in s]
        if len(set(a)) == 1 and len(set(b)) == 1 and a[0] == b[0]: continue
        ks.append(kb(a, b))
    ks.sort()
    return dict(n=len(pairs), kappa=round(kb([p[0] for p in pairs], [p[1] for p in pairs]), 2), ci=(round(ks[int(.025 * len(ks))], 2), round(ks[int(.975 * len(ks)) - 1], 2)))
ident = lambda v: v
S['ft_boot'] = {'stage:A': boot('stage', 'A'), 'stage:P': boot('stage', 'P'), 'stage:C': boot('stage', 'C'), 'judge:SEP': boot('judge', 'SEP'), 'judge:RULE': boot('judge', 'RULE'),
                'judge_exposed': boot('judge_exposed', mapf=ident), 'public_bench': boot('public_bench', mapf=ident), 'fpr': boot('fpr', mapf=ident),
                'adaptive': boot('adaptive', mapf=lambda v: 'Y' if v[:1] in '12' else ('N' if v[:1] == '0' else '?'))}
# audit of double-excluded
au = list(csv.DictReader(open(W + 'pb/audit150_C.tsv'), delimiter='\t'))
S['audit_exc'] = dict(n=len(au), inc=sum(r['decision'] == 'INC' for r in au), ci=wilson(sum(r['decision'] == 'INC' for r in au), len(au)), borderline=sum(r['borderline'] == 'Y' for r in au))
hum = [c for c in D if has(c, 'ft_judge', 'HUMAN') or 'confirm' in c['ft_decisions']]
S['human2'] = dict(n=len(hum), d6=sum(has(c, 'D', 'D6') for c in hum), burdenY=sum(c['ft_hitl_burden'].startswith('Y') for c in hum), known=sum(c['ft_hitl_burden'][:1] in 'YN' for c in hum))
S['final_adjudicated'] = sum(c['coding_source'] == 'adjudicated' for c in C)
S['gold_in_final'] = 21
json.dump(S, open(W + 'STATS10.json', 'w'), ensure_ascii=False, indent=1, default=str)
for k in ['judge_input', 'judge_input_rel', 'pre_gate2', 'strata2', 'path1_def_share', 'adv_only2', 'ft_boot', 'audit_exc', 'human2', 'final_adjudicated', 'adaptive_time']: print(k, S[k])
