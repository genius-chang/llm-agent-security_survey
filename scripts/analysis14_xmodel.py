import os
RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'raw')
# -*- coding: utf-8 -*-
"""Cross-model check (v14): a different model (claude-sonnet-5-5) re-judged random samples blind.
Screening: 200 random candidates from the 1,204 metadata-search candidates (seed 20261002), codebook pb/CODEBOOK_SCREEN.md (rules R1-R5).
Abstract coding: 60 random papers from the 208-paper corpus, codebook pb/CODEBOOK_CODE.md.
Output: XMODEL14.json (agreement with the final decisions/codes in FINAL_CORPUS.json)."""
import json, csv, re
import os
W = RAW + os.sep
def LL(x): return [] if x in (None, '', '-', '?') else [y.strip() for y in re.split(r'[;,]', x) if y.strip() and y.strip() not in ('-', '?')]
def kb(x, y):
    n = len(x); po = sum(p == q for p, q in zip(x, y)) / n; pa = sum(x) / n; pb = sum(y) / n; pe = pa * pb + (1 - pa) * (1 - pb)
    return dict(n=n, po=round(po, 2), kappa=round((po - pe) / (1 - pe), 2) if pe < 1 else 1.0, pabak=round(2 * po - 1, 2), pos_final=sum(x), pos_other=sum(y))
key = json.load(open(W + 'xmodel/KEY_screen.json')); rows = list(csv.DictReader(open(W + 'xmodel/xs_result.tsv'), delimiter='\t'))
a = [key[r['id']]['final_inc'] for r in rows]; b = [r['decision'] == 'INC' for r in rows]
S = dict(model='claude-sonnet-5-5', screen=kb(a, b))
S['screen'].update(final_exc_other_inc=sum((not x) and y for x, y in zip(a, b)), final_inc_other_exc=sum(x and (not y) for x, y in zip(a, b)),
                   final_exc_other_inc_borderline=sum((not x) and y and r['borderline'] == 'Y' for x, y, r in zip(a, b, rows)), disagree=sum(x != y for x, y in zip(a, b)))
ck = json.load(open(W + 'xmodel/KEY_code.json')); F = {c['id']: c for c in json.load(open(W + 'FINAL_CORPUS.json'))}
cr = list(csv.DictReader(open(W + 'xmodel/xc_result.tsv'), delimiter='\t'))
labs = [('type', 'A'), ('type', 'D'), ('type', 'B'), ('actor', 'EXT'), ('actor', 'USR'), ('actor', 'AGT'), ('actor', 'SUP'), ('actor', 'NON'), ('T', 'T1'), ('T', 'T2'), ('T', 'T3'), ('T', 'T4'), ('T', 'T5'), ('T', 'T6'),
        ('viol', 'AI'), ('viol', 'OI'), ('viol', 'C'), ('viol', 'AV'), ('viol', 'S'), ('multistage', 'Y'), ('embodied', 'Y')]
lab = {}
for f, v in labs:
    lab[f + ':' + v] = kb([v in LL(F[ck[r['id']]][f]) for r in cr], [v in LL(r[f]) for r in cr])
ks = sorted(x['kappa'] for x in lab.values())
S['code'] = dict(n=len(cr), labels=len(labs), min=ks[0], max=ks[-1], median=ks[len(ks) // 2], per_label=lab)
# conditional labels (as in the same-model check): D1-D6 among papers both coded as defenses, T5a-c among papers both coded T5
dd = [r for r in cr if 'D' in LL(F[ck[r['id']]]['type']) and 'D' in LL(r['type'])]
tt = [r for r in cr if 'T5' in LL(F[ck[r['id']]]['T']) and 'T5' in LL(r['T'])]
lab2 = {}
for v in ('D1', 'D2', 'D3', 'D4', 'D5', 'D6'): lab2['D:' + v] = kb([v in LL(F[ck[r['id']]]['D']) for r in dd], [v in LL(r['D']) for r in dd])
for v in ('a', 'b', 'c'): lab2['T5sub:' + v] = kb([v in LL(F[ck[r['id']]]['T5sub']) for r in tt], [v in LL(r['T5sub']) for r in tt])
k2 = sorted([x['kappa'] for x in lab.values()] + [x['kappa'] for x in lab2.values()])
S['code30'] = dict(labels=len(k2), n_def=len(dd), n_t5=len(tt), min=k2[0], max=k2[-1], median=round((k2[len(k2) // 2 - 1] + k2[len(k2) // 2]) / 2, 2) if len(k2) % 2 == 0 else k2[len(k2) // 2],
                   per_label=lab2, lowest=sorted([(v['kappa'], k) for k, v in list(lab.items()) + list(lab2.items())])[:6])
json.dump(S, open(W + 'XMODEL14.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps({k: (v if k != 'code' else {kk: vv for kk, vv in v.items() if kk != 'per_label'}) for k, v in S.items()}, ensure_ascii=False))
