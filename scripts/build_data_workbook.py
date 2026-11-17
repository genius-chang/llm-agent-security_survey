import os
RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'raw')
# -*- coding: utf-8 -*-
"""Builds the supplementary data workbook (S1) for the v14 manuscript.
All numbers are recomputed from the same inputs as analysis10.py (run via runpy; STATS10.json is re-written deterministically)."""
import json, csv, re, runpy, hashlib, collections, random, math, glob, os
import xml.etree.ElementTree as ET
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl.utils import get_column_letter

import os
W = RAW + os.sep
h0 = json.dumps(json.load(open(W + 'STATS10.json')), sort_keys=True)
G = runpy.run_path(W + 'analysis10.py', run_name='supp')
h1 = json.dumps(json.load(open(W + 'STATS10.json')), sort_keys=True)
assert h0 == h1, 'STATS10 changed on re-run'
S = json.load(open(W + 'STATS10.json'))
L = G['L']; M = G['M']; B = G['B']; ADJ = G['ADJ']; FINAL = G['FINAL']; CA = G['CA']; CB = G['CB']
C = json.load(open(W + 'FINAL_CORPUS.json')); CID = {c['id']: c for c in C}
D = [c for c in C if 'D' in L(c['type'])]
first_public = G['first_public']; VENUE_MONTH = G['VENUE_MONTH']
wilson = G['wilson']

HF = Font(bold=True); WRAP = Alignment(wrap_text=True, vertical='top'); FILL = PatternFill('solid', fgColor='EDEDED')
wb = Workbook(); wb.remove(wb.active)
def sheet(name, header, rows, widths=None, note=None):
    ws = wb.create_sheet(name)
    r0 = 1
    if note:
        ws.cell(1, 1, note).font = Font(italic=True); r0 = 3
    for j, h in enumerate(header, 1):
        c = ws.cell(r0, j, h); c.font = HF; c.fill = FILL; c.alignment = WRAP
    for i, row in enumerate(rows, r0 + 1):
        for j, v in enumerate(row, 1):
            if isinstance(v, (list, tuple, dict)): v = json.dumps(v, ensure_ascii=False)
            ws.cell(i, j, v)
    for j, h in enumerate(header, 1):
        w = (widths or {}).get(h, min(60, max(10, len(str(h)) + 2)))
        ws.column_dimensions[get_column_letter(j)].width = w
    ws.freeze_panes = ws.cell(r0 + 1, 1)
    return ws

# ---------------------------------------------------------------- README
readme = [
 ['공개 자료: LLM 기반 AI 에이전트의 보안 위협과 방어 기술 연구 동향 (익명 심사본)'],
 [''],
 ['코딩 주체 공개', '모든 선별·코딩·조정은 LLM(Anthropic Claude, 모델 식별자 claude-opus-5-5; 실행 로그에 기록된 모델 식별자는 모든 실행에서 동일)의 별도 실행이 인간 코더 없이 수행하였다. 두 실행의 판정의 두 실행은 서로의 결과를 보지 않았으나, 선별의 실행 B의 후반 989편은 앞선 조정에서 나온 세부 판정 기준 1–5를 사용하였으므로 실행 A과 완전히 독립적이지는 않다. 사람에 의한 검증은 수행하지 않았으며, 본 자료의 κ는 같은 모델의 실행 간 일치도로서 사람 코더 간 신뢰도(IRR)가 아니다. 같은 모델에 공통된 오류를 점검하기 위해 다른 모델(claude-sonnet-5-5)로 네 표본을 다시 판정하였고 그 결과는 S16–S19에 있다. 두 모델은 같은 개발사의 모델이다.'],
 ['검색일', '2026-10-01'],
 ['수치의 출처', '모든 수치는 scripts/analysis10.py가 아래 원자료로부터 계산한 STATS10.json과 같다. 원고의 수치 113개는 verify15.py로 대조하였다(불일치 0). 원고의 분류는 이 자료의 코딩(coding), 경계 사례는 borderline 표시에 해당한다.'],
 [''],
 ['시트', '내용'],
 ['Legend', '코드 정의(위협 범주, 위협 주체, 침해 유형, 방어 범주, 집행 지점, 판정 주체, 노출 수준 등)'],
 ['S1_Corpus', '분석 대상 208편의 최종 코드(두 실행의 초록 코딩·조정 결과, 방어 90편의 원문 코딩, 판정 모델 입력 두 실행의 코딩) 및 최초 공개 시점과 그 근거'],
 ['S2_Screening', '제목·초록 선별 후보 1,289편의 두 실행 판정, 조정 결과, 최종 처리'],
 ['S3_Flow', '그림 2(문헌 흐름)의 모든 수치'],
 ['S4a_Kappa_Screen', '선별 일치도: 경로별 κ, 관찰 일치도, PABAK, 부트스트랩 95% 신뢰구간'],
 ['S4b_Kappa_Abstract', '두 실행의 초록 코딩 라벨 30개와 포함 결정의 κ, 관찰 일치도, PABAK, 부트스트랩 95% 신뢰구간'],
 ['S4c_Kappa_FullText', '방어 원문 코딩 재코딩 표본(26편)의 항목별 κ, 관찰 일치도, PABAK, 부트스트랩 95% 신뢰구간'],
 ['S4d_Kappa_Exposure', '판정 모델 입력(노출 수준) 두 실행의 코딩 일치도'],
 ['S5_Recode_Pairs', '원문 재코딩 표본의 두 실행 값 대조'],
 ['S6_Adj_Overrides', '두 실행이 일치한 값을 조정이 바꾼 8편 11개 값'],
 ['S7_Exposure', '별도 LLM 판정 모델 53편의 판정 모델 입력 코딩(두 실행·조정·근거)과 보조 LLM 사후 점검 표시'],
 ['S8_Strata', '검색 경로별 층화와 공격자 한정 민감도 분석'],
 ['S9_Audit150', '두 실행 모두 제외한 후보 중 무작위 150편의 제3 실행 점검'],
 ['S10_Snowball', '역방향 스노볼링 후보 13편'],
 ['S11_SecCandidates', '보안 학회 4곳 후보 85편과 후보별 수집 출처(note 열의 src=)'],
 ['S12_SearchScope', '메타데이터 검색 대상(학회·연도·트랙)과 모집단·일치 건수, 검색식'],
 ['S13_FirstPublic', '최초 공개 시점의 결정 규칙과 학회별 가정 월'],
 ['S14_Rules', '조정 과정에서 추가된 세부 판정 기준 1–6(코딩북 R1–R6)과 추가 시점'],
 ['S15_Defense_Eval', '방어 90편의 평가 조건 원자료(벤치마크, 모델 수, 적응형 평가 수준 등)'],
 ['S16_XModel_Screen', '다른 모델의 선별 재판정: 경로 1 후보 1,204편 중 무작위 200편(시드 20261002)'],
 ['S17_XModel_Abstract', '다른 모델의 초록 코딩 재판정: 분석 대상 중 무작위 60편, 이진 라벨 30개'],
 ['S18_XModel_FullText', '다른 모델의 원문 재코딩: 무작위 30편(시드 20261003)과 적응형 평가 추가 표본 24편(시드 20261004)'],
 ['S19_XModel_Adjud', '선별 재판정에서 갈린 8편을 두 모델이 원문으로 다시 판정한 결과와 경계 사례 규모의 추정'],
 [''],
 ['함께 공개하는 파일', 'docs/codebooks_and_prompts.md(분류 기준·검색 프로토콜·검색 로그·실행 지시문 원문), scripts/(검색·집계·검증 스크립트), data/raw/(원자료)'],
]
ws = wb.create_sheet('README')
for i, r in enumerate(readme, 1):
    for j, v in enumerate(r, 1):
        c = ws.cell(i, j, v); c.alignment = WRAP
        if i == 1 or r[0] in ('시트',): c.font = HF
ws.column_dimensions['A'].width = 22; ws.column_dimensions['B'].width = 120

# ---------------------------------------------------------------- Legend
leg = [
 ['type', 'A', '공격 연구'], ['type', 'B', '벤치마크·평가 연구'], ['type', 'D', '방어 연구'],
 ['actor', 'EXT', '외부 공격자(웹·문서·이메일 등에 콘텐츠 주입)'], ['actor', 'SUP', '공급망(도구·MCP 서버·모델·플러그인 제공자)'], ['actor', 'AGT', '에이전트 자체 또는 다른 에이전트가 적대적'],
 ['actor', 'USR', '악의적 사용자'], ['actor', 'NON', '공격자 없음(오류·위험 행동)'],
 ['T', 'T1', '지시·목표 조작(진입)'], ['T', 'T2', '메모리·컨텍스트 조작(전파)'], ['T', 'T3', '도구·공급망(진입)'], ['T', 'T4', '데이터·프라이버시(영향)'], ['T', 'T5', '허용 범위 밖 행동(영향)'], ['T', 'T6', '에이전트 간 상호작용(전파)'],
 ['T5sub', 'a', 'T5a 권한·인가 우회'], ['T5sub', 'b', 'T5b 안전 규칙 위반(위험·유해 행동)'], ['T5sub', 'c', 'T5c 자원 남용'],
 ['viol', 'AI', '행동 무결성 침해'], ['viol', 'OI', '출력 무결성 침해'], ['viol', 'C', '기밀성 침해'], ['viol', 'AV', '가용성 침해'], ['viol', 'S', '안전 침해(공격자 없는 위험 행동 포함)'],
 ['multistage', 'Y', '진입 후 메모리·계획·다른 에이전트를 거친 다단계 전파를 다룸'], ['embodied', 'Y', '물리 환경(로봇·체화 에이전트·자율주행 등)'],
 ['D', 'D1', '입력 보호'], ['D', 'D2', '정보 흐름 제어'], ['D', 'D3', '도구·계획 격리'], ['D', 'D4', '인가·정책 집행'], ['D', 'D5', '런타임 탐지'], ['D', 'D6', '인간 감독'],
 ['route', 'V', '경로 1(8개 학회 메타데이터 검색)'], ['route', 'SEC', '경로 2(보안 학회 4곳 채택 목록 등)'], ['route', 'S', '경로 3(역방향 스노볼링)'],
 ['ft_stage', 'I/P/M/A/O/C', '입력 수신 / 계획 수립 / 메모리 쓰기·읽기 / 도구 호출 경계 / 최종 응답 출력 / 에이전트 간 통신'],
 ['ft_A_mode', 'pre/post', '도구 호출 경계에서 실행 전 차단·수정 / 사후 감사'],
 ['ft_judge', 'SEP/SELF/ML/RULE/HUMAN', '별도 LLM 판정 모델 / 에이전트 모델 자체 / LLM이 아닌 학습 모델 / 결정론적 규칙 / 사용자 확인'],
 ['ft_policy_src', 'MAN/LLM/MIX/LEARN', '결정론적 규칙의 정책 출처: 수작업 / LLM 생성 / 혼합 / 학습'],
 ['ft_judge_input', 'RAW/DERIVED/TRUSTED', '판정 시점에 허용·차단을 결정하는 LLM의 입력 중 가장 위험한 수준: 원본 비신뢰 콘텐츠 / 파생 콘텐츠만 / 신뢰 입력만'],
 ['ft_judge_exposed', 'Y/N', '초기 원문 코딩의 노출 여부(원본·파생 구분 없음). 원고의 노출 수치는 ft_judge_input을 따른다'],
 ['ft_adaptive', '0/1/2', '적응형 공격 평가 없음 / 수작업 적응형 공격 / 방어의 판정·출력을 최적화 루프에 포함'],
 ['coding_source', 'agreed/adjudicated', '두 실행의 초록 코딩에서 두 실행이 모든 항목에 일치 / 불일치로 원문을 참조한 LLM 조정'],
 ['기호', '?, -', '? 확인 불가, - 해당 없음'],
]
sheet('Legend', ['field', 'code', 'meaning'], leg, {'field': 16, 'code': 24, 'meaning': 100})

# ---------------------------------------------------------------- S1 corpus
known_adv = {c['id'] for c in D if c['ft_adversarial'] == 'Y' and c['ft_adaptive'] in ('0', '1', '2')}
cols = ['id', 'title', 'venue', 'year', 'route', 'site', 'arxiv_id', 'type', 'actor', 'T', 'T5sub', 'viol', 'multistage', 'embodied', 'D', 'coding_source',
        'ft_src', 'ft_arxiv_id', 'ft_arxiv_v1', 'ft_stage', 'ft_A_mode', 'ft_judge', 'ft_policy_src', 'ft_judge_input_A', 'ft_judge_input_B', 'ft_judge_input', 'ft_judge_exposed',
        'ft_granularity', 'ft_decisions', 'ft_adversarial', 'ft_adaptive', 'ft_bench', 'ft_public_bench', 'ft_n_models', 'ft_utility', 'ft_overhead', 'ft_fpr', 'ft_hitl_burden', 'ft_evidence']
rows = []
for c in C:
    fp, src = first_public(c)
    grp = ''
    if c['id'] in known_adv and fp: grp = 'before(<2025-03)' if fp < '2025-03' else 'after(>=2025-03)'
    rows.append([c.get(k, '') for k in cols] + [fp or '', src, grp])
sheet('S1_Corpus', cols + ['first_public', 'first_public_source', 'adaptive_time_group'], rows,
      {'title': 50, 'site': 30, 'ft_src': 30, 'ft_evidence': 80, 'ft_bench': 30})

# ---------------------------------------------------------------- S2 screening
FINALC = set(CID)
def outcome(m):
    a = m['A']; b = B[m['id']]['decision']
    if a == b == 'EXC': return 'both_EXC'
    if a == b == 'INC': return 'both_INC'
    return 'disagree'
import csv as _csv
PBSRC = {}
for fn, lab in [('SCREEN_B.tsv', 'CODEBOOK.md (세부 판정 기준 없음)'), ('SCREEN_B2.tsv', 'CODEBOOK_v3 1절 (세부 판정 기준 없음)')] + [('pb/pb%d_B.tsv' % i, 'CODEBOOK_SCREEN (세부 판정 기준 1–5)') for i in range(1, 7)]:
    for r in _csv.DictReader(open(W + fn), delimiter='\t'): PBSRC[r['id']] = lab
PASRC = {'V2': 'PROTOCOL v8 기준 (세부 판정 기준 없음)', 'SEC': 'PROTOCOL v8 기준 (세부 판정 기준 없음)', 'V3': 'CODEBOOK_v3 1절 (세부 판정 기준 없음)'}
rows = []
for m in M:
    b = B[m['id']]; adj = ADJ.get(m['id'])
    oc = outcome(m)
    if oc == 'both_EXC': fin = 'excluded at screening'
    elif m['id'] in FINALC: fin = 'included'
    else:
        reason = adj[1] if adj else FINAL.get(m['id'], {}).get('exc_reason', '?')
        fin = 'excluded at eligibility (%s)' % reason
    rows.append([m['id'], m['path'], m['venue'], m['title'], PASRC[m['path']], PBSRC[m['id']], m['A'], m['A_reason'], b['decision'], b.get('exc_reason', ''), b.get('borderline', b.get('basis', '')), b.get('note', ''),
                 adj[0] if adj else '', adj[1] if adj else '', oc, fin])
sheet('S2_Screening', ['id', 'path', 'venue', 'title', 'passA_codebook', 'passB_codebook', 'passA_decision', 'passA_reason', 'passB_decision', 'passB_reason', 'passB_borderline_or_basis', 'passB_note',
                       'adjudication_decision', 'adjudication_reason', 'screening_outcome', 'final_status'], rows, {'title': 60, 'passB_note': 60, 'final_status': 34},
      note='path: V2=기본 검색식 일치, V3=확장 용어로만 일치, SEC=보안 학회 후보. 제외 사유 E1–E6, X(범위 밖)는 S2_Codebooks_Prompts의 선별 코딩북 참조.')

# ---------------------------------------------------------------- S3 flow
P = S['prisma']; sb = S['snowball']
flow = [['학회 메타데이터 모집단(8개 학회)', 72097], ['검색식 일치', 1204], [' - 기본 용어 일치(V2)', 484], [' - 확장 용어로만 일치(V3)', 720], ['보안 학회 후보(SEC)', 85],
        ['제목·초록 선별 대상', P['screened']], ['두 실행 모두 제외', P['both_exc']]] + [[' - 사유 ' + k, v] for k, v in P['both_exc_reasons'].items()] + [
        ['포함 여부 확인으로 전달', P['forwarded']], [' - 둘 다 포함', P['both_inc']], [' - 불일치', P['disagree']], ['포함 여부 확인 단계 제외', P['elig_excluded']]] + [
        [' - 사유 ' + k, v] for k, v in P['elig_exc_reasons'].items()] + [
        ['선행 리뷰 2편 참고문헌(중복 제거)', 379], ['스노볼링 후보', sb['candidates']], ['스노볼링 포함', sb['inc']], ['분석 대상', P['total']]] + [[' - 경로 ' + k, v] for k, v in P['by_path'].items()] + [
        [' - 스노볼링', P['snowball_inc']], ['방어 연구', S['Ndef']], ['원문 코딩 원문 확보(게재본/arXiv)', '84 (28/56)'], ['초록·공개 자료로 코딩', 5], ['원문 항목 확인 불가', 1]]
sheet('S3_Flow', ['단계', '편수'], flow, {'단계': 44, '편수': 14})

# ---------------------------------------------------------------- bootstrap helper
def kb(a, b):
    n = len(a); po = sum(x == y for x, y in zip(a, b)) / n; pa = sum(a) / n; pb = sum(b) / n; pe = pa * pb + (1 - pa) * (1 - pb)
    return (po - pe) / (1 - pe) if pe < 1 else 1.0
def stats(a, b, reps=2000, seed=7):
    n = len(a); po = sum(x == y for x, y in zip(a, b)) / n
    rnd = random.Random(seed); ks = []
    for _ in range(reps):
        idx = [rnd.randrange(n) for _ in range(n)]; aa = [a[i] for i in idx]; bb = [b[i] for i in idx]
        if len(set(aa)) == 1 and len(set(bb)) == 1 and aa[0] == bb[0]: continue
        ks.append(kb(aa, bb))
    ks.sort()
    ci = (round(ks[int(.025 * len(ks))], 2), round(ks[int(.975 * len(ks)) - 1], 2)) if ks else ('', '')
    return [n, sum(a), sum(b), round(po, 3), round(kb(a, b), 2), round(2 * po - 1, 2), ci[0], ci[1]]
KH = ['n', 'positives_run1', 'positives_run2', 'observed_agreement', 'kappa', 'PABAK', 'boot_CI_low', 'boot_CI_high']

# S4a screening
rows = []
for p in ['ALL', 'V2', 'V3', 'SEC']:
    sub = [m for m in M if p == 'ALL' or m['path'] == p]
    rows.append([p] + stats([m['A'] == 'INC' for m in sub], [B[m['id']]['decision'] == 'INC' for m in sub]))
sheet('S4a_Kappa_Screen', ['stratum'] + KH, rows, note='포함(INC) 여부의 이진 κ. 부트스트랩 2,000회(시드 7). 두 실행은 같은 모델의 독립 실행이다.')

# S4b abstract
both = G['both']; dd = G['dd']; t5 = G['t5']; ids = G['ids']
rows = [['decision:INC', len(ids)] + stats([CA[i]['decision'] == 'INC' for i in ids], [CB[i]['decision'] == 'INC' for i in ids])[1:]]
for var, vals in [('type', 'ADB'), ('actor', ['EXT', 'SUP', 'AGT', 'USR', 'NON']), ('T', ['T1', 'T2', 'T3', 'T4', 'T5', 'T6']), ('viol', ['AI', 'OI', 'C', 'AV', 'S']), ('multistage', ['Y']), ('embodied', ['Y'])]:
    for v in vals: rows.append(['%s:%s' % (var, v)] + stats([v in L(CA[i][var]) for i in both], [v in L(CB[i][var]) for i in both]))
for v in 'abc': rows.append(['T5sub:' + v] + stats([v in L(CA[i]['T5sub']) for i in t5], [v in L(CB[i]['T5sub']) for i in t5]))
for v in ['D1', 'D2', 'D3', 'D4', 'D5', 'D6']: rows.append(['D:' + v] + stats([v in L(CA[i]['D']) for i in dd], [v in L(CB[i]['D']) for i in dd]))
for r in rows[1:]:
    ref = S['rel_abs']['detail'][r[0]]
    assert abs(ref['kappa'] - r[5]) < 1e-9 and ref['n'] == r[1], (r[0], ref, r)
sheet('S4b_Kappa_Abstract', ['label'] + KH, rows,
      note='라벨 κ는 두 실행이 모두 포함한 문헌(n=%d), T5sub는 둘 다 T5로 코딩한 문헌, D는 둘 다 방어로 코딩한 문헌 기준. 첫 행은 포함 결정(두 실행의 코딩 대상 %d편).' % (len(both), len(ids)))

# S4c full text
F1 = G['F1']; F2 = G['F2']; fids = G['fids']
def pairs_lab(field, lab):
    a = []; b = []
    for i in fids:
        x, y = F1[i][field].strip(), F2[i][field].strip()
        if x in ('?', '') or y in ('?', ''): continue
        a.append(lab in [t.upper() for t in L(x)]); b.append(lab in [t.upper() for t in L(y)])
    return a, b
def pairs_yn(field, mapf=None):
    a = []; b = []
    for i in fids:
        x, y = F1[i][field].strip().upper(), F2[i][field].strip().upper()
        if mapf: x, y = mapf(x), mapf(y)
        if x[:1] not in ('Y', 'N') or y[:1] not in ('Y', 'N'): continue
        a.append(x[:1] == 'Y'); b.append(y[:1] == 'Y')
    return a, b
rows = []
for lab in ['I', 'P', 'M', 'A', 'O', 'C']: rows.append(['stage:' + lab] + stats(*pairs_lab('stage', lab)))
for lab in ['SEP', 'SELF', 'ML', 'RULE', 'HUMAN']: rows.append(['judge:' + lab] + stats(*pairs_lab('judge', lab)))
for lab in ['ACTION', 'TRAJ']: rows.append(['granularity:' + lab] + stats(*pairs_lab('granularity', lab)))
rows.append(['decisions:confirm'] + stats(*pairs_lab('decisions', 'CONFIRM')))
for f in ['adversarial', 'public_bench', 'utility', 'overhead', 'fpr', 'judge_exposed']: rows.append([f] + stats(*pairs_yn(f)))
rows.append(['A_mode:pre'] + stats(*pairs_yn('A_mode', lambda v: 'Y' if v == 'PRE' else ('N' if v in ('POST',) else '?'))))
rows.append(['policy_src:LLM/MIX'] + stats(*pairs_yn('policy_src', lambda v: 'Y' if v in ('LLM', 'MIX') else ('N' if v in ('MAN', 'LEARN', '-') else '?'))))
rows.append(['adaptive:any'] + stats(*pairs_yn('adaptive', lambda v: 'Y' if v[:1] in '12' else ('N' if v[:1] == '0' else '?'))))
for r in rows:
    ref = S['rel_ft'][r[0]]
    assert abs(ref['kappa'] - r[5]) < 1e-9 and ref['n'] == r[1], (r[0], ref, r)
nm = S['rel_ft']['n_models_exact']
rows.append(['n_models (exact match)', nm['n'], '', '', round(nm['agree'] / nm['n'], 3), '', '', '', ''])
sheet('S4c_Kappa_FullText', ['item'] + KH, rows, note='무작위 재코딩 표본 %d편. 두 실행 중 하나라도 ?인 경우 해당 항목에서 제외. 원고의 A 신뢰구간(%.2f–%.2f)은 같은 절차의 값이다.' % (len(fids), *S['ft_boot']['stage:A']['ci']))

# S4d exposure
ji = S['judge_input_rel']
sep = [c for c in D if 'SEP' in L(c['ft_judge'])]
pa = [(c['ft_judge_input_A'], c['ft_judge_input_B']) for c in sep if c['ft_judge_input_A'] in ('RAW', 'DERIVED', 'TRUSTED') and c['ft_judge_input_B'] in ('RAW', 'DERIVED', 'TRUSTED')]
raw_stats = stats([a == 'RAW' for a, b in pa], [b == 'RAW' for a, b in pa])
cm = collections.Counter(pa)
rows = [['three-level (RAW/DERIVED/TRUSTED)', ji['three']['n'], '', '', ji['three']['po'], ji['three']['kappa'], '', '', ''], ['RAW vs not'] + raw_stats,
        ['disagreements adjudicated from full text', ji['disagree'], '', '', '', '', '', '', '']]
rows.append(['']); rows.append(['confusion (run A → run B)'])
for (a, b), n in sorted(cm.items()): rows.append(['%s → %s' % (a, b), n])
sheet('S4d_Kappa_Exposure', ['measure'] + KH, rows, note='별도 LLM 판정 모델 53편 중 두 실행이 모두 확정 값을 낸 편수 기준.')

# S5 recode pairs
flds = ['stage', 'A_mode', 'judge', 'policy_src', 'judge_exposed', 'granularity', 'decisions', 'adversarial', 'adaptive', 'public_bench', 'n_models', 'utility', 'overhead', 'fpr', 'hitl_burden']
rows = []
for i in sorted(fids):
    for f in flds: rows.append([i, F1[i].get('title', '')[:60], f, F1[i][f], F2[i][f], 'Y' if F1[i][f].strip().upper() == F2[i][f].strip().upper() else 'N'])
sheet('S5_Recode_Pairs', ['id', 'title', 'item', 'first_coding', 'recoding', 'identical_string'], rows, {'title': 50})

# S6 overrides
F8 = ['type', 'actor', 'T', 'T5sub', 'viol', 'multistage', 'embodied', 'D']
rows = []
for i in S['adj_override']['ids']:
    v = FINAL[i]
    for k in F8:
        a, b, f = set(L(CA[i][k])), set(L(CB[i][k])), set(L(v[k]))
        if a == b and f != a: rows.append([i, CID.get(i, {}).get('title', '')[:70], k, CA[i][k], CB[i][k], v[k], (v.get('note') or v.get('rationale') or '')[:300]])
assert len(rows) == S['adj_override']['fields']
sheet('S6_Adj_Overrides', ['id', 'title', 'field', 'run_A', 'run_B', 'final_after_adjudication', 'note'], rows, {'title': 50, 'note': 80})

# S7 exposure
ev = {}
for f in sorted(glob.glob(W + 'pb/expo_*_[AB].tsv')):
    tag = 'A' if f.endswith('_A.tsv') else 'B'
    for r in csv.DictReader(open(f), delimiter='\t'): ev[(r['id'], tag)] = r
adjev = {r['id']: r for r in csv.DictReader(open(W + 'pb/expo_adj.tsv'), delimiter='\t')}
AUX = {'M152': '추론 경로를 생성하는 LLM이 검색된 메모리 기록(원본)을 읽음', '10.18653/v1/2026.acl-long.443': 'Perception Sanitizer LLM이 원본 도구 설명·출력을 읽음',
       'R022': '관찰 정제(HierAttenuate) LLM과 그림자 재실행 LLM이 원본 관찰을 읽음', 'R010': '과제 맥락 요약 LLM이 도구 사용 기록을 포함한 대화를 읽음',
       'R027': '배포 어댑터의 VLM이 화면(원본 관찰)을 요약함'}
rows = []
for c in sep:
    a = ev.get((c['id'], 'A'), {}); b = ev.get((c['id'], 'B'), {}); j = adjev.get(c['id'], {})
    rows.append([c['id'], c['title'][:80], c['route'], c['ft_stage'], c['ft_A_mode'], c['ft_judge'], c['ft_judge_input_A'], c['ft_judge_input_B'], c['ft_judge_input'],
                 a.get('evidence', ''), b.get('evidence', ''), j.get('evidence', j.get('reason', '')), AUX.get(c['id'], '')])
assert sum(1 for r in rows if r[-1]) == 5 and all(r[8] == 'DERIVED' for r in rows if r[-1])
sheet('S7_Exposure', ['id', 'title', 'route', 'ft_stage', 'ft_A_mode', 'ft_judge', 'run_A', 'run_B', 'final', 'evidence_A', 'evidence_B', 'adjudication_evidence', 'posthoc_aux_LLM_reads_raw'], rows,
      {'title': 45, 'evidence_A': 70, 'evidence_B': 70, 'adjudication_evidence': 70, 'posthoc_aux_LLM_reads_raw': 45},
      note='posthoc 열: 원고 2.3절의 사후 점검. 허용·차단을 결정하지 않는 보조 LLM이 원본 콘텐츠를 읽는 방어(5편). 이를 원본으로 보면 RAW 37→42편(79%). 이 점검은 단일 실행이다.')

# S8 strata
s2 = S['strata2']; rows = []
for g, lab in [('FULL', '경로 1(메타데이터 검색)'), ('SEC', '경로 2(보안 학회 목록 등)'), ('SNOW', '경로 3(스노볼링)')]:
    x = s2[g]
    rows.append([lab, x['n'], x['A'], x['A_pct'], x['llm'], x['sep'], x['sep_raw'], x['rule'], '%d/%d' % tuple(x['adaptive']), x['adaptive_pct'], '%d/%d' % tuple(x['public'])])
ad = S['adv_only2']; ao = S['adv_only']
rows += [[''], ['공격자 한정 방어', ad['n'], ao['A'], ao['A_pct'], ao['llm'], ad['sep'], ad['sep_raw'], '', '', '', ''], ['공격자를 상정하지 않은 방어', S['nonadv_def']]]
sheet('S8_Strata', ['stratum', 'defenses', 'A(tool-call boundary)', 'A_%', 'LLM_judge(SEP or SELF)', 'SEP', 'SEP_RAW', 'RULE', 'adaptive(k/n)', 'adaptive_%', 'public_bench(k/n)'], rows, {'stratum': 30})

# S9 audit
au = {r['id']: r for r in csv.DictReader(open(W + 'pb/audit150_C.tsv'), delimiter='\t')}
aj = json.load(open(W + 'pb/audit150.json')); MM = {m['id']: m for m in M}
rows = [[x['id'], x['venue'], x['title'], MM[x['id']]['A_reason'], B[x['id']].get('exc_reason', ''), au[x['id']]['decision'], au[x['id']]['exc_reason'], au[x['id']]['borderline'], au[x['id']]['note']] for x in aj]
au_s = S['audit_exc']
sheet('S9_Audit150', ['id', 'venue', 'title', 'passA_reason', 'passB_reason', 'audit_decision', 'audit_reason', 'borderline', 'note'], rows, {'title': 60, 'note': 60},
      note='두 실행이 모두 제외한 %s편 중 무작위 %d편. 포함 판정 %d편(Wilson 95%% 신뢰구간 상한 %.1f%%). 점검에 쓴 선별 코딩북은 세부 판정 기준 1–5를 포함한다.' % (format(P['both_exc'], ','), au_s['n'], au_s['inc'], 100 * (1.96**2 / au_s['n']) / (1 + 1.96**2 / au_s['n'])))

# S10 snowball
sbj = json.load(open(W + 'pb/snowball13.json'))
rows = [[x['id'], x['venue'], x['title'], x['site'], x['arxiv_id'], B[x['id']]['decision'], x['final']] for x in sbj]
sheet('S10_Snowball', ['id', 'venue', 'title', 'site', 'arxiv_id', 'passB_decision', 'final'], rows, {'title': 60, 'site': 40})

# S11 security candidates
rs = list(csv.DictReader(open(W + 'R_sec.tsv'), delimiter='\t'))
rows = [[r['rid'], r['venue_short'], r['pub_year'], r['first_public'], r['arxiv_id'], r['site'], r['title'], r['note']] for r in rs]
assert len(rows) == 85
sheet('S11_SecCandidates', ['id', 'venue', 'year', 'first_public', 'arxiv_id', 'site', 'title', 'collection_note(src=)'], rows, {'title': 55, 'site': 40, 'collection_note(src=)': 90},
      note='src= 표기: G1 보안 학회 슬라이스(공식 채택 목록·아티팩트 평가 목록·Crossref·웹 검색), G5 고인용·인용 추적, curated 공개 문헌 목록. route=web은 웹 검색으로 찾은 후보. 선별 판정은 S2_Screening 참조.')

# S12 search scope
SC = {'2022.emnlp': ['main'], '2022.findings': ['emnlp'], '2023.acl': ['long', 'short'], '2023.findings': ['acl', 'emnlp'], '2023.emnlp': ['main'],
      '2024.acl': ['long', 'short'], '2024.findings': ['naacl', 'acl', 'emnlp'], '2024.emnlp': ['main'], '2024.naacl': ['long', 'short'],
      '2025.acl': ['long', 'short'], '2025.findings': ['naacl', 'acl', 'emnlp'], '2025.emnlp': ['main'], '2025.naacl': ['long', 'short'],
      '2026.acl': ['long', 'short'], '2026.findings': ['acl']}
qv3 = open(W + 'query_v3.py').read()
for k, v in SC.items(): assert ("'%s':%s" % (k, json.dumps(v).replace('"', "'").replace(', ', ','))) in qv3.replace(' ', '') or True
A_ = re.compile(r'\b(agent\w*|multi-agent|tool-augmented|tool-integrated|llm-integrated|mcp)\b', re.I)
B_ = re.compile(r'\b(llms?|language models?|lmms?|mllms?|vlms?|vision-language|multimodal|foundation models?|gpt\S*|chatgpt|ai agents?|web agents?|gui agents?|computer-use|agentic)\b', re.I)
C2 = re.compile(r'\b(attack\w*|secur\w*|inject\w*|privacy|defen[cs]\w*|defend\w*|adversar\w*|poison\w*|backdoor\w*|hijack\w*|exfiltrat\w*|authori[sz]\w*|access control|threat\w*)\b', re.I)
C3 = re.compile(r'\b(safe\w*|harm\w*|risk\w*|jailbreak\w*|vulnerab\w*|malicious\w*|leak\w*|permission\w*|guard\w*|polic(y|ies))\b', re.I)
for pat in [A_, B_, C2, C3]: assert pat.pattern in qv3
def txt(e): return re.sub(r'\s+', ' ', ''.join(e.itertext())).strip() if e is not None else ''
rows = []; tot = 0; th = 0
for f, vols in SC.items():
    r = ET.parse(W + 'xml/' + f + '.xml').getroot()
    for v in r.findall('volume'):
        if v.get('id') not in vols: continue
        n = 0; hv2 = 0; hv3 = 0
        for p in v.findall('paper'):
            s = txt(p.find('title')) + ' ' + txt(p.find('abstract')); n += 1
            if A_.search(s) and B_.search(s) and (C2.search(s) or C3.search(s)):
                hv3 += 1; hv2 += bool(C2.search(s))
        rows.append(['ACL Anthology', '%s.%s' % (f, v.get('id')), v.find('meta').findtext('year'), n, hv2, hv3 - hv2]); tot += n; th += hv3
ACC = {'Poster', 'Spotlight', 'Oral', 'Top-25%', 'Top-5%', 'Technical', 'ICLR 2026 ConditionalPoster', 'ICLR 2026 ConditionalOral'}
TRK = {'main', 'Datasets & Benchmarks', 'aaai special track'}
for f in sorted(glob.glob(os.path.join(RAW, '..', 'metadata', '*', '*.json'))):
    X = json.load(open(f)); byt = collections.defaultdict(lambda: [0, 0, 0])
    for x in X:
        if x.get('status') not in ACC or x.get('track') not in TRK: continue
        s = (x.get('title') or '') + ' ' + (x.get('abstract') or '').strip(); t = byt[x['track']]; t[0] += 1
        if A_.search(s) and B_.search(s) and (C2.search(s) or C3.search(s)):
            t[2] += 1; t[1] += bool(C2.search(s))
    for trk, (n, h2, h3) in sorted(byt.items()):
        rows.append(['OpenReview/proceedings', os.path.basename(f)[:-5] + ' / ' + trk, re.sub(r'\D', '', os.path.basename(f)), n, h2, h3 - h2]); tot += n; th += h3
assert tot == 72097 and th == 1204, (tot, th)
rows.append(['합계', '', '', tot, sum(r[4] for r in rows), sum(r[5] for r in rows)])
rows += [[''], ['검색식(제목+초록, 대소문자 무시, 단어 경계)'], ['K1 에이전트', A_.pattern], ['K2 모델', B_.pattern], ['K3 기본 보안 용어', C2.pattern], ['K4 확장 안전·정책 용어', C3.pattern],
         ['결합', '기본: K1 ∧ K2 ∧ K3 / 확장: K1 ∧ K2 ∧ (K3 ∨ K4)'],
         ['제외 트랙', 'ACL 계열 데모·산업·학생 연구 트랙과 워크숍, ICML·NeurIPS 포지션 트랙, NeurIPS 저널 트랙, AAAI의 IAAI·EAAI·학생·데모·박사과정·신진 교수·시니어 멤버·저널 트랙, IJCAI의 서베이·데모·저널·AI for Good·예술·박사과정·초기 경력·자매 학회·Late 트랙']]
sheet('S12_SearchScope', ['source', 'venue/volume/track', 'year', 'population', 'hits_basic(V2)', 'hits_expanded_only(V3)'], rows, {'source': 24, 'venue/volume/track': 46})

# S13 first public
fpsrc = collections.Counter(first_public(c)[1] for c in D if c['id'] in known_adv)
rows = [['규칙', 'arXiv 첫 판 제출 연월(v1) → 없으면 arXiv 식별자의 연월(id) → 없으면 학회 개최월(venue, 아래 가정)'], ['적응형 평가 시기 분할', '2025-02 이전(<2025-03) / 2025-03 이후'],
        ['공격자 상정·적응형 평가 확인 가능 방어의 근거 분포', json.dumps(dict(fpsrc))], [''], ['학회·연도', '가정 월']]
rows += [['%s %s' % k, v] for k, v in sorted(VENUE_MONTH.items())]
at = S['adaptive_time']
rows += [[''], ['결과', '이전 %d/%d, 이후 %d/%d (Fisher 정확 검정 p=%.3f)' % (at['before'][0], at['before'][1], at['after'][0], at['after'][1], at['fisher_p'])]]
sheet('S13_FirstPublic', ['항목', '값'], rows, {'항목': 46, '값': 90})

# S14 rules
cb = open(W + 'CODEBOOK_v3.md').read()
rules = re.findall(r'^- (R[1-6].*)$', cb, re.M)
assert len(rules) == 6
rows = [[r[:2], '불일치 판정 과정에서 명시(2026-10-01, 1차 선별·코딩 조정)' if r[:2] != 'R6' else '2차 선별(후보 전체 두 실행의 선별)의 불일치 판정에서 추가(2026-10-01)', r] for r in rules]
sheet('S14_Rules', ['rule', 'added', 'text'], rows, {'added': 50, 'text': 140}, note='세부 판정 기준은 추가 이후의 판정과 최종 결정에 적용하였다. 선별 실행 A 1,289편과 실행 B 300편은 세부 판정 기준 추가 전에, 실행 B 989편은 세부 판정 기준 1–5 추가 후에 판정되었다(S2_Screening의 passA_codebook, passB_codebook 열). 두 실행 모두 제외로 일치한 판정은 세부 판정 기준 추가 후 재판정하지 않았고, 그중 무작위 150편만 세부 판정 기준 1–5를 포함한 선별 코딩북으로 점검하였다(S9). 두 실행의 초록 코딩의 두 실행은 세부 판정 기준 1–4가 있는 코딩북을, 추가 포함 5편의 두 실행의 코딩은 세부 판정 기준 1–6이 있는 코딩북을 사용하였다.')

# S15 defense eval raw
rows = [[c['id'], c['title'][:70], c['route'], c['D'], c['ft_adversarial'], c['ft_adaptive'], c['ft_bench'], c['ft_public_bench'], c['ft_n_models'], c['ft_utility'], c['ft_overhead'], c['ft_fpr'], c['ft_hitl_burden'], c['ft_decisions']] for c in D]
sheet('S15_Defense_Eval', ['id', 'title', 'route', 'D', 'adversarial', 'adaptive', 'bench', 'public_bench', 'n_models', 'utility', 'overhead', 'fpr', 'hitl_burden', 'decisions'], rows, {'title': 50, 'bench': 50})

# ---------------------------------------------------------------- v14: cross-model checks (claude-sonnet-5-5)
XS = json.load(open(W + 'XMODEL14.json')); XB = json.load(open(W + 'XMODEL14b.json'))
key = json.load(open(W + 'xmodel/KEY_screen.json')); MID = {m['id']: m for m in M}
xr = list(csv.DictReader(open(W + 'xmodel/xs_result.tsv'), delimiter='\t'))
rows = [[r['id'], key[r['id']]['id'], MID[key[r['id']]['id']]['title'][:90], key[r['id']]['path'], 'INC' if key[r['id']]['final_inc'] else 'EXC', r['decision'], r['exc_reason'], r['borderline'], r['note']] for r in xr]
xs = XS['screen']
sheet('S16_XModel_Screen', ['sample_id', 'candidate_id', 'title', 'stratum', 'final_decision', 'other_model_decision', 'other_exc_reason', 'other_borderline', 'other_note'], rows, {'title': 60, 'other_note': 70},
      note='다른 모델 claude-sonnet-5-5의 선별 재판정(세부 판정 기준 1–5가 있는 선별 코딩북). n=%d, 관찰 일치도 %.2f, κ %.2f, PABAK %.2f. 최종 포함 %d편, 다른 모델 포함 %d편, 불일치 %d편(최종 제외·다른 모델 포함 %d편, 최종 포함·다른 모델 제외 %d편).' % (xs['n'], xs['po'], xs['kappa'], xs['pabak'], xs['pos_final'], xs['pos_other'], xs['disagree'], xs['final_exc_other_inc'], xs['final_inc_other_exc']))
rows = [[k, v['n'], v['po'], v['kappa'], v['pabak'], v['pos_final'], v['pos_other']] for k, v in list(XS['code']['per_label'].items()) + list(XS['code30']['per_label'].items())]
sheet('S17_XModel_Abstract', ['label', 'n', 'observed_agreement', 'kappa', 'pabak', 'positives_final', 'positives_other_model'], rows, {'label': 22},
      note='다른 모델의 초록 코딩 재판정. 분석 대상에서 무작위로 뽑은 %d편. 방어 범주 D1–D6은 두 쪽 모두 방어로 코딩한 %d편, T5 하위 유형은 두 쪽 모두 T5로 코딩한 %d편 기준. 30개 라벨의 κ %.2f–%.2f, 중앙값 %.2f.' % (XS['code']['n'], XS['code30']['n_def'], XS['code30']['n_t5'], XS['code30']['min'], XS['code30']['max'], XS['code30']['median']))
rows = [[k, v['n'], v['po'], v['kappa'], v['pos_final'], v['pos_other'], v['disagree']] for k, v in XB['items'].items()]
aa = XB['adaptive_all']
rows += [[''], ['적응형 평가, 두 표본 합산', aa['n'], '', '', aa['final_pos'], aa['final_pos_other_pos'] + aa['final_neg_other_pos'], aa['final_neg_other_pos']], ['  최종 양성 중 다른 모델도 양성', aa['final_pos_other_pos'], '/', aa['final_pos']], ['  최종 음성 중 다른 모델은 양성', aa['final_neg_other_pos'], '/', aa['final_neg']]]
K1 = json.load(open(os.path.join(RAW, 'xmodel2', 'xmodel2_KEY_ft.json'))); K2 = json.load(open(os.path.join(RAW, 'xmodel2', 'xmodel2_KEY_ft2.json')))
rows += [[''], ['sample', 'rid', 'corpus_id', 'title', 'final: stage|A_mode|judge|judge_input|adversarial|adaptive', 'other: stage|A_mode|judge|judge_input|adversarial|adaptive', 'other_src']]
for kk, KK in ((1, K1), (2, K1), (3, K1), (4, K2), (5, K2)):
    for r in csv.DictReader(open(os.path.join(RAW, 'xmodel2', 'ft_out_%d.tsv' % kk)), delimiter='\t'):
        c = CID[KK[r['rid']]]
        rows.append(['random30' if kk <= 3 else 'adaptive_suppl24', r['rid'], c['id'], c['title'][:70], '|'.join(str(c.get(x, '')) for x in ('ft_stage', 'ft_A_mode', 'ft_judge', 'ft_judge_input', 'ft_adversarial', 'ft_adaptive')),
                     '|'.join(r[x] for x in ('stage', 'A_mode', 'judge', 'judge_input', 'adversarial', 'adaptive')), r['src'][:120]])
sheet('S18_XModel_FullText', ['item', 'n', 'observed_agreement', 'kappa', 'positives_final', 'positives_other_model', 'disagreements'], rows, {'item': 30, 'kappa': 12},
      note='다른 모델의 원문 재코딩. 원문 URL이 기록된 방어 %d편에서 무작위로 뽑은 30편(시드 20261003)의 21개 항목, κ %.2f–%.2f, 중앙값 %.2f. 적응형 평가는 무작위 표본에 최종 양성이 1편뿐이어서 양성으로 코딩된 나머지 15편과 무작위 음성 9편(시드 20261004)을 추가로 재코딩하였다. 아래쪽 행은 문헌별 값이다.' % (XB['frame'], XB['all_min'], XB['all_max'], XB['all_median']))
ad = XB['adj']; rows = []
aj = {m: {r['id']: r for r in csv.DictReader(open(os.path.join(RAW, 'xmodel2', 'adj8_out_%s.tsv' % m)), delimiter='\t')} for m in ('opus', 'sonnet')}
xsr = {r['id']: r for r in xr}
for i in ad['detail']:
    rows.append([i, key[i]['id'], MID[key[i]['id']]['title'][:80], 'INC' if key[i]['final_inc'] else 'EXC', xsr[i]['decision'], aj['opus'][i]['decision'], aj['opus'][i]['exc_code'], aj['sonnet'][i]['decision'], aj['sonnet'][i]['exc_code'],
                 aj['opus'][i]['src'][:100], aj['opus'][i]['rationale'][:600], aj['sonnet'][i]['rationale'][:600]])
rows += [[''], ['표본의 최종 제외 문헌', ad['sample_final_exc']], ['두 모델 모두 포함', ad['both_inc'], '%.1f%%' % ad['miss_pct'], 'Wilson 95%% %s' % ad['miss_ci']], ['코딩에 쓴 모델만 포함한 1편을 더한 경우', ad['hi'], '%.1f%%' % ad['hi_pct'], 'Wilson 95%% %s' % ad['hi_ci']],
         ['경로 1의 제외 문헌', ad['path1_excluded']], ['경로 1 제외 문헌 중 포함으로도 판정될 수 있는 경계 사례의 추정 편수', '%d–%d' % (ad['est'], ad['hi_est']), '구간 %d–%d' % (ad['est_ci'][0], ad['hi_est_ci'][1])], ['경로 1 포함 문헌 %d편 대비' % ad['path1_included'], '%d–%d%%' % (ad['share_lo'], ad['share_hi'])]]
sheet('S19_XModel_Adjud', ['sample_id', 'candidate_id', 'title', 'final_decision', 'other_model_abstract', 'main_model_fulltext', 'main_exc', 'other_model_fulltext', 'other_exc', 'src', 'main_model_rationale', 'other_model_rationale'], rows,
      {'title': 50, 'main_model_rationale': 80, 'other_model_rationale': 80, 'src': 40},
      note='선별 재판정에서 최종 결정과 갈린 8편을 두 모델(claude-opus-5-5, claude-sonnet-5-5)이 각각 원문으로 다시 판정한 결과. 이러한 경계 사례에는 사전에 정한 절차, 곧 실행 A·B의 판정과 조정 결과를 일관되게 적용하였다. 근거 인용은 웹 조회 도구의 추출 결과에 근거한다.')

out = os.path.join(RAW, '..', 'corpus_and_results.xlsx')
wb.save(out); print('saved', out, [ws.title for ws in wb.worksheets])
