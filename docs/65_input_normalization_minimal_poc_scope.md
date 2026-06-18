# 입력 정규화 최소 PoC 범위

## 목적

이 문서는 Phase 2에서 입력 정규화 로직을 어느 범위까지 코드 PoC로 구현할지 결정합니다.

현재 목표는 전체 운영 자동화가 아니라, HWPX 보고서 4종에 한정해 사용자의 비식별 업무 지시를 표준 입력 구조로 정리할 수 있는지 검증하는 것입니다.

## 결론

입력 정규화는 문서 기준으로만 두지 않고 최소 코드 PoC를 작성합니다.

다만 범위는 HWPX 보고서 4종으로 제한합니다.

- `one_page_report`
- `project_plan`
- `result_report`
- `review_report`

XLSX, Email, 공문, 민원 관련 외부 전달문은 이번 최소 PoC 범위에서 제외합니다.

## 구현 범위

### 포함

| 항목 | 포함 여부 | 설명 |
|---|---|---|
| 문서 유형 후보 판정 | 포함 | 키워드 기반으로 HWPX 보고서 4종 후보 판정 |
| 표준 입력 구조 생성 | 포함 | `docs/61_input_normalization_schema.md` 구조 사용 |
| `content_inputs` 생성 | 포함 | 목적, 배경, 주요 내용, 일정, 예산, 실적 등 placeholder 중심 |
| `missing_fields` 생성 | 포함 | 확인되지 않은 필수값 분리 |
| `security_flags` 초기 판정 | 포함 | 실제값 의심 신호를 플래그로 표시 |
| `routing_decision` 생성 | 포함 | `ready_for_draft`, `needs_more_input`, `needs_security_review`, `blocked` |
| placeholder fixture 테스트 | 포함 | 실제값 없는 JSON fixture 사용 |

### 제외

| 항목 | 제외 사유 |
|---|---|
| OpenAI API 호출 | 실제 연동 전 보안 필터 검증 필요 |
| Make.com 연동 | 운영 자동화 범위 아님 |
| Email 자동 발송 | 금지 업무 |
| HWPX 템플릿 생성 | 이미 별도 렌더러와 로컬 템플릿 정책 존재 |
| 실제 원문 파싱 | 보안 원칙 위반 가능 |
| 실제 HWPX 양식 처리 | 저장소 밖 수동 절차 대상 |
| 정교한 자연어 이해 모델 | 최소 PoC 범위를 초과 |
| C/D등급 문서 처리 | 외부 처리 금지 또는 내부 참고만 가능 |

## 권장 파일 구조

```text
normalizers/
├── README.md
├── input_normalizer_poc.py
├── security_filter_poc.py
├── fixtures/
│   ├── safe_one_page_report_request.json
│   ├── missing_project_plan_request.json
│   ├── review_report_needs_security_review.json
│   └── blocked_real_value_like_request.json
└── output/
    ├── .gitignore
    └── .gitkeep
```

## fixture Git 포함 여부

fixture는 Git에 포함합니다.

조건:

- 실제 개인정보 없음
- 실제 기관명 없음
- 실제 문서번호 없음
- 실제 공문 원문 없음
- 실제 예산액, 실적 수치, 담당자명 없음
- 차단 케이스도 실제값 대신 설명형 placeholder 사용

`normalizers/output/` 산출물은 Git에서 제외합니다.

## 보안 필터와 정규화 로직 경계

정규화 로직과 보안 필터는 분리합니다.

```text
input_normalizer_poc.py
→ 입력 구조화, 문서 유형 후보 판정, 누락값 분리

security_filter_poc.py
→ 위험 신호 판정, 라우팅 상태 보정, 차단 사유 생성
```

정규화 단계는 위험한 입력을 안전하다고 확정하지 않습니다. 위험 신호가 있으면 `security_flags`에 표시하고 보안 필터가 최종 라우팅을 결정합니다.

## 최소 테스트 케이스

| 케이스 | 입력 | 기대 결과 |
|---|---|---|
| 안전 원페이지 보고서 | 비식별 원페이지 보고 요청 | `one_page_report`, `ready_for_draft` |
| 누락값 추진계획서 | 일정ㆍ예산 미확정 계획서 요청 | `project_plan`, `needs_more_input` |
| 결과보고서 누락값 | 실적ㆍ예산 집행 정보 미확정 | `result_report`, `needs_more_input` |
| 검토보고서 보안 검토 | 법무ㆍ계약ㆍ개인정보 검토 가능성 | `review_report`, `needs_security_review` |
| 차단 요청 | 실제값 또는 실제 원문 의심 설명형 입력 | `unknown`, `blocked` |

## 구현 원칙

- 키워드 기반 규칙부터 시작합니다.
- 판단이 애매하면 더 보수적인 라우팅을 선택합니다.
- 실제값을 추출하거나 저장하지 않습니다.
- 원문 전체를 output에 남기지 않습니다.
- 출력 JSON은 문서화된 스키마와 비교 가능해야 합니다.
- renderer와 직접 연결하지 않고 정규화 결과 파일만 생성합니다.

## 완료 조건

- HWPX 보고서 4종 후보 판정 가능
- placeholder fixture 기반 테스트 가능
- `security_flags`와 `routing_decision` 생성 가능
- blocked/needs_security_review 케이스 포함
- output 산출물 Git 제외
- 기존 HWPX/XLSX/Markdown/Email 렌더러와 독립

## 다음 단계

다음 작업은 위 범위를 기준으로 `normalizers/` 최소 PoC 골격을 작성하는 것입니다.

코드 작성 전에도 실제 원문, 실제 개인정보, 실제 HWPX 양식은 사용하지 않습니다.
