# normalizers fixture 확장 후보 검토

## 목적

`docs/84_hwpx_report_user_input_templates.md`의 사용자 입력 템플릿을 기준으로 `normalizers/fixtures/`를 확장할 필요가 있는지 검토합니다.

이번 문서는 fixture를 즉시 늘리는 작업이 아니라, 현재 6종 fixture가 커버하는 범위와 추가 후보의 우선순위를 정리합니다.

## 현재 fixture 범위

| fixture | document_type | routing | payload | 역할 |
|---|---|---|---|---|
| `safe_one_page_report_request.json` | `one_page_report` | `ready_for_draft` | 생성 | 안전 입력 정상 경로 |
| `missing_project_plan_request.json` | `project_plan` | `needs_more_input` | 생성 | 계획서 누락값 경로 |
| `missing_result_report_request.json` | `result_report` | `needs_more_input` | 생성 | 결과보고서 누락값 경로 |
| `review_report_needs_security_review.json` | `review_report` | `needs_security_review` | 미생성 | 검토보고서 기본 보안 경로 |
| `approved_review_report_request.json` | `review_report` | `ready_for_draft` | 생성 | 승인된 검토보고서 제한 경로 |
| `blocked_real_value_like_request.json` | `unknown` | `blocked` | 미생성 | 금지 자동화 차단 경로 |

## 현재 fixture로 충분한 범위

- HWPX 보고서 4종 document_type 판정
- `ready_for_draft`, `needs_more_input`, `needs_security_review`, `blocked` 라우팅 전체
- payload 생성/미생성 분기
- `review_report` 승인/미승인 경로 분리
- mapped HWPX 렌더링 4종 연결
- 실제값 없는 placeholder 기반 회귀 테스트

## 확장 후보

| 후보 | 목적 | 현재 추가 여부 | 이유 |
|---|---|---|---|
| `template_one_page_report_request.json` | `docs/84` one_page_report 입력 템플릿 반영 | 보류 | 현재 `safe_one_page_report_request.json`과 역할 중복 |
| `template_project_plan_request.json` | project_plan 템플릿 입력 반영 | 보류 | 현 normalizer는 project_plan 누락 필드를 고정 생성하므로 새 fixture만으로 ready 경로 검증 불가 |
| `template_result_report_request.json` | result_report 템플릿 입력 반영 | 보류 | 현 normalizer는 result_report 누락 필드를 고정 생성하므로 새 fixture만으로 ready 경로 검증 불가 |
| `review_report_without_gate_from_template.json` | 템플릿 기반 review_report 미승인 경로 확인 | 보류 | 기존 `review_report_needs_security_review.json`과 역할 중복 |
| `review_report_with_gate_from_template.json` | 템플릿 기반 review_report 승인 경로 확인 | 보류 | 기존 `approved_review_report_request.json`과 역할 중복 |
| `blocked_template_real_value_request.json` | 금지 입력 예시 차단 확인 | 보류 | 기존 blocked fixture가 실제 원문/자동화 금지 요청을 커버 |

## 즉시 추가하지 않는 이유

현재 fixture 6종은 최소 회귀 테스트에 필요한 상태 전이를 모두 포함합니다.

지금 fixture를 단순히 늘리면 다음 문제가 생깁니다.

- 동일한 routing을 반복 검증하는 중복 fixture 증가
- 입력 템플릿 문서와 코드 기능의 차이를 fixture 이름만으로 가리는 문제
- project_plan/result_report의 ready 경로가 코드상 아직 별도로 열려 있지 않은 상태에서 의미 없는 기대값 생성
- 회귀 테스트 실행 결과는 길어지지만 새 보장 범위는 작음

## fixture 추가 전 선행 조건

fixture를 추가하려면 먼저 다음 중 하나가 필요합니다.

1. `normalizers/input_normalizer_poc.py`가 fixture의 명시적 safe known values를 읽어 `missing_fields`를 줄일 수 있어야 함
2. `project_plan`과 `result_report`에서 실제값이 아닌 placeholder-confirmed 값을 구분할 수 있어야 함
3. `docs/84` 입력 템플릿을 fixture 구조로 옮길 때 `request_text` 외의 structured field를 받을지 결정해야 함
4. fixture 이름과 기대 routing이 기존 6종과 중복되지 않아야 함

## 향후 추가 우선순위

추가가 필요해지면 다음 순서를 권장합니다.

1. `project_plan_ready_placeholder_request.json`
   - 목적: 일정ㆍ예산이 실제값이 아니라 placeholder-confirmed 상태일 때 `ready_for_draft` 가능 여부 검토
   - 선행 조건: missing_fields 생성 규칙 개선

2. `result_report_ready_placeholder_request.json`
   - 목적: 실적ㆍ예산 집행 정보가 placeholder-confirmed 상태일 때 `ready_for_draft` 가능 여부 검토
   - 선행 조건: missing_fields 생성 규칙 개선

3. `unknown_document_type_needs_more_input_request.json`
   - 목적: 문서 유형이 애매하지만 차단은 아닌 입력을 `needs_more_input`으로 보낼지 검토
   - 선행 조건: 현재 unknown은 blocked로 가는 정책 재검토

4. `template_based_review_report_gate_request.json`
   - 목적: `docs/84` review_report 템플릿과 승인 신호를 더 직접 연결
   - 선행 조건: 기존 approved fixture와 중복 가치 비교

## 보안 조건

추가 fixture는 다음 조건을 반드시 지켜야 합니다.

- 실제 공문 원문 사용 금지
- 실제 개인정보 사용 금지
- 실제 기관명, 부서명, 담당자명 사용 금지
- 실제 문서번호, 민원번호, 사건번호 사용 금지
- 실제 예산액, 일정, 실적 수치 사용 금지
- 실제 승인자명, 결재번호, 검토의견 원문 사용 금지
- Email/API/Make.com 연동 금지

## 결론

현재는 fixture를 즉시 추가하지 않고 기존 6종을 회귀 테스트 기준으로 유지합니다.

다음 단계는 fixture를 늘리기 전에 `missing_fields` 생성 규칙을 더 정교하게 만들지 여부를 검토하는 것입니다.
