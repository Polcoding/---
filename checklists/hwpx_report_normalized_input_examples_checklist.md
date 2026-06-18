# HWPX 보고서 정규화 예시 체크리스트

## 목적

`docs/64_hwpx_report_normalized_input_examples.md`가 HWPX 보고서 4종의 입력 정규화 기준을 안전하게 설명하는지 확인합니다.

## 기준 문서

- `docs/60_hwpx_report_input_requirements.md`
- `docs/61_input_normalization_schema.md`
- `docs/62_security_filter_requirements.md`
- `docs/63_input_normalization_test_cases.md`

## 구성 확인

| 완료 | 항목 |
|---|---|
| [x] | `one_page_report` 예시가 포함되었는가 |
| [x] | `project_plan` 예시가 포함되었는가 |
| [x] | `result_report` 예시가 포함되었는가 |
| [x] | `review_report` 예시가 포함되었는가 |
| [x] | 각 예시에 `content_inputs`가 포함되었는가 |
| [x] | 각 예시에 `missing_fields`가 포함되었는가 |
| [x] | 각 예시에 `security_flags`가 포함되었는가 |
| [x] | 각 예시에 `routing_decision`이 포함되었는가 |
| [x] | 문서 유형별 기본 라우팅 기준이 포함되었는가 |

## 보안 검수

| 완료 | 항목 |
|---|---|
| [x] | 실제 개인정보를 포함하지 않았는가 |
| [x] | 실제 기관명, 업체명, 담당자명을 포함하지 않았는가 |
| [x] | 실제 문서번호, 민원번호, 접수번호, 사건번호를 포함하지 않았는가 |
| [x] | 실제 공문 또는 보고서 원문을 포함하지 않았는가 |
| [x] | 실제 예산액 또는 실적 수치를 포함하지 않았는가 |
| [x] | 확인되지 않은 값은 `[확인 필요]` 또는 `missing_fields`로 분리했는가 |
| [x] | 검토보고서 라우팅을 보수적으로 두었는가 |

## 다음 단계 판단

| 완료 | 항목 |
|---|---|
| [x] | 입력 정규화 로직의 최소 구현 범위 검토로 넘어갈 수 있는가 |
| [x] | 구현 전 테스트 fixture 전환 여부를 별도 판단해야 함을 남겼는가 |
