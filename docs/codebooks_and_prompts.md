# 검색 프로토콜, 분류 기준(코딩북), 검색 로그, 실행 지시문

본 자료는 익명 심사본과 함께 공개하는 자료이다. 모든 선별·코딩·조정은 인간 코더 없이 LLM의 별도 실행이 수행하였다. 각 실행은 아래 지시문과 해당 코딩북만 입력으로 받았으며, 같은 문헌을 판정하는 두 실행은 서로의 결과 파일을 열지 않도록 지시되었다. 실행은 Claude Agent SDK 기반의 에이전트 실행 환경에서 하위 에이전트로 이루어졌고 디코딩 설정은 지정하지 않았다. 웹 문서는 질의에 대한 추출 결과를 돌려주는 웹 조회 도구로 읽었다. 코딩북과 지시문은 실행 당시의 원문이어서 일부 용어가 원고의 최종 용어와 다르다. 코딩은 분류, 코딩북은 분류 기준, 판정기는 판정 모델, 적대자는 공격자, 통제는 제어, 원천은 원본, 세칙은 세부 판정 기준, 과정이나 코더 A·B는 실행 A·B에 해당한다. 원고 검토(방법론·문체·사실·서지 점검)에 쓴 실행은 데이터 생성에 관여하지 않았으므로 지시문을 수록하지 않았다. 파일 경로는 작업 환경의 경로를 그대로 두었다.

## 1. 실행 목록

| 순서 | 실행 | 기록된 모델 식별자 |
|---|---|---|
| 1 | High-citation and snowball route | claude-opus-5-5 |
| 2 | ML venues search/screen | claude-opus-5-5 |
| 3 | NLP venues search/screen | claude-opus-5-5 |
| 4 | Security venues search/screen | claude-opus-5-5 |
| 5 | AI/SE/journal venues search | claude-opus-5-5 |
| 6 | Screen ML hits batch B | claude-opus-5-5 |
| 7 | Re-code NLP included records | claude-opus-5-5 |
| 8 | Screen ML hits batch A | claude-opus-5-5 |
| 9 | Consolidate security venue records | claude-opus-5-5 |
| 10 | Code control point for 75 defenses | claude-opus-5-5 |
| 11 | Independent screener: 150 sample | claude-opus-5-5 |
| 12 | Independent coder B: corpus labels | claude-opus-5-5 |
| 13 | Screen v3 expanded hits chunk 3-4 | claude-opus-5-5 |
| 14 | Screen v3 expanded hits chunk 5-6 | claude-opus-5-5 |
| 15 | Screen v3 expanded hits chunk 1-2 | claude-opus-5-5 |
| 16 | Full-text coding defenses chunk 4 | claude-opus-5-5 |
| 17 | Full-text coding defenses chunk 5 | claude-opus-5-5 |
| 18 | Full-text coding defenses chunk 3 | claude-opus-5-5 |
| 19 | Full-text coding defenses chunk 2 | claude-opus-5-5 |
| 20 | Backward snowballing from SoK and survey | claude-opus-5-5 |
| 21 | Full-text coding defenses chunk 1 | claude-opus-5-5 |
| 22 | Independent screener B on expanded sample | claude-opus-5-5 |
| 23 | Adjudicate screening and snowball scope | claude-opus-5-5 |
| 24 | Fetch abstracts for 36 papers | claude-opus-5-5 |
| 25 | Coder A: v3 coding part a | claude-opus-5-5 |
| 26 | Coder B: v3 coding part a | claude-opus-5-5 |
| 27 | Coder A: v3 coding part b | claude-opus-5-5 |
| 28 | Coder B: v3 coding part b | claude-opus-5-5 |
| 29 | Adjudicate coding disagreements part 1 | claude-opus-5-5 |
| 30 | Adjudicate coding disagreements part 2 | claude-opus-5-5 |
| 31 | Full-text coding defenses chunk 6b | claude-opus-5-5 |
| 32 | Second full-text coder subset b | claude-opus-5-5 |
| 33 | Full-text coding defenses chunk 6a | claude-opus-5-5 |
| 34 | Second full-text coder subset a | claude-opus-5-5 |
| 35 | Blind screening pass B batch 1 | claude-opus-5-5 |
| 36 | Blind screening pass B batch 3 | claude-opus-5-5 |
| 37 | Blind screening pass B batch 2 | claude-opus-5-5 |
| 38 | Blind screening pass B batch 4 | claude-opus-5-5 |
| 39 | Blind screening pass B batch 5 | claude-opus-5-5 |
| 40 | Blind screening pass B batch 6 | claude-opus-5-5 |
| 41 | Adjudicate screening disagreements A | claude-opus-5-5 |
| 42 | Adjudicate screening disagreements B | claude-opus-5-5 |
| 43 | Abstract coding new papers coder A | claude-opus-5-5 |
| 44 | Abstract coding new papers coder B | claude-opus-5-5 |
| 45 | Full-text coding new defenses | claude-opus-5-5 |
| 46 | Adjudicate M054 coding disagreement | claude-opus-5-5 |
| 47 | Audit 150 double-excluded candidates | claude-opus-5-5 |
| 48 | Exposure recoding coder B part 1 | claude-opus-5-5 |
| 49 | Exposure recoding coder A part 2 | claude-opus-5-5 |
| 50 | Exposure recoding coder A part 1 | claude-opus-5-5 |
| 51 | Exposure recoding coder B part 2 | claude-opus-5-5 |
| 52 | Adjudicate exposure-level disagreements | claude-opus-5-5 |
| 53 | Cross-model blind abstract coding check | claude-sonnet-5-5 |
| 54 | Cross-model blind screening check | claude-sonnet-5-5 |
| 55 | Full-text adjudication (main model) | claude-opus-5-5 |
| 56 | Cross-model full-text coding 2 | claude-sonnet-5-5 |
| 57 | Cross-model full-text coding 3 | claude-sonnet-5-5 |
| 58 | Cross-model full-text coding 1 | claude-sonnet-5-5 |
| 59 | Full-text adjudication (other model) | claude-sonnet-5-5 |
| 60 | Cross-model full-text coding 5 | claude-sonnet-5-5 |
| 61 | Cross-model full-text coding 4 | claude-sonnet-5-5 |

실행과 최종 데이터의 대응(번호는 위 표): 선별 실행 A의 판정은 실행 1–9(학회군별 검색·선별, 재판정, 통합)와 13–15(확장 용어 후보 선별)에서 나왔다. 선별 실행 B는 실행 11(150편 표본, 세부 판정 기준 없음), 22(확장 후보 150편 표본, 세부 판정 기준 없음), 35–40(나머지 989편과 경로 3 후보, 세부 판정 기준 R1–R5)이다. 선별 불일치 조정은 23, 41, 42, 경로 3 후보 확인은 20, 초록 확보는 24이다. 초록 코딩의 실행 A·B는 25–28(세부 판정 기준 R1–R4)과 43–44(추가 포함 5편, 세부 판정 기준 R1–R6), 그 조정은 29–30과 46이다. 방어 원문 코딩은 16–19, 21, 31, 33, 45, 같은 모델의 무작위 재코딩 표본은 32, 34이다. 판정 모델 입력의 실행 A·B는 48–51, 그 조정은 52이며, 두 실행이 모두 제외한 후보의 점검은 47이다. 실행 10(초기 집행 지점 코딩)과 12(초기 코더 B)의 결과는 최종 집계에 쓰이지 않았다. 다른 모델 claude-sonnet-5-5의 점검은 실행 53, 54, 55, 56, 57, 58, 59, 60, 61이다. 선별 200편과 초록 코딩 60편, 원문 코딩 30편(세 실행)과 적응형 평가 추가 표본 24편(두 실행), 선별에서 갈린 8편의 원문 재판정이며, 같은 8편은 코딩에 쓴 모델 claude-opus-5-5의 별도 실행도 원문으로 재판정하였다.

## 2. 검색·선별 프로토콜

# 검색·선별 프로토콜 (권고 B 재수행, v8)

- 검색일: 2026-10-01 (단일 검색일)
- 검색 하한: 2022-10-06 (ReAct 최초 공개일). 상한은 두지 않음(검색일까지 공개된 문헌).
- 기간 판정: 최초 공개일(arXiv 첫 버전 날짜, 없으면 게재일). 인용 서지는 동료심사 게재처.
- 유효 조사 기간: 포함된 문헌 중 최초 공개일이 가장 이른 문헌 ~ 가장 늦은 문헌 (데이터에서 도출)

## 1차 데이터베이스
Semantic Scholar Academic Graph API, /paper/search/bulk (제목·초록 불리언 검색)

Q = (agent | agents | agentic | "multi-agent" | "tool-augmented" | "tool-integrated" | "LLM-integrated" | MCP)
  + (LLM | LLMs | "language model" | "language models")
  + (attack | attacks | security | injection | privacy | defense | adversarial | poisoning | backdoor | hijacking | exfiltration | authorization | "access control" | threat | threats)
publicationDateOrYear = 2022-10-06:2026-09-30

### 경로 V (학회·저널 범위)
venue 필터:
- 보안: IEEE S&P, USENIX Security, ACM CCS, NDSS
- ML: NeurIPS, ICML, ICLR
- NLP: ACL, EMNLP, NAACL (Findings 포함; S2는 모학회로 표기)
- AI·SE: AAAI, IJCAI, ICSE, FSE
- 저널: IEEE TDSC, IEEE TIFS, ACM TOPS

### 경로 C (고인용 예외)
venue 무관, minCitationCount=50 → 범위 밖 동료심사 문헌은 예외 포함, arXiv 전용 문헌은 '고인용 프리프린트'로 별도 집계(코퍼스 외)

### 경로 S (스노볼링)
동료심사 SoK/서베이(USENIX Sec 2026 SoK, ACM CSUR 2025 Deng et al.)의 참고문헌 중 범위 내 문헌 보완

## 포함 기준
I1 대상: 도구·웹·코드·메모리·다른 에이전트 중 하나 이상을 통해 실제 행동(외부 부작용)하는 LLM 기반 시스템(에이전트 또는 도구·플러그인 통합 LLM 애플리케이션)
I2 주 기여: 적대적 위협에 대한 공격, 방어, 벤치마크·측정, 또는 행동 정책·권한의 런타임 집행
I3 공개: 동료심사 게재(경로 V의 학회·저널) 또는 경로 C 예외
I4 최초 공개일 ≥ 2022-10-06

## 제외 기준
E1 단일 LLM 수준 탈옥·유해 출력, 행동 없는 프롬프트 인젝션(분류기·번역기 등)
E2 적대자·권한 없이 성능·환각·일반 안전성만 평가
E3 서베이·SoK·포지션(맥락 자료, 스노볼링에만 사용)
E4 LLM 에이전트를 보안 과업에 활용(AI for security: 침투 테스트, 취약점 탐지 등)
E5 에이전트 실행 루프와 무관하게 기존 웹·API·공급망 보안으로 동일하게 설명되는 위협
E6 모델 학습 단계 공격(학습 데이터 오염·백도어)으로 에이전트 행동 경로를 다루지 않는 연구

## 코딩(포함 문헌 전체)
- 유형: A(공격) / D(방어) / B(벤치마크·측정) — 복수 가능
- 위협 T1–T6 (다중 라벨): T1 지시·목표 조작, T2 메모리·컨텍스트(RAG) 조작, T3 도구·공급망(MCP, 도구 설명), T4 데이터·프라이버시 유출, T5 권한·인가(과잉 권한, 위험 행동), T6 에이전트 간 상호작용
- 방어 D1–D6 (방어 문헌만): D1 입력 보호(탐지·정제·프롬프트 방어·파인튜닝), D2 정보 흐름 통제, D3 도구·계획 격리, D4 인가·정책 집행, D5 런타임 탐지(행동·궤적 감시), D6 인간 감독

## 작업 지침(하위 작업자 공통)
1. S2 bulk search 호출은 WebFetch로 한다. URL 형식(공백은 그대로 둬도 됨):
   https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=(agent|agents|agentic|"multi-agent"|"tool-augmented"|"tool-integrated"|"LLM-integrated"|MCP)+(LLM|LLMs|"language model"|"language models")+(attack|attacks|security|injection|privacy|defense|adversarial|poisoning|backdoor|hijacking|exfiltration|authorization|"access control"|threat|threats)&publicationDateOrYear=2022-10-06:2026-09-30&venue=<VENUES>&fields=title,venue,year,publicationDate,citationCount,externalIds&sort=publicationDate:asc
   - 429가 나오면 Bash `sleep 90` 후 재시도(최대 20회). 응답이 잘리면 publicationDateOrYear를 연도(또는 반기)로 쪼개 전 건을 받는다.
   - WebFetch prompt 예: 'Print "total" and then EVERY entry verbatim, one per line: publicationDate | year | venue | citationCount | ArXiv id (or -) | DOI (or -) | title. Do not omit any entries.'
   - 반환된 total과 실제 받은 건수를 로그에 남긴다.
2. S2가 끝내 불가하면 대체 경로(Crossref API: https://api.crossref.org/works?query.bibliographic=...&filter=from-pub-date:2022-10-06,until-pub-date:2026-09-30&select=DOI,title,container-title,type,published&rows=40 / 공식 프로시딩 페이지 / WebSearch)를 쓰고 로그에 명시한다.
3. 게재 확인: 검색일(2026-10-01)까지 해당 학회·저널에 실제 게재(프로시딩 공개)된 것만 I3 충족. 2026년 하반기 학회(CCS 2026, EMNLP 2026, NeurIPS 2026, AAAI 2027 등)의 채택 논문은 미게재로 제외(E코드 'NP').
4. 최초 공개일: arXiv id가 있으면 YYMM에서 연월을 취하고(가능하면 S2 publicationDate가 arXiv 날짜인지 확인), 없으면 게재일.
5. 선별은 제목(+필요 시 초록)으로 한다. 애매하면 WebSearch로 초록을 확인한다. 추측으로 포함하지 않는다.
6. 출력 TSV 열(탭 구분, 헤더 포함):
   first_public(YYYY-MM) | venue_short | pub_year | citations | arxiv_id | doi_or_url | title | decision(INC/EXC) | reason(I 또는 E1–E6/NP) | type(A/D/B 조합) | T(예: T1;T4) | D(예: D2;D3, 방어 아니면 -) | note
   제외 문헌도 모두 기록(사유 포함).
7. 로그 파일: 호출 URL, 시각, total, 받은 건수, 대체 경로 사용 여부.

## 개정(v8-2, 2026-10-01): API 차단에 따른 경로 재정의와 코딩 세칙
- 경로 V는 공식 메타데이터 전수 검색으로 수행: (a) ACL Anthology 공식 XML(ACL·EMNLP·NAACL, Findings 포함), (b) OpenReview 기반 학회 메타데이터(papercopilot/paperlists: ICLR 2023–2026, ICML 2023–2026, NeurIPS 2023–2025, AAAI 2023–2025, IJCAI 2023–2024; 채택 논문만). 질의 Q를 제목+초록 정규식으로 적용.
- 보안 4대 학회는 전수 메타데이터 확보 불가 → 공식 채택 목록(S&P 2026, NDSS 2024·2025), 아티팩트 평가 목록(secartifacts), Crossref(NDSS), 웹 검색, 큐레이션 목록을 결합(완전성 미보장, 한계로 명시).
- 트랙: 본 학술대회 논문 트랙(main, Findings, NeurIPS Datasets & Benchmarks, AAAI special track)만 포함. demo·industry·SRW·student·doctoral·position·journal track은 제외(사유 'TR').
- ICSE·FSE·저널: 검색 미수행 → 경로 C(인용 50회 이상)·S(스노볼링)로만 포함.

### 위협 코딩 세칙
- T1 지시·목표 조작: 직접/간접 프롬프트 인젝션, 에이전트 대상 탈옥으로 행동 유도, 팝업·기만 UI, 환경 내 적대적 콘텐츠
- T2 메모리·컨텍스트 조작: 장기 메모리·RAG 지식베이스·대화 이력 오염, 세션 간 지속 조작
- T3 도구·공급망: 도구 설명·메타데이터 오염, 악성 도구·MCP 서버·플러그인·스킬, 도구 선택 조작, 백도어 모델·어댑터(제3자 구성요소 오염)
- T4 데이터·프라이버시: 민감정보·자격증명 유출·반출, 맥락적 프라이버시 위반, 메모리·지식 파일 추출, 부채널 유출
- T5 권한·인가: 위임 범위를 넘는 행동의 실현(과잉 권한, 접근 통제 우회, 위험·유해 행동 실행, 자원 남용·DoS)
- T6 에이전트 간 상호작용: 다중 에이전트 간 전파·감염, 통신 조작, 공모, 에이전트 프로토콜(A2A) 공격
### 방어 코딩 세칙
- D1 입력 보호: 입력 단계의 주입 탐지·정제·경계 표시, 모델 견고화(미세조정·정렬)
- D2 정보 흐름 통제: 출처·라벨·오염(taint) 추적, 데이터 최소화, 맥락적 흐름 검사
- D3 도구·계획 격리: 계획 선확정·이중 LLM·샌드박스·앱/도구 격리, 도구 호출 구조 제한
- D4 인가·정책 집행: 명시적 권한·정책·규칙의 결정론적 집행(권한 통제, 정책 언어, 접근 통제)
- D5 런타임 탐지: LLM·학습 모델 판정기로 행동·궤적·메시지를 감시(정합성 판정, 가드레일 모델, 이상 탐지)
- D6 인간 감독: 사용자 확인·승인을 설계 요소로 포함


## 3. 코딩북 v1(초기 독립 선별·코딩용)

원본 파일: `CODEBOOK.md`

### 코딩북 (LLM 기반 AI 에이전트 보안 서베이) — 독립 코딩용

이 코딩북만 보고 판정한다. 다른 코더의 결과 파일(G*.tsv, R_*.tsv, corpus_all.json, defense_coding.tsv 등)은 열지 않는다.

#### 1. 선별(포함/제외)
포함(INC): 다음을 모두 만족
- I1 대상: 도구·웹/GUI·코드 실행·메모리·다른 에이전트·로봇 구동 중 하나 이상을 통해 실제 행동(외부 부작용)을 수행하는 LLM(멀티모달 포함) 기반 시스템(에이전트, 도구·플러그인 통합 LLM 애플리케이션)
- I2 주 기여: (a) 적대적 위협에 대한 공격, 방어, 벤치마크·측정 또는 (b) 행동 정책·권한의 실행 중(런타임) 집행 메커니즘
제외(EXC) 사유 코드:
- E1 행동 요소가 없는 단일 LLM 수준 연구(탈옥·유해 출력, 행동 없는 프롬프트 인젝션, RAG 질의응답 오염 등)
- E2 적대자 없이 성능·환각·일반 안전성·비적대적 프라이버시 경향만 평가(런타임 집행 메커니즘 제안이 없는 경우)
- E3 서베이·SoK·포지션·입장 논문
- E4 LLM 에이전트를 보안 과업에 활용(침투 테스트, 취약점 탐지, CTF, 피싱 탐지 등 AI for security)
- E5 에이전트 실행 루프와 무관하게 기존 웹·API·네트워크 보안으로 동일하게 설명되는 위협
- E6 학습 단계 공격(데이터 오염·백도어)으로 에이전트 행동 경로를 다루지 않는 연구
- X 비LLM 시스템(다중 에이전트 강화학습 등) 또는 주제 무관

#### 2. 유형(type, 복수 가능)
A 공격(새 공격 기법·위협 실증) / D 방어(탐지·차단·격리·집행 메커니즘 제안) / B 벤치마크·측정(평가 환경, 데이터셋, 대규모 측정·실증 분석)
- 방어가 부차적 실험(기존 방어로 완화 시도 정도)에 그치면 D로 코딩하지 않는다.

#### 3. 위협 범주(T, 다중 라벨; 논문이 다루는 위협 모두)
- T1 지시·목표 조작: 직접/간접 프롬프트 인젝션, 행동을 유도하는 에이전트 탈옥, 팝업·기만 UI·다크 패턴, 환경·도구 출력에 심긴 적대적 콘텐츠
- T2 메모리·컨텍스트 조작: 장기 메모리·RAG 지식베이스·대화 이력 오염, 세션 간 지속 조작 (메모리에서 정보를 '추출'하는 것은 T4)
- T3 도구·공급망: 도구 설명·메타데이터 오염, 악성 도구·MCP 서버·플러그인·스킬, 도구 선택 조작, 백도어가 심긴 모델·어댑터·서드파티 에이전트
- T4 데이터·프라이버시: 민감정보·자격증명 유출·반출, 맥락적 프라이버시 위반, 메모리·지식 파일 추출, 부채널 유출
- T5 권한·인가: 위임 범위를 넘는 행동의 실현(과잉 권한, 접근 통제 우회, 위험·유해 행동 실행, 자원 남용·DoS, 샌드박스 탈출, 감독 회피)
- T6 에이전트 간 상호작용: 다중 에이전트 간 전파·감염, 통신 조작, 공모, 악성 에이전트, A2A 등 에이전트 프로토콜 공격

#### 4. 방어 범주(D, D로 코딩된 논문만, 다중 라벨)
- D1 입력 보호: 입력 단계 주입 탐지·정제·경계 표시, 모델 견고화(미세조정·정렬·안전 지침 주입)
- D2 정보 흐름 통제: 출처·라벨·오염(taint) 추적, 데이터 최소화, 맥락적 흐름(CI) 검사
- D3 도구·계획 격리: 계획 선확정, 이중 LLM, 샌드박스·앱/도구 격리, 도구 호출 구조 제한
- D4 인가·정책 집행: 명시적 권한·정책·규칙을 결정론적으로 집행(권한 통제, 정책 언어, 접근 통제)
- D5 런타임 탐지: LLM·학습 모델 판정기로 행동·궤적·메시지를 감시(정합성 판정, 가드레일 모델, 이상 탐지)
- D6 인간 감독: 사용자 확인·승인을 설계 요소로 포함

#### 5. 통제 시점(stage, 방어만, 복수 가능)
- I 입력 수용(신뢰할 수 없는 입력·사용자 데이터가 컨텍스트에 들어가기 전 처리, 모델 자체 견고화 포함)
- P 계획 수립(외부 데이터를 읽기 전 계획·제어 흐름·정책 확정, 계획 검증)
- M 메모리 쓰기·읽기(장기 메모리·RAG 저장·검색 시점 검사)
- A 행동 직전 도구 호출 경계(도구 호출·인자를 허용/차단/수정, 행동을 게이트하는 런타임 감시)
- C 에이전트 간 통신(메시지·위상에 대한 검사)

#### 6. 판정 주체(authority, 방어만, 복수 가능)
- LLM: 프롬프트되거나 미세조정된 LLM(가드 에이전트 포함)이 허용 여부를 판정
- ML: LLM이 아닌 학습 모델(분류기, GNN, 임베딩 유사도 임계값 등)이 판정
- RULE: 결정론적 규칙·정책·라벨·격리를 코드가 집행
- HUMAN: 사용자 확인이 판정에 포함
- policy_by_llm: 결정론적으로 집행되는 계획·정책·규칙을 LLM이 자연어 작업·명세로부터 생성하면 Y, 아니면 N


## 4. 코딩북 v3(선별·초록 코딩, 세부 판정 기준 R1–R6 포함 현재 판)

원본 파일: `CODEBOOK_v3.md`

### 코딩북 v3 (고정본, 2026-10-01) — LLM 기반 AI 에이전트 보안 체계적 문헌 매핑

이 코딩북만 보고 판정한다. 다른 코더의 결과 파일(G*.tsv, R_*.tsv, CODER_*.tsv, SCREEN_*.tsv, FT_*.tsv, corpus_*.json, defense_coding.tsv 등)은 열지 않는다. 추측하지 말고, 근거가 없으면 '?'로 둔다.

#### 1. 선별(포함/제외)
포함(INC): 다음을 모두 만족
- I1 대상: 도구·웹/GUI·코드 실행·메모리·다른 에이전트·로봇 구동 중 하나 이상을 통해 실제 행동(외부 부작용 또는 다른 에이전트에 대한 행동)을 수행하는 LLM(멀티모달 포함) 기반 시스템
- I2 주 기여: (a) 적대적 위협에 대한 공격, 방어, 벤치마크·측정, 또는 (b) 적대자 유무와 무관하게 에이전트 행동에 대한 정책·권한·안전 규칙을 실행 중에 집행하는 메커니즘
제외(EXC) 사유 코드:
- E1 행동 요소가 없는 단일 LLM 수준 연구(탈옥·유해 출력, 행동 없는 프롬프트 인젝션, RAG 질의응답 오염, 텍스트만 출력하는 응용)
- E2 적대자 없이 성능·환각·일반 안전성·비적대적 위험 경향만 평가하고 런타임 집행 메커니즘을 제안하지 않음
- E3 서베이·SoK·포지션·입장 논문
- E4 LLM 에이전트를 보안 과업에 활용(침투 테스트, 취약점 탐지, CTF, 피싱·봇 탐지 등)
- E5 에이전트 실행 루프와 무관하게 기존 웹·API·네트워크 보안으로 동일하게 설명되는 위협
- E6 학습 단계 공격(데이터 오염·백도어)으로 에이전트 행동 경로를 다루지 않는 연구
- X 비LLM 시스템(다중 에이전트 강화학습, RL 정책 등) 또는 주제 무관

#### 2. 포함 문헌의 초록 수준 코딩
- type(복수): A 공격(새 공격 기법·위협 실증) / D 방어(탐지·차단·격리·집행 메커니즘 제안이 주요 기여) / B 벤치마크·측정(평가 환경, 데이터셋, 대규모 측정·실증 분석). 방어가 부차적 실험에 그치면 D가 아니다.
- actor(복수, 논문이 상정하는 위협 주체): EXT 외부 콘텐츠 제공자(웹·문서·이메일·도구 출력·환경) / SUP 도구·MCP 서버·플러그인·스킬·모델·어댑터 공급자 / AGT 악성·감염된 다른 에이전트 / USR 악의적 사용자(직접 오용) / NON 적대자 없음(오류·비적대적 위험)
- T(복수):
  - T1 지시·목표 조작: 직접/간접 프롬프트 인젝션, 행동을 유도하는 탈옥, 팝업·기만 UI·다크 패턴, 환경·도구 출력에 심긴 적대적 콘텐츠
  - T2 메모리·컨텍스트 조작: 장기 메모리·RAG 지식베이스·대화 이력 오염, 세션 간 지속 조작(메모리에서 정보를 '추출'하는 것은 T4)
  - T3 도구·공급망: 도구 설명·메타데이터 오염, 악성 도구·MCP 서버·플러그인·스킬, 도구 선택 조작, 백도어가 심긴 모델·어댑터·서드파티 에이전트
  - T4 데이터·프라이버시: 민감정보·자격증명 유출·반출, 맥락적 프라이버시 위반, 메모리·지식 파일 추출, 부채널 유출
  - T5 위임 범위 밖 행동의 실현(아래 하위 유형 중 하나 이상)
  - T6 에이전트 간 상호작용: 다중 에이전트 간 전파·감염, 통신 조작, 공모, 악성 에이전트, A2A 등 프로토콜 공격
- T5sub(T5일 때 복수): a 권한·인가(과잉 권한, 접근 통제 우회, 혼동된 대리인, 권한 상승, 샌드박스 탈출) / b 안전 규칙 위반 행동(유해·위험·불법 행동 실행) / c 가용성(자원 남용, DoS, 무한 루프)
- viol(복수, 침해 유형): AI 행동 무결성(의도하지 않은 도구 호출·행동) / OI 출력 무결성(사용자에게 전달되는 응답·판단의 조작) / C 기밀성 / AV 가용성 / S 안전(물리·유해 결과)
- multistage: Y = 영향이 단일 즉시 행동을 넘어 메모리 지속·세션 간·계획 오염·다중 홉(에이전트 간) 등으로 전파된 뒤 실현되는 경로를 시연하거나 그것을 방어 대상으로 삼음 / N = 그 외
- embodied: Y = 로봇·체화 시뮬레이터·자율주행 등 물리 환경에서 행동 / N
- D(방어만, 복수):
  - D1 입력 보호: 입력 단계 주입 탐지·정제·경계 표시, 모델 견고화(미세조정·정렬·안전 지침 주입)
  - D2 정보 흐름 통제: 출처·라벨·오염(taint) 추적, 데이터 최소화, 맥락적 흐름(CI) 검사
  - D3 도구·계획 격리: 계획 선확정, 이중 LLM, 샌드박스·앱/도구 격리, 도구 호출 구조 제한
  - D4 인가·정책 집행: 명시적 권한·정책·규칙을 결정론적으로 집행(권한 통제, 정책 언어, 접근 통제)
  - D5 런타임 탐지: LLM·학습 모델 판정기로 행동·궤적·메시지를 감시(정합성 판정, 가드레일 모델, 이상 탐지)
  - D6 인간 감독: 사용자 확인·승인을 설계 요소로 포함
값이 없으면 '-'.

#### 3. 선별 판정 세칙(불일치 판정 과정에서 명시, 2026-10-01 추가)
- R1 I2(b)는 실행 중 개별 행동을 검사·제약·상향(확인 요청)하는 명시적 런타임 메커니즘(감시기, 검증기, 게이트, 정책 엔진, 확인 요청 장치)을 요구한다. 적대자 없이 에이전트 모델을 미세조정하거나 프롬프트로 안전하게 만드는 것만으로는 E2이다. 적대자를 상정하면 모델 견고화도 I2(a)의 방어(D1)이다.
- R2 다중 LLM·다중 에이전트 시스템은 에이전트 간 메시지가 다른 에이전트의 행동을 결정하는 경우 행동하는 시스템(I1)으로 본다. 악성 에이전트·모델이 상정되면 최종 출력이 텍스트여도 I2(a)이다.
- R3 도구(검색 포함)를 사용하는 에이전트는 피해가 행동이 아니라 응답 출력으로 나타나더라도 I1을 충족한다(침해 유형 OI). 실험이 도구 사용 없이 텍스트 처리만 수행하면 E1이다.
- R4 핵심 기여가 신뢰성·성능이고 안전 집행 요소가 부차적이면 E2이다.
- R5(행위자 세칙) 평가·감시 대상 에이전트 자체가 적대적으로 행동하는 경우(오정렬·계략·감독 회피)는 AGT로 코딩한다. 수동적 네트워크 관찰자 등 외부 관찰자는 EXT로 코딩한다. 질의만으로 메모리를 오염시키는 공격자는 USR로 코딩한다.
- R6(에이전트 적대자 세칙, 2차 선별 판정에서 추가) 에이전트 자체를 적대자로 보는 연구는 에이전트에 적대적 목표를 부여하거나(지시·미세조정·레드팀) 감독 회피를 유도하여 평가한 경우에 I2(a)로 본다. 적대적 목표 없이 일반 에이전트의 자발적 위험 행동·기만 경향만 측정하고 런타임 집행 메커니즘을 제안하지 않은 연구는 E2이다.


## 5. 블라인드 선별 코딩북(둘째 과정 989편과 제외 점검에 사용, 세부 판정 기준 R1–R5)

원본 파일: `pb/CODEBOOK_SCREEN.md`

### 선별 코딩북 v3 — LLM 기반 AI 에이전트 보안 체계적 문헌 매핑

이 코딩북만 보고 판정한다. 다른 코더의 결과 파일(G*.tsv, R_*.tsv, CODER_*.tsv, SCREEN_*.tsv, FT_*.tsv, corpus_*.json, defense_coding.tsv 등)은 열지 않는다. 추측하지 말고, 근거가 없으면 '?'로 둔다.

#### 1. 선별(포함/제외)
포함(INC): 다음을 모두 만족
- I1 대상: 도구·웹/GUI·코드 실행·메모리·다른 에이전트·로봇 구동 중 하나 이상을 통해 실제 행동(외부 부작용 또는 다른 에이전트에 대한 행동)을 수행하는 LLM(멀티모달 포함) 기반 시스템
- I2 주 기여: (a) 적대적 위협에 대한 공격, 방어, 벤치마크·측정, 또는 (b) 적대자 유무와 무관하게 에이전트 행동에 대한 정책·권한·안전 규칙을 실행 중에 집행하는 메커니즘
제외(EXC) 사유 코드:
- E1 행동 요소가 없는 단일 LLM 수준 연구(탈옥·유해 출력, 행동 없는 프롬프트 인젝션, RAG 질의응답 오염, 텍스트만 출력하는 응용)
- E2 적대자 없이 성능·환각·일반 안전성·비적대적 위험 경향만 평가하고 런타임 집행 메커니즘을 제안하지 않음
- E3 서베이·SoK·포지션·입장 논문
- E4 LLM 에이전트를 보안 과업에 활용(침투 테스트, 취약점 탐지, CTF, 피싱·봇 탐지 등)
- E5 에이전트 실행 루프와 무관하게 기존 웹·API·네트워크 보안으로 동일하게 설명되는 위협
- E6 학습 단계 공격(데이터 오염·백도어)으로 에이전트 행동 경로를 다루지 않는 연구
- X 비LLM 시스템(다중 에이전트 강화학습, RL 정책 등) 또는 주제 무관

#### 3. 선별 판정 세칙(불일치 판정 과정에서 명시, 2026-10-01 추가)
- R1 I2(b)는 실행 중 개별 행동을 검사·제약·상향(확인 요청)하는 명시적 런타임 메커니즘(감시기, 검증기, 게이트, 정책 엔진, 확인 요청 장치)을 요구한다. 적대자 없이 에이전트 모델을 미세조정하거나 프롬프트로 안전하게 만드는 것만으로는 E2이다. 적대자를 상정하면 모델 견고화도 I2(a)의 방어(D1)이다.
- R2 다중 LLM·다중 에이전트 시스템은 에이전트 간 메시지가 다른 에이전트의 행동을 결정하는 경우 행동하는 시스템(I1)으로 본다. 악성 에이전트·모델이 상정되면 최종 출력이 텍스트여도 I2(a)이다.
- R3 도구(검색 포함)를 사용하는 에이전트는 피해가 행동이 아니라 응답 출력으로 나타나더라도 I1을 충족한다(침해 유형 OI). 실험이 도구 사용 없이 텍스트 처리만 수행하면 E1이다.
- R4 핵심 기여가 신뢰성·성능이고 안전 집행 요소가 부차적이면 E2이다.
- R5(행위자 세칙) 평가·감시 대상 에이전트 자체가 적대적으로 행동하는 경우(오정렬·계략·감독 회피)는 AGT로 코딩한다. 수동적 네트워크 관찰자 등 외부 관찰자는 EXT로 코딩한다. 질의만으로 메모리를 오염시키는 공격자는 USR로 코딩한다.


## 6. 초록 코딩 코딩북(추가 포함 문헌, 세부 판정 기준 R1–R6)

원본 파일: `pb/CODEBOOK_CODE.md`

### 초록 수준 코딩북 v3

이 코딩북만 보고 판정한다. 다른 코더의 결과 파일은 열지 않는다. 근거가 없으면 '?'로 둔다.

#### 2. 포함 문헌의 초록 수준 코딩
- type(복수): A 공격(새 공격 기법·위협 실증) / D 방어(탐지·차단·격리·집행 메커니즘 제안이 주요 기여) / B 벤치마크·측정(평가 환경, 데이터셋, 대규모 측정·실증 분석). 방어가 부차적 실험에 그치면 D가 아니다.
- actor(복수, 논문이 상정하는 위협 주체): EXT 외부 콘텐츠 제공자(웹·문서·이메일·도구 출력·환경) / SUP 도구·MCP 서버·플러그인·스킬·모델·어댑터 공급자 / AGT 악성·감염된 다른 에이전트 / USR 악의적 사용자(직접 오용) / NON 적대자 없음(오류·비적대적 위험)
- T(복수):
  - T1 지시·목표 조작: 직접/간접 프롬프트 인젝션, 행동을 유도하는 탈옥, 팝업·기만 UI·다크 패턴, 환경·도구 출력에 심긴 적대적 콘텐츠
  - T2 메모리·컨텍스트 조작: 장기 메모리·RAG 지식베이스·대화 이력 오염, 세션 간 지속 조작(메모리에서 정보를 '추출'하는 것은 T4)
  - T3 도구·공급망: 도구 설명·메타데이터 오염, 악성 도구·MCP 서버·플러그인·스킬, 도구 선택 조작, 백도어가 심긴 모델·어댑터·서드파티 에이전트
  - T4 데이터·프라이버시: 민감정보·자격증명 유출·반출, 맥락적 프라이버시 위반, 메모리·지식 파일 추출, 부채널 유출
  - T5 위임 범위 밖 행동의 실현(아래 하위 유형 중 하나 이상)
  - T6 에이전트 간 상호작용: 다중 에이전트 간 전파·감염, 통신 조작, 공모, 악성 에이전트, A2A 등 프로토콜 공격
- T5sub(T5일 때 복수): a 권한·인가(과잉 권한, 접근 통제 우회, 혼동된 대리인, 권한 상승, 샌드박스 탈출) / b 안전 규칙 위반 행동(유해·위험·불법 행동 실행) / c 가용성(자원 남용, DoS, 무한 루프)
- viol(복수, 침해 유형): AI 행동 무결성(의도하지 않은 도구 호출·행동) / OI 출력 무결성(사용자에게 전달되는 응답·판단의 조작) / C 기밀성 / AV 가용성 / S 안전(물리·유해 결과)
- multistage: Y = 영향이 단일 즉시 행동을 넘어 메모리 지속·세션 간·계획 오염·다중 홉(에이전트 간) 등으로 전파된 뒤 실현되는 경로를 시연하거나 그것을 방어 대상으로 삼음 / N = 그 외
- embodied: Y = 로봇·체화 시뮬레이터·자율주행 등 물리 환경에서 행동 / N
- D(방어만, 복수):
  - D1 입력 보호: 입력 단계 주입 탐지·정제·경계 표시, 모델 견고화(미세조정·정렬·안전 지침 주입)
  - D2 정보 흐름 통제: 출처·라벨·오염(taint) 추적, 데이터 최소화, 맥락적 흐름(CI) 검사
  - D3 도구·계획 격리: 계획 선확정, 이중 LLM, 샌드박스·앱/도구 격리, 도구 호출 구조 제한
  - D4 인가·정책 집행: 명시적 권한·정책·규칙을 결정론적으로 집행(권한 통제, 정책 언어, 접근 통제)
  - D5 런타임 탐지: LLM·학습 모델 판정기로 행동·궤적·메시지를 감시(정합성 판정, 가드레일 모델, 이상 탐지)
  - D6 인간 감독: 사용자 확인·승인을 설계 요소로 포함
값이 없으면 '-'.

#### 3. 선별 판정 세칙(불일치 판정 과정에서 명시, 2026-10-01 추가)
- R1 I2(b)는 실행 중 개별 행동을 검사·제약·상향(확인 요청)하는 명시적 런타임 메커니즘(감시기, 검증기, 게이트, 정책 엔진, 확인 요청 장치)을 요구한다. 적대자 없이 에이전트 모델을 미세조정하거나 프롬프트로 안전하게 만드는 것만으로는 E2이다. 적대자를 상정하면 모델 견고화도 I2(a)의 방어(D1)이다.
- R2 다중 LLM·다중 에이전트 시스템은 에이전트 간 메시지가 다른 에이전트의 행동을 결정하는 경우 행동하는 시스템(I1)으로 본다. 악성 에이전트·모델이 상정되면 최종 출력이 텍스트여도 I2(a)이다.
- R3 도구(검색 포함)를 사용하는 에이전트는 피해가 행동이 아니라 응답 출력으로 나타나더라도 I1을 충족한다(침해 유형 OI). 실험이 도구 사용 없이 텍스트 처리만 수행하면 E1이다.
- R4 핵심 기여가 신뢰성·성능이고 안전 집행 요소가 부차적이면 E2이다.
- R5(행위자 세칙) 평가·감시 대상 에이전트 자체가 적대적으로 행동하는 경우(오정렬·계략·감독 회피)는 AGT로 코딩한다. 수동적 네트워크 관찰자 등 외부 관찰자는 EXT로 코딩한다. 질의만으로 메모리를 오염시키는 공격자는 USR로 코딩한다.
- R6(에이전트 적대자 세칙, 2차 선별 판정에서 추가) 에이전트 자체를 적대자로 보는 연구는 에이전트에 적대적 목표를 부여하거나(지시·미세조정·레드팀) 감독 회피를 유도하여 평가한 경우에 I2(a)로 본다. 적대적 목표 없이 일반 에이전트의 자발적 위험 행동·기만 경향만 측정하고 런타임 집행 메커니즘을 제안하지 않은 연구는 E2이다.


## 7. 원문 코딩 코딩북(방어 90편)

원본 파일: `EVAL_CODEBOOK_v2.md`

### 방어 연구 원문(full text) 코딩북 v2 (고정본, 2026-10-01)

대상: 방어 논문 목록(JSON). 각 논문의 원문을 읽고 아래 항목을 코딩한다. 다른 코더의 결과 파일(FT_*.tsv, defense_coding.tsv, corpus_*.json, CODER_*.tsv 등)은 열지 않는다. 원문 근거로만 판정하고, 확인할 수 없으면 '?'로 둔다.

#### 원문 찾기
- ACL 계열(site가 aclanthology.org): https://aclanthology.org/<id>.pdf 를 연다(게재본).
- 그 밖: arxiv_id가 있으면 https://arxiv.org/abs/<id> (판 이력 확인)와 https://arxiv.org/html/<id> 를 연다. 없으면 WebSearch로 "<제목> arXiv"를 1회 검색해 결과의 arxiv.org 링크를 쓴다. NDSS·USENIX는 학회 PDF(ndss-symposium.org, usenix.org)도 가능.
- openreview.net PDF는 403이므로 쓰지 않는다. WebSearch는 여러 작업자가 공유하는 예산이므로 논문당 최대 1회.
- 읽은 판(게재본 또는 arXiv vN)을 src에 기록한다.

#### 항목
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

#### 출력
TSV, 헤더:
rid	title	src	arxiv_id	arxiv_v1	stage	A_mode	judge	policy_src	judge_exposed	granularity	decisions	adversarial	adaptive	bench	public_bench	n_models	utility	overhead	fpr	hitl_burden	evidence


## 8. 판정 모델 입력(노출 수준) 코딩북

원본 파일: `pb/EXPOSURE_CODEBOOK.md`

### 노출 수준 세부 코딩북 (2026-10-01)

대상: 별도 LLM 판정기(가드 LLM, 검증 LLM, 판정 에이전트)를 두거나, 결정론적으로 집행되는 정책·규칙·계획을 LLM이 생성하는 에이전트 방어 논문. 원문을 읽고 아래 항목을 코딩한다. 다른 코더의 결과 파일은 열지 않는다. 근거가 없으면 '?'.

정의
- 원천 비신뢰 콘텐츠: 사용자 작업 밖에서 들어온 원문 그대로의 콘텐츠 — 도구 출력, 웹 페이지, 이메일·문서, 검색 결과, 메모리에서 읽은 기록, 다른 에이전트의 메시지 본문, 도구 설명(메타데이터).
- 파생 콘텐츠: 에이전트(LLM)가 원천 비신뢰 콘텐츠를 읽은 뒤 만든 것 — 제안된 도구 호출과 인자, 계획, 요약, 추론 과정(CoT).
- 신뢰 입력: 사용자 질의·작업, 시스템 프롬프트, 사전에 작성된 정책 문서, 도구 이름·스키마(설명 문장 제외는 아님; 도구 설명 문장은 원천 비신뢰로 본다).

항목
- judge_input (별도 LLM 판정기가 있을 때만; 없으면 '-'): 판정 LLM이 판정 시점에 입력으로 받는 것 중 가장 위험한 수준
  - RAW: 원천 비신뢰 콘텐츠를 직접 입력으로 받음(일부라도)
  - DERIVED: 원천 비신뢰 콘텐츠는 받지 않고 파생 콘텐츠(제안된 행동·인자, 계획, 요약)만 받음
  - TRUSTED: 신뢰 입력만 받음
- policy_input (LLM이 정책·규칙·계획을 생성할 때만; 없으면 '-'): 정책을 생성하는 LLM이 입력으로 받는 것 중 가장 위험한 수준(RAW / DERIVED / TRUSTED, 위와 같은 정의)
- policy_time (policy_input이 '-'가 아닐 때): RUNTIME(실행 중 작업마다 생성) / OFFLINE(배포 전 또는 설계 시점에 생성)
- evidence: 판정 근거가 되는 원문 문장 인용(짧게)과 절 번호


## 8a. 다른 모델 원문 재코딩 코딩북(7과 8을 합친 판)

원본 파일: `../xmodel2/CODEBOOK_FT.md`

### 방어 연구 원문(full text) 코딩북 v2 (고정본, 2026-10-01)

대상: 방어 논문 목록(JSON). 각 논문의 원문을 읽고 아래 항목을 코딩한다. 다른 코더의 결과 파일은 열지 않는다(/home/claude/w/search, /home/claude/w/review*, /home/claude/w/supp 디렉터리와 FINAL_CORPUS.json, STATS*.json은 열지 않는다). 원문 근거로만 판정하고, 확인할 수 없으면 '?'로 둔다.

#### 원문 찾기
- 입력 JSON의 fulltext_url이 가리키는 판을 읽는다(같은 판으로 비교하기 위함). 열리지 않으면 아래 규칙으로 대체하고 src에 실제로 읽은 URL을 적는다.
- ACL 계열(site가 aclanthology.org): https://aclanthology.org/<id>.pdf 를 연다(게재본).
- 그 밖: arxiv_id가 있으면 https://arxiv.org/abs/<id> (판 이력 확인)와 https://arxiv.org/html/<id> 를 연다. 없으면 WebSearch로 "<제목> arXiv"를 1회 검색해 결과의 arxiv.org 링크를 쓴다. NDSS·USENIX는 학회 PDF(ndss-symposium.org, usenix.org)도 가능.
- openreview.net PDF는 403이므로 쓰지 않는다. WebSearch는 여러 작업자가 공유하는 예산이므로 논문당 최대 1회.
- 읽은 판(게재본 또는 arXiv vN)을 src에 기록한다.

#### 항목
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

#### 출력
TSV, 헤더:
rid	title	src	stage	A_mode	judge	policy_src	judge_exposed	granularity	decisions	adversarial	adaptive	bench	public_bench	n_models	utility	overhead	fpr	hitl_burden	judge_input	evidence


#### 추가 항목: judge_input (헤더의 hitl_burden 뒤, evidence 앞에 열 추가)

- 원천 비신뢰 콘텐츠: 사용자 작업 밖에서 들어온 원문 그대로의 콘텐츠 — 도구 출력, 웹 페이지, 이메일·문서, 검색 결과, 메모리에서 읽은 기록, 다른 에이전트의 메시지 본문, 도구 설명(메타데이터).
- 파생 콘텐츠: 에이전트(LLM)가 원천 비신뢰 콘텐츠를 읽은 뒤 만든 것 — 제안된 도구 호출과 인자, 계획, 요약, 추론 과정(CoT).
- 신뢰 입력: 사용자 질의·작업, 시스템 프롬프트, 사전에 작성된 정책 문서, 도구 이름·스키마(설명 문장 제외는 아님; 도구 설명 문장은 원천 비신뢰로 본다).

항목
- judge_input (별도 LLM 판정기가 있을 때만; 없으면 '-'): 판정 LLM이 판정 시점에 입력으로 받는 것 중 가장 위험한 수준
  - RAW: 원천 비신뢰 콘텐츠를 직접 입력으로 받음(일부라도)
  - DERIVED: 원천 비신뢰 콘텐츠는 받지 않고 파생 콘텐츠(제안된 행동·인자, 계획, 요약)만 받음
  - TRUSTED: 신뢰 입력만 받음


## 8b. 선별 불일치 원문 재판정 코딩북

원본 파일: `../xmodel2/CODEBOOK_ADJ.md`

### 선별 조정 코딩북 (원문 확인)

#### 1. 선별(포함/제외)
포함(INC): 다음을 모두 만족
- I1 대상: 도구·웹/GUI·코드 실행·메모리·다른 에이전트·로봇 구동 중 하나 이상을 통해 실제 행동(외부 부작용 또는 다른 에이전트에 대한 행동)을 수행하는 LLM(멀티모달 포함) 기반 시스템
- I2 주 기여: (a) 적대적 위협에 대한 공격, 방어, 벤치마크·측정, 또는 (b) 적대자 유무와 무관하게 에이전트 행동에 대한 정책·권한·안전 규칙을 실행 중에 집행하는 메커니즘
제외(EXC) 사유 코드:
- E1 행동 요소가 없는 단일 LLM 수준 연구(탈옥·유해 출력, 행동 없는 프롬프트 인젝션, RAG 질의응답 오염, 텍스트만 출력하는 응용)
- E2 적대자 없이 성능·환각·일반 안전성·비적대적 위험 경향만 평가하고 런타임 집행 메커니즘을 제안하지 않음
- E3 서베이·SoK·포지션·입장 논문
- E4 LLM 에이전트를 보안 과업에 활용(침투 테스트, 취약점 탐지, CTF, 피싱·봇 탐지 등)
- E5 에이전트 실행 루프와 무관하게 기존 웹·API·네트워크 보안으로 동일하게 설명되는 위협
- E6 학습 단계 공격(데이터 오염·백도어)으로 에이전트 행동 경로를 다루지 않는 연구
- X 비LLM 시스템(다중 에이전트 강화학습, RL 정책 등) 또는 주제 무관


#### 3. 선별 판정 세칙(불일치 판정 과정에서 명시, 2026-10-01 추가)
- R1 I2(b)는 실행 중 개별 행동을 검사·제약·상향(확인 요청)하는 명시적 런타임 메커니즘(감시기, 검증기, 게이트, 정책 엔진, 확인 요청 장치)을 요구한다. 적대자 없이 에이전트 모델을 미세조정하거나 프롬프트로 안전하게 만드는 것만으로는 E2이다. 적대자를 상정하면 모델 견고화도 I2(a)의 방어(D1)이다.
- R2 다중 LLM·다중 에이전트 시스템은 에이전트 간 메시지가 다른 에이전트의 행동을 결정하는 경우 행동하는 시스템(I1)으로 본다. 악성 에이전트·모델이 상정되면 최종 출력이 텍스트여도 I2(a)이다.
- R3 도구(검색 포함)를 사용하는 에이전트는 피해가 행동이 아니라 응답 출력으로 나타나더라도 I1을 충족한다(침해 유형 OI). 실험이 도구 사용 없이 텍스트 처리만 수행하면 E1이다.
- R4 핵심 기여가 신뢰성·성능이고 안전 집행 요소가 부차적이면 E2이다.
- R5(행위자 세칙) 평가·감시 대상 에이전트 자체가 적대적으로 행동하는 경우(오정렬·계략·감독 회피)는 AGT로 코딩한다. 수동적 네트워크 관찰자 등 외부 관찰자는 EXT로 코딩한다. 질의만으로 메모리를 오염시키는 공격자는 USR로 코딩한다.
- R6(에이전트 적대자 세칙, 2차 선별 판정에서 추가) 에이전트 자체를 적대자로 보는 연구는 에이전트에 적대적 목표를 부여하거나(지시·미세조정·레드팀) 감독 회피를 유도하여 평가한 경우에 I2(a)로 본다. 적대적 목표 없이 일반 에이전트의 자발적 위험 행동·기만 경향만 측정하고 런타임 집행 메커니즘을 제안하지 않은 연구는 E2이다.


## 9. 검색 로그


### G1_security.log.md

#### G1 검색 로그: 보안 학회 (IEEE S&P, USENIX Security, ACM CCS, NDSS)

- 작업자 슬라이스: G1_security
- 검색일: 2026-10-01 (실행 시각 2026-09-30 23:31 – 2026-10-01 00:55 UTC)
- 출력: G1_security.tsv (79건 선별, 27건 INC)

##### 1. 1차 경로: Semantic Scholar bulk search, 실패

URL (PROTOCOL.md 작업지침 1 그대로, VENUES = 보안 4개 학회):
```
https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=(agent|agents|agentic|"multi-agent"|"tool-augmented"|"tool-integrated"|"LLM-integrated"|MCP)+(LLM|LLMs|"language model"|"language models")+(attack|attacks|security|injection|privacy|defense|adversarial|poisoning|backdoor|hijacking|exfiltration|authorization|"access control"|threat|threats)&publicationDateOrYear=2022-10-06:2026-09-30&venue=IEEE Symposium on Security and Privacy,USENIX Security Symposium,Conference on Computer and Communications Security,Network and Distributed System Security Symposium&fields=title,venue,year,publicationDate,citationCount,externalIds&sort=publicationDate:asc
```
- Bash curl로 직접 호출: 에이전트 프록시가 CONNECT 403으로 차단 (조직 정책). dblp, Crossref, usenix.org, arXiv도 curl은 같은 403.
- WebFetch로 호출: 23:31부터 00:08 UTC까지 20회 모두 HTTP 429 (매번 `sleep 90` 후 재시도). 00:12에 1회 더 시도했으나 역시 429 (상한 20회를 넘긴 시도이므로 여기 명시함).
- total: 받지 못함. 받은 건수: 0. 그래서 S2 기반 citationCount 열은 모두 "-"이다.
- 연도별 분할 질의는 하지 않았다. 응답이 잘린 것이 아니라 429로 거부된 것이기 때문이다.

##### 2. 대체 경로 (PROTOCOL 작업지침 2)

###### 2a. Crossref API (WebFetch)
- `query.bibliographic=LLM+agents+prompt+injection&filter=prefix:10.14722,from-pub-date:2022-10-06,until-pub-date:2026-09-30&rows=40` (NDSS DOI 접두어): total=60, 받은 건수 40.
- `query.bibliographic=agent+agents+agentic+tool+plugin+LLM-integrated&filter=prefix:10.14722,from-pub-date:2023-01-01,...&rows=40`: total=63, 받은 건수 40. 새로 확인된 문헌: SAGA (ndss.2026.230869).
- 두 질의의 offset=40 페이지: 429. WebFetch 프록시가 "Do not fetch this page again"으로 거부해 나머지 약 20건(NDSS 관련도 하위권)은 확보하지 못함.
- CCS (prefix 10.1145): `filter=isbn:9798400715259` → 0건 (필터 무효). `filter=container-title:` → 무시됨. `filter=type:proceedings-article`를 넣으면 필터가 무시된 응답이 옴.
  - `query.bibliographic=Computer+Communications+Security+LLM+agent+...&filter=prefix:10.1145,from-pub-date:2025-10-01,until-pub-date:2025-11-30&rows=80`: total=2836. 이 중 10.1145/3719027.* (CCS 2025) 항목만 골라 확인 (AgentSentinel, SecAlign, Give LLMs a Security Course, Agentic Shell Honeypot 포스터).
  - 같은 조건에 더 좁힌 질의(rows=100): total=794. 3719027 DOI는 2건뿐이었다. 응답이 잘린 것으로 보이며 신뢰도는 낮다.
- S&P (10.1109)와 CCS 2023/2024는 Crossref 질의 전에 429와 프록시 거부가 반복되어 수행하지 못함.

###### 2b. 공식 프로그램/채택 페이지 (WebFetch)
- sp2026.ieee-security.org/accepted-papers.html: 253편 확인. 키워드 목록을 두 번 받았는데 서로 일치함. 이 페이지가 S&P 2026 문헌의 주 출처.
- sp2025 accepted-papers: 내용 없음 (JS로 로드되는 페이지). S&P 2024: 확인하지 못함.
- ndss2024/2025/2026 accepted-papers: 2024는 140편, 2025는 211편을 전부 확인. 2026은 265편이지만 응답이 알파벳 "P"에서 잘림. 두 번째 요청에서는 존재하지 않는 제목을 지어내는 응답(hallucination)이 나와 폐기했고, 대신 Crossref로 보완함.
- NDSS 2026 프로그램 페이지: 1일차 세션만 받음 (잘림).
- usenix.org: sec26 technical-sessions와 cycle1-accepted-papers는 잘림. sec26_contents.pdf는 일부 목록만 받음 (Lethal Trifecta, MASLeak 등이 빠져 있어 불완전함이 분명함). sec25 technical-sessions도 잘림. 개별 presentation 페이지와 prepub PDF로 초록을 확인함.
- CCS 2025 accepted-papers와 ACM DL TOC: JS 페이지이거나 403. researchr ccs-2025는 잘린 목록만 받음.
- dblp: robots.txt로 차단.

###### 2c. WebSearch
- 약 60회 질의 (학회·연도 × agent/prompt injection/MCP/web agent/tool/multi-agent 조합, site:usenix.org 포함). 이후 세션 WebSearch 예산(200회, 다른 병렬 작업자와 공유)이 소진되어 중단함.
- 이 경로로 찾은 문헌은 note에 "route=web"으로 표시함.

##### 3. 판정 규칙 적용 메모
- 게재 확인: 공식 학회 페이지, 학회 DOI(Crossref), usenix.org 페이지 중 하나로 확인한 것만 해당 학회로 기록함. 2차 출처만 있는 문헌(Flashboom)은 note에 그렇게 적음.
- CCS 2026 문헌은 검색 결과에 나오지 않음 (해당되면 NP).
- Greshake et al.은 AISec'23 워크숍이므로 NP로 기록함 (awesome-list가 CCS'23으로 잘못 표기).
- first_public: arXiv id를 도구 출력에서 확인한 경우 그 연월을 씀. 기억에 의존한 id는 note에 "arXiv id recalled"로 표시함. arXiv를 확인하지 못한 경우 학회 게재 연월을 씀 (USENIX Sec 2025=2025-08, 2026=2026-08; S&P 2026=2026-05; NDSS 2026=2026-02; CCS 2025=2025-10). 이런 문헌은 실제 최초 공개일이 더 이를 수 있다.
- 경계 사례는 note에 "borderline"으로 표시함: SecAlign, Rennervate(NDSS'26), 챗봇 플러그인(S&P'26), LLM App Stores(S&P'25). 초록을 확인하지 못한 문헌은 "RECHECK"로 표시함 (Hijacking LALMs via Auditory PI).

##### 4. 완전성 평가 (중요)
- S2 경로가 완전히 실패했고 대체 경로도 rate limit과 응답 잘림으로 부분적이다. 이 슬라이스는 불완전하다.
- 특히 누락 가능성이 큰 범위:
  - CCS 2023, 2024, 2025 전체
  - S&P 2024, 2025 전체
  - USENIX Security 2024, 2025, 2026 (공식 목록을 끝까지 받지 못함)
  - NDSS 2026 중 Crossref 하위 20건
- 권고: S2 rate limit이 풀린 뒤 PROTOCOL URL을 다시 실행하고 이 TSV와 대조할 것.


### G2_ml.log.md

#### G2_ml 검색 로그 (ML venues: NeurIPS / ICML / ICLR)

- 검색일: 2026-10-01 (작업 시각 2026-09-30 23:31 ~ 2026-10-01 00:40 UTC 무렵)
- 프로토콜: /home/claude/w/search/PROTOCOL.md v8
- 출력: /home/claude/w/search/G2_ml.tsv (179행 = INC 72 + EXC 107)

##### 1. 1차 경로 (S2 bulk search) — 실패

URL (WebFetch, 공백 원문 유지):
```
https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=(agent|agents|agentic|"multi-agent"|"tool-augmented"|"tool-integrated"|"LLM-integrated"|MCP)+(LLM|LLMs|"language model"|"language models")+(attack|attacks|security|injection|privacy|defense|adversarial|poisoning|backdoor|hijacking|exfiltration|authorization|"access control"|threat|threats)&publicationDateOrYear=2022-10-06:2026-09-30&venue=Neural Information Processing Systems,International Conference on Machine Learning,International Conference on Learning Representations&fields=title,venue,year,publicationDate,citationCount,externalIds&sort=publicationDate:asc
```

| # | 시각(UTC, 대략) | 범위 | 결과 | total | 받은 건수 |
|---|---|---|---|---|---|
| 0 | 23:31 | 전체 | sleep 40 후 첫 호출, HTTP 429 | - | 0 |
| 1-19 | 23:34 ~ 00:11 | 전체 (1회는 2022-10-06:2023-12-31 분할) | 매회 `sleep 90` 후 재시도, 모두 HTTP 429 | - | 0 |
| 20 | 00:11 | 전체 | HTTP 429 (재시도 상한 20회 도달) | - | 0 |

- 보조 시도: Bash curl → api.semanticscholar.org는 egress 프록시가 CONNECT 거부(403, 조직 정책). OpenAlex API(WebFetch)도 429.
- **결론: S2 경로 V(ML venue)는 이 세션에서 0건 수신. total 미확인.**

##### 2. 대체 경로 (프로토콜 작업지침 2항)

- Crossref API (query.bibliographic=agent LLM prompt injection attack, rows=40): ICLR/ICML/NeurIPS 문헌 0건 (Crossref는 세 학회 프로시딩을 거의 색인하지 않음) → 사용 불가.
- 공식 프로시딩 목록 페이지(proceedings.mlr.press/v235, v267; mlanthology.org/iclr/2025; proceedings.neurips.cc/paper_files/paper/2025): WebFetch 출력이 잘림(앞쪽 600~1000건만 보임) 또는 권한 미승인 → 전수 확인 불가.
- 실제 사용한 경로 (모두 note에 `route=web`):
  1. WebSearch: venue×주제 조합 질의 다수 (예: "ICLR 2025 LLM agent prompt injection benchmark", "neurips.cc virtual 2025 poster ...", "icml.cc virtual 2026 poster ...", "proceedings.mlr.press v267 ...", 개별 제목 검증). 세션 WebSearch 예산(200회, 병렬 작업자와 공유)이 소진되어 이후 검증이 중단됨.
  2. 학회 공식 페이지(iclr.cc/icml.cc/neurips.cc 포스터·오럴 URL, proceedings.iclr.cc / papers.neurips.cc / proceedings.mlr.press PDF·HTML)로 게재 확인.
  3. 2차 목록: github.com/jiaxianyan/icml-iclr-2026-agent-papers (ICLR 2026 / ICML 2026 agent 논문 목록, 안전·보안 섹션 48/82건 전체 열람; ICML 목록은 icml.cc /poster/ 링크 제공 → 본 트랙), en.papernotes.org (ICLR2026/ICML2026/ICML2025/NeurIPS2025 카테고리·노트; 워크숍 논문도 섞여 있어 노트의 venue 표기를 개별 확인), cua.ai NeurIPS 2025 CUA 목록, alexdrouin NeurIPS 2025 목록.
- 워크숍 판정: neurips.cc/icml.cc/iclr.cc 의 비-poster 이벤트 ID URL(예: /virtual/2025/128597, /virtual/2025/49348) 및 papernotes "workshop" 표기 → `WS`. 인용수(≥50 예외) 확인은 S2 불가로 미수행.

##### 3. 선별 결과

| venue | INC |
|---|---|
| ICML 2024 | 1 |
| NeurIPS 2024 (D&B 포함) | 5 |
| ICLR 2025 | 8 |
| ICML 2025 | 8 |
| NeurIPS 2025 (D&B 포함) | 11 |
| ICLR 2026 | 20 |
| ICML 2026 | 19 |
| NeurIPS 2023 / ICLR 2024 / ICML 2023 | 0 (ICLR 2024 ToolEmu는 E2) |
| 합계 | 72 |

- 유형(주 라벨 조합): A 23, B 23, D 15, A;B 4, A;D 4, B;D 3 (다중 라벨 집계: A 31, B 30, D 22)
- 제외 107: E2 36, E1 21, E4 18, WS 18, E3 6, E5 3, E6 3, NP 2
- NeurIPS 2026: 검색일 기준 미개최 → 해당 후보 없음(검색하지 않음, NP 규칙상 전부 제외 대상)
- 최초 공개(first_public) 범위(INC): 2024-02 (Agent Smith; Watch Out for Your Agents; Secret Collusion) ~ 2026-07 (ICML 2026 arXiv 미확인 12편에 학회 개최월 대입). arXiv로 확인된 최신은 2026-06 (MINIM, 2606.13949).

##### 4. 한계·후속 검증 필요 (중요)

1. **S2 total 미확보** → 재현성 요구(총건수 대비 수신건수) 미충족. S2 rate limit 해소 후 동일 URL 재실행 및 본 TSV와 대조 필요.
2. **웹 경로 재현율 한계**: ICML 2024/2025, NeurIPS 2024/2025는 전수 목록 확인 불가 → 누락 가능성 있음(특히 NeurIPS 2025 본 트랙).
3. note에 `arXiv id/month from prior knowledge, not re-verified` 표기된 11편(Watch Out, AgentDojo, BadRobot, BALD, GuardAgent, ShieldAgent, AdvAgent, WASP, Security Challenges, RiOSWorld, ToolEmu)은 arXiv id·월을 재확인할 것.
4. ICML 2026 12편은 arXiv id 미확인 → first_public=2026-07(게재월) 임시값. arXiv 확인 시 대부분 더 이른 월로 바뀜.
5. `NEEDS-CHECK` 표기 EXC 행(GUARDIAN, AIR, ANCHOR, Cybersecurity Refusals, TRACER, PrivAct, Contextualized Privacy Defense, Prompt Injection as Role Confusion, Security–Fidelity Tradeoffs, Log-To-Leak, Hiding in Plain Floats, Inference-Time Backdoors via Chat Templates)은 초록 미확인 상태의 보수적 제외 → 초록 확인 후 INC 전환 가능.
6. AdvAgent(ICML 2025)와 GhostEI-Bench(ICLR 2026)는 2차 목록으로만 venue 확인(공식 포스터 URL 미확인).
7. citations 열은 S2 불가로 전부 '-'.


### G3_nlp.log.md

#### G3_nlp 검색 로그 (NLP venues: ACL, EMNLP, NAACL incl. Findings)

- 작업자: G3 (NLP slice)
- 검색일: 2026-10-01 (UTC 2026-09-30 23:3x ~ 2026-10-01)
- VENUES = Annual Meeting of the Association for Computational Linguistics,Conference on Empirical Methods in Natural Language Processing,North American Chapter of the Association for Computational Linguistics

##### 1. S2 bulk search (경로 V, 1차) — 실패

URL (WebFetch):
https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=(agent|agents|agentic|"multi-agent"|"tool-augmented"|"tool-integrated"|"LLM-integrated"|MCP)+(LLM|LLMs|"language model"|"language models")+(attack|attacks|security|injection|privacy|defense|adversarial|poisoning|backdoor|hijacking|exfiltration|authorization|"access control"|threat|threats)&publicationDateOrYear=2022-10-06:2026-09-30&venue=<VENUES>&fields=title,venue,year,publicationDate,citationCount,externalIds&sort=publicationDate:asc

| # | 시각(UTC, 대략) | 결과 |
|---|---|---|
| 0 | 2026-09-30 23:33 (sleep 70 후) | HTTP 429 |
| - | 23:34 | (Bash curl 시도) 프록시 CONNECT 403 — api.semanticscholar.org, api.crossref.org는 Bash egress 정책상 차단. 이후 WebFetch만 사용 |
| 1 | 23:36 | 429 |
| 2 | 23:38 | 429 |
| 3 | 23:39 | 429 |
| 4 | 23:41 | 429 |
| 5 | 23:47 | 429 |
| 6 | 23:49 | 429 |
| 7 | 23:50 | 429 |
| 8 | 23:52 | 429 |
| 9 | 23:55 | 429 |
| 10 | 23:58 | 429 |
| 11 | 2026-10-01 00:00 | 429 |
| 12 | 00:03 | 429 |
| 13 | 00:07 | 429 |
| 14 | 00:11 | 429 |
| 15 | 00:16 | 429 |
| 16 | 00:21 | 429 |
| 17 | 00:26 | 429 |
| 18 | 00:31 | 429 |

- 최초 호출 + 재시도 20회(각 재시도 전 sleep 90~300 s) 모두 HTTP 429. total = 확인 불가, 받은 건수 = 0.
- S2 경로 결론: **불가(route failure)**.

##### 2. Crossref (독립 경로, prefix 10.18653) — 실패

URL (WebFetch): https://api.crossref.org/works?query.bibliographic=LLM+agent+prompt+injection&filter=prefix:10.18653,from-pub-date:2022-10-06,until-pub-date:2026-09-30&select=DOI,title,container-title,published&rows=40
- 시도 6회 (23:36, 23:41, 23:50, 00:00, 00:11, 00:26): 모두 HTTP 429. Bash curl은 프록시 403.
- 변형 질의(agent attack / agent privacy / multi-agent security / tool agent defense / web agent attack / memory poisoning agent)는 기본 질의가 계속 429여서 실행하지 못함.
- Crossref 경로 결론: **불가(route failure)**.

##### 3. 기타 시도
- ACL Anthology 볼륨 페이지 (https://aclanthology.org/volumes/2025.findings-naacl/) WebFetch: 응답이 56/수백 편에서 잘림 → 볼륨 전수 열람 경로 불가.
- dblp.org search API, export.arxiv.org API: WebFetch robots.txt 차단.

##### 4. 대체 경로 계획 1(WebSearch + 공식 프로시딩 페이지) — 폐기
- 처음 계획: WebSearch(site:aclanthology.org)로 후보를 모으고 Anthology 논문 페이지로 확인. 아래 사유로 쓰지 않았고 5절의 경로로 바꿈.

- WebSearch: 1회 성공(site:aclanthology.org 예비 질의, 후보 확인용) 후 세션 WebSearch 예산(200회, 병렬 작업자 공유) 소진으로 추가 질의 불가 → WebSearch 경로도 사실상 불가.

##### 5. 실제 사용한 대체 경로: ACL Anthology 공식 메타데이터(XML) + 프로토콜 불리언 질의의 로컬 적용 (route=anthology-xml)

- 출처: GitHub acl-org/acl-anthology, branch master, commit d9a3b806f3703df4bedacdd1e662800b423f7d87 (2026-10-01 UTC 00:4x 기준, `git ls-remote`)
  - https://raw.githubusercontent.com/acl-org/acl-anthology/master/data/xml/{2022.emnlp,2022.findings,2023.acl,2023.findings,2023.emnlp,2024.acl,2024.findings,2024.emnlp,2024.naacl,2025.acl,2025.findings,2025.emnlp,2025.naacl,2026.acl,2026.findings}.xml (모두 HTTP 200)
  - 2023.naacl.xml, 2026.naacl.xml, 2026.emnlp.xml → 404 (NAACL 2023·2026 미개최, EMNLP 2026 프로시딩 미공개 → EMNLP 2026 채택 논문은 구조적으로 NP)
- 범위 볼륨: 2022 EMNLP main/demos/industry + Findings-EMNLP 2022 (2022-12 게재, 하한 2022-10-06 이후); ACL·EMNLP·NAACL 2023–2026의 main(long/short), demo, industry, SRW, Findings(ACL/EMNLP/NAACL). 제외: tutorials, Findings-EACL/AACL/IJCNLP(범위 밖 venue), 개별 workshop XML(미수집). SRW 일치 건은 WS로 제외 기록.
- 질의: 프로토콜 Q를 제목+초록에 대소문자 무시 정규식으로 적용 (스크립트: /home/claude/w/search/G3_nlp_screen.py)
  - A = agent\w* | multi-agent | tool-augmented | tool-integrated | llm-integrated | mcp
  - B = llms? | language models?
  - C = attack\w* | secur\w* | inject\w* | privacy | defen[cs]\w* | defend\w* | adversar\w* | poison\w* | backdoor\w* | hijack\w* | exfiltrat\w* | authori[sz]\w* | access control | threat\w*
  - S2의 어간 처리 차이를 감안해 일부 접두 일치로 넓혔음(재현율↑, 수작업 선별로 보정).
- 결과: 범위 볼륨 내 논문 24,263편 중 질의 일치 249편 (S2 total에 대응하는 값 = 249, 받은 건수 = 249, 잘림 없음).
  - 일치 분포: 2026 Findings-ACL 56, 2026 ACL long 54, 2025 EMNLP main 25, 2025 Findings-EMNLP 24, 2025 ACL long 19, 2025 Findings-ACL 11, 2024 Findings-EMNLP 6, 2024 EMNLP main 6, 2025 Findings-NAACL 6, 2025 EMNLP industry 6, 2025 NAACL long 6, 2026 ACL demo 6, 2026 ACL industry 5, 2024 Findings-ACL 4, 2024 ACL long 2, 2025 ACL SRW 2, 2025 ACL industry 2, 기타 각 1 (2022 EMNLP main, 2022 Findings-EMNLP, 2023 EMNLP main, 2024 Findings-NAACL, 2024 EMNLP demo, 2025 EMNLP demos, 2025 NAACL SRW, 2025 NAACL demo, 2026 ACL SRW).
  - 초록 결측: 2024–2026 일부 볼륨에서 0–3% 논문의 초록이 XML에 없음(제목만 매칭) → 소폭 누락 가능.
- 공식 프로시딩 페이지 확인: 2025.findings-naacl.395 페이지 WebFetch로 venue·DOI 일치 확인(표본).

##### 6. 선별 결과
- 249건 전수 선별(제목+초록, 초록 불충분 시 전문 초록 확인). INC 67 / EXC 182 (E2 126, E1 33, E4 10, E3 8, WS 4, E6 1; NP 0 — EMNLP 2026은 XML 부재로 후보 자체가 없음).
- INC venue: ACL 31(industry/demo 포함), Findings-ACL 15, Findings-EMNLP 10, EMNLP 9(demo/industry 포함), Findings-NAACL 2. 게재연도: 2024 5, 2025 31, 2026 31.
- demo/industry 트랙은 본회의 프로시딩(동료심사)으로 보고 INC하되 note에 표기. SRW(Student Research Workshop)는 WS로 제외.
- 경계 사례(note에 borderline 표기): Caution for the Environment(ACL 2025), Privacy Collapse(ACL 2026), PS-Bench(ACL 2026). 비적대적 프라이버시 유출(Privacy in Action, CI-Work)은 T4·권한(정보 흐름) 문제로 보고 INC. 비적대적 일반 안전(LCO, Safety Sidecar, MADRA 등)은 E2, 행동 정책 집행이 주 기여인 TrustAgent·SafeMCP·OS-Sentinel은 I2(런타임 집행)로 INC.

##### 7. 한계 (상위 작업자 확인 필요)
- citations: S2 불가로 전부 NA.
- first_public: arXiv id 조회 경로(S2, arXiv API/검색, WebSearch) 모두 불가. arxiv.org/abs 단건 확인이 된 InjecAgent(2403.02691, v1 2024-03-05)만 arXiv 날짜 사용, 나머지 66건은 프로시딩 게재월(상한값)로 기입하고 note에 표기. → 유효 조사 기간 산정 전 S2/arXiv로 보정 필요(특히 2024–2025 게재 논문은 arXiv v1이 수개월 앞섬).
- Crossref 독립 경로 미수행(429) → route=crossref 보완 건 없음.



### G4_ai_se_jnl.log.md

#### G4 로그 — AI·SE·저널 (AAAI, IJCAI, ICSE, FSE, TDSC, TIFS, TOPS)

- 검색일: 2026-10-01 (작업 시각 UTC 2026-09-30 23:31 ~ 2026-10-01 01:06)
- 결과 상태: **경로 실패 — 슬라이스 미완료(불완전).** 아래 TSV는 대체 경로로 우연히 확보된 소수 기록만 담고 있으며, 해당 venue 전체에 대한 체계적 검색 결과가 아님. 재수행 필요.

##### 1. S2 bulk search (WebFetch)
URL (주 쿼리, 프로토콜 Q 그대로):
`https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=(agent|agents|agentic|"multi-agent"|"tool-augmented"|"tool-integrated"|"LLM-integrated"|MCP)+(LLM|LLMs|"language model"|"language models")+(attack|...|threats)&publicationDateOrYear=2022-10-06:2026-09-30&venue=AAAI Conference on Artificial Intelligence,International Joint Conference on Artificial Intelligence,International Conference on Software Engineering,IEEE Transactions on Dependable and Secure Computing,IEEE Transactions on Information Forensics and Security,ACM Transactions on Privacy and Security&fields=title,venue,year,publicationDate,citationCount,externalIds&sort=publicationDate:asc`

| # | 시각(UTC) | 변형 | 결과 |
|---|---|---|---|
| 1 | 23:33 | 전체 기간 | 429 |
| 2 | 23:35 | 전체 | 429 |
| 3 | 23:37 | 전체 | 429 |
| 4 | 23:38 | 전체 | 429 |
| 5 | 23:40 | 전체 | 429 |
| 6 | 23:41 | 전체 | 429 |
| 7 | 23:43 | 전체 | 429 |
| 8 | 23:49 | 전체 | 429 |
| 9 | 23:51 | 2022-10-06:2024-12-31 분할 | 429 |
| 10 | 23:56 | 전체 | 429 |
| 11 | 23:58 | 전체 | 429 |
| 12 | 00:01 | 전체 | 429 |
| 13 | 00:04 | 전체 | 429 |
| 14 | 00:08 | 전체 | 429 |
| 15 | 00:10 | 전체 | 429 |
| 16 | 00:11 | venue=AAAI 단독 | 429 |
| 17 | 00:16 | 전체 | 429 |
| 18 | 00:21 | 전체 | 429 |
| 19 | 00:26 | 전체 | 429 |
| 20 | 00:31 | 전체 | 429 (프로토콜 상한 도달) |
| 21 | 00:44 | 전체 (추가 재시도) | 429 |
| 22 | 00:55 | 전체 (추가 재시도) | 429 |
| 23 | 01:04 | 전체 (추가 재시도) | 429 |
| FSE | 01:05 | venue=ESEC/SIGSOFT FSE,Proc. ACM Softw. Eng. | 429 |

- 재시도 간 대기: Bash sleep 90~590초.
- total / 받은 건수: **0 / 0** (응답 수신 실패).
- 참고: S2 단건 조회(`/paper/arXiv:2302.12173`)는 00:09에 1회 성공 → IP 차단이 아닌 검색 엔드포인트 rate limit. 이후 단건 조회(`arXiv:2502.19145`)와 `/paper/search`, `/paper/search/match`도 429.
- Bash curl로 직접 호출 시도: 에이전트 프록시가 api.semanticscholar.org / api.crossref.org CONNECT 거부(403, 조직 정책) → 불가.

##### 2. Crossref (대체 경로)
- `https://api.crossref.org/works?query.bibliographic=LLM+agent+attack&filter=prefix:10.1609,from-pub-date:2022-10-06,until-pub-date:2026-09-30&select=DOI,title,container-title,published&rows=40` — 23:38, 23:40, 23:43, 23:53, 00:45: 모두 429.
- 동일 + `&mailto=...` — WebFetch 프록시가 429로 거부하며 해당 페이지 재요청 금지 지시 → 중단(사용자에게 알림 전송).
- `query.bibliographic=LLM+agent+prompt+injection` (prefix 10.1609) — 00:32: 429.
- IJCAI(10.24963), ACM(10.1145), IEEE(10.1109) 변형 및 저널 container-title 변형: **미실행** (선행 호출이 모두 429).
- total / 받은 건수: **0 / 0**.

##### 3. 기타 대체 경로
- dblp API: robots.txt 차단. ojs.aaai.org 검색 페이지, arxiv.org: WebFetch 권한 요청 무응답(PROVENANCE_REQUIRED).
- WebSearch: 3회 실행 후 세션 WebSearch 예산(200회, 병렬 작업자와 공유) 소진.
  - "AAAI 2025 prompt injection LLM agent attack ojs.aaai.org"
  - "ojs.aaai.org LLM agents indirect prompt injection defense AAAI-26"
  - "ojs.aaai.org multi-agent system LLM attack security AAAI 2025"
- WebSearch 결과에 나온 ojs.aaai.org 원문(갤리) 6건을 WebFetch로 열어 제목·초록·회차·arXiv id 확인 → TSV 기록(note에 route=websearch+ojs).
- 슬라이스 venue 밖 결과(KDD 2025 10.1145/3690624.3709179, AIES, MDPI Information, ScienceDirect ICT Express, arXiv 전용 2602.22724 등)는 본 슬라이스 범위가 아니므로 기록하지 않음.

##### 4. 결과
- TSV: /home/claude/w/search/G4_ai_se_jnl.tsv — 8건(INC 2, EXC 6: E2×2, E1×1, E4×2, WS×1).
- IJCAI, ICSE, FSE, TDSC, TIFS, TOPS: **0건 확인 — 검색 자체가 수행되지 못함(결과 없음이 아님).**
- 미검증 항목: Multi-Agent Security Tax의 arXiv id 2502.19145는 기억에 의존, S2 429로 미확인. 미확인 시 first_public은 게재월(AAAI-25, 2025-04)로 대체해야 함. 모든 citations는 미수집('-').
- 권고: rate limit이 풀린 시점(또는 API key 사용)에 G4 슬라이스 전체 재수행.


### G5_cite_snowball.log.md

#### G5 log — route C (high-citation), early boundary, route S (snowball)

Search date: 2026-10-01 (KST). Worker started 2026-09-30T23:33Z (after `sleep 130` stagger).

##### 1. Route C — S2 bulk query (minCitationCount=50, no venue filter)

URL (WebFetch):
```
https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=(agent|agents|agentic|"multi-agent"|"tool-augmented"|"tool-integrated"|"LLM-integrated"|MCP)+(LLM|LLMs|"language model"|"language models")+(attack|attacks|security|injection|privacy|defense|adversarial|poisoning|backdoor|hijacking|exfiltration|authorization|"access control"|threat|threats)&publicationDateOrYear=2022-10-06:2026-09-30&minCitationCount=50&fields=title,venue,year,publicationDate,citationCount,externalIds&sort=publicationDate:asc
```

| attempt | time (UTC, approx.) | result |
|---|---|---|
| 1 | 23:35 | 429 |
| 2–20 | 23:36 – ~00:35 | 429 every time (sleep 60–300 s between tries; 2 tries used reordered parameters to avoid caching; 1 try was a single-paper lookup `paper/arXiv:2302.12173`; 1 try used `/paper/search` relevance endpoint) |
| extra probe | ~00:50 | 429 |

- **total = not obtained; rows received = 0. Route C via S2 FAILED.**
- Direct `curl` to api.semanticscholar.org, api.crossref.org, api.openalex.org, dblp.org and export.arxiv.org: the agent proxy rejects the CONNECT (403). curl to usenix.org and arxiv.org is also blocked.
- Fallback attempts:
  - OpenAlex via WebFetch (`/works?filter=cited_by_count:>49,...`) returned 429 (2 tries).
  - Crossref via WebFetch (`query.bibliographic=LLM agents prompt injection attack security`, sort=is-referenced-by-count) responded, but returned irrelevant items. Crossref also does not cover arXiv-only records, so it can't stand in for route C.
  - Citation-count sources tried and found unusable: semanticscholar.org HTML (403), dl.acm.org (403), Google Scholar/dblp (robots), pith.science (403), alphaxiv/lacuna/awesomepapers/paperswithcode.co (no counts, or 0 or wrong).
- **Substitute procedure:** I identified candidates from (a) the SoK reference list, (b) the Deng et al. reference list, (c) WebSearch for well-known agent-security works, and (d) the early-window queries. Publication status was verified per record (arXiv abs comments/journal-ref, dblp search snippet, publisher/proceedings pages, project pages). **Citation counts are recorded as `NA`. The ≥50 condition is NOT machine-verified for any record.** Each route-C INC and each PRE row carries the flag "cite>=50 unverified" and must be re-checked when S2 is available.
- The WebSearch budget (200 per session) ran out during verification. Some venue claims for inV rows therefore come from memory and are marked "venue from memory" in the note column.

##### 2. Early boundary (2022-10-06 – 2023-06-30)

WebSearch queries: "indirect prompt injection LLM-integrated applications 2023 attack plugins", "ChatGPT plugins security analysis 2023 paper", "2023 LLM agent tool use attack ... AutoGPT security", "arXiv 2023 LLM-integrated OR application-integrated prompt injection attack March April May 2023", plus per-paper venue checks.

| first public | work | venue | I1? | decision |
|---|---|---|---|---|
| 2022-11 | Perez & Ribeiro 2211.09527 | NeurIPS ML Safety WS 2022 | no (single LLM, no tools) | EXC E1 |
| 2023-02-11 | Kang et al. 2302.05733 | IEEE SPW 2024 (dblp conf/sp key), ICML'23 WS | no (jailbreak/malicious content) | EXC E1 |
| **2023-02-23** | **Greshake et al. 2302.12173** | **AISec'23 (ACM DOI 10.1145/3605764.3623985)** | **yes (retrieval/plugin/email-acting apps, Bing Chat, code completion)** | **INC (route C)** |
| 2023-04 | Li et al. 2304.05197 Multi-step jailbreaking privacy | EMNLP Findings 2023 | mostly single LLM; New Bing retrieval part is borderline | EXC E1 |
| 2023-05 | Pan et al. 2305.13661 misinformation pollution | EMNLP Findings 2023 | no (ODQA) | EXC E1 |
| 2023-06 | Liu et al. HouYi 2306.05499 | arXiv only | apps without tool actions (borderline) | EXC E1 |

No other in-scope (I1+I2) agent or tool-integrated work first made public in this window was found. The next earliest in-scope works are 2023-08 Pedro et al. (ICSE'25), 2023-09 LLMSmith (CCS'24), and 2023-09 Iqbal et al. ChatGPT plugins (AIES'24).

**Earliest included record: Greshake et al., arXiv v1 2023-02-23** (abs page lists "v1 Thu, 23 Feb 2023"; v2 2023-05-05). It is peer-reviewed at AISec '23, a CCS workshop and not CCS main, so it enters through route C. Its ≥50 citations are not machine-verified. It is cited by both seed surveys (SoK [48]; Deng).

##### 3. Snowballing (route S)

- **SoK (Kim, Guo, Song; USENIX Security '26, pp. 6047–6066).** Source: https://www.usenix.org/system/files/usenixsecurity26-kim-juhee-agentic.pdf and the prepub PDF. Refs [1]–[148] were extracted verbatim. WebFetch truncated the rest: the reference list ends at [162], and [149]–[162] were not readable. The extended arXiv version is 2603.11088 (Kim, Liu, Wang, Qiu, Li, Guo, Song).
- **Deng et al. (ACM CSUR 2025, DOI 10.1145/3716628).** arXiv PDF: truncated. arXiv HTML v2: the bibliography came back only as a paraphrased author/topic list, not verbatim. ACM DL: 403. Only works that could be identified unambiguously were used.
- In-scope referenced works were kept if they were in a route-V venue (per the SoK's own bibliography entry, or per a venue page verified this session) or were arXiv-only and plausibly high-citation (PRE).
- I left out of the rows SoK-cited arXiv works whose citation count is likely below 50: Prompt Flow Integrity [60], Les Dissonances [74], Firewalls [1], AgentArmor [136], SentinelAgent [51], PromptArmor [123], Jha et al. [56], Takedown [65], Real AI agents with fake memories [106]. Re-check these when S2 is back.

##### 4. Output

`/home/claude/w/search/G5_cite_snowball.tsv`: 67 records plus a header.

- INC 33: 5 through route C (outside route V), 28 inV cross-check rows covered by the route-V worker.
- PRE 13: high-citation arXiv-only preprints, kept out of the corpus. ≥50 is unverified for all of them.
- EXC 21, with reasons E1, E2 or E3.

Route failures: S2 (all 20 retries returned 429), OpenAlex (429), Crossref (unusable for this purpose), curl egress (proxy 403), the Deng bibliography (no verbatim list), and SoK refs [149]–[162] (truncated).


### SNOWBALL.log.md

#### SNOWBALL log: one backward-snowballing iteration (Wohlin 2014) from 2 seed reviews

- Date: 2026-10-01. Output: `/home/claude/w/search/SNOWBALL.tsv` (379 distinct works + header, 10 columns, validated).
- Scope pre-check rule: CODEBOOK_v3.md §1 (INC-candidate / EXC E1–E6, X; `?` = no evidence). Judged on title only (plus the abstract for the few arXiv abs pages I read). It is a **pre-check**, not a final screening decision.
- Files read: `G5_cite_snowball.log.md` and `CODEBOOK_v3.md` only. No other coding files were opened.
- Network: curl to arxiv.org, usenix.org and crossref is proxy-blocked (403), so all retrieval went through WebFetch.

##### 1. Seed S1: Kim, Guo, Song, "SoK: Attack and Defense Landscape of Agentic AI Systems", USENIX Security 2026

**Completeness: 162 / 162 references obtained.** [1]–[148] are verbatim. [149]–[162] are reconstructed: 10 high confidence, 4 inferred.

| URL (WebFetch) | result |
|---|---|
| https://www.usenix.org/system/files/usenixsecurity26-kim-juhee-agentic.pdf | 4 range queries ([1]–[40], [41]–[85], [86]–[129], [130]–end). Text truncated inside [140]. In-text citation contexts for [140]–[162] were extracted from the body. The highest citation in the body is [162], so the total is 162. |
| https://www.usenix.org/conference/usenixsecurity26/presentation/kim-juhee (404); …/presentation/kim-juhee-agentic | The presentation page gave the prepub PDF link. |
| https://www.usenix.org/system/files/conference/usenixsecurity26/sec26_prepub_kim-juhee-agentic.pdf | [138]–[148] verbatim. Truncated at "[149] H. Ya…". |
| https://arxiv.org/abs/2603.11088 , https://arxiv.org/html/2603.11088v1 (3 queries), https://arxiv.org/pdf/2603.11088v1 | This is the **extended** arXiv version ("The Attack and Defense Landscape of Agentic AI: A Comprehensive Survey", 7 authors, author-year citations, about 362 references). It is NOT the seed's reference list. HTML truncated in §5.2.2. PDF truncated at its ref [24]. It was used only to read the titles in the `#bib.bibN "title"` citation anchors. |

**Reconstruction of [149]–[162].** The S1 bibliography is alphabetical by first-author surname. I combined three things: (a) each number's in-text context in the USENIX PDF; (b) the same sentence in arXiv 2603.11088v1 with its titled citation anchors; (c) the full set of Y/Z-surname works cited in 2603.11088v1, slotted alphabetically between [148] Yang Y. and the end.

- High confidence (context + anchor + alphabetical position all agree):
  - [149] ControlNet (Yao H.; the prepub prints "H. Ya…")
  - [150] ReAct
  - [151] Yu M. survey ("closest surveys [31,151]")
  - [155] ASB
  - [156] "LLM agents should employ security principles"
  - [157] HoneyBee
  - [159] GUARDIAN
  - [160] MELON
  - [161] Zod
  - [162] PoisonedRAG
- **Inferred (flagged `S1-recon INFERRED slot`):**
  - [152] Yueh-Han et al., decomposition monitors. The context is "distributed harm [140,152]", but the matching sentence was not visible in the extended HTML.
  - [153] InjecAgent ("V1 IPI [48,54,153]").
  - [154] Zhang C., "Goal-guided generative PI". No in-text context was found. It is the only remaining candidate between Zhan and Zhang H.
  - [158] RTBAS ("integrity protection [60,158,160]"). It is the only candidate between Zhong H. and Zhou J.
- Bibliographic details (initials, venue) for [149]–[162] are not verbatim.

##### 2. Seed S2: Deng et al., "AI Agents Under Threat", ACM CSUR 57(7), 2025 (DOI 10.1145/3716628)

**Completeness: 235 / 235 references obtained** (Crossref `reference-count` = 235 and the array has 235 items; keys e_1_3_1_2_2 … e_1_3_1_236_2, ref_no = key−1). This is the published CSUR reference list, which is preferable to the arXiv one.

| URL (WebFetch) | result |
|---|---|
| https://arxiv.org/html/2406.02630 (latest) and https://arxiv.org/html/2406.02630v1 | Truncated in §5. The bibliography is **not** reachable. (The task suggested the arXiv HTML; it is not usable through WebFetch.) |
| https://api.crossref.org/works/10.1145/3716628 (6 range queries) | All 235 deposited references. One response in the 91–135 range was condensed (first author plus title only). One response mis-numbered items by 1, which I corrected by key. |
| api.crossref.org/works?filter=doi:…(batch) | The first try silently ignored the filter (returned unrelated items). The retry returned **429 from the proxy** (user informed). A single-DOI Crossref lookup also returned **429** (user informed). I did not retry either. |
| api.openalex.org/works?filter=doi:…(batch) | 429 (target). Not retried. |
| api.semanticscholar.org/graph/v1/paper/arXiv:2406.02630/references | 429. Not retried. |
| doi.org/10.1109/TDSC.2024.3367737 , doi.org/10.1109/CISS59072.2024.10480189 | Permission prompt timed out, so not fetched. |
| aclanthology.org/{N19-3002, 2023.findings-emnlp.88, 2023.acl-long.293, 2023.inlg-main.3, 2021.eacl-main.74, 2023.findings-acl.881, 2021.acl-long.329, 2024.findings-emnlp.79, 2021.emnlp-main.168, 2020.findings-emnlp.301, 2023.eacl-main.199, 2023.findings-emnlp.272, 2023.emnlp-main.397, 2023.emnlp-main.741, 2023.emnlp-main.765, 2021.findings-emnlp.320, 2021.findings-emnlp.210}/ | Resolved 17 DOI-only ACL references. All 10 identifications I had made from memory were confirmed. |
| ojs.aaai.org/index.php/AAAI/article/view/{26596, 26240} | Resolved 2 AAAI DOI-only references. |

DOI-only S2 references: 36. Their resolution:
- 19 resolved via ACL Anthology / AAAI OJS.
- 1 resolved via WebSearch (ref 188: Weeks et al., ACSAC'23).
- 9 titled from memory and flagged "memory (unverified)" (refs 38, 53, 83, 100, 133, 136, 164, 165, 213; refs 38 and 83 are explicit guesses).
- **7 unresolved:** refs 9 (AIJ 2021), 17 (CSDE 2023), 21 (CVPR 2022), 48 (ICITR 2023), 110 (CISS 2024), 111 (TDSC 2024), 205 (BigDIA 2023).
  - Refs 9 and 21 are coded X, inferred from venue and year (they predate LLM agents).
  - The other 5 have scope `?`.

Four S2 titles (refs 115, 123, 131, 134) were not returned by the condensed Crossref response. They are recorded by journal + DOI; the ref 134 title is from memory.

##### 3. Overlap and duplicates

- 16 works are cited by both seeds and merged into one `both` row each: GPT-4, AgentPoison, Greshake, RAG (Lewis), Personal LLM agents, Formal-LLM, HouYi, Liu Y. (formalizing PI), Perez & Ribeiro, Toolformer, LLaMA, Instruction hierarchy, CoT, PRSA, InjecAgent, PoisonedRAG.
- S2 contains 2 internal duplicates: refs 55/56 (Greshake arXiv v1 title + AISec version) and 137/138 (Perez, NeurIPS WS + arXiv).
- Distinct works: 162 + 235 − 16 overlap − 2 internal duplicates = **379**.

##### 4. Venue verification (status as of 2026-10-01)

Status is set to `peer-reviewed` only when one of these holds:
- the seed bibliography prints a venue;
- a DOI identifies one;
- an arXiv abs comment, journal-ref or a venue page confirms it;
- for 4 INC rows, prior log or memory (flagged below).

For EXC rows, venues I know from memory but did not verify are written as `arXiv (mem: …)` and the status stays `arXiv`.

arXiv abs pages fetched (comments/journal-ref):
- 2503.18813, 2504.11703, 2505.23643, 2503.03704, 2506.12104 (NeurIPS'25), 2406.09187 (ICML'25)
- 2504.19793, 2504.03111 (NDSS'26), 2506.00641 (NeurIPS'25), 2503.18492, 2505.19234, 2502.08966
- 2507.15219, 2410.14923, 2403.02817, 2509.17488 (Findings EMNLP'25), 2502.01822 (TMLR 2026), 2503.15547
- 2505.03574, 2505.04799 (metadata unreadable), 2310.03185, 2505.24201, 2510.17276, 2509.24240
- 2506.07564 (unreadable), 2503.16248, 2504.03767, 2410.03055, 2508.01249, 2409.19091
- 2511.17959 (IEEE S&P 2026), 2402.16965 (unreadable), 2402.18649, 2311.11855, 2312.00374 (NDSS'25)
- 2402.08567 (ICML'24), 2409.11295 (ICLR'25), 2410.13691, 2406.12814 (ICLR'25), 2402.11208 (NeurIPS'24)
- Plus robopair.org (ICRA 2025).

WebSearch: **25 / 25 used**.

| # | query (abridged) | finding |
|---|---|---|
| 1–2 | DOI pairs (TDSC/CISS; ICITR/CSDE) | no match (OR queries do not work) |
| 3 | "10.1145/3627106.3627122" | Weeks et al., ACSAC'23 |
| 4 | CaMeL | **IEEE SaTML 2026** (computer.org CSDL) |
| 5 | Progent | no venue (arXiv) |
| 6 | ToolHijacker | **NDSS 2026** (ndss-symposium.org) |
| 7 | MINJA | **NeurIPS 2025** (neurips.cc poster 118152) |
| 8 | GUARDIAN | **NeurIPS 2025** (neurips.cc, papers.nips.cc) |
| 9, 15 | RoboPAIR | search inconclusive; robopair.org states **ICRA 2025** |
| 10 | VeriSafe Agent | **MobiCom 2025** (DOI 10.1145/3680207.3765248) |
| 11 | PromptArmor | no venue (arXiv) |
| 12 | AI Worm | **CCS 2025**, retitled "…Preventing the propagation of adversarial self-replicating prompts…" (DOI 10.1145/3719027.3765196) |
| 13 | Imprompter | no venue (arXiv) |
| 14 | Evil Geniuses | no venue (arXiv) |
| 16 | WIPI | no venue (arXiv) |
| 17 | RTBAS | no venue (arXiv) |
| 18 | PFI | no venue (arXiv) |
| 19 | FIDES | no venue (arXiv; MSR page) |
| 20 | f-secure | no venue (arXiv) |
| 21 | AgentArmor | no venue (arXiv) |
| 22 | Real AI agents w/ fake memories | no venue (arXiv) |
| 23 | Permissive IFA | **TMLR** (mlanthology tmlr/2025; TmlrPub) |
| 24 | Jha et al. ControlValve | no venue (arXiv; MSR page) |
| 25 | Wu F. "A new era in LLM security" | no venue (dblp CoRR only) |

Incidental finding: Yu M. et al. survey = KDD 2025 (DOI 10.1145/3711896.3736561), from the query 13 results.

**Peer-reviewed INC rows whose venue rests on memory or the prior log rather than a fetch this session:**
- S1[155] ASB (ICLR 2025)
- S1[160] MELON (ICML 2025)
- S2[103] LLMSmith (CCS 2024; G5 log)
- S2[135] P2SQL (ICSE 2025; G5 log)

Venues printed in the S1 bibliography (e.g., NDSS 2026 for ACE/SAGA, EMNLP 2025 for IPIGuard/MCIP) were taken as given and not re-verified. The bibliography does not say whether these are main track or Findings.

##### 5. Results

| | S1 | S2 | distinct |
|---|---|---|---|
| references obtained / total | 162/162 | 235/235 | 379 works |
| peer-reviewed | 68 | 118 | 176 |
| arXiv (incl. non-archival workshops) | 40 | 104 | 136 |
| other (blogs, docs, standards, news, CVE) | 54 | 13 | 67 |
| INC-candidate (any status) | 58 | 24 | 78 |
| **peer-reviewed + INC-candidate** | **28** | **16** (15 distinct) | **40** |
| arXiv + INC-candidate | 18 | 5 | 23 |
| other (grey) + INC-candidate topic | 12 | 3 | 15 |
| `?` (unresolved title) | 0 | 5 | 5 |

Borderline INC-candidates to re-check at full-text screening:
- AgentAuditor and R-Judge: evaluators/judges of agent trajectories.
- Permissive IFA: label propagation; agent setting.
- TrustAgent and Privacy in Action: non-adversarial, included via I2(b) runtime enforcement.
- AirGapAgent: whether agent actions are in scope.
- Agent Smith: harmful outputs that propagate between agents.
- The workshop items Motwani and Terekhov, and Evil Geniuses.

Borderline EXC (coded E1, could be argued INC):
- HouYi, SecAlign, NeMo Guardrails, Wen et al. (ICLR'25 AI-control).
- Formal-LLM (E2).


## 10. 실행 지시문 원문


### 10.1 High-citation and snowball route

모델 식별자: claude-opus-5-5

```text
You are executing one slice of a reproducible literature search for a Korean survey paper on LLM-based AI agent security. Read the protocol first: /home/claude/w/search/PROTOCOL.md (Korean; follow inclusion I1–I4, exclusion E1–E6/NP, coding type/T/D, TSV columns, log).

Your slice: route C (high-citation exception) and the early-period boundary.
1. Start with `sleep 130` (Bash) to stagger. Run the protocol's S2 bulk query WITHOUT a venue filter but with &minCitationCount=50 via WebFetch. On 429: `sleep 90`, retry up to 20 times. Split by half-year if truncated. Log totals/rows.
2. For every in-scope record (I1, I2, I4 satisfied), determine its publication status as of 2026-10-01: (a) published in one of the protocol's route-V venues (mark "inV" — another worker covers those, still list it), (b) peer-reviewed elsewhere (workshop, other conference/journal: give venue) → route-C inclusion, (c) arXiv-only → mark decision "PRE" (high-citation preprint, tallied separately, not in corpus). Verify venue status using S2 venue fields, WebSearch, or the paper's own page; note the evidence.
3. Early boundary check: independently identify ALL candidate agent/LLM-integrated-application security works first made public between 2022-10-06 and 2023-06-30 (any venue or arXiv), e.g. Greshake et al. (arXiv 2302.12173, AISec 2023), Perez & Ribeiro (2211.09527), Kang et al. (2302.05733), Liu et al. HouYi (2306.05499), and any others you find via WebSearch/S2 (queries: "indirect prompt injection 2023", "LLM-integrated application attack 2023", "plugin security LLM 2023", "ChatGPT plugins security"). For each: first public date, peer-reviewed venue (if any), citations, and whether it meets I1 (acting system with tools/plugins/retrieval actions) or fails (E1 single LLM). This determines the earliest included record.
4. Backward snowballing: fetch the reference list of the peer-reviewed SoK "SoK: Attack and Defense Landscape of Agentic AI Systems" (Kim, Guo, Song; USENIX Security 2026; find its arXiv/usenix PDF or HTML) and Deng et al. "AI Agents Under Threat" (ACM CSUR 2025, arXiv 2406.02630 HTML). List in-scope referenced works that are peer-reviewed in route-V venues or have ≥50 citations; mark note "route=snowball". Keep it to what you can verify.
5. Write TSV to /home/claude/w/search/G5_cite_snowball.tsv (decision values INC / EXC / PRE, reason codes) and log to /home/claude/w/search/G5_cite_snowball.log.md.

Return a short summary: counts, the earliest included record with evidence, number of high-citation arXiv-only preprints, route failures.
```


### 10.2 ML venues search/screen

모델 식별자: claude-opus-5-5

```text
You are executing one slice of a reproducible literature search for a Korean survey paper on LLM-based AI agent security. Read the protocol first: /home/claude/w/search/PROTOCOL.md (Korean; follow it exactly: inclusion I1–I4, exclusion E1–E6/NP, coding type/T/D, TSV columns, log).

Your slice: ML venues. VENUES parameter for the Semantic Scholar bulk search:
Neural Information Processing Systems,International Conference on Machine Learning,International Conference on Learning Representations

Steps:
1. Start with `sleep 40` (Bash) to stagger with parallel workers. Run the S2 bulk query from the protocol via WebFetch with this venue list. Semantic Scholar is often rate-limited (HTTP 429): on 429, run Bash `sleep 90` and retry, up to 20 times. This slice may return many rows; if output looks truncated or WebFetch cannot print all, split by year or half-year (e.g., 2022-10-06:2023-12-31, 2024-01-01:2024-12-31, 2025-01-01:2025-06-30, 2025-07-01:2025-12-31, 2026-01-01:2026-09-30) and fetch each. Record in the log the total reported and rows received per call.
2. Cross-check completeness with WebSearch for agent-security papers at NeurIPS 2023/2024/2025 (incl. Datasets & Benchmarks), ICML 2024/2025/2026, ICLR 2024/2025/2026 (queries like "ICLR 2025 LLM agent prompt injection benchmark"). Add missing in-scope papers with note "route=web".
3. Screen every record and code included ones per protocol. Verify venue publication by search date 2026-10-01 (NeurIPS 2026 → NP; workshop papers at these venues are not main-venue → exclude with reason "WS" unless you note citations ≥50). First public date = arXiv first version month when an arXiv id exists.
4. Write TSV to /home/claude/w/search/G2_ml.tsv and log to /home/claude/w/search/G2_ml.log.md.

Be accurate; do not include anything you could not verify. Exclude single-LLM jailbreak/prompt injection with no tool/action/agent component (E1), non-adversarial safety/capability benchmarks (E2), LLM-for-security-tasks (E4), training-time poisoning not tied to agent action paths (E6). Return a short summary: counts (retrieved, screened, included by type), earliest and latest included first_public, any route failures.
```


### 10.3 NLP venues search/screen

모델 식별자: claude-opus-5-5

```text
You are executing one slice of a reproducible literature search for a Korean survey paper on LLM-based AI agent security. Read the protocol first: /home/claude/w/search/PROTOCOL.md (Korean; follow it exactly: inclusion I1–I4, exclusion E1–E6/NP, coding type/T/D, TSV columns, log).

Your slice: NLP venues (main + Findings; Semantic Scholar labels Findings with the parent venue). VENUES parameter:
Annual Meeting of the Association for Computational Linguistics,Conference on Empirical Methods in Natural Language Processing,North American Chapter of the Association for Computational Linguistics

Steps:
1. Start with `sleep 70` (Bash) to stagger with parallel workers. Run the S2 bulk query from the protocol via WebFetch with this venue list. On HTTP 429: Bash `sleep 90`, retry up to 20 times. If output is truncated, split by year/half-year and fetch each. Log total reported and rows received per call.
2. Independent route: the ACL Anthology papers have DOIs (10.18653), so also run Crossref queries, e.g. https://api.crossref.org/works?query.bibliographic=LLM+agent+prompt+injection&filter=prefix:10.18653,from-pub-date:2022-10-06,until-pub-date:2026-09-30&select=DOI,title,container-title,published&rows=40 and variants (agent attack; agent privacy; multi-agent security; tool agent defense; web agent attack; memory poisoning agent). Add in-scope papers missing from S2 with note "route=crossref".
3. Screen every record and code included ones per protocol. Publication by search date 2026-10-01 (EMNLP 2026 → NP). Findings count as peer-reviewed (note "Findings"). Workshop papers → exclude with reason "WS". First public date = arXiv first version month when an arXiv id exists.
4. Write TSV to /home/claude/w/search/G3_nlp.tsv and log to /home/claude/w/search/G3_nlp.log.md.

Be accurate; do not include anything you could not verify. Exclude single-LLM jailbreak/prompt injection with no tool/action/agent component (E1), non-adversarial safety/capability work (E2), LLM-for-security-tasks (E4). Return a short summary: counts, earliest/latest included first_public, route failures.
```


### 10.4 Security venues search/screen

모델 식별자: claude-opus-5-5

```text
You are executing one slice of a reproducible literature search for a Korean survey paper on LLM-based AI agent security. Read the protocol first: /home/claude/w/search/PROTOCOL.md (Korean; follow it exactly: inclusion I1–I4, exclusion E1–E6/NP, coding type/T/D, TSV columns, log).

Your slice: SECURITY venues. VENUES parameter for the Semantic Scholar bulk search:
IEEE Symposium on Security and Privacy,USENIX Security Symposium,Conference on Computer and Communications Security,Network and Distributed System Security Symposium

Steps:
1. Start with `sleep 10` (Bash) to stagger with parallel workers. Run the S2 bulk query from the protocol via WebFetch with this venue list. Semantic Scholar is often rate-limited (HTTP 429): on 429, run Bash `sleep 90` and retry, up to 20 times. If output looks truncated, split by year (2022-10-06:2023-12-31, 2024, 2025, 2026-01-01:2026-09-30) and fetch each. Record in the log the total reported and rows received.
2. Also cross-check completeness by an independent route: WebSearch (and WebFetch of official program pages where they load) for agent-security papers at USENIX Security 2024/2025/2026, IEEE S&P 2024/2025/2026, CCS 2023/2024/2025, NDSS 2024/2025/2026 (e.g., queries like "USENIX Security 2025 prompt injection LLM agent"). Add any in-scope paper missing from S2 results, marking note "route=web".
3. Screen every record and code included ones per protocol. Verify that the paper actually appeared at that venue by the search date 2026-10-01 (CCS 2026 is after the search date → NP). First public date = arXiv first version month when an arXiv id exists.
4. Write TSV to /home/claude/w/search/G1_security.tsv and log to /home/claude/w/search/G1_security.log.md.

Be accurate; do not include anything you could not verify. Exclude single-LLM prompt injection/jailbreak work that has no tool/action/agent component (E1), and "LLM for security tasks" (E4). LLM-integrated applications with tool/plugin actions count as I1. Return a short summary: counts (retrieved, screened, included by type), earliest and latest included first_public, any route failures.
```


### 10.5 AI/SE/journal venues search

모델 식별자: claude-opus-5-5

```text
You are executing one slice of a reproducible literature search for a Korean survey paper on LLM-based AI agent security. Read the protocol first: /home/claude/w/search/PROTOCOL.md (Korean; follow it exactly: inclusion I1–I4, exclusion E1–E6/NP, coding type/T/D, TSV columns, log).

Your slice: AI, SE and journal venues. VENUES parameter for the Semantic Scholar bulk search:
AAAI Conference on Artificial Intelligence,International Joint Conference on Artificial Intelligence,International Conference on Software Engineering,IEEE Transactions on Dependable and Secure Computing,IEEE Transactions on Information Forensics and Security,ACM Transactions on Privacy and Security
(FSE: S2 venue names vary — try a separate call with venue=ESEC/SIGSOFT FSE and venue=Proc. ACM Softw. Eng. and keep only FSE papers.)

Steps:
1. Start with `sleep 100` (Bash) to stagger with parallel workers. Run the S2 bulk query from the protocol via WebFetch. On HTTP 429: Bash `sleep 90`, retry up to 20 times. Split by year if truncated. Log totals and rows received.
2. Independent route via Crossref (DOIs): AAAI prefix 10.1609, IJCAI 10.24963, ICSE/FSE/TOPS ACM 10.1145, TDSC/TIFS IEEE 10.1109. Example: https://api.crossref.org/works?query.bibliographic=LLM+agent+attack&filter=prefix:10.1609,from-pub-date:2022-10-06,until-pub-date:2026-09-30&select=DOI,title,container-title,published&rows=40 ; for journals use query.container-title=IEEE+Transactions+on+Dependable+and+Secure+Computing. Use several topical variants (prompt injection agent; multi-agent security; tool agent privacy; memory poisoning agent; MCP security). Add in-scope papers missing from S2 with note "route=crossref".
3. Screen every record and code included ones per protocol. Publication by search date 2026-10-01 (AAAI 2027 → NP). First public date = arXiv first version month when arXiv id exists. Workshop/bridge papers → exclude "WS".
4. Write TSV to /home/claude/w/search/G4_ai_se_jnl.tsv and log to /home/claude/w/search/G4_ai_se_jnl.log.md.

Be accurate; do not include anything you could not verify. Exclude single-LLM jailbreak/prompt injection with no tool/action/agent component (E1), non-adversarial safety/capability work (E2), LLM-for-security-tasks (E4). Return a short summary: counts, earliest/latest included first_public, route failures.
```


### 10.6 Screen ML hits batch B

모델 식별자: claude-opus-5-5

```text
Screen and code literature records for a survey on LLM-based AI agent security. Read /home/claude/w/search/PROTOCOL.md fully (Korean), especially inclusion I1–I4, exclusion E1–E6, and the section "개정(v8-2)" with the threat (T1–T6) and defense (D1–D6) coding rules — apply those rules strictly.

Input: /home/claude/w/search/ml_hits_b.json (102 records; each has rid, venue (e.g. icml2026, nips2025), track, status, title, abstract). All are accepted main-track (or NeurIPS Datasets & Benchmarks) papers that matched a keyword query; most will NOT be in scope. Decide each from title+abstract (abstract is given; no web search needed — web search budget is exhausted). You may use WebFetch on https://arxiv.org/abs/<id> only to find the arXiv first-version month for INCLUDED papers if you know the arXiv id with high confidence; otherwise leave arxiv_id "-" and set first_public to the conference month (ICML 2026=2026-07, NeurIPS 2024=2024-12, NeurIPS 2025=2025-12, AAAI 2025=2025-02) and note "fp=conf".

Key scope reminders: I1 requires an LLM-based system that acts (tools, web/GUI, code execution, memory, other agents, robots/embodied actuation via LLM planner). Pure chat jailbreak / single-LLM prompt injection without actions → E1. Non-adversarial capability/safety evaluation without attacker and without runtime policy enforcement → E2. LLM agents used to do security tasks (pentest, vuln finding, CTF) → E4. Multi-agent RL (non-LLM) → exclude E2 (note "non-LLM"). Training-time poisoning/backdoor not about agent action paths → E6; backdoors that trigger agent actions → include, T3.

Output: TSV /home/claude/w/search/R_ml_b.tsv, tab-separated with header:
rid	first_public	venue_short	pub_year	arxiv_id	site	title	decision	reason	type	T	D	note
venue_short like ICML, NeurIPS, NeurIPS-DB (Datasets & Benchmarks track), AAAI. decision INC/EXC; reason I or E1..E6; type A/D/B combos (A attack, D defense, B benchmark/measurement); T e.g. T1;T4; D for defenses only else "-". One-line note for borderline decisions. Return counts (INC, EXC by reason, INC by type) and the list of included titles with their codes, briefly.
```


### 10.7 Re-code NLP included records

모델 식별자: claude-opus-5-5

```text
Re-screen and re-code NLP-venue records for a survey on LLM-based AI agent security, so that coding is consistent with other venue groups. Read /home/claude/w/search/PROTOCOL.md fully (Korean), especially I1–I4, E1–E6, and section "개정(v8-2)" (track rule 'TR', and the T1–T6 / D1–D6 coding rules — apply strictly; note e.g. LLM-judge alignment checks at action time are D5, not D4; backdoors that trigger agent actions are T3).

Inputs: /home/claude/w/search/G3_nlp.tsv (249 screened records from an earlier worker, with decisions and codes) and /home/claude/w/search/nlp_hits.json (same 249 records with full abstracts; match by DOI/title). No web search is available (budget exhausted); decide from title+abstract. You may use WebFetch on https://arxiv.org/abs/<id> to get arXiv first-version months for INCLUDED papers only when you know the arXiv id with high confidence; otherwise keep first_public as proceedings month with note "fp=conf".

Tasks:
1. Apply the track rule: demo, industry, SRW tracks → EXC reason TR.
2. Re-check every INC and every E2/E1 exclusion for consistency with the scope rules (acting LLM system; adversarial threat or runtime policy enforcement). Non-adversarial privacy leakage by agents in action (contextual integrity) may stay INC under T4 as before.
3. Re-code type, T, D for all INC rows using the v8-2 rules.
Output: /home/claude/w/search/R_nlp.tsv with header:
rid	first_public	venue_short	pub_year	arxiv_id	site	title	decision	reason	type	T	D	note
(rid = DOI). Return counts (INC, EXC by reason, INC by type) and a list of changed decisions/codes versus G3 with one-line reasons.
```


### 10.8 Screen ML hits batch A

모델 식별자: claude-opus-5-5

```text
Screen and code literature records for a survey on LLM-based AI agent security. Read /home/claude/w/search/PROTOCOL.md fully (Korean), especially inclusion I1–I4, exclusion E1–E6, and the section "개정(v8-2)" with the threat (T1–T6) and defense (D1–D6) coding rules — apply those rules strictly.

Input: /home/claude/w/search/ml_hits_a.json (102 records; each has rid, venue (e.g. iclr2026), track, status, title, abstract). All are accepted main-track papers at ICLR/ICML/NeurIPS/AAAI/IJCAI that matched a keyword query; most will NOT be in scope. Decide each from title+abstract (abstract is given; no web search needed — web search budget is exhausted). You may use WebFetch on https://arxiv.org/abs/<id> only to find the arXiv first-version month for INCLUDED papers if you know/can infer the arXiv id with high confidence; otherwise leave arxiv_id "-" and set first_public to the conference month (ICLR 2025=2025-04, ICLR 2026=2026-04, ICML 2024=2024-07, ICML 2025=2025-07, ICML 2026=2026-07, NeurIPS 2024=2024-12, NeurIPS 2025=2025-12, AAAI 2025=2025-02) and note "fp=conf".

Key scope reminders: I1 requires an LLM-based system that acts (tools, web/GUI, code execution, memory, other agents, robots/embodied actuation via LLM planner). Pure chat jailbreak / single-LLM prompt injection without actions → E1. Non-adversarial capability/safety evaluation without attacker and without runtime policy enforcement → E2. LLM agents used to do security tasks (pentest, vuln finding, CTF) → E4. Multi-agent RL (non-LLM) → exclude E2 (note "non-LLM"). Training-time poisoning/backdoor that is not about agent action paths → E6; backdoors that trigger agent actions → include, T3.

Output: TSV /home/claude/w/search/R_ml_a.tsv, tab-separated with header:
rid	first_public	venue_short	pub_year	arxiv_id	site	title	decision	reason	type	T	D	note
venue_short like ICLR, ICML, NeurIPS, NeurIPS-DB (Datasets & Benchmarks track), AAAI, IJCAI. decision INC/EXC; reason I or E1..E6; type A/D/B combos (A attack, D defense, B benchmark/measurement); T e.g. T1;T4; D for defenses only else "-". Write a one-line note justifying borderline decisions. Return counts (INC, EXC by reason, INC by type) and list of included titles with their codes, briefly.
```


### 10.9 Consolidate security venue records

모델 식별자: claude-opus-5-5

```text
Consolidate the security-venue slice (IEEE S&P, USENIX Security, ACM CCS, NDSS) for a survey on LLM-based AI agent security. Read /home/claude/w/search/PROTOCOL.md fully (Korean), especially I1–I4, E1–E6, and section "개정(v8-2)" (T1–T6 / D1–D6 coding rules — apply strictly).

Inputs:
- /home/claude/w/search/G1_security.tsv and G1_security.log.md (earlier worker; partial coverage)
- /home/claude/w/search/G5_cite_snowball.tsv (rows marked inV for security venues; snowballed from a USENIX Security 2026 SoK)
- Additional candidate titles found in artifact-evaluation lists and a curated list. Run this to see them:
  python3 - <<'EOF'
  import re,glob
  for f in glob.glob('/home/claude/w/sa/_conferences/*/results.md'):
      v=f.split('/')[-2]
      if re.match(r'(usenixsec202[3-6]|ndss202[4-6]|sp2026)',v):
          for t in re.findall(r"title:\s*['\"]?(.*?)['\"]?\s*$",open(f).read(),re.M): print(v,'|',t)
  EOF
  Scan ALL those titles (not only keyword hits) for agent/LLM-integrated-application security papers; also scan /home/claude/w/Academic_LLM_Sec_Papers/Readme.md sections S&P/CCS/USENIX Security/NDSS 2023–2025.
- No web search is available (budget exhausted). You can WebFetch https://arxiv.org/abs/<id> pages and individual usenix.org presentation pages / ndss-symposium.org paper pages if needed to read an abstract or confirm the venue. Do not include anything whose venue you cannot confirm from a fetched page or the lists above; if venue known only from memory, mark note "venue=memory".

Rules: published by 2026-10-01 (CCS 2026 → NP). Greshake et al. (AISec 2023 workshop) is NOT a CCS main paper — leave it out of this slice (it's handled in route C). Exclude E1 (no action component), E4 (LLM used for security tasks), etc.

Output: /home/claude/w/search/R_sec.tsv with header:
rid	first_public	venue_short	pub_year	arxiv_id	site	title	decision	reason	type	T	D	note
venue_short S&P / USENIX / CCS / NDSS. first_public = arXiv v1 month if arXiv id confirmed (fetch abs page), else conference month with note "fp=conf" (USENIX Sec 2024=2024-08, 2025=2025-08, 2026=2026-08; S&P 2024=2024-05, 2025=2025-05, 2026=2026-05; NDSS 2024=2024-02, 2025=2025-02, 2026=2026-02; CCS 2023=2023-11, 2024=2024-10, 2025=2025-10). Include rows for every in-scope paper (INC) and for exclusions you considered seriously. Note each INC row's source (G1 / G5 / secartifacts / curated). Return counts (INC by venue-year, INC by type) and the list of INC titles with codes.
```


### 10.10 Code control point for 75 defenses

모델 식별자: claude-opus-5-5

```text
Code 75 defense papers (LLM-based AI agent security) on two additional axes. Input: /home/claude/w/search/defenses.json (rid, venue, year, title, T, D, abstract; 18 have empty abstracts — for those, use arXiv abstract pages via WebFetch https://arxiv.org/abs/<id> if you know the id with high confidence (e.g., AirGapAgent 2405.05175, IsolateGPT 2403.04960, CaMeL 2503.18813, Prompt Infection 2410.07283, AgentSpec 2503.18666, ACE 2504.20984, SAGA 2504.21034, AI Worm 2403.02817), or your reliable knowledge; mark "src=knowledge" when not read). Web search is unavailable.

Background (attack chain): an agent loop observes o_t and takes actions a_t (tool calls). Control stages where a defense is enforced:
- I: input acceptance (filtering/detecting/marking untrusted inputs or user data before they enter the model context; data minimization before interaction; model hardening against injected inputs counts as I)
- P: planning (fixing allowed plan/control flow/tool graph/policy before reading untrusted data, plan verification)
- M: memory write/read (checks on what is stored in or retrieved from long-term memory/RAG)
- A: action boundary immediately before a tool call / action executes (checking/allowing/blocking/modifying a tool call or its arguments; runtime monitors over actions/trajectories that gate execution)
- C: inter-agent communication (checks on messages/topology among agents)
Multiple stages allowed.

Axis 2 — decision authority ("판정 주체"): who/what makes the allow/deny judgment at enforcement time:
- LLM: an LLM (prompted or fine-tuned LLM judge/guard agent) decides
- ML: a non-LLM learned model (classifier, GNN, embedding detector) decides
- RULE: deterministic rules/policies/labels/isolation enforced by code (policies may be generated by an LLM beforehand — then also note "policy-by-LLM")
- HUMAN: user confirmation is part of the decision
Use combinations like "RULE+HUMAN" or "LLM+RULE". Also a flag policy_by_llm = Y if deterministic policies/plans are derived by an LLM from the natural-language task.

Output TSV /home/claude/w/search/defense_coding.tsv with header:
rid	title	stage	authority	policy_by_llm	note
Be consistent; use the abstract wording as evidence; one short note per row. Then report aggregate counts: number of papers including each stage (I,P,M,A,C), number with A, number with A only, counts per authority category (count a paper in every category it has), and how many rely on LLM judgment at decision time (authority contains LLM) or policy_by_llm=Y.
```


### 10.11 Independent screener: 150 sample

모델 식별자: claude-opus-5-5

```text
You are an independent second screener for a systematic mapping study on LLM-based AI agent security. Read the codebook /home/claude/w/search/CODEBOOK.md (section 1 is the screening rule) and apply it exactly. Do NOT open other result files in /home/claude/w/search (G*.tsv, R_*.tsv, corpus_all.json, CODER_*.tsv, defense_coding.tsv) — your judgment must be blind.

Input: /home/claude/w/search/blind_screen_sample.json (150 records: id, title, venue, abstract; 19 have no abstract). Decide INC or EXC (with exclusion code E1–E6 or X) for each from title+abstract. For records without an abstract, decide from the title, or if truly undecidable use at most 15 WebSearch queries in total (shared budget) to find the abstract (arxiv.org/abs, usenix.org, ndss-symposium.org pages). Mark basis.

Write /home/claude/w/search/SCREEN_B.tsv with header:
id	decision	exc_reason	basis	note
Return counts INC/EXC and by reason.
```


### 10.12 Independent coder B: corpus labels

모델 식별자: claude-opus-5-5

```text
You are an independent second coder for a systematic mapping study on LLM-based AI agent security. Read the codebook /home/claude/w/search/CODEBOOK.md carefully and follow it exactly. Do NOT open any other coding/result files in /home/claude/w/search (e.g., G*.tsv, R_*.tsv, corpus_all.json, defense_coding.tsv, FT_*.tsv) — your coding must be blind and independent.

Input: /home/claude/w/search/blind_corpus.json (193 records: id, title, venue, year, abstract). For each record code: decision (INC/EXC per codebook section 1 — you may disagree with inclusion), exc_reason (if EXC), type (A/D/B, multiple joined by ';'), T (T1..T6, ';'), D (D1..D6 for defenses only, else '-'), stage (I/P/M/A/C for defenses only), authority (LLM/ML/RULE/HUMAN joined by '+', defenses only), policy_by_llm (Y/N, defenses only), basis ('abstract' or 'title-only' or 'fetched-abstract').

40 records have empty abstracts (mostly security-conference papers). For those, try to obtain the abstract: you may use WebSearch (budget is shared across many workers — use at most 30 searches total) and WebFetch on arxiv.org/abs/<id> or usenix.org / ndss-symposium.org paper pages found in search results. If you cannot obtain it, code from the title and mark basis 'title-only'. Do not rely on memory of other people's classifications.

Write a TSV to /home/claude/w/search/CODER_B.tsv with header:
id	decision	exc_reason	type	T	D	stage	authority	policy_by_llm	basis	note
Return brief counts: INC/EXC, type counts, T counts, D counts.
```


### 10.13 Screen v3 expanded hits chunk 3-4

모델 식별자: claude-opus-5-5

```text
You are screener A for a systematic mapping study on LLM-based AI agent security. Read /home/claude/w/search/CODEBOOK_v3.md and apply section 1 (screening) and, for included records, section 2 (abstract-level coding) exactly. Do NOT open any other result files in /home/claude/w/search except your inputs.

Inputs: /home/claude/w/search/v3_screen_3.json and /home/claude/w/search/v3_screen_4.json (120 records each: id, title, venue, abstract). These records matched an expanded keyword query (security OR safety/policy terms) in accepted papers of ACL/EMNLP/NAACL, ICLR, ICML, NeurIPS, AAAI, IJCAI; most will be excluded (e.g., RL 'policy' papers → X; non-adversarial agent safety benchmarks without a runtime enforcement mechanism → E2). Note I2(b): runtime enforcement mechanisms for agent action policies/safety rules are INCLUDED even without an adversary. Decide from title+abstract only; no web access needed.

Output TSV /home/claude/w/search/S3A_34.tsv with header:
id	decision	exc_reason	type	actor	T	T5sub	viol	multistage	embodied	D	note
(For EXC rows put '-' in coding columns.) Return counts: INC, EXC by reason, and the list of INC titles with type/T/D.
```


### 10.14 Screen v3 expanded hits chunk 5-6

모델 식별자: claude-opus-5-5

```text
You are screener A for a systematic mapping study on LLM-based AI agent security. Read /home/claude/w/search/CODEBOOK_v3.md and apply section 1 (screening) and, for included records, section 2 (abstract-level coding) exactly. Do NOT open any other result files in /home/claude/w/search except your inputs.

Inputs: /home/claude/w/search/v3_screen_5.json and /home/claude/w/search/v3_screen_6.json (120 records each: id, title, venue, abstract). These records matched an expanded keyword query (security OR safety/policy terms) in accepted papers of ACL/EMNLP/NAACL, ICLR, ICML, NeurIPS, AAAI, IJCAI; most will be excluded (e.g., RL 'policy' papers → X; non-adversarial agent safety benchmarks without a runtime enforcement mechanism → E2). Note I2(b): runtime enforcement mechanisms for agent action policies/safety rules are INCLUDED even without an adversary. Decide from title+abstract only; no web access needed.

Output TSV /home/claude/w/search/S3A_56.tsv with header:
id	decision	exc_reason	type	actor	T	T5sub	viol	multistage	embodied	D	note
(For EXC rows put '-' in coding columns.) Return counts: INC, EXC by reason, and the list of INC titles with type/T/D.
```


### 10.15 Screen v3 expanded hits chunk 1-2

모델 식별자: claude-opus-5-5

```text
You are screener A for a systematic mapping study on LLM-based AI agent security. Read /home/claude/w/search/CODEBOOK_v3.md and apply section 1 (screening) and, for included records, section 2 (abstract-level coding) exactly. Do NOT open any other result files in /home/claude/w/search except your inputs.

Inputs: /home/claude/w/search/v3_screen_1.json and /home/claude/w/search/v3_screen_2.json (120 records each: id, title, venue, abstract). These records matched an expanded keyword query (security OR safety/policy terms) in accepted papers of ACL/EMNLP/NAACL, ICLR, ICML, NeurIPS, AAAI, IJCAI; most will be excluded (e.g., RL 'policy' papers → X; non-adversarial agent safety benchmarks without a runtime enforcement mechanism → E2). Note I2(b): runtime enforcement mechanisms for agent action policies/safety rules are INCLUDED even without an adversary. Decide from title+abstract only; no web access needed.

Output TSV /home/claude/w/search/S3A_12.tsv with header:
id	decision	exc_reason	type	actor	T	T5sub	viol	multistage	embodied	D	note
(For EXC rows put '-' in coding columns.) Return counts: INC, EXC by reason, and the list of INC titles with type/T/D.
```


### 10.16 Full-text coding defenses chunk 4

모델 식별자: claude-opus-5-5

```text
Code defense papers from their FULL TEXT for a systematic mapping study on LLM-agent security. Read /home/claude/w/search/EVAL_CODEBOOK_v2.md and follow it exactly (how to find full text, every field, output format). Do not open other result files (FT_*.tsv, defense_coding.tsv, corpus_*.json, CODER_*.tsv).
Input: /home/claude/w/search/ft_chunk4.json (15 papers: rid, title, venue, year, arxiv_id, site). Most are ACL Anthology papers: open https://aclanthology.org/<id>.pdf (derive <id> from the site URL). For others, find the arXiv version (one WebSearch per paper at most) and read arxiv.org/html/<id>. If rate-limited (429), wait (Bash sleep 60) and retry. If no full text is reachable, code from the abstract page and write 'abstract-only' in src.
Output: /home/claude/w/search/FT_4.tsv. Return a short summary (how many read in full text, adaptive level counts, public_bench counts).
```


### 10.17 Full-text coding defenses chunk 5

모델 식별자: claude-opus-5-5

```text
Code defense papers from their FULL TEXT for a systematic mapping study on LLM-agent security. Read /home/claude/w/search/EVAL_CODEBOOK_v2.md and follow it exactly (how to find full text, every field, output format). Do not open other result files (FT_*.tsv, defense_coding.tsv, corpus_*.json, CODER_*.tsv).
Input: /home/claude/w/search/ft_chunk5.json (15 papers: rid, title, venue, year, arxiv_id, site). Many are security-conference papers (USENIX Security, NDSS, CCS, S&P) and a few others: use the USENIX presentation page PDF, ndss-symposium.org PDF, or the arXiv version (one WebSearch per paper at most; read arxiv.org/html/<id>). If rate-limited (429), wait (Bash sleep 60) and retry. If no full text is reachable, code from the abstract page and write 'abstract-only' in src.
Output: /home/claude/w/search/FT_5.tsv. Return a short summary (how many read in full text, adaptive level counts, public_bench counts).
```


### 10.18 Full-text coding defenses chunk 3

모델 식별자: claude-opus-5-5

```text
Code defense papers from their FULL TEXT for a systematic mapping study on LLM-agent security. Read /home/claude/w/search/EVAL_CODEBOOK_v2.md and follow it exactly (how to find full text, every field, output format). Do not open other result files (FT_*.tsv, defense_coding.tsv, corpus_*.json, CODER_*.tsv).
Input: /home/claude/w/search/ft_chunk3.json (15 papers: rid, title, venue, year, arxiv_id, site). Many are NeurIPS/ACL papers: openreview PDFs return 403, so for non-ACL papers find the arXiv version (one WebSearch per paper at most) and read arxiv.org/html/<id> or arxiv.org/abs/<id>; for ACL Anthology papers open https://aclanthology.org/<id>.pdf. If arXiv HTML is rate-limited (429), wait (Bash sleep 60) and retry. If no full text is reachable, code from the abstract page and write 'abstract-only' in src.
Output: /home/claude/w/search/FT_3.tsv. Return a short summary (how many read in full text, adaptive level counts, public_bench counts).
```


### 10.19 Full-text coding defenses chunk 2

모델 식별자: claude-opus-5-5

```text
Code defense papers from their FULL TEXT for a systematic mapping study on LLM-agent security. Read /home/claude/w/search/EVAL_CODEBOOK_v2.md and follow it exactly (how to find full text, every field, output format). Do not open other result files (FT_*.tsv, defense_coding.tsv, corpus_*.json, CODER_*.tsv).
Input: /home/claude/w/search/ft_chunk2.json (15 papers: rid, title, venue, year, arxiv_id, site). Many are ICML/NeurIPS papers: openreview PDFs return 403, so find the arXiv version (one WebSearch per paper at most) and read arxiv.org/html/<id> or arxiv.org/abs/<id>. If arXiv HTML is rate-limited (429), wait (Bash sleep 60) and retry. If no full text is reachable, code from the abstract page and write 'abstract-only' in src.
Output: /home/claude/w/search/FT_2.tsv. Return a short summary (how many read in full text, adaptive level counts, public_bench counts).
```


### 10.20 Backward snowballing from SoK and survey

모델 식별자: claude-opus-5-5

```text
Perform one iteration of backward snowballing (Wohlin 2014 style) for a systematic mapping study on LLM-based AI agent security, from two peer-reviewed seed reviews:
 (S1) J. Kim, W. Guo, D. Song, "SoK: Attack and Defense Landscape of Agentic AI Systems", USENIX Security 2026 (find its arXiv version or the USENIX PDF; the arXiv HTML bibliography is preferable),
 (S2) Z. Deng et al., "AI Agents Under Threat: A Survey of Key Security Challenges and Future Pathways", ACM Computing Surveys 57(7), 2025 (arXiv 2406.02630; use https://arxiv.org/html/2406.02630 latest version's bibliography).
A previous attempt extracted S1 references [1]–[148] only; see /home/claude/w/search/G5_cite_snowball.log.md for what failed (you may read that log, but not other coding files). Try to get the COMPLETE reference lists (if a page is truncated, fetch the bibliography in parts, e.g., arxiv.org/html/<id>v<k> or the PDF; arXiv HTML pages can be large).

For every referenced work, record: seed (S1/S2/both), ref title, first author, year, publication status as of 2026-10-01 (venue name if peer-reviewed conference/journal/workshop with proceedings; 'arXiv' if preprint only; 'other' for blogs/standards), and a scope pre-check per /home/claude/w/search/CODEBOOK_v3.md section 1 (INC-candidate / EXC with reason) based on title (+abstract if you can cheaply see it). Verify publication venue when the reference list says arXiv but the work may since have been published (use dblp-like evidence from search results, ACL Anthology, NeurIPS/ICML/ICLR proceedings pages, usenix.org, ndss-symposium.org, ACM/IEEE pages). Use at most 25 WebSearch queries (shared budget across many workers).

Output TSV /home/claude/w/search/SNOWBALL.tsv with header:
seed	ref_no	title	first_author	year	status	venue	scope	reason	evidence
and a log /home/claude/w/search/SNOWBALL.log.md (URLs fetched, completeness of each list: number of references obtained vs total). Return: number of references per seed, how many are peer-reviewed + INC-candidate, and list those with venue.
```


### 10.21 Full-text coding defenses chunk 1

모델 식별자: claude-opus-5-5

```text
Code defense papers from their FULL TEXT for a systematic mapping study on LLM-agent security. Read /home/claude/w/search/EVAL_CODEBOOK_v2.md and follow it exactly (how to find full text, every field, output format). Do not open other result files (FT_*.tsv, defense_coding.tsv, corpus_*.json, CODER_*.tsv).
Input: /home/claude/w/search/ft_chunk1.json (15 papers: rid, title, venue, year, arxiv_id, site). Many are ICLR/ICML/NeurIPS papers: openreview PDFs return 403, so find the arXiv version (one WebSearch per paper at most) and read arxiv.org/html/<id> or arxiv.org/abs/<id>. If arXiv HTML is rate-limited (429), wait (Bash sleep 60) and retry. If no full text is reachable, code from the abstract page and write 'abstract-only' in src.
Output: /home/claude/w/search/FT_1.tsv. Return a short summary (how many read in full text, adaptive level counts, public_bench counts).
```


### 10.22 Independent screener B on expanded sample

모델 식별자: claude-opus-5-5

```text
You are an independent second screener for a systematic mapping study on LLM-based AI agent security. Read /home/claude/w/search/CODEBOOK_v3.md section 1 (screening rule) and apply it exactly. Do NOT open other result files in /home/claude/w/search (S3A_*.tsv, SCREEN_*.tsv, R_*.tsv, CODER_*.tsv, corpus_*.json etc.) — your judgment must be blind.

Input: /home/claude/w/search/blind_screen_sample2.json (150 records: id, title, venue, abstract). Decide INC or EXC (with exclusion code E1–E6 or X) from title+abstract only. Remember I2(b): runtime enforcement mechanisms for agent action policies/safety rules are included even without an adversary; non-adversarial safety evaluations without such a mechanism are E2; RL 'policy' or non-LLM work is X.

Write /home/claude/w/search/SCREEN_B2.tsv with header:
id	decision	exc_reason	note
Return counts INC/EXC and by reason.
```


### 10.23 Adjudicate screening and snowball scope

모델 식별자: claude-opus-5-5

```text
You are the adjudicator (third, independent reviewer) for screening disagreements in a systematic mapping study on LLM-based AI agent security. Read /home/claude/w/search/CODEBOOK_v3.md fully, especially section 1 and section 3 (adjudication rules R1–R4), and apply them strictly and consistently.

Inputs:
1. /home/claude/w/search/adj_screen_items.json — 10 records where screener A and screener B disagreed (title, venue, abstract, each screener's decision and note). Decide INC/EXC (with code) for each. Where the abstract is insufficient (especially R017 ObliInjection, M093 SafeSearch, M182 TRAP, Q125, Q691, the Safety Sidecar ACL Findings 2026 paper, and the ACL 2025 'Caution for the Environment' paper), consult the full text: ACL Anthology papers at https://aclanthology.org/<id>.pdf (derive from DOI 10.18653/v1/<id>), others via arXiv (one WebSearch per paper at most; read arxiv.org/abs or arxiv.org/html) or the NDSS paper PDF.
2. /home/claude/w/search/adj_snowball_items.json — 13 references found by backward snowballing from two peer-reviewed reviews; they are published in venues OUTSIDE the systematically searched set. Decide INC/EXC for each using the same criteria (read the abstract/full text via arXiv or the venue page; one WebSearch each at most). For the five '[title unresolved]' DOI entries, try to resolve the title (e.g., WebFetch https://doi.org/<doi> may redirect to IEEE Xplore which may be blocked; a single WebSearch of the DOI string is acceptable); if unresolvable, mark 'UNRESOLVED'. Also verify the venue/publication status (peer-reviewed, published by 2026-10-01) of each INC with a fetched page, and record its arXiv id and v1 date if any.
Use at most 20 WebSearch queries in total (shared budget).

Output TSV /home/claude/w/search/ADJ_SCREEN.tsv with header:
id_or_title	final_decision	exc_reason	rule_applied	evidence	venue_verified	arxiv_id	arxiv_v1
Return a short summary table.
```


### 10.24 Fetch abstracts for 36 papers

모델 식별자: claude-opus-5-5

```text
Fetch the official abstracts (verbatim text, not a summary) for 36 papers listed in /home/claude/w/search/need_abstracts.json (fields: id, title, venue, site, arxiv_id, note). Do not classify or code anything; only retrieve abstracts.
How: prefer the arXiv abs page (https://arxiv.org/abs/<arxiv_id>) when arxiv_id is given; otherwise the 'site' URL (USENIX presentation pages and NDSS paper pages show the abstract; doi.org links for ACM may be blocked). For R019/R020 (IEEE S&P 2026) and others without a usable URL, use at most one WebSearch each to find an arXiv or venue page (total WebSearch budget: 12). In WebFetch prompts, ask to "return the abstract verbatim". If rate-limited (429), wait (Bash sleep 60) and retry once. Also record the arXiv v1 submission date when you see it on an abs page.
Write /home/claude/w/search/fetched_abstracts.json as a list of {id, abstract, source_url, arxiv_v1} (abstract '' if not found). Return how many were found.
```


### 10.25 Coder A: v3 coding part a

모델 식별자: claude-opus-5-5

```text
You are coder A in a double-coding procedure for a systematic mapping study on LLM-based AI agent security. Read /home/claude/w/search/CODEBOOK_v3.md completely (sections 1, 2 and 3) and apply it exactly. Work blind: do NOT open any other coding/result files in /home/claude/w/search (CODER_*, R_*, G*, S3A_*, SCREEN_*, FT_*, ADJ_*, corpus_*, final_includes_pre.json, defense_coding.tsv). Use only the codebook and your input file; decide from title+abstract (no web access needed).

Input: /home/claude/w/search/blindv3_a.json (104 records: id, title, venue, year, abstract). These have passed screening, but re-check inclusion: if you think a record should be excluded under the codebook (including rules R1–R4), set decision EXC with the code; otherwise INC and code all section-2 variables (type, actor, T, T5sub, viol, multistage, embodied, D). Use ';' to join multiple values and '-' for not applicable.

Output TSV /home/claude/w/search/CA_a.tsv with header:
id	decision	exc_reason	type	actor	T	T5sub	viol	multistage	embodied	D	note
Return brief counts.
```


### 10.26 Coder B: v3 coding part a

모델 식별자: claude-opus-5-5

```text
You are coder B in a double-coding procedure for a systematic mapping study on LLM-based AI agent security. Another coder codes the same records independently; you must not see their work. Read /home/claude/w/search/CODEBOOK_v3.md completely (sections 1, 2 and 3) and apply it exactly. Work blind: do NOT open any other coding/result files in /home/claude/w/search (CA_*, CODER_*, R_*, G*, S3A_*, SCREEN_*, FT_*, ADJ_*, corpus_*, final_includes_pre.json, defense_coding.tsv). Use only the codebook and your input file; decide from title+abstract (no web access needed).

Input: /home/claude/w/search/blindv3_a.json (104 records: id, title, venue, year, abstract). These have passed screening, but re-check inclusion: if you think a record should be excluded under the codebook (including rules R1–R4), set decision EXC with the code; otherwise INC and code all section-2 variables (type, actor, T, T5sub, viol, multistage, embodied, D). Use ';' to join multiple values and '-' for not applicable.

Output TSV /home/claude/w/search/CB_a.tsv with header:
id	decision	exc_reason	type	actor	T	T5sub	viol	multistage	embodied	D	note
Return brief counts.
```


### 10.27 Coder A: v3 coding part b

모델 식별자: claude-opus-5-5

```text
You are coder A in a double-coding procedure for a systematic mapping study on LLM-based AI agent security. Read /home/claude/w/search/CODEBOOK_v3.md completely (sections 1, 2 and 3) and apply it exactly. Work blind: do NOT open any other coding/result files in /home/claude/w/search (CODER_*, R_*, G*, S3A_*, SCREEN_*, FT_*, ADJ_*, corpus_*, final_includes_pre.json, defense_coding.tsv). Use only the codebook and your input file; decide from title+abstract (no web access needed).

Input: /home/claude/w/search/blindv3_b.json (103 records: id, title, venue, year, abstract). These have passed screening, but re-check inclusion: if you think a record should be excluded under the codebook (including rules R1–R4), set decision EXC with the code; otherwise INC and code all section-2 variables (type, actor, T, T5sub, viol, multistage, embodied, D). Use ';' to join multiple values and '-' for not applicable.

Output TSV /home/claude/w/search/CA_b.tsv with header:
id	decision	exc_reason	type	actor	T	T5sub	viol	multistage	embodied	D	note
Return brief counts.
```


### 10.28 Coder B: v3 coding part b

모델 식별자: claude-opus-5-5

```text
You are coder B in a double-coding procedure for a systematic mapping study on LLM-based AI agent security. Another coder codes the same records independently; you must not see their work. Read /home/claude/w/search/CODEBOOK_v3.md completely (sections 1, 2 and 3) and apply it exactly. Work blind: do NOT open any other coding/result files in /home/claude/w/search (CA_*, CODER_*, R_*, G*, S3A_*, SCREEN_*, FT_*, ADJ_*, corpus_*, final_includes_pre.json, defense_coding.tsv). Use only the codebook and your input file; decide from title+abstract (no web access needed).

Input: /home/claude/w/search/blindv3_b.json (103 records: id, title, venue, year, abstract). These have passed screening, but re-check inclusion: if you think a record should be excluded under the codebook (including rules R1–R4), set decision EXC with the code; otherwise INC and code all section-2 variables (type, actor, T, T5sub, viol, multistage, embodied, D). Use ';' to join multiple values and '-' for not applicable.

Output TSV /home/claude/w/search/CB_b.tsv with header:
id	decision	exc_reason	type	actor	T	T5sub	viol	multistage	embodied	D	note
Return brief counts.
```


### 10.29 Adjudicate coding disagreements part 1

모델 식별자: claude-opus-5-5

```text
You are the adjudicator (third reviewer) for coding disagreements in a systematic mapping study on LLM-based AI agent security. Read /home/claude/w/search/CODEBOOK_v3.md completely (sections 1–3, including rules R1–R5) and apply it strictly.

Input: /home/claude/w/search/adj_code_items_1.json — 42 records. Each has title, venue, abstract, 'diff' (the variables on which coder A and coder B disagreed), and both coders' full codings and notes. For each record, produce the FINAL coding for ALL variables (decision, exc_reason, type, actor, T, T5sub, viol, multistage, embodied, D): for agreed variables keep the agreed value unless it clearly violates the codebook; for disputed variables decide by the codebook. If the abstract is insufficient for a disputed decision/type/T/D, consult the full text (ACL Anthology PDF https://aclanthology.org/<id>.pdf for 10.18653 DOIs; arXiv abs/html otherwise; at most 10 WebSearch queries in total). Be consistent across records (e.g., T5 is coded only when the paper's focus is unsafe/unauthorized/availability-harming actions; plain goal hijacking by injection is T1 with viol AI; multistage Y only for propagation via memory, plan contamination, cross-session or multi-hop between agents).

Output TSV /home/claude/w/search/ADJ_CODE_1.tsv with header:
id	decision	exc_reason	type	actor	T	T5sub	viol	multistage	embodied	D	basis	rationale
(basis: abstract / fulltext). Return a short summary of decisions changed vs. either coder.
```


### 10.30 Adjudicate coding disagreements part 2

모델 식별자: claude-opus-5-5

```text
You are the adjudicator (third reviewer) for coding disagreements in a systematic mapping study on LLM-based AI agent security. Read /home/claude/w/search/CODEBOOK_v3.md completely (sections 1–3, including rules R1–R5) and apply it strictly.

Inputs:
(1) /home/claude/w/search/adj_code_items_2.json — 41 records. Each has title, venue, abstract, 'diff' (variables on which coder A and coder B disagreed, or 'decision(both EXC)' meaning both coders excluded a record that had passed screening — for those, decide inclusion from the FULL TEXT), and both coders' codings and notes. Produce the FINAL coding for ALL variables (decision, exc_reason, type, actor, T, T5sub, viol, multistage, embodied, D).
(2) /home/claude/w/search/adj_r1_check.json — 17 included records that both coders agreed have no adversary (actor NON). Check each against rule R1 (I2(b) requires an explicit runtime mechanism that checks/constrains/escalates individual actions; training- or prompting-only safety without an adversary is E2) and R4. Output a final decision for each (keep INC or change to EXC with reason); keep their other codes unchanged unless clearly wrong.
If the abstract is insufficient, consult the full text (ACL Anthology PDF https://aclanthology.org/<id>.pdf for 10.18653 DOIs; arXiv abs/html otherwise; at most 12 WebSearch queries in total). Be consistent: T5 only when the paper's focus is unsafe/unauthorized/availability-harming actions; plain injection hijacking is T1 with viol AI; multistage Y only for propagation via memory, plan contamination, cross-session or multi-hop between agents.

Output TSV /home/claude/w/search/ADJ_CODE_2.tsv (for both inputs; for (2) fill all columns with the final values) with header:
id	decision	exc_reason	type	actor	T	T5sub	viol	multistage	embodied	D	basis	rationale
Return a short summary of inclusion changes.
```


### 10.31 Full-text coding defenses chunk 6b

모델 식별자: claude-opus-5-5

```text
Code defense papers from their FULL TEXT for a systematic mapping study on LLM-agent security. Read /home/claude/w/search/EVAL_CODEBOOK_v2.md and follow it exactly. Do not open other result files (FT_*.tsv, defense_coding.tsv, corpus_*.json, CA_*/CB_*, ADJ_*).
Input: /home/claude/w/search/ft_chunk6b.json (7 papers: ICML 2026 papers and two with arXiv ids). For ICML papers, openreview PDFs return 403, so find the arXiv version (one WebSearch per paper at most) and read arxiv.org/html/<id>. If rate-limited (429), wait (Bash sleep 60) and retry once. If no full text is reachable, code from the abstract page and write 'abstract-only' in src.
Output: /home/claude/w/search/FT_6b.tsv. Return a short summary.
```


### 10.32 Second full-text coder subset b

모델 식별자: claude-opus-5-5

```text
You are the SECOND, independent full-text coder for a reliability check in a systematic mapping study on LLM-agent security. Read /home/claude/w/search/EVAL_CODEBOOK_v2.md and follow it exactly. You must NOT open any other coder's result files (FT_*.tsv, defense_coding.tsv, corpus_*.json, CA_*/CB_*, ADJ_*, final_codes.json).
Input: /home/claude/w/search/ft2_b.json (13 papers: rid, title, venue, year, arxiv_id, site, fulltext_url_hint). 'fulltext_url_hint' is only a URL where the full text was previously found (no codes are given); use it to avoid searching. If empty, find the full text as the codebook says (one WebSearch per paper at most). If rate-limited (429), wait (Bash sleep 60) and retry once.
Output: /home/claude/w/search/FT2_b.tsv (same header as the codebook). Return a short summary.
```


### 10.33 Full-text coding defenses chunk 6a

모델 식별자: claude-opus-5-5

```text
Code defense papers from their FULL TEXT for a systematic mapping study on LLM-agent security. Read /home/claude/w/search/EVAL_CODEBOOK_v2.md and follow it exactly. Do not open other result files (FT_*.tsv, defense_coding.tsv, corpus_*.json, CA_*/CB_*, ADJ_*).
Input: /home/claude/w/search/ft_chunk6a.json (8 papers). Hints: Q049 is ACL Anthology 2025.findings-acl.784, Q086 is 2025.emnlp-main.714, Q125 is 2026.acl-long.725 (open https://aclanthology.org/<id>.pdf); N009 'Visual Inception' is ACL 2026 (find its Anthology id or arXiv with one WebSearch). ICLR/ICML papers: openreview PDFs return 403, so find the arXiv version (one WebSearch per paper at most) and read arxiv.org/html/<id>. If rate-limited (429), wait (Bash sleep 60) and retry once.
Output: /home/claude/w/search/FT_6a.tsv. Return a short summary.
```


### 10.34 Second full-text coder subset a

모델 식별자: claude-opus-5-5

```text
You are the SECOND, independent full-text coder for a reliability check in a systematic mapping study on LLM-agent security. Read /home/claude/w/search/EVAL_CODEBOOK_v2.md and follow it exactly. You must NOT open any other coder's result files (FT_*.tsv, defense_coding.tsv, corpus_*.json, CA_*/CB_*, ADJ_*, final_codes.json).
Input: /home/claude/w/search/ft2_a.json (13 papers: rid, title, venue, year, arxiv_id, site, fulltext_url_hint). 'fulltext_url_hint' is only a URL where the full text was previously found (no codes are given); use it to avoid searching. If empty, find the full text as the codebook says (one WebSearch per paper at most). If rate-limited (429), wait (Bash sleep 60) and retry once.
Output: /home/claude/w/search/FT2_a.tsv (same header as the codebook). Return a short summary.
```


### 10.35 Blind screening pass B batch 1

모델 식별자: claude-opus-5-5

```text
You are an independent screener in a systematic mapping study on LLM-based AI agent security. Work BLIND: read ONLY these two files: /home/claude/w/search/pb/CODEBOOK_SCREEN.md (the screening codebook, in Korean) and /home/claude/w/search/pb/pb1.json (190 candidate papers: id, venue, title, abstract). Do NOT open, list, or grep any other file or directory under /home/claude/w (other screeners' results must not influence you).

For EVERY item decide INC or EXC strictly by the codebook (inclusion I1 and I2(a)/(b); exclusion codes E1–E6, X; and the detailed rules R1–R5 in section 3). Judge from the title and abstract. Do not guess beyond the text; when the case is borderline, still decide, and mark borderline=Y with a one-line reason.

Write the result to /home/claude/w/search/pb/pb1_B.tsv (tab-separated, header line exactly: id	decision	exc_reason	borderline	note). exc_reason is '-' for INC; borderline is Y or N; note ≤ 20 words in English. One row per input item, same order, all 190 rows. Process the items in chunks (e.g., 30 at a time) so you don't lose track, and verify at the end with a short Python check that the TSV has 190 data rows with unique ids matching the input. Do not use WebSearch. Final message: counts of INC/EXC by reason and number of borderline items.
```


### 10.36 Blind screening pass B batch 3

모델 식별자: claude-opus-5-5

```text
You are an independent screener in a systematic mapping study on LLM-based AI agent security. Work BLIND: read ONLY these two files: /home/claude/w/search/pb/CODEBOOK_SCREEN.md (the screening codebook, in Korean) and /home/claude/w/search/pb/pb3.json (190 candidate papers: id, venue, title, abstract). Do NOT open, list, or grep any other file or directory under /home/claude/w (other screeners' results must not influence you).

For EVERY item decide INC or EXC strictly by the codebook (inclusion I1 and I2(a)/(b); exclusion codes E1–E6, X; and the detailed rules R1–R5 in section 3). Judge from the title and abstract. Do not guess beyond the text; when the case is borderline, still decide, and mark borderline=Y with a one-line reason.

Write the result to /home/claude/w/search/pb/pb3_B.tsv (tab-separated, header line exactly: id	decision	exc_reason	borderline	note). exc_reason is '-' for INC; borderline is Y or N; note ≤ 20 words in English. One row per input item, same order, all 190 rows. Process the items in chunks (e.g., 30 at a time) so you don't lose track, and verify at the end with a short Python check that the TSV has 190 data rows with unique ids matching the input. Do not use WebSearch. Final message: counts of INC/EXC by reason and number of borderline items.
```


### 10.37 Blind screening pass B batch 2

모델 식별자: claude-opus-5-5

```text
You are an independent screener in a systematic mapping study on LLM-based AI agent security. Work BLIND: read ONLY these two files: /home/claude/w/search/pb/CODEBOOK_SCREEN.md (the screening codebook, in Korean) and /home/claude/w/search/pb/pb2.json (190 candidate papers: id, venue, title, abstract). Do NOT open, list, or grep any other file or directory under /home/claude/w (other screeners' results must not influence you).

For EVERY item decide INC or EXC strictly by the codebook (inclusion I1 and I2(a)/(b); exclusion codes E1–E6, X; and the detailed rules R1–R5 in section 3). Judge from the title and abstract. Do not guess beyond the text; when the case is borderline, still decide, and mark borderline=Y with a one-line reason.

Write the result to /home/claude/w/search/pb/pb2_B.tsv (tab-separated, header line exactly: id	decision	exc_reason	borderline	note). exc_reason is '-' for INC; borderline is Y or N; note ≤ 20 words in English. One row per input item, same order, all 190 rows. Process the items in chunks (e.g., 30 at a time) so you don't lose track, and verify at the end with a short Python check that the TSV has 190 data rows with unique ids matching the input. Do not use WebSearch. Final message: counts of INC/EXC by reason and number of borderline items.
```


### 10.38 Blind screening pass B batch 4

모델 식별자: claude-opus-5-5

```text
You are an independent screener in a systematic mapping study on LLM-based AI agent security. Work BLIND: read ONLY these two files: /home/claude/w/search/pb/CODEBOOK_SCREEN.md (the screening codebook, in Korean) and /home/claude/w/search/pb/pb4.json (177 candidate papers: id, venue, title, abstract). Do NOT open, list, or grep any other file or directory under /home/claude/w (other screeners' results must not influence you).

For EVERY item decide INC or EXC strictly by the codebook (inclusion I1 and I2(a)/(b); exclusion codes E1–E6, X; and the detailed rules R1–R5 in section 3). Judge from the title and abstract. Do not guess beyond the text; when the case is borderline, still decide, and mark borderline=Y with a one-line reason.

Write the result to /home/claude/w/search/pb/pb4_B.tsv (tab-separated, header line exactly: id	decision	exc_reason	borderline	note). exc_reason is '-' for INC; borderline is Y or N; note ≤ 20 words in English. One row per input item, same order, all 177 rows. Process the items in chunks (e.g., 30 at a time) so you don't lose track, and verify at the end with a short Python check that the TSV has 177 data rows with unique ids matching the input. Do not use WebSearch. Final message: counts of INC/EXC by reason and number of borderline items.
```


### 10.39 Blind screening pass B batch 5

모델 식별자: claude-opus-5-5

```text
You are an independent screener in a systematic mapping study on LLM-based AI agent security. Work BLIND: read ONLY these two files: /home/claude/w/search/pb/CODEBOOK_SCREEN.md (the screening codebook, in Korean) and /home/claude/w/search/pb/pb5.json (176 candidate papers: id, venue, title, abstract). Do NOT open, list, or grep any other file or directory under /home/claude/w (other screeners' results must not influence you).

For EVERY item decide INC or EXC strictly by the codebook (inclusion I1 and I2(a)/(b); exclusion codes E1–E6, X; and the detailed rules R1–R5 in section 3). Judge from the title and abstract. Do not guess beyond the text; when the case is borderline, still decide, and mark borderline=Y with a one-line reason.

Write the result to /home/claude/w/search/pb/pb5_B.tsv (tab-separated, header line exactly: id	decision	exc_reason	borderline	note). exc_reason is '-' for INC; borderline is Y or N; note ≤ 20 words in English. One row per input item, same order, all 176 rows. Process the items in chunks (e.g., 30 at a time) so you don't lose track, and verify at the end with a short Python check that the TSV has 176 data rows with unique ids matching the input. Do not use WebSearch. Final message: counts of INC/EXC by reason and number of borderline items.
```


### 10.40 Blind screening pass B batch 6

모델 식별자: claude-opus-5-5

```text
You are an independent screener in a systematic mapping study on LLM-based AI agent security. Work BLIND: read ONLY these two files: /home/claude/w/search/pb/CODEBOOK_SCREEN.md (the screening codebook, in Korean) and /home/claude/w/search/pb/pb6.json (79 candidate papers: id, venue, title, abstract, site, arxiv_id). Do NOT open, list, or grep any other file or directory under /home/claude/w (other screeners' results must not influence you).

Many items in this batch have an empty abstract. For those, obtain the abstract with WebFetch (at most 2 fetches per item): if arxiv_id is a real id, fetch https://arxiv.org/abs/<arxiv_id>; otherwise fetch the 'site' URL (USENIX/NDSS/ACM/IEEE pages) and extract the abstract. Do not use WebSearch (budget exhausted). If no abstract can be obtained, judge from the title and write 'title-only' in the note. Never put any email address in any request.

For EVERY item decide INC or EXC strictly by the codebook (inclusion I1 and I2(a)/(b); exclusion codes E1–E6, X; and the detailed rules R1–R5 in section 3). Judge from the title and abstract. When the case is borderline, still decide, and mark borderline=Y with a one-line reason.

Write the result to /home/claude/w/search/pb/pb6_B.tsv (tab-separated, header line exactly: id	decision	exc_reason	borderline	note). exc_reason is '-' for INC; borderline is Y or N; note ≤ 20 words in English (include 'abs:arxiv' / 'abs:site' / 'title-only' to show the source). One row per input item, same order, all 79 rows. Verify at the end with a short Python check that the TSV has 79 data rows with unique ids matching the input. Final message: counts of INC/EXC by reason, borderline count, and how many were title-only.
```


### 10.41 Adjudicate screening disagreements A

모델 식별자: claude-opus-5-5

```text
You are the adjudicator in a systematic mapping study on LLM-based AI agent security. Two independent screeners disagreed on the papers in /home/claude/w/search/pb/adj_a.json (fields: id, venue, title, abstract, A/A_reason = screener A, B/B_reason/B_note = screener B). Decide each case using the FULL TEXT of the paper and the codebook /home/claude/w/search/pb/CODEBOOK_SCREEN.md (inclusion I1, I2(a)/(b); exclusions E1–E6, X; detailed rules R1–R5). For consistency, read the earlier adjudication decisions in /home/claude/w/search/pb/ADJ_PRECEDENTS.tsv and follow the same interpretation of the rules (e.g., R1 runtime mechanism requirement, R2 multi-agent with malicious agents, R3 tool-using agents with output harm, R4 reliability-first contributions, R5 agent-as-adversary actor rule). Note that R5 is an actor-coding rule; inclusion still requires I1 (the system performs real actions via tools/web/code/memory/other agents/robots) and I2.

Finding full text: openreview.net PDFs return 403 — use arXiv instead (WebFetch https://arxiv.org/abs/<id> to find versions, then https://arxiv.org/html/<id> or the PDF). If you do not know the arXiv id, WebFetch https://arxiv.org/a/... is not possible; instead try WebFetch on "https://arxiv.org/abs/" search is not available — so use https://www.semanticscholar.org or https://scholar.archive.org only if reachable; otherwise use the venue page (icml.cc/virtual, iclr.cc/virtual, neurips.cc, aclanthology.org) for the abstract and say 'abstract-only'. Do not use WebSearch (budget exhausted). Never include any email address in any request.

Key questions per paper: Does the evaluated system actually execute actions (tool calls, code execution, web/GUI actions, memory writes, messages that determine other agents' actions, robot control) in the experiments, or is it text-only/QA (E1)? Is there an adversary or adversarially-behaving agent central to the contribution (I2(a)), or a runtime enforcement mechanism over agent actions (I2(b), R1), versus a non-adversarial capability/risk-tendency evaluation without a runtime mechanism (E2) or reliability-first (R4)? Is the LLM agent the attacker's tool used for a security task (E4)?

Write /home/claude/w/search/pb/ADJ_SCREEN2_a.tsv with header exactly: id	final_decision	exc_reason	rule_applied	evidence	src
(evidence = a short quote or precise description from the full text, ≤ 40 words; src = URL and version actually read, or 'abstract-only'). One row per item (9 rows). Final message: the table of decisions with one-line reasons.
```


### 10.42 Adjudicate screening disagreements B

모델 식별자: claude-opus-5-5

```text
You are the adjudicator in a systematic mapping study on LLM-based AI agent security. Two independent screeners disagreed on the papers in /home/claude/w/search/pb/adj_b.json (fields: id, venue, title, abstract, A/A_reason = screener A, B/B_reason/B_note = screener B). Decide each case using the FULL TEXT of the paper and the codebook /home/claude/w/search/pb/CODEBOOK_SCREEN.md (inclusion I1, I2(a)/(b); exclusions E1–E6, X; detailed rules R1–R5). For consistency, read the earlier adjudication decisions in /home/claude/w/search/pb/ADJ_PRECEDENTS.tsv and follow the same interpretation of the rules (e.g., R1 runtime mechanism requirement, R2 multi-agent with malicious agents, R3 tool-using agents with output harm, R4 reliability-first contributions, R5 agent-as-adversary actor rule). Note that R5 is an actor-coding rule; inclusion still requires I1 (the system performs real actions via tools/web/code/memory/other agents/robots) and I2.

Finding full text: ACL Anthology papers: WebFetch https://aclanthology.org/<anthology-id>.pdf (the id is in the DOI after 'v1/', e.g., 10.18653/v1/2026.acl-long.1134 → 2026.acl-long.1134). Security-venue papers (ids R…): use arXiv (WebFetch https://arxiv.org/abs/<id> then /html/<id>) if you can identify the id from the venue page, or the USENIX/IEEE/NDSS paper page; ACM DL may be blocked. For Q-ids from ACL Findings, use the ACL Anthology PDF (find the anthology id from https://aclanthology.org/ venue listing only if needed; otherwise arXiv). Do not use WebSearch (budget exhausted). Never include any email address in any request.

Key questions per paper: Does the evaluated system actually execute actions (tool calls, code execution, web/GUI actions, memory writes, messages that determine other agents' actions, robot control) in the experiments, or is it text-only/QA (E1)? Is there an adversary or adversarially-behaving agent central to the contribution (I2(a)), or a runtime enforcement mechanism over agent actions (I2(b), R1), versus a non-adversarial capability/risk-tendency evaluation without a runtime mechanism (E2) or reliability-first (R4)? Is the LLM agent the attacker's tool used for a security task (E4)? Does R3 apply (tool-using agent whose harm appears in output)?

Write /home/claude/w/search/pb/ADJ_SCREEN2_b.tsv with header exactly: id	final_decision	exc_reason	rule_applied	evidence	src
(evidence = a short quote or precise description from the full text, ≤ 40 words; src = URL and version actually read, or 'abstract-only'). One row per item (9 rows). Final message: the table of decisions with one-line reasons.
```


### 10.43 Abstract coding new papers coder A

모델 식별자: claude-opus-5-5

```text
You are an independent coder in a systematic mapping study on LLM-based AI agent security. Work BLIND: read ONLY /home/claude/w/search/pb/CODEBOOK_CODE.md (codebook, Korean) and /home/claude/w/search/pb/new_inc5.json (5 included papers: id, title, venue, abstract, arxiv_id). Do not open any other file under /home/claude/w.

For papers whose abstract is empty, fetch the abstract with WebFetch from https://arxiv.org/abs/<arxiv_id> (abstract page only; do not read the full text). Code each paper from its title and abstract only, following section 2 of the codebook: type (A/D/B, multiple), actor (EXT/SUP/AGT/USR/NON, multiple), T (T1–T6, multiple), T5sub (a/b/c if T5, else '-'), viol (AI/OI/C/AV/S, multiple), multistage (Y/N), embodied (Y/N), D (D1–D6 if type includes D, else '-'), and also decision (INC, or EXC with code if you think it should not have been included). Use ';' to separate multiple values. Follow rules R1–R6 in section 3. Do not use WebSearch. Never put an email address in any request.

Write /home/claude/w/search/pb/CA_new.tsv with header exactly:
id	decision	exc_reason	type	actor	T	T5sub	viol	multistage	embodied	D	note
(5 rows). Final message: the table.
```


### 10.44 Abstract coding new papers coder B

모델 식별자: claude-opus-5-5

```text
You are an independent coder in a systematic mapping study on LLM-based AI agent security. Work BLIND: read ONLY /home/claude/w/search/pb/CODEBOOK_CODE.md (codebook, Korean) and /home/claude/w/search/pb/new_inc5.json (5 included papers: id, title, venue, abstract, arxiv_id). Do not open any other file under /home/claude/w, including any CA_*.tsv files.

For papers whose abstract is empty, fetch the abstract with WebFetch from https://arxiv.org/abs/<arxiv_id> (abstract page only; do not read the full text). Code each paper from its title and abstract only, following section 2 of the codebook: type (A/D/B, multiple), actor (EXT/SUP/AGT/USR/NON, multiple), T (T1–T6, multiple), T5sub (a/b/c if T5, else '-'), viol (AI/OI/C/AV/S, multiple), multistage (Y/N), embodied (Y/N), D (D1–D6 if type includes D, else '-'), and also decision (INC, or EXC with code if you think it should not have been included). Use ';' to separate multiple values. Follow rules R1–R6 in section 3. Do not use WebSearch. Never put an email address in any request.

Write /home/claude/w/search/pb/CB_new.tsv with header exactly:
id	decision	exc_reason	type	actor	T	T5sub	viol	multistage	embodied	D	note
(5 rows). Final message: the table.
```


### 10.45 Full-text coding new defenses

모델 식별자: claude-opus-5-5

```text
You are a full-text coder in a systematic mapping study on LLM-based AI agent security. Read ONLY /home/claude/w/search/EVAL_CODEBOOK_v2.md (full-text defense codebook, Korean) and /home/claude/w/search/pb/new_inc5.json (5 papers with arxiv_id). Do not open other files under /home/claude/w.

For each paper, read the full text: WebFetch https://arxiv.org/abs/<arxiv_id> (record the version history: v1 submission date and latest version), then https://arxiv.org/html/<arxiv_id> (or the PDF if HTML is unavailable). If arXiv returns 429, wait and retry once, then try the PDF URL https://arxiv.org/pdf/<arxiv_id>. Do not use WebSearch. Never put an email address in any request.

First decide whether the paper proposes a defense (detection, blocking, isolation, enforcement, oversight mechanism) as a main contribution (not merely testing existing mitigations). For papers that do, code every item of the full-text codebook (src, arxiv_id, arxiv_v1, stage, A_mode, judge, policy_src, judge_exposed, granularity, decisions, adversarial, adaptive with a quoted evidence sentence, bench, public_bench, n_models, utility, overhead, fpr, hitl_burden, evidence). For papers that do not propose a defense, still fill rid, title, src, arxiv_id, arxiv_v1 and put 'NOT_DEFENSE' in the evidence column with '-' elsewhere.

Write /home/claude/w/search/pb/FT_new.tsv, tab-separated, with the exact header from the codebook's 출력 section:
rid	title	src	arxiv_id	arxiv_v1	stage	A_mode	judge	policy_src	judge_exposed	granularity	decisions	adversarial	adaptive	bench	public_bench	n_models	utility	overhead	fpr	hitl_burden	evidence
(5 rows; rid = the id field). Final message: a short summary per paper.
```


### 10.46 Adjudicate M054 coding disagreement

모델 식별자: claude-opus-5-5

```text
You are the adjudicator for one coding disagreement in a systematic mapping study. Codebook: /home/claude/w/search/pb/CODEBOOK_CODE.md (Korean; see 'viol' definitions: AI 행동 무결성, OI 출력 무결성 = 사용자에게 전달되는 응답·판단의 조작, C, AV, S). Paper: M054 "Spilling the Beans: Teaching LLMs to Self-Report Their Hidden Objectives" (ICLR 2026, arXiv 2511.06626). Coder A coded viol = AI; coder B coded viol = AI;OI (reason: the agent lies when interrogated about its hidden objective). Read the paper's full text (WebFetch https://arxiv.org/html/2511.06626 or the PDF https://arxiv.org/pdf/2511.06626) and decide the final viol value (also confirm or correct T5sub, currently 'b' from both coders, by checking what the hidden side tasks are in the evaluation). Do not use WebSearch. Never include an email address in any request. Write one line to /home/claude/w/search/pb/ADJ_CODE_new.tsv with header: id	field	final	evidence	src  (one row per field you decide: viol and T5sub). Final message: your decisions with one-sentence evidence each.
```


### 10.47 Audit 150 double-excluded candidates

모델 식별자: claude-opus-5-5

```text
You are a third, independent screener auditing exclusions in a systematic mapping study on LLM-based AI agent security. Work BLIND: read ONLY /home/claude/w/search/pb/CODEBOOK_SCREEN.md (screening codebook in Korean; note section 3 rules R1–R5) and /home/claude/w/search/pb/audit150.json (150 candidates: id, venue, title, abstract, sometimes site/arxiv_id). Do not open, list, or grep any other file under /home/claude/w. Also apply this rule R6: an agent-as-adversary study counts as I2(a) only when the agent is given an adversarial objective or is red-teamed / induced to evade oversight; studies that only measure spontaneous risky behavior or deception propensity of benign agents without a runtime enforcement mechanism are E2.

For each item decide INC or EXC (with code E1–E6 or X) strictly by the codebook, from title and abstract. For the few items with an empty abstract, you may WebFetch the arXiv abs page (https://arxiv.org/abs/<arxiv_id>) or the given site once; otherwise judge from the title and note 'title-only'. Do not use WebSearch. Never include an email address in any request. Mark borderline=Y when the case is borderline.

Write /home/claude/w/search/pb/audit150_C.tsv with header exactly: id	decision	exc_reason	borderline	note  (150 rows, same order; note ≤ 20 words). Verify with a short Python check (150 unique ids matching input). Final message: number of INC decisions with their ids and one-line reasons, and the number of borderline items.
```


### 10.48 Exposure recoding coder B part 1

모델 식별자: claude-opus-5-5

```text
You are an independent full-text coder (coder B) in a systematic mapping study on LLM-agent security. Read ONLY /home/claude/w/search/pb/EXPOSURE_CODEBOOK.md (Korean codebook) and /home/claude/w/search/pb/expo_1.json (30 defense papers: id, title, venue, arxiv_id, fulltext_url, has_separate_llm_judge, has_llm_generated_rules). Do not open any other file under /home/claude/w (blind coding; never open files whose names end in _A.tsv).

For each paper read the full text: use fulltext_url if given (aclanthology.org PDFs, usenix.org, ndss-symposium.org, arxiv.org/html or pdf); otherwise https://arxiv.org/html/<arxiv_id> or https://arxiv.org/pdf/<arxiv_id>. If arXiv rate-limits (429), wait briefly and try the other arXiv URL form once. Do not use WebSearch. Never include an email address in any request. Focus on the method section describing what the judge/guard LLM receives as input at decision time, and what the policy-generating LLM receives.

Code judge_input (RAW/DERIVED/TRUSTED/'-'/?), policy_input (RAW/DERIVED/TRUSTED/'-'/?), policy_time (RUNTIME/OFFLINE/'-'/?), evidence (short quote + section). Write /home/claude/w/search/pb/expo_1_B.tsv with header exactly: id	judge_input	policy_input	policy_time	src	evidence  (30 rows; src = URL+version actually read, or 'abstract-only'). Verify with a short Python check. Final message: counts per value and the ids you could not read.
```


### 10.49 Exposure recoding coder A part 2

모델 식별자: claude-opus-5-5

```text
You are an independent full-text coder (coder A) in a systematic mapping study on LLM-agent security. Read ONLY /home/claude/w/search/pb/EXPOSURE_CODEBOOK.md (Korean codebook) and /home/claude/w/search/pb/expo_2.json (30 defense papers: id, title, venue, arxiv_id, fulltext_url, has_separate_llm_judge, has_llm_generated_rules). Do not open any other file under /home/claude/w (blind coding).

For each paper read the full text: use fulltext_url if given (aclanthology.org PDFs, usenix.org, ndss-symposium.org, arxiv.org/html or pdf); otherwise https://arxiv.org/html/<arxiv_id> or https://arxiv.org/pdf/<arxiv_id>. If arXiv rate-limits (429), wait briefly and try the other arXiv URL form once. Do not use WebSearch. Never include an email address in any request. Focus on the method section describing what the judge/guard LLM receives as input at decision time, and what the policy-generating LLM receives.

Code judge_input (RAW/DERIVED/TRUSTED/'-'/?), policy_input (RAW/DERIVED/TRUSTED/'-'/?), policy_time (RUNTIME/OFFLINE/'-'/?), evidence (short quote + section). Write /home/claude/w/search/pb/expo_2_A.tsv with header exactly: id	judge_input	policy_input	policy_time	src	evidence  (30 rows; src = URL+version actually read, or 'abstract-only'). Verify with a short Python check. Final message: counts per value and the ids you could not read.
```


### 10.50 Exposure recoding coder A part 1

모델 식별자: claude-opus-5-5

```text
You are an independent full-text coder (coder A) in a systematic mapping study on LLM-agent security. Read ONLY /home/claude/w/search/pb/EXPOSURE_CODEBOOK.md (Korean codebook) and /home/claude/w/search/pb/expo_1.json (30 defense papers: id, title, venue, arxiv_id, fulltext_url, has_separate_llm_judge, has_llm_generated_rules). Do not open any other file under /home/claude/w (blind coding).

For each paper read the full text: use fulltext_url if given (aclanthology.org PDFs, usenix.org, ndss-symposium.org, arxiv.org/html or pdf); otherwise https://arxiv.org/html/<arxiv_id> or https://arxiv.org/pdf/<arxiv_id>. If arXiv rate-limits (429), wait briefly and try the other arXiv URL form once. Do not use WebSearch. Never include an email address in any request. Focus on the method section describing what the judge/guard LLM receives as input at decision time, and what the policy-generating LLM receives.

Code judge_input (RAW/DERIVED/TRUSTED/'-'/?), policy_input (RAW/DERIVED/TRUSTED/'-'/?), policy_time (RUNTIME/OFFLINE/'-'/?), evidence (short quote + section). Write /home/claude/w/search/pb/expo_1_A.tsv with header exactly: id	judge_input	policy_input	policy_time	src	evidence  (30 rows; src = URL+version actually read, or 'abstract-only'). Verify with a short Python check. Final message: counts per value and the ids you could not read.
```


### 10.51 Exposure recoding coder B part 2

모델 식별자: claude-opus-5-5

```text
You are an independent full-text coder (coder B) in a systematic mapping study on LLM-agent security. Read ONLY /home/claude/w/search/pb/EXPOSURE_CODEBOOK.md (Korean codebook) and /home/claude/w/search/pb/expo_2.json (30 defense papers: id, title, venue, arxiv_id, fulltext_url, has_separate_llm_judge, has_llm_generated_rules). Do not open any other file under /home/claude/w (blind coding; never open files whose names end in _A.tsv).

For each paper read the full text: use fulltext_url if given (aclanthology.org PDFs, usenix.org, ndss-symposium.org, arxiv.org/html or pdf); otherwise https://arxiv.org/html/<arxiv_id> or https://arxiv.org/pdf/<arxiv_id>. If arXiv rate-limits (429), wait briefly and try the other arXiv URL form once. Do not use WebSearch. Never include an email address in any request. Focus on the method section describing what the judge/guard LLM receives as input at decision time, and what the policy-generating LLM receives.

Code judge_input (RAW/DERIVED/TRUSTED/'-'/?), policy_input (RAW/DERIVED/TRUSTED/'-'/?), policy_time (RUNTIME/OFFLINE/'-'/?), evidence (short quote + section). Write /home/claude/w/search/pb/expo_2_B.tsv with header exactly: id	judge_input	policy_input	policy_time	src	evidence  (30 rows; src = URL+version actually read, or 'abstract-only'). Verify with a short Python check. Final message: counts per value and the ids you could not read.
```


### 10.52 Adjudicate exposure-level disagreements

모델 식별자: claude-opus-5-5

```text
You are the adjudicator for 5 coding disagreements in a systematic mapping study on LLM-agent security. Codebook: /home/claude/w/search/pb/EXPOSURE_CODEBOOK.md (Korean). Disagreements: /home/claude/w/search/pb/expo_dis.json (id, title, arxiv_id, fulltext_url, coder A value + evidence, coder B value + evidence) for the field judge_input (RAW = the separate LLM judge receives original untrusted content such as tool outputs, web pages, documents, retrieved memory, other agents' message bodies, or tool-description text, at least in part; DERIVED = only content derived by the agent/another LLM from untrusted content, e.g., proposed tool calls and arguments, plans, summaries, sanitized observations; TRUSTED = only trusted input such as user query, system prompt, pre-written policy documents, tool names/schemas). Read the relevant method section of each paper's full text via WebFetch (fulltext_url, or https://arxiv.org/html/<arxiv_id> / https://arxiv.org/pdf/<arxiv_id>; for TrustAgent use https://aclanthology.org/2024.findings-emnlp.585.pdf). Do not use WebSearch; never include an email address in any request. Decide the final value for each paper. Write /home/claude/w/search/pb/expo_adj.tsv with header: id	final	evidence	src (5 rows). Final message: the decisions with one-line reasons.
```


### 10.53 Cross-model blind abstract coding check

모델 식별자: claude-sonnet-5-5

```text
You are an independent coder in a systematic mapping study on LLM-based AI agent security. Work BLIND: read ONLY these two files: /home/claude/w/xmodel/CODEBOOK_CODE.md (the abstract-level coding codebook, in Korean) and /home/claude/w/xmodel/xc.json (60 included papers: id, venue, title, abstract). Do NOT open, list, or grep any other file or directory under /home/claude/w (other coders' results must not influence you).

For EVERY item, code the abstract-level fields strictly by the codebook, from the title and abstract only: type (A/D/B, multiple allowed), actor (EXT/SUP/AGT/USR/NON, multiple), T (T1–T6, multiple), T5sub (a/b/c when T5), viol (AI/OI/C/AV/S, multiple), multistage (Y/N), embodied (Y/N), D (D1–D6, multiple, only when type includes D). Apply the detailed rules in section 3 where relevant. Use ';' between multiple values and '-' when a field has no value. Do not guess beyond the text.

Write the result to /home/claude/w/xmodel/xc_result.tsv (tab-separated, header line exactly: id	type	actor	T	T5sub	viol	multistage	embodied	D	note). note ≤ 15 words in English. One row per input item, same order, all 60 rows. Process the items in chunks (e.g., 15 at a time), and verify at the end with a short Python check that the TSV has 60 data rows with unique ids matching the input. Do not use WebSearch. Final message: counts of each type and each T category.
```


### 10.54 Cross-model blind screening check

모델 식별자: claude-sonnet-5-5

```text
You are an independent screener in a systematic mapping study on LLM-based AI agent security. Work BLIND: read ONLY these two files: /home/claude/w/xmodel/CODEBOOK_SCREEN.md (the screening codebook, in Korean) and /home/claude/w/xmodel/xs.json (200 candidate papers: id, venue, title, abstract). Do NOT open, list, or grep any other file or directory under /home/claude/w (other screeners' results must not influence you).

For EVERY item decide INC or EXC strictly by the codebook (inclusion I1 and I2(a)/(b); exclusion codes E1–E6, X; and the detailed rules R1–R5 in section 3). Judge from the title and abstract. Do not guess beyond the text; when the case is borderline, still decide, and mark borderline=Y with a one-line reason.

Write the result to /home/claude/w/xmodel/xs_result.tsv (tab-separated, header line exactly: id	decision	exc_reason	borderline	note). exc_reason is '-' for INC; borderline is Y or N; note ≤ 20 words in English. One row per input item, same order, all 200 rows. Process the items in chunks (e.g., 25 at a time) so you don't lose track, and verify at the end with a short Python check that the TSV has 200 data rows with unique ids matching the input. Do not use WebSearch. Final message: counts of INC/EXC by reason and number of borderline items.
```


### 10.55 Full-text adjudication (main model)

모델 식별자: claude-opus-5-5

```text
You are an adjudicator in the screening stage of a systematic mapping study on the security of LLM-based AI agents. Eight candidate papers received conflicting include/exclude judgments at the title/abstract stage. Decide each one from the FULL TEXT, strictly applying the codebook.

Inputs:
- Codebook (Korean): /home/claude/w/xmodel2/CODEBOOK_ADJ.md (inclusion criteria I1, I2; exclusion codes E1–E6, X; decision rules R1–R6). Read it fully first.
- Papers: /home/claude/w/xmodel2/adj8_in.json (id, venue, title, abstract).

Procedure for each paper:
1. Find and read the full text with WebSearch/WebFetch (arXiv abs/html/pdf, ACL Anthology PDF, proceedings pages; openreview.net PDFs usually return 403, so prefer arXiv). Read the method and evaluation sections, not only the abstract.
2. Decide INC or EXC under the codebook. For EXC give the exclusion code. Apply the rules literally: I1 (does the studied system actually act via tools/web/code execution/memory/other agents/robots, and do the experiments involve such actions?), I2(a) (adversarial threat: attack, defense, or benchmark/measurement) or I2(b) (a mechanism that enforces policies/permissions/safety rules on agent actions at run time, regardless of adversary; see R1, R4, R6).
3. State which criteria/rules decided it and quote 1–2 short phrases from the full text as evidence. Mark borderline=Y if a reasonable coder could decide otherwise, and say why.
Independence: do not open any other file under /home/claude/w (no prior decisions are provided on purpose), and in particular do not open adj8_out_sonnet.tsv or anything under /home/claude/w/search, /home/claude/w/xmodel, /home/claude/w/review*.

Output: write /home/claude/w/xmodel2/adj8_out_opus.tsv with header: id, decision(INC/EXC), exc_code, borderline(Y/N), src(URL and version actually read), rationale(criteria and rules applied, with short quotes). Tab-separated, one row per paper, no tabs/newlines inside fields. Final answer: the table in compact form.
```


### 10.56 Cross-model full-text coding 2

모델 식별자: claude-sonnet-5-5

```text
You are an independent coder in a systematic mapping study of LLM-agent security defenses. Code 10 defense papers from their full text, strictly following the codebook.

Inputs:
- Codebook (Korean): /home/claude/w/xmodel2/CODEBOOK_FT.md — read it fully first and follow it exactly (item definitions, allowed values, TSV header including the added judge_input column).
- Paper list: /home/claude/w/xmodel2/ft_in_2.json (10 papers; each has rid, title, venue, year, arxiv_id, site, fulltext_url, version_note).

Rules:
- Read the full text of each paper at fulltext_url using WebFetch (for long papers, fetch more than once with different prompts focused on: method/architecture and what the judging component receives as input; threat model; evaluation setup incl. adaptive attacks, benchmarks, models, utility, overhead, false positives). If the URL fails, follow the fallback rules in the codebook (arXiv abs/html/pdf; at most one WebSearch per paper) and record the URL actually read in src.
- Independence: do NOT open any file under /home/claude/w other than the two input files above (in particular not /home/claude/w/search, /home/claude/w/review*, /home/claude/w/supp, FINAL_CORPUS.json, STATS*.json, or any other coder's results). Judge only from the paper text. If something cannot be determined from the text, write '?'.
- Multi-valued fields use ';' as separator. Use exactly the codes in the codebook (stage: I,P,M,A,O,C; A_mode: pre/post/-; judge: SEP,SELF,ML,RULE,HUMAN; policy_src: MAN/LLM/LEARN/MIX/-; judge_exposed: Y/N/-; granularity: INPUT,ACTION,TRAJ,MSG,OUTPUT; decisions: allow,block,modify,limit,confirm; adversarial: Y/N; adaptive: 0/1/2/NA; public_bench: Y/N; n_models: integer or ?; utility/overhead/fpr: Y/N; hitl_burden: Y/N/-; judge_input: RAW/DERIVED/TRUSTED/- ).
- In evidence, quote short phrases from the paper supporting judge, judge_input, A_mode and adaptive.

Output: write a TSV file /home/claude/w/xmodel2/ft_out_2.tsv with the header given in the codebook (rid, title, src, stage, A_mode, judge, policy_src, judge_exposed, granularity, decisions, adversarial, adaptive, bench, public_bench, n_models, utility, overhead, fpr, hitl_burden, judge_input, evidence), one row per paper, tab-separated, no tabs or newlines inside fields. Final answer: the path, the number of rows written, and a list of papers whose full text could not be read (if any).
```


### 10.57 Cross-model full-text coding 3

모델 식별자: claude-sonnet-5-5

```text
You are an independent coder in a systematic mapping study of LLM-agent security defenses. Code 10 defense papers from their full text, strictly following the codebook.

Inputs:
- Codebook (Korean): /home/claude/w/xmodel2/CODEBOOK_FT.md — read it fully first and follow it exactly (item definitions, allowed values, TSV header including the added judge_input column).
- Paper list: /home/claude/w/xmodel2/ft_in_3.json (10 papers; each has rid, title, venue, year, arxiv_id, site, fulltext_url, version_note).

Rules:
- Read the full text of each paper at fulltext_url using WebFetch (for long papers, fetch more than once with different prompts focused on: method/architecture and what the judging component receives as input; threat model; evaluation setup incl. adaptive attacks, benchmarks, models, utility, overhead, false positives). If the URL fails, follow the fallback rules in the codebook (arXiv abs/html/pdf; at most one WebSearch per paper) and record the URL actually read in src.
- Independence: do NOT open any file under /home/claude/w other than the two input files above (in particular not /home/claude/w/search, /home/claude/w/review*, /home/claude/w/supp, FINAL_CORPUS.json, STATS*.json, or any other coder's results). Judge only from the paper text. If something cannot be determined from the text, write '?'.
- Multi-valued fields use ';' as separator. Use exactly the codes in the codebook (stage: I,P,M,A,O,C; A_mode: pre/post/-; judge: SEP,SELF,ML,RULE,HUMAN; policy_src: MAN/LLM/LEARN/MIX/-; judge_exposed: Y/N/-; granularity: INPUT,ACTION,TRAJ,MSG,OUTPUT; decisions: allow,block,modify,limit,confirm; adversarial: Y/N; adaptive: 0/1/2/NA; public_bench: Y/N; n_models: integer or ?; utility/overhead/fpr: Y/N; hitl_burden: Y/N/-; judge_input: RAW/DERIVED/TRUSTED/- ).
- In evidence, quote short phrases from the paper supporting judge, judge_input, A_mode and adaptive.

Output: write a TSV file /home/claude/w/xmodel2/ft_out_3.tsv with the header given in the codebook (rid, title, src, stage, A_mode, judge, policy_src, judge_exposed, granularity, decisions, adversarial, adaptive, bench, public_bench, n_models, utility, overhead, fpr, hitl_burden, judge_input, evidence), one row per paper, tab-separated, no tabs or newlines inside fields. Final answer: the path, the number of rows written, and a list of papers whose full text could not be read (if any).
```


### 10.58 Cross-model full-text coding 1

모델 식별자: claude-sonnet-5-5

```text
You are an independent coder in a systematic mapping study of LLM-agent security defenses. Code 10 defense papers from their full text, strictly following the codebook.

Inputs:
- Codebook (Korean): /home/claude/w/xmodel2/CODEBOOK_FT.md — read it fully first and follow it exactly (item definitions, allowed values, TSV header including the added judge_input column).
- Paper list: /home/claude/w/xmodel2/ft_in_1.json (10 papers; each has rid, title, venue, year, arxiv_id, site, fulltext_url, version_note).

Rules:
- Read the full text of each paper at fulltext_url using WebFetch (for long papers, fetch more than once with different prompts focused on: method/architecture and what the judging component receives as input; threat model; evaluation setup incl. adaptive attacks, benchmarks, models, utility, overhead, false positives). If the URL fails, follow the fallback rules in the codebook (arXiv abs/html/pdf; at most one WebSearch per paper) and record the URL actually read in src.
- Independence: do NOT open any file under /home/claude/w other than the two input files above (in particular not /home/claude/w/search, /home/claude/w/review*, /home/claude/w/supp, FINAL_CORPUS.json, STATS*.json, or any other coder's results). Judge only from the paper text. If something cannot be determined from the text, write '?'.
- Multi-valued fields use ';' as separator. Use exactly the codes in the codebook (stage: I,P,M,A,O,C; A_mode: pre/post/-; judge: SEP,SELF,ML,RULE,HUMAN; policy_src: MAN/LLM/LEARN/MIX/-; judge_exposed: Y/N/-; granularity: INPUT,ACTION,TRAJ,MSG,OUTPUT; decisions: allow,block,modify,limit,confirm; adversarial: Y/N; adaptive: 0/1/2/NA; public_bench: Y/N; n_models: integer or ?; utility/overhead/fpr: Y/N; hitl_burden: Y/N/-; judge_input: RAW/DERIVED/TRUSTED/- ).
- In evidence, quote short phrases from the paper supporting judge, judge_input, A_mode and adaptive.

Output: write a TSV file /home/claude/w/xmodel2/ft_out_1.tsv with the header given in the codebook (rid, title, src, stage, A_mode, judge, policy_src, judge_exposed, granularity, decisions, adversarial, adaptive, bench, public_bench, n_models, utility, overhead, fpr, hitl_burden, judge_input, evidence), one row per paper, tab-separated, no tabs or newlines inside fields. Final answer: the path, the number of rows written, and a list of papers whose full text could not be read (if any).
```


### 10.59 Full-text adjudication (other model)

모델 식별자: claude-sonnet-5-5

```text
You are an adjudicator in the screening stage of a systematic mapping study on the security of LLM-based AI agents. Eight candidate papers received conflicting include/exclude judgments at the title/abstract stage. Decide each one from the FULL TEXT, strictly applying the codebook.

Inputs:
- Codebook (Korean): /home/claude/w/xmodel2/CODEBOOK_ADJ.md (inclusion criteria I1, I2; exclusion codes E1–E6, X; decision rules R1–R6). Read it fully first.
- Papers: /home/claude/w/xmodel2/adj8_in.json (id, venue, title, abstract).

Procedure for each paper:
1. Find and read the full text with WebSearch/WebFetch (arXiv abs/html/pdf, ACL Anthology PDF, proceedings pages; openreview.net PDFs usually return 403, so prefer arXiv). Read the method and evaluation sections, not only the abstract.
2. Decide INC or EXC under the codebook. For EXC give the exclusion code. Apply the rules literally: I1 (does the studied system actually act via tools/web/code execution/memory/other agents/robots, and do the experiments involve such actions?), I2(a) (adversarial threat: attack, defense, or benchmark/measurement) or I2(b) (a mechanism that enforces policies/permissions/safety rules on agent actions at run time, regardless of adversary; see R1, R4, R6).
3. State which criteria/rules decided it and quote 1–2 short phrases from the full text as evidence. Mark borderline=Y if a reasonable coder could decide otherwise, and say why.
Independence: do not open any other file under /home/claude/w (no prior decisions are provided on purpose).

Output: write /home/claude/w/xmodel2/adj8_out_sonnet.tsv with header: id, decision(INC/EXC), exc_code, borderline(Y/N), src(URL and version actually read), rationale(criteria and rules applied, with short quotes). Tab-separated, one row per paper, no tabs/newlines inside fields. Final answer: the table in compact form.
```


### 10.60 Cross-model full-text coding 5

모델 식별자: claude-sonnet-5-5

```text
You are an independent coder in a systematic mapping study of LLM-agent security defenses. Code 12 defense papers from their full text, strictly following the codebook.

Inputs:
- Codebook (Korean): /home/claude/w/xmodel2/CODEBOOK_FT.md — read it fully first and follow it exactly (item definitions, allowed values, TSV header including the added judge_input column).
- Paper list: /home/claude/w/xmodel2/ft_in_5.json (12 papers; each has rid, title, venue, year, arxiv_id, site, fulltext_url, version_note).

Rules:
- Read the full text of each paper at fulltext_url using WebFetch (for long papers, fetch more than once with different prompts focused on: method/architecture and what the judging component receives as input; threat model; evaluation setup incl. adaptive attacks — look carefully in the evaluation section, the discussion/limitations and the appendix for any attack designed with knowledge of the defense or optimized against it; benchmarks, models, utility, overhead, false positives). If the URL fails, follow the fallback rules in the codebook (arXiv abs/html/pdf; at most one WebSearch per paper) and record the URL actually read in src.
- Independence: do NOT open any file under /home/claude/w other than the two input files above (in particular not /home/claude/w/search, /home/claude/w/review*, /home/claude/w/supp, /home/claude/w/xmodel2/ft_out_*.tsv, FINAL_CORPUS.json, STATS*.json, or any other coder's results). Judge only from the paper text. If something cannot be determined from the text, write '?'.
- Multi-valued fields use ';' as separator. Use exactly the codes in the codebook (stage: I,P,M,A,O,C; A_mode: pre/post/-; judge: SEP,SELF,ML,RULE,HUMAN; policy_src: MAN/LLM/LEARN/MIX/-; judge_exposed: Y/N/-; granularity: INPUT,ACTION,TRAJ,MSG,OUTPUT; decisions: allow,block,modify,limit,confirm; adversarial: Y/N; adaptive: 0/1/2/NA; public_bench: Y/N; n_models: integer or ?; utility/overhead/fpr: Y/N; hitl_burden: Y/N/-; judge_input: RAW/DERIVED/TRUSTED/- ).
- In evidence, quote short phrases from the paper supporting judge, judge_input, A_mode and adaptive.

Output: write a TSV file /home/claude/w/xmodel2/ft_out_5.tsv with the header given in the codebook (rid, title, src, stage, A_mode, judge, policy_src, judge_exposed, granularity, decisions, adversarial, adaptive, bench, public_bench, n_models, utility, overhead, fpr, hitl_burden, judge_input, evidence), one row per paper, tab-separated, no tabs or newlines inside fields. Final answer: the path, the number of rows written, and a list of papers whose full text could not be read (if any).
```


### 10.61 Cross-model full-text coding 4

모델 식별자: claude-sonnet-5-5

```text
You are an independent coder in a systematic mapping study of LLM-agent security defenses. Code 12 defense papers from their full text, strictly following the codebook.

Inputs:
- Codebook (Korean): /home/claude/w/xmodel2/CODEBOOK_FT.md — read it fully first and follow it exactly (item definitions, allowed values, TSV header including the added judge_input column).
- Paper list: /home/claude/w/xmodel2/ft_in_4.json (12 papers; each has rid, title, venue, year, arxiv_id, site, fulltext_url, version_note).

Rules:
- Read the full text of each paper at fulltext_url using WebFetch (for long papers, fetch more than once with different prompts focused on: method/architecture and what the judging component receives as input; threat model; evaluation setup incl. adaptive attacks — look carefully in the evaluation section, the discussion/limitations and the appendix for any attack designed with knowledge of the defense or optimized against it; benchmarks, models, utility, overhead, false positives). If the URL fails, follow the fallback rules in the codebook (arXiv abs/html/pdf; at most one WebSearch per paper) and record the URL actually read in src.
- Independence: do NOT open any file under /home/claude/w other than the two input files above (in particular not /home/claude/w/search, /home/claude/w/review*, /home/claude/w/supp, /home/claude/w/xmodel2/ft_out_*.tsv, FINAL_CORPUS.json, STATS*.json, or any other coder's results). Judge only from the paper text. If something cannot be determined from the text, write '?'.
- Multi-valued fields use ';' as separator. Use exactly the codes in the codebook (stage: I,P,M,A,O,C; A_mode: pre/post/-; judge: SEP,SELF,ML,RULE,HUMAN; policy_src: MAN/LLM/LEARN/MIX/-; judge_exposed: Y/N/-; granularity: INPUT,ACTION,TRAJ,MSG,OUTPUT; decisions: allow,block,modify,limit,confirm; adversarial: Y/N; adaptive: 0/1/2/NA; public_bench: Y/N; n_models: integer or ?; utility/overhead/fpr: Y/N; hitl_burden: Y/N/-; judge_input: RAW/DERIVED/TRUSTED/- ).
- In evidence, quote short phrases from the paper supporting judge, judge_input, A_mode and adaptive.

Output: write a TSV file /home/claude/w/xmodel2/ft_out_4.tsv with the header given in the codebook (rid, title, src, stage, A_mode, judge, policy_src, judge_exposed, granularity, decisions, adversarial, adaptive, bench, public_bench, n_models, utility, overhead, fpr, hitl_burden, judge_input, evidence), one row per paper, tab-separated, no tabs or newlines inside fields. Final answer: the path, the number of rows written, and a list of papers whose full text could not be read (if any).
```
