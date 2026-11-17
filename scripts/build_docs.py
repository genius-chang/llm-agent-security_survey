import os
RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'raw')
# Builds S2_Codebooks_Prompts.md (then .docx via pandoc): protocol, codebooks, search logs, verbatim run prompts.
import json, glob, os, re
SA = '/root/.claude/projects/-home-claude/63729225-5277-5d00-85c2-218f28e7e8b8/subagents/'
import os
W = RAW + os.sep
EXCL = re.compile(r'Review|review|Fact|fact|Verify reference|final check|Third-round|logic audit|Re-audit|Final error check|consistency check|concision check|reviewer check')
def prompt_of(f):
    for l in open(f):
        d = json.loads(l)
        if d.get('type') == 'user':
            c = d['message']['content']
            if isinstance(c, list):
                c = '\n'.join(x.get('text', '') for x in c if isinstance(x, dict) and x.get('type') == 'text' and not x.get('text', '').lstrip().startswith('<system-reminder>'))
            return re.sub(r'<system-reminder>.*?</system-reminder>', '', c, flags=re.S).strip()
    return ''
def model_of(f):
    ms = set()
    for l in open(f):
        d = json.loads(l); m = d.get('message', {})
        if isinstance(m, dict) and m.get('model'): ms.add(m['model'])
    return ', '.join(sorted(ms))
runs = []
for f in sorted(glob.glob(SA + '*.jsonl'), key=os.path.getmtime):
    meta = json.load(open(f.replace('.jsonl', '.meta.json')))
    desc = meta.get('description', '')
    if EXCL.search(desc): continue
    runs.append((desc, model_of(f), prompt_of(f)))
out = []
out.append('# 검색 프로토콜, 분류 기준(코딩북), 검색 로그, 실행 지시문\n')
out.append('본 자료는 익명 심사본과 함께 공개하는 자료이다. 모든 선별·코딩·조정은 인간 코더 없이 LLM의 별도 실행이 수행하였다. '
           '각 실행은 아래 지시문과 해당 코딩북만 입력으로 받았으며, 같은 문헌을 판정하는 두 실행은 서로의 결과 파일을 열지 않도록 지시되었다. '
           '실행은 Claude Agent SDK 기반의 에이전트 실행 환경에서 하위 에이전트로 이루어졌고 디코딩 설정은 지정하지 않았다. 웹 문서는 질의에 대한 추출 결과를 돌려주는 웹 조회 도구로 읽었다. '
           '코딩북과 지시문은 실행 당시의 원문이어서 일부 용어가 원고의 최종 용어와 다르다. 코딩은 분류, 코딩북은 분류 기준, 판정기는 판정 모델, 적대자는 공격자, 통제는 제어, 원천은 원본, 세칙은 세부 판정 기준, 과정이나 코더 A·B는 실행 A·B에 해당한다. '
           '원고 검토(방법론·문체·사실·서지 점검)에 쓴 실행은 데이터 생성에 관여하지 않았으므로 지시문을 수록하지 않았다. 파일 경로는 작업 환경의 경로를 그대로 두었다.\n')
out.append('## 1. 실행 목록\n')
out.append('| 순서 | 실행 | 기록된 모델 식별자 |\n|---|---|---|')
for i, (d, m, p) in enumerate(runs, 1): out.append('| %d | %s | %s |' % (i, d, m))
out.append('\n실행과 최종 데이터의 대응(번호는 위 표): 선별 실행 A의 판정은 실행 1–9(학회군별 검색·선별, 재판정, 통합)와 13–15(확장 용어 후보 선별)에서 나왔다. '
           '선별 실행 B는 실행 11(150편 표본, 세부 판정 기준 없음), 22(확장 후보 150편 표본, 세부 판정 기준 없음), 35–40(나머지 989편과 경로 3 후보, 세부 판정 기준 R1–R5)이다. 선별 불일치 조정은 23, 41, 42, '
           '경로 3 후보 확인은 20, 초록 확보는 24이다. 초록 코딩의 실행 A·B는 25–28(세부 판정 기준 R1–R4)과 43–44(추가 포함 5편, 세부 판정 기준 R1–R6), 그 조정은 29–30과 46이다. '
           '방어 원문 코딩은 16–19, 21, 31, 33, 45, 같은 모델의 무작위 재코딩 표본은 32, 34이다. 판정 모델 입력의 실행 A·B는 48–51, 그 조정은 52이며, 두 실행이 모두 제외한 후보의 점검은 47이다. '
           '실행 10(초기 집행 지점 코딩)과 12(초기 코더 B)의 결과는 최종 집계에 쓰이지 않았다. '
           '다른 모델 claude-sonnet-5-5의 점검은 실행 %s이다. 선별 200편과 초록 코딩 60편, 원문 코딩 30편(세 실행)과 적응형 평가 추가 표본 24편(두 실행), 선별에서 갈린 8편의 원문 재판정이며, 같은 8편은 코딩에 쓴 모델 claude-opus-5-5의 별도 실행도 원문으로 재판정하였다.\n' % ', '.join(str(i) for i, (d, m, p) in enumerate(runs, 1) if 'sonnet' in m or 'main model' in d))
out.append('## 2. 검색·선별 프로토콜\n')
out.append(open(W + 'PROTOCOL.md').read())
for title, fn in [('3. 코딩북 v1(초기 독립 선별·코딩용)', 'CODEBOOK.md'), ('4. 코딩북 v3(선별·초록 코딩, 세부 판정 기준 R1–R6 포함 현재 판)', 'CODEBOOK_v3.md'),
                  ('5. 블라인드 선별 코딩북(둘째 과정 989편과 제외 점검에 사용, 세부 판정 기준 R1–R5)', 'pb/CODEBOOK_SCREEN.md'), ('6. 초록 코딩 코딩북(추가 포함 문헌, 세부 판정 기준 R1–R6)', 'pb/CODEBOOK_CODE.md'),
                  ('7. 원문 코딩 코딩북(방어 90편)', 'EVAL_CODEBOOK_v2.md'), ('8. 판정 모델 입력(노출 수준) 코딩북', 'pb/EXPOSURE_CODEBOOK.md'),
                  ('8a. 다른 모델 원문 재코딩 코딩북(7과 8을 합친 판)', '../xmodel2/CODEBOOK_FT.md'), ('8b. 선별 불일치 원문 재판정 코딩북', '../xmodel2/CODEBOOK_ADJ.md')]:
    out.append('\n## %s\n\n원본 파일: `%s`\n' % (title, fn))
    out.append(re.sub(r'^(#+) ', lambda m: '#' * (len(m.group(1)) + 2) + ' ', open(W + fn).read(), flags=re.M))
out.append('\n## 9. 검색 로그\n')
for fn in ['G1_security.log.md', 'G2_ml.log.md', 'G3_nlp.log.md', 'G4_ai_se_jnl.log.md', 'G5_cite_snowball.log.md', 'SNOWBALL.log.md']:
    out.append('\n### %s\n' % fn)
    out.append(re.sub(r'^(#+) ', lambda m: '#' * (len(m.group(1)) + 3) + ' ', open(W + fn).read(), flags=re.M))
out.append('\n## 10. 실행 지시문 원문\n')
for i, (d, m, p) in enumerate(runs, 1):
    out.append('\n### 10.%d %s\n\n모델 식별자: %s\n\n```text\n%s\n```\n' % (i, d, m, p.replace('```', "'''")))
md = '\n'.join(out)
open(os.path.join(RAW, '..', '..', 'docs', 'codebooks_and_prompts.md'), 'w').write(md)
print('runs', len(runs), 'chars', len(md))
