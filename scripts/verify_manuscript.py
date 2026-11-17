import os
RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'raw')
# v15: check every reported number in the manuscript against STATS10.json / FINAL_CORPUS.json (independent of the text file).
# Text is read from v15.docx; floating text boxes (tables, figures) are extracted separately, table rows as ' | '.
import json, re, sys, zipfile, csv, math, collections
from lxml import etree
S = json.load(open(os.path.join(RAW, 'STATS10.json')))
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
DOCX = sys.argv[1] if len(sys.argv) > 1 else 'manuscript.docx'
z = zipfile.ZipFile(DOCX); r = etree.fromstring(z.read('word/document.xml'))
def _inner(e, p):
    a = e.getparent()
    while a is not None and a is not p:
        if a.tag == W + 'txbxContent': return True
        a = a.getparent()
    return False
def ptxt(p):
    s = ''
    for e in p.iter(W + 't', W + 'br'):
        if _inner(e, p): continue
        s += (e.text or '') if e.tag == W + 't' else ' '
    return s
def ctext(c):
    s = ''
    for e in c.iter():
        if e.tag == W + 't': s += e.text or ''
        elif e.tag == W + 'br': s += ' '
    return s
def block(e, out):
    if e.tag == W + 'p':
        out.append(ptxt(e))
        for tb in e.iter(W + 'txbxContent'):
            out.append('[FLOAT]')
            for ch in tb: block(ch, out)
            out.append('[/FLOAT]')
    elif e.tag == W + 'tbl':
        for tr in e.findall(W + 'tr'): out.append(' | '.join(ctext(tc) for tc in tr.findall(W + 'tc')))
body = r.find(W + 'body'); lines = []
for e in body: block(e, lines)
T = '\n'.join(lines)
open(DOCX.replace('.docx', '.txt'), 'w').write('\n'.join('L%d: %s' % (i + 1, x) for i, x in enumerate(lines) if x.strip()))
ok = 0; bad = []
def need(s, why=''):
    global ok
    if s in T: ok += 1
    else: bad.append((s, why))
def wil(k, n, z_=1.96):
    p = k / n; d = 1 + z_ * z_ / n; c = p + z_ * z_ / (2 * n); h = z_ * math.sqrt(p * (1 - p) / n + z_ * z_ / (4 * n * n))
    return (round(100 * (c - h) / d), round(100 * (c + h) / d))
N = S['N']; ND = S['Ndef']; t = S['T']; a = S['actor']; v = S['viol']
pc = lambda k, n: round(100 * k / n)
# ---------- v15 checks: every number stated in the manuscript text, tables and notes
CC = json.load(open(os.path.join(RAW, 'FINAL_CORPUS.json')))
def LL(x): return [] if x in (None, '', '-', '?') else [y.strip() for y in re.split(r'[;,]', x) if y.strip() and y.strip() not in ('-', '?')]
DD = [c for c in CC if 'D' in LL(c['type'])]
ms = S['multistage']; sp = S['sep']; ji = S['judge_input']; l = S['llm']; A = S['A']; am = S['A_mode']; st = S['stage']; ap = S['adaptive']; ev = S['eval']; nm = S['n_models']
s2 = S['strata2']; ad = S['adv_only']; a2 = S['adv_only2']; pg = S['pre_gate2']; ru = S['rule']; g = S['granularity']; e = S['embodied']; h = S['human2']; fs = S['ft_src']; pr = S['prisma']; k = S['screen_kappa']; ra = S['rel_abs']; jr = S['judge_input_rel']
# abstract (Korean and English), conclusion
need('분석 대상의 %d%%는 지시·목표 조작을, %d%%는 다단계 전파를' % (pc(t['T1'], N), ms['pct']))
need('방어의 %d%%는 도구 호출 경계를 집행 지점으로 삼았고, %d%%는 별도의 LLM 판정 모델을 두었으며 그중 %d%%에서 판정 모델이' % (A['pct'], sp['pct'], ji['raw_pct']))
need('공격자를 가정한 방어 중 적응형 공격으로 평가한 연구는 %d%%였다. 방어 범주는 기존' % ap['pct'])
need('Of the selected papers, %d%% addressed instruction and goal manipulation and %d%% addressed multi-step propagation' % (pc(t['T1'], N), ms['pct']))
need('Of the defenses, %d%% used the tool-call boundary as an enforcement point and %d%% used a separate LLM judge; in %d%% of these, the judge read original untrusted content directly' % (A['pct'], sp['pct'], ji['raw_pct']))
need('Of the defenses assuming an attacker, %d%% were evaluated against adaptive attacks' % ap['pct']); need('we selected %d published papers' % N); need('게재 논문 %d편을 선정' % N); need('without human coders'); need('인간 코더 없이')
need('게재 논문 %d편과 그중 방어 %d편을 분류한 결과, 지시·목표 조작을 다룬 연구가 %d%%로 가장 많았고 다단계 전파를 다룬 연구는 %d%%였다' % (N, ND, pc(t['T1'], N), ms['pct']))
need('방어의 %d%%가 도구 호출 경계를 집행 지점으로 삼았고 %d%%가 별도 LLM 판정 모델을 두었으며, 그중 %d%%는 원본 비신뢰 콘텐츠를 직접 읽었다. 공격자를 가정한 방어 중 적응형 공격으로 평가한 연구는 %d%%였다' % (A['pct'], sp['pct'], ji['raw_pct'], ap['pct']))
need('방어의 %d%%가 경로 1에서 나왔으므로' % S['path1_def_share']); need('%d편에서 초록에만 근거하므로' % (N - S['final_adjudicated'])); need('방어 %d편은 arXiv 판을 기준으로' % fs['arxiv'])
need('사람에 의한 검증은 하지 않았다'); need('게재 논문 %d편의 위협을 공격 체인 단계에 따라 분류하고, 방어 %d편의' % (N, ND)); need('GitHub 저장소에 공개한다')
# 2.2
need('72,097편'); need('일치한 문헌은 1,204편이었다'); need('후보 85편'); need('참고문헌 379편'); need('후보 13편을 찾았다')
need('포함 기준을 충족하는 21편은 모두 검색식에 일치하였고, 보안 학회 4곳의 범위 내 문헌 10편은 모두')
yr = collections.Counter(c['year'] for c in CC)
need('게재 연도는 2023년 %d편, 2024년 %d편, 2025년 %d편, 2026년 %d편이다' % (yr['2023'], yr['2024'], yr['2025'], yr['2026']))
# 2.3
_pb = set()
for _i in range(1, 7):
    for _r in csv.DictReader(open(os.path.join(RAW, 'pb/pb%d_B.tsv') % _i), delimiter='\t'): _pb.add(_r['id'])
_M = json.load(open(os.path.join(RAW, 'MASTER_SCREEN_base.json'))); _in = sum(m['id'] in _pb for m in _M)
need('실행 B는 처음 %d편 이후의 %d편에 이 기준을 적용하였다' % (len(_M) - _in, _in))
need('후보 %s편의 포함 여부를 각각 판정하였고, 실행 간 일치도는 Cohen의 κ[' % format(len(_M), ',')); need('] %.2f였다' % k['ALL']['kappa'])
need('둘 다 제외한 %s편을 빼고 %d편을 다음 단계로 넘겼으며, 조정과 초록 기준 분류 단계에서 %d편이 제외되어 %d편이 남았다. 여기에 경로 3의 후보 %d편 중 %d편을 더해 %d편' % (format(pr['both_exc'], ','), pr['forwarded'], pr['elig_excluded'], pr['included_db'], S['snowball']['candidates'], pr['snowball_inc'], pr['total']))
assert pr['forwarded'] - pr['elig_excluded'] == pr['included_db'] and pr['included_db'] + pr['snowball_inc'] == pr['total'] == N
need('이진 라벨 30개의 실행 간 κ는 %.2f–%.2f, 중앙값 %.2f였고, 불일치가 있는 %d편은' % (ra['min'], ra['max'], ra['median'], S['final_adjudicated']))
need('별도 LLM 판정 모델을 둔 %d편은 판정 모델이 받는 입력을' % ji['n']); need('분류하였고, κ는 %.2f이었다' % jr['three']['kappa'])
need('원문은 %d편에서 확보하였고 게재본이 %d편, arXiv 판이 %d편이었으며, %d편은 초록과 공개 자료로 분류하였고 1편은 확인할 수 없었다' % (fs['arxiv'] + fs['published'] + 1, fs['published'] + 1, fs['arxiv'], fs['abstract'] - 1)); assert fs['arxiv'] + fs['published'] + 1 + fs['abstract'] == ND; need('방어 %d편은 한 차례의 실행이 원문을 근거로' % ND)
X = json.load(open(os.path.join(RAW, 'XMODEL14.json'))); xs = X['screen']; xc = X['code']; x3 = X['code30']; Y = json.load(open(os.path.join(RAW, 'XMODEL14b.json'))); yc = Y['core']
need('다른 모델인 %s의 표본 재판정으로 점검' % X['model']); need('무작위로 뽑은 %d편에서 최종 결정과의 κ가 %.2f였다' % (xs['n'], xs['kappa']))
_key = json.load(open(os.path.join(RAW, 'xmodel/KEY_screen.json'))); _xr = list(csv.DictReader(open(os.path.join(RAW, 'xmodel/xs_result.tsv')), delimiter='\t'))
_dis = [r for r in _xr if (r['decision'] == 'INC') != _key[r['id']]['final_inc']]
assert len(_dis) == xs['disagree']
need('판정이 달랐던 %d편 중 %d편은 다른 모델이 스스로 경계 사례로 표시한' % (len(_dis), sum(r['borderline'] == 'Y' for r in _dis)))
_adj=json.load(open(os.path.join(RAW, 'XMODEL14b.json')))['adj']
need('%d편 가운데 최종 결정에서 제외된 문헌도 %d편이며, 이들은 분류에 쓴 모델과 다른 모델이 각각 원문으로 다시 판정하여도 모두 포함 %d편, 모두 제외 %d편, 불일치 %d편으로 갈렸다' % (_adj['n'], _adj['final_exc'], _adj['both_inc'], _adj['both_exc'], _adj['split'])); assert _adj['both_inc'] + _adj['both_exc'] + _adj['split'] == _adj['final_exc']
assert sum(not _key[r['id']]['final_inc'] for r in _dis) == _adj['final_exc'] and len(_dis) == _adj['n']
need('무작위로 뽑은 %d편에서 이진 라벨 %d개의 κ가 %.2f–%.2f, 중앙값 %.2f이었다' % (xc['n'], x3['labels'], x3['min'], x3['max'], x3['median']))
need('무작위로 뽑은 방어 %d편에서 %d개 항목의 κ 중앙값이 %.2f였다' % (Y['n'], Y['n_items'], Y['all_median']))
_core = [yc[q]['kappa'] for q in ('stage:A', 'A_pre', 'judge:SEP', 'llm_dependent', 'adversarial')]; need('도구 호출 경계, 실행 전 차단, 별도 LLM 판정 모델, LLM 의존 여부, 공격자 가정은 %.2f–%.2f, 결정론적 규칙과 계획 수립은 %.2f–%.2f이었다' % (min(_core), max(_core), Y['items']['judge:RULE']['kappa'], Y['items']['stage:P']['kappa']))
need('판정 모델이 원본을 읽는지에 대한 κ는 두 모델이 모두 별도 판정 모델로 분류한 %d편에서 %.2f이었다' % (Y['judge_input_both_sep']['n'], Y['judge_input_both_sep']['kappa']))
ya2 = Y['adaptive_all']; need('양성으로 분류된 %d편 전부를 포함한 %d편을 재판정하게 하였고 %d편이 일치' % (ya2['final_pos'], ya2['n'], ya2['n'] - ya2['final_neg_other_pos'] - (ya2['final_pos'] - ya2['final_pos_other_pos']))); assert ya2['final_pos'] == ap['n']
# 3
need('T1을 다룬 연구가 %d편, %d%%로 가장 많았고, 위협 주체는 외부 콘텐츠 제공자가 %d편, 악의적 사용자가 %d편이었다' % (t['T1'], pc(t['T1'], N), a['EXT'], a['USR']))
need('행동 무결성 %d편, 기밀성 %d편, 안전 %d편, 출력 무결성 %d편, 가용성 %d편' % (v['AI'], v['C'], v['S'], v['OI'], v['AV']))
need('다단계 전파를 다룬 연구는 %d편, %d%%였고, 그중 %d편은 T6이나 T2에도' % (ms['n'], ms['pct'], ms['T6'] + ms['T2'] - ms['both']))
_t1 = [c for c in CC if 'T1' in LL(c['T'])]
need('T1 연구 %d편은 중복을 포함해 %d편이 외부 콘텐츠 제공자를, %d편이 악의적 사용자를' % (len(_t1), sum('EXT' in LL(c['actor']) for c in _t1), sum('USR' in LL(c['actor']) for c in _t1))); assert len(_t1) == t['T1']
sub = S['T5sub']; need('%d편은 중복을 포함해 T5a 권한·인가 우회 %d편, T5b 안전 규칙 위반 %d편, T5c 자원 남용 %d편' % (t['T5'], sub['a'], sub['b'], sub['c']))
need('%d편 중 %d편은 위협 주체가 악의적 사용자이거나 공격자가 없는' % (S['T5b_only_USR_NON'][1], S['T5b_only_USR_NON'][0]))
need('지시·목표 조작을 다룬 연구가 %d%%로 가장 많았고, 위협 주체로는 외부 콘텐츠 제공자 다음으로 악의적 사용자가 %d%%를 차지하였다' % (pc(t['T1'], N), pc(a['USR'], N)))
need('다단계 전파를 다룬 연구는 %d%%였고, 그중 %d%%는 메모리나' % (ms['pct'], round(100 * (ms['T6'] + ms['T2'] - ms['both']) / ms['n'])))
for kk in ['T1', 'T2', 'T3', 'T4', 'T5', 'T6']:
    ab, d = S['tab1'][kk]; need('| %d/%d/%d' % (t[kk], ab, d), 'tab2 ' + kk)
# 4
need('방어 %d편 중 %d편은 둘 이상의 범주를 결합' % (ND, S['multiD']))
pd_ = S['perD']; names = {'D1': '입력 보호', 'D2': '정보 흐름 제어', 'D3': '도구·계획 격리', 'D4': '인가·정책 집행', 'D5': '런타임 탐지', 'D6': '인간 감독'}
stg = {'D1': 'I %d, A %d' % (pd_['D1']['stages']['I'], pd_['D1']['stages']['A']), 'D2': 'I %d, A %d' % (pd_['D2']['stages']['I'], pd_['D2']['stages']['A']),
       'D3': 'A %d, P %d, C %d' % (pd_['D3']['stages']['A'], pd_['D3']['stages']['P'], pd_['D3']['stages']['C']), 'D4': 'A %d, P %d' % (pd_['D4']['stages']['A'], pd_['D4']['stages']['P']),
       'D5': 'A %d, C %d, I %d' % (pd_['D5']['stages']['A'], pd_['D5']['stages']['C'], pd_['D5']['stages']['I']), 'D6': 'A %d' % pd_['D6']['stages']['A']}
for dk, dd in pd_.items():
    row = [l_ for l_ in lines if l_.startswith('%s %s %d편 |' % (dk, names[dk], dd['n']))]
    if len(row) == 1 and (' | %s | ' % stg[dk]) in row[0] and (' | %d/%d | ' % (dd['llm'], dd['llm_policy'])) in row[0]: ok += 1
    else: bad.append(('tab3 row', dk, row[:1]))
need('D2 %d편 중 %d편과 D3 %d편 중 %d편은 LLM 의존 방어이고' % (pd_['D2']['n'], pd_['D2']['llm'], pd_['D3']['n'], pd_['D3']['llm']))
need('D6 인간 감독으로 분류된 방어는 %d편이지만, 원문 기준으로 사용자 확인을 판정 주체나 결정 유형으로 쓰는 방어는 %d편이었다. 그중 보고 여부를 확인할 수 있는 %d편에서 확인 요청의 빈도와 같이 사용자에게 주는 부담을 보고한 연구는 %d편' % (S['human']['D6'], h['n'], h['known'], h['burdenY']))
need('A 도구 호출 경계를 포함한 방어가 %d편, %d%%로 가장 많았고, 그중 실행 전에 차단·수정할 수 있는 방어는 %d편으로 전체의 %d%%였다' % (A['n'], A['pct'], am['pre'], pc(am['pre'], ND)))
for s_, row in S['tab3'].items():
    name = {'I': 'I 입력 수신', 'P': 'P 계획 수립', 'M': 'M 메모리 쓰기·읽기', 'A': 'A 도구 호출 경계', 'O': 'O 최종 응답 출력', 'C': 'C 에이전트 간 통신', 'ALL': '전체'}[s_]
    need(name + ' | ' + ' | '.join(str(x) for x in row), 'tab4 ' + s_)
need('별도 LLM 판정 모델을 둔 방어는 %d편으로 %d%%였고, 그중 %d편, 즉 %d%%에서 판정 모델이' % (sp['n'], sp['pct'], ji['RAW'], ji['raw_pct']))
need('파생 콘텐츠만 받는 경우는 %d편, 신뢰 입력만 받는 경우는 %d편이었고 %d편은 확인할 수 없었다' % (ji['DERIVED'], ji['TRUSTED'], ji['unknown']))
need('강건성에 의존하는 방어는 %d편, %d%%였으며, 이 둘을 합친 LLM 의존 방어는 %d편, %d%%이다' % (S['selfonly']['n'], pc(S['selfonly']['n'], ND), l['n'], l['pct'])); assert l['n'] == sp['n'] + S['selfonly']['n']
llmset = [c for c in DD if 'SEP' in LL(c['ft_judge']) or 'SELF' in LL(c['ft_judge'])]
rl = [c for c in DD if 'RULE' in LL(c['ft_judge']) and c['ft_policy_src'] in ('LLM', 'MIX')]
nol = [c for c in DD if c not in llmset and c not in rl]
unk = [c for c in nol if '?' in (c['ft_judge'] or '') or c['ft_policy_src'] in ('?', '') or (c['ft_judge'] or '').strip() in ('', '?')]
rest = [c for c in DD if c not in llmset]
need('나머지 %d편 중 %d편은 판정과 정책 생성 어디에도 LLM이 관여하지 않았고, %d편은 결정론적 규칙이 집행하는 정책을 LLM이 생성하였으며, %d편은 확인할 수 없었다' % (len(rest), len(nol) - len(unk), len(rest) - len(nol), len(unk)))
need('결정론적 규칙으로 집행하는 방어 전체로 보면 %d편 중 %d편에서' % (ru['n'], ru['llm_policy']))
need('방어의 %d%%인 %d편이 나온 경로 1에서는 LLM 의존 방어가 %d편, %d%%였으나, 경로 2의 방어 %d편에서는 %d편이었고 결정론적 규칙을 쓰는 방어가 %d편' % (S['path1_def_share'], s2['FULL']['n'], s2['FULL']['llm'], pc(s2['FULL']['llm'], s2['FULL']['n']), s2['SEC']['n'], s2['SEC']['llm'], s2['SEC']['rule']))
need('공격자를 가정한 방어 %d편으로 한정해도 LLM 의존 방어의 비율 %d%%와 원본을 직접 읽는 판정 모델의 비율 %d%%는 같았다' % (ad['n'], ad['llm_pct'], a2['sep_raw_pct'])); assert ad['llm_pct'] == l['pct'] and a2['sep_raw_pct'] == ji['raw_pct']
need('T1을 다룬 방어가 %d편인 반면 T2는 %d편, T3은 %d편' % (S['tab1']['T1'][1], S['tab1']['T2'][1], S['tab1']['T3'][1]))
t6 = S['T6def']; need('T6을 다룬 방어 %d편 중 결정론적 규칙을 쓰는 방어는' % t6['n']); need('를 포함한 %d편이었다' % t6['rule'])
need('최종 응답 출력 O를 검사하는 방어는 %d편' % st['O'])
need('방어가 가장 많이 개입하는 지점은 도구 호출 경계로 %d%%이고, 이 경계에서 실행 전에 차단·수정하는 방어는 %d%%이다. 방어의 %d%%는 허용 여부의 판정을 LLM에 의존하며, 별도 판정 모델의 %d%%는' % (A['pct'], pc(am['pre'], ND), l['pct'], ji['raw_pct']))
need('95%% Wilson 신뢰구간은 도구 호출 경계 %d%%에 대해 %d–%d%%, 별도 LLM 판정 모델 %d%%에 대해 %d–%d%%, 그중 원본 비신뢰 콘텐츠를 직접 읽는 %d%%에 대해 %d–%d%%, LLM 의존 방어 %d%%에 대해 %d–%d%%' % (
    A['pct'], A['ci'][0], A['ci'][1], sp['pct'], sp['ci'][0], sp['ci'][1], ji['raw_pct'], ji['raw_ci'][0], ji['raw_ci'][1], l['pct'], l['ci'][0], l['ci'][1]))
_self = [c for c in DD if 'SELF' in LL(c['ft_judge'])]; need('에이전트 모델 자체 %d편에는 별도 판정 모델도 함께 둔 %d편이' % (len(_self), sum('SEP' in LL(c['ft_judge']) for c in _self)))
# 5
need('공격자를 가정한 방어 %d편 중 평가 여부를 확인할 수 있는 %d편에서 적응형 공격으로 평가한 연구는 %d편, %d%%였고, 방어의 판정을 최적화 루프에 넣은 평가는 %d편' % (ap['adv'], ap['known'], ap['n'], ap['pct'], ap['lvl2']))
need('방어 90편 중 %d편은 자체 환경을 하나 이상 사용' % S['own_env']); need('확인할 수 있는 %d편 중 %d편, %d%%가 공개 벤치마크를 하나 이상' % (ev['public_bench'][1], ev['public_bench'][0], ev['public_bench'][2]))
need(']로 %d편이었다' % S['agentdojo']); need('%d편에서 그 중앙값은 %d개였고 %d편은 단일 모델로만' % (nm['known'], nm['median'], nm['one']))
need('보고한 연구는 각각 %d%%, %d%%, %d%%였다' % (ev['utility'][2], ev['overhead'][2], ev['fpr'][2]))
need('| %d%%, %d/%d편' % (ap['pct'], ap['n'], ap['known'])); need('공개 벤치마크 %d%%, %d/%d편' % (ev['public_bench'][2], ev['public_bench'][0], ev['public_bench'][1])); need('모델 수 중앙값 %d개' % nm['median'])
need('| %d%%, %d/%d편' % (ev['utility'][2], ev['utility'][0], ev['utility'][1])); need('| %d%%, %d/%d편' % (ev['overhead'][2], ev['overhead'][0], ev['overhead'][1]))
need('오탐률 %d%%, %d/%d편' % (ev['fpr'][2], ev['fpr'][0], ev['fpr'][1])); need('확인 요청 부담 %d/%d편' % (h['burdenY'], h['known']))
need('RP2 %d–%d%%, RP3 %d–%d%%, RP4 %d–%d%%, RP5 %d–%d%%, RP6 오탐률 %d–%d%%' % (ap['ci'][0], ap['ci'][1], ev['public_bench'][3][0], ev['public_bench'][3][1], ev['utility'][3][0], ev['utility'][3][1], ev['overhead'][3][0], ev['overhead'][3][1], ev['fpr'][3][0], ev['fpr'][3][1]))
need('공격자를 가정한 방어 중 적응형 공격으로 평가한 연구는 %d%%에 그쳤고' % ap['pct'])
# 6
need('별도 판정 모델을 둔 방어는 %d편, 방어 %d편의 %d%%였고' % (ji['RAW'], ND, pc(ji['RAW'], ND)))
pre = [c for c in DD if 'A' in LL(c['ft_stage']) and (c['ft_A_mode'] or '').strip().lower().startswith('pre')]
raw = [c for c in pre if 'SEP' in LL(c['ft_judge']) and c['ft_judge_input'] == 'RAW']
need('방어 %d편 중 %d편은 별도 LLM 판정 모델을 두었고, 그중 %d편의 판정 모델은 원본 비신뢰 콘텐츠를 직접 받았다' % (pg['n'], pg['sep'], pg['sep_raw'])); assert len(raw) == pg['sep_raw'] and len(pre) == pg['n'] == am['pre']
need('이 %d편에서는 같은 행동의' % len(raw)); need('이 가운데 %d편은 집행 지점이 도구 호출 경계 하나뿐이어서 원본을 읽는 판정이 곧 실행 전 판정이고, 나머지 %d편에서는' % (sum(len(LL(c['ft_stage'])) == 1 for c in raw), sum(len(LL(c['ft_stage'])) >= 2 for c in raw))); need('에이전트 모델 자체가 판정하는 %d편에서는' % pg['selfonly'])
need('별도 판정 모델이 원본 비신뢰 콘텐츠를 직접 읽는 방어 %d편, %d%%에서는' % (ji['RAW'], pc(ji['RAW'], ND))); need('결정론적 규칙으로 집행하는 방어 %d편 중 %d편은 정책이나 계획을 LLM이' % (ru['n'], ru['llm_policy']))
# 7
need('개별 행동 단위로 판정한 방어는 %d편, 여러 단계의 궤적 단위로 판정한 방어는 %d편이었고 %d편은 두 단위를 모두 썼으며, 궤적 단위 방어 %d편 중 %d편은 LLM 의존 방어' % (g['ACTION'], g['TRAJ'], g['both'], g['TRAJ'], g['TRAJ_llm']))
need('%d편이며, 중복을 포함해 공격 %d편, 벤치마크 %d편, 방어 %d편' % (e['n'], e['A'], e['B'], e['D']))
emb = [c for c in CC if (c.get('embodied') or '').upper().startswith('Y')]
e5 = [c for c in emb if 'T5' in LL(c['T'])]; e5b = [c for c in e5 if 'b' in LL(c['T5sub'])]; e5a = [c for c in e5 if 'a' in LL(c['T5sub'])]; edef = [c for c in emb if 'D' in LL(c['type'])]
if len(emb) == e['n'] and len(e5) == len(e5b) and not e5a and all((c['ft_adversarial'] or '').upper().startswith('N') for c in edef):
    need('T5에 해당하는 %d편은 T5b 안전 규칙 위반만 다루었고 방어 %d편은 모두 공격자를 가정하지 않았다. 곧 물리 환경에서 권한·인가 우회를' % (len(e5), len(edef)))
else: bad.append(('embodied',))
# forbidden phrases / terminology (v15 rules)
for bad_term in ['판정자', '원천 비신뢰', '적대자', '견고화', '과차단', '판정기', '계보', '실현 단계', '동료 심사', '적응형 공격자 평가', '검사기', '입력 수용', '세칙', 'LLM 기반 보조 도구', 'LLM checker',
                 '접근 통제', '흐름 통제', '사용 통제', 'LLM 판정 방어', '첫째 경로', '둘째 경로', '첫째 과정', '둘째 과정', '인스턴스', '실행 감시기', '성립 전제', '입장 논문', '이중 판정', '이중 코딩',
                 '절반을 넘는다', '케이퍼빌리티', '판정 구성요소', '구조로 보장', '검토 부담', '다단계 경로', 'arXiv 2판', '미측정', '확인 부담', '검토자', 'deciding component', '보충 자료', '누락', '코딩', '서베이: 공격',
                 '7.4절', '6.1절에서', 'RQ1:', 'RQ2:', 'RQ3:', 'RQ4:', 'supplementary']:
    if bad_term in T.replace('디코딩',''): bad.append(('term', bad_term))
print('checked', ok, 'mismatches', len(bad))
for b in bad: print('XX', b)
