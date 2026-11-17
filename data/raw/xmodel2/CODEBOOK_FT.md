# 방어 연구 원문(full text) 코딩북 v2 (고정본, 2026-10-01)

대상: 방어 논문 목록(JSON). 각 논문의 원문을 읽고 아래 항목을 코딩한다. 다른 코더의 결과 파일은 열지 않는다(/home/claude/w/search, /home/claude/w/review*, /home/claude/w/supp 디렉터리와 FINAL_CORPUS.json, STATS*.json은 열지 않는다). 원문 근거로만 판정하고, 확인할 수 없으면 '?'로 둔다.

## 원문 찾기
- 입력 JSON의 fulltext_url이 가리키는 판을 읽는다(같은 판으로 비교하기 위함). 열리지 않으면 아래 규칙으로 대체하고 src에 실제로 읽은 URL을 적는다.
- ACL 계열(site가 aclanthology.org): https://aclanthology.org/<id>.pdf 를 연다(게재본).
- 그 밖: arxiv_id가 있으면 https://arxiv.org/abs/<id> (판 이력 확인)와 https://arxiv.org/html/<id> 를 연다. 없으면 WebSearch로 "<제목> arXiv"를 1회 검색해 결과의 arxiv.org 링크를 쓴다. NDSS·USENIX는 학회 PDF(ndss-symposium.org, usenix.org)도 가능.
- openreview.net PDF는 403이므로 쓰지 않는다. WebSearch는 여러 작업자가 공유하는 예산이므로 논문당 최대 1회.
- 읽은 판(게재본 또는 arXiv vN)을 src에 기록한다.

## 항목
- src: 실제로 읽은 URL과 판
- arxiv_id, arxiv_v1: arXiv 식별자와 v1 제출일(YYYY-MM-DD, abs 페이지의 Submission history). 없으면 '-'
- stage(복수): 방어가 판정을 집행하는 지점
  - I 입력 수용: 비신뢰 입력·사용자 데이터가 모델 컨텍스트에 들어가기 전 처리(탐지·정제·최소화), 모델 자체 견고화
  - P 계획 수립: 외부 데이터를 읽기 전 계획·제어 흐름·허용 행동 집합·정책을 확정하거나 계획을 검증
  - M 메모리 쓰기·읽기: 장기 메모리·RAG 저장·검색 시점 검사
  - A 행동 경계: 도구 호출·행동(인자 포함)의 실행 여부를 판정
  - O 출력: 사용자에게 전달되는 최종 응답을 검사·수정
  - C 에이전트 간 통신: 에이전트 간 메시지·위상에 대한 검사
- A_mode: A가 있을 때 pre(실행 전에 차단·수정 가능) / post(사후 감사·탐지만) / '-'
- judge(복수): 집행 시점에 허용 여부를 판정하는 주체
  - SEP 별도의 LLM 판정기·가드 에이전트·검증 LLM
  - SELF 에이전트 모델 자체(미세조정·정렬·안전 지침 주입 등으로 스스로 거부·판단)
  - ML 비LLM 학습 모델(분류기, GNN, 임베딩 유사도 임계값 등)
  - RULE 결정론적 규칙·정책·라벨 검사·격리 구조
  - HUMAN 사용자 확인
- policy_src: RULE이 집행하는 정책·계획·허용 집합의 출처 — MAN(사람이 사전 작성) / LLM(LLM이 실행 시 자연어 작업·명세로부터 생성) / LEARN(데이터로 학습) / MIX / '-'(RULE 없음)
- judge_exposed: 판정하는 LLM(SEP·SELF) 또는 실행 시 정책을 생성하는 LLM이 비신뢰 콘텐츠(도구 출력, 웹, 검색 문서, 다른 에이전트 메시지)를 입력으로 받으면 Y, 신뢰 입력(사용자 질의, 도구 스키마)만 받으면 N, LLM이 판정·정책 생성에 관여하지 않으면 '-'
- granularity(복수): 판정 단위 — INPUT / ACTION(개별 호출) / TRAJ(여러 단계의 궤적·계획 전체) / MSG(에이전트 간 메시지) / OUTPUT
- decisions(복수): allow / block / modify(인자·출력 수정, 정제) / limit(허용 집합·권한·도구 제한, 격리) / confirm(사용자 확인 요청)
- adversarial: 위협 모델이 적대자를 상정하면 Y, 오류·비적대적 위험만이면 N
- adaptive: 0 = 적응형 공격 평가 없음 / 1 = 방어 메커니즘을 알고 수작업으로 설계한 공격으로 평가 / 2 = 방어의 판정·출력을 최적화 루프에 넣은 공격(PAIR·GCG 등을 방어를 포함한 시스템에 대해 최적화)으로 평가 / NA = adversarial이 N. 기존 공격을 여러 종 쓴 것만으로는 0. 근거 문장을 짧게 인용
- bench: 보안 평가에 쓴 벤치마크·환경(세미콜론 구분). 저자가 만든 환경은 'own:<이름>'
- public_bench: 기존 공개 보안 벤치마크(AgentDojo, ASB, InjecAgent, WASP, AgentHarm, PrivacyLens 등)를 1개 이상 쓰면 Y
- n_models: 방어를 적용해 평가한 백본 LLM 수(정수 또는 '?')
- utility: 방어 적용 시 정상 과제 성공률(무공격 또는 공격 하)을 보고하면 Y
- overhead: 지연·토큰·LLM 호출 수·비용 중 하나 이상을 정량 보고하면 Y(종류 기재, 예: Y:token;latency)
- fpr: 정상 행동·과제에 대한 오탐·과차단률을 보고하면 Y
- hitl_burden: 사용자 확인의 빈도·검토 부담을 측정하면 Y, 확인 요청을 쓰지 않으면 '-'
- evidence: adaptive 판정 근거 인용과 기타 메모(짧게)

## 출력
TSV, 헤더:
rid	title	src	stage	A_mode	judge	policy_src	judge_exposed	granularity	decisions	adversarial	adaptive	bench	public_bench	n_models	utility	overhead	fpr	hitl_burden	judge_input	evidence


## 추가 항목: judge_input (헤더의 hitl_burden 뒤, evidence 앞에 열 추가)

- 원천 비신뢰 콘텐츠: 사용자 작업 밖에서 들어온 원문 그대로의 콘텐츠 — 도구 출력, 웹 페이지, 이메일·문서, 검색 결과, 메모리에서 읽은 기록, 다른 에이전트의 메시지 본문, 도구 설명(메타데이터).
- 파생 콘텐츠: 에이전트(LLM)가 원천 비신뢰 콘텐츠를 읽은 뒤 만든 것 — 제안된 도구 호출과 인자, 계획, 요약, 추론 과정(CoT).
- 신뢰 입력: 사용자 질의·작업, 시스템 프롬프트, 사전에 작성된 정책 문서, 도구 이름·스키마(설명 문장 제외는 아님; 도구 설명 문장은 원천 비신뢰로 본다).

항목
- judge_input (별도 LLM 판정기가 있을 때만; 없으면 '-'): 판정 LLM이 판정 시점에 입력으로 받는 것 중 가장 위험한 수준
  - RAW: 원천 비신뢰 콘텐츠를 직접 입력으로 받음(일부라도)
  - DERIVED: 원천 비신뢰 콘텐츠는 받지 않고 파생 콘텐츠(제안된 행동·인자, 계획, 요약)만 받음
  - TRUSTED: 신뢰 입력만 받음
