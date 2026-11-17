# [KCI] LLM 기반 AI 에이전트의 보안 위협과 방어 기술 연구 동향

**Research Trends in Security Threats and Defenses for LLM-Based AI Agents: Focusing on Attack Chains and Enforcement Points**
— data, classification criteria, prompts, and scripts (Journal of Internet Computing and Services, 2026)

이 저장소는 위 논문의 문헌 검색식, 분류 기준(코딩북), 실행 지시문, 문헌 목록, 분류 결과, 항목별 일치도, 분석 스크립트를 담고 있습니다. 논문의 모든 수치는 이 자료에서 재계산할 수 있습니다.

## 구성

| 경로 | 내용 |
|---|---|
| `data/corpus_and_results.xlsx` | 집계 결과 24개 시트. 첫 시트(README)에 시트별 설명이 있습니다. 분석 대상 208편의 분류 결과(S1_Corpus), 후보 1,289편의 선별 판정(S2_Screening), 문헌 흐름, 일치도, 다른 모델 점검 결과(S16–S19) 등 |
| `data/raw/` | 실행별 원자료: 선별·분류·조정 결과(TSV/JSON), 최종 코퍼스 `FINAL_CORPUS.json`, 논문 수치 `STATS10.json`, 다른 모델 점검 집계 `XMODEL14.json`·`XMODEL14b.json` |
| `data/raw/xmodel/`, `data/raw/xmodel2/` | 다른 모델(claude-sonnet-5-5)의 표본 재판정 입력·출력과 코딩북. 선별 200편, 초록 기준 60편, 원문 기준 30편과 24편, 경계 사례 8편의 원문 재판정(`adj8_*`) |
| `docs/codebooks_and_prompts.md` | 검색·선별 프로토콜, 분류 기준(코딩북), 검색 로그, 실행 61건의 지시문 원문 |
| `scripts/` | 검색식 적용, 코퍼스 구성, 집계, 일치도 계산, 원고 수치 대조, 그림 생성 |

## 논문의 주요 항목과 자료의 대응

| 논문 | 자료 |
|---|---|
| 2.2절 검색식, 부록 A | `scripts/query_v3.py`, `S12_SearchScope` 시트 |
| 2.3절 포함·제외 기준, 세부 판정 기준 | `docs/codebooks_and_prompts.md` 2–8절, `S14_Rules` 시트 |
| 2.3절 실행 A·B 일치도(κ 0.92, PABAK 0.96) | `S4a_Kappa_Screen` 시트, `data/raw/MASTER_SCREEN_base.json`, `SCREEN_B*.tsv` |
| 2.3절 다른 모델 재판정(κ 0.82, 0.88, 0.89, 0.61) | `S16`–`S18` 시트, `data/raw/xmodel*/` |
| 2.3절 경계 사례 8편의 원문 재판정(포함 3·제외 3·상이 1) | `S19_XModel_Adjud` 시트, `data/raw/xmodel2/adj8_*` |
| 표 2–5, 4장–6장의 편수와 비율 | `STATS10.json` (생성: `scripts/analysis10.py`), 문헌별 라벨은 `S1_Corpus` 시트 |
| 그림 2 문헌 흐름 | `S3_Flow` 시트, `scripts/fig2.py` |

## 재현

```bash
cd scripts
python3 analysis10.py          # data/raw/STATS10.json 재생성 (논문 수치의 단일 출처)
python3 analysis14_xmodel.py   # XMODEL14.json  (다른 모델 점검: 선별 200편, 초록 기준 60편)
python3 analysis14_xmodel2.py  # XMODEL14b.json (다른 모델 점검: 원문 기준, 경계 사례 8편)
python3 verify_manuscript.py manuscript.docx   # 원고 docx의 수치와 용어를 자료와 대조
```

`query_v3.py`(검색식 적용)는 8개 학회의 메타데이터(약 540 MB)가 필요하여 동봉하지 않았습니다. 다음을 `data/metadata/`에 두면 실행됩니다.
- `acl_xml/`: [acl-org/acl-anthology](https://github.com/acl-org/acl-anthology) 커밋 d9a3b806f3703df4bedacdd1e662800b423f7d87의 `data/xml/`
- `paperlists/`: [papercopilot/paperlists](https://github.com/papercopilot/paperlists) 커밋 9fcfd1234879a8e5630b5116dde411ec143dd763의 학회별 폴더(iclr, icml, nips, aaai, ijcai)

의존성: Python 3.10+, `openpyxl`, `matplotlib`, `lxml`.

## 용어

논문의 "분류"는 이 자료의 "코딩(coding)", "분류 기준"은 "코딩북(codebook)", "경계 사례"는 `borderline` 표시에 해당합니다. 분류 기준과 지시문은 실행 당시의 원문 그대로이므로 일부 용어가 논문의 최종 용어와 다릅니다(판정기 → 판정 모델, 적대자 → 공격자, 원천 → 원본, 세칙 → 세부 판정 기준, 코더 A·B → 실행 A·B).

## 수행 방식

- 선별과 분류는 사전에 정의한 기준에 따라 LLM(claude-opus-5-5)의 별도 실행이 수행하였고, 사람에 의한 표본 검증은 수행하지 않았습니다. 일치도는 판정의 일관성을 나타내며 정확성을 보장하지 않습니다.
- 같은 문헌을 판정한 실행 A와 실행 B는 서로의 결과를 보지 않았습니다. 선별 실행 B의 후반 989편은 앞선 조정에서 나온 세부 판정 기준을 사용했습니다.
- 분류의 일관성은 다른 모델(claude-sonnet-5-5)의 표본 재판정으로 점검했습니다. 두 모델은 같은 개발사의 모델입니다.
- 경계 사례(선별 재판정에서 판정이 갈린 8편)에는 사전에 정의한 실행 A·B와 조정 절차의 기준을 일관되게 적용했으며, 점검용 재판정으로 분석 대상을 바꾸지 않았습니다.
- 원문은 질의에 대한 추출 결과를 돌려주는 웹 조회 도구로 읽었으므로, 결과 파일의 근거 인용문은 원문과 글자 단위로 대조되지 않았습니다.

## 인용

Y. E. Chang, "LLM 기반 AI 에이전트의 보안 위협과 방어 기술 연구 동향: 공격 체인과 집행 지점을 중심으로," Journal of Internet Computing and Services, 2026 (게재 확정, 권·호 미정).
