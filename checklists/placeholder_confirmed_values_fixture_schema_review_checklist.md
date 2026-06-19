# placeholder_confirmed_values fixture schema 검토 체크리스트

## 목적

`docs/92_placeholder_confirmed_values_fixture_schema_review.md` 기준으로 fixture schema 확장 여부를 안전하게 판단했는지 확인합니다.

## schema 판단

| 완료 | 항목 |
|---|---|
| [x] | `placeholder_confirmed_values`를 fixture schema 후보로 문서화했는가 |
| [x] | 기존 fixture 6종에 바로 추가하지 않기로 했는가 |
| [x] | helper 검증을 기존 routing 회귀 테스트와 분리했는가 |
| [x] | `expected_placeholder_confirmed_validation` 후보 구조를 정리했는가 |

## 보류 범위

| 완료 | 항목 |
|---|---|
| [x] | `missing_fields` 자동 제외를 보류했는가 |
| [x] | routing 결과 변경을 보류했는가 |
| [x] | `project_plan` ready 경로 개방을 보류했는가 |
| [x] | `result_report` ready 경로 개방을 보류했는가 |
| [x] | HWPX payload 반영을 보류했는가 |

## 회귀 기준

| 완료 | 항목 |
|---|---|
| [x] | 기존 fixture 6종을 회귀 기준으로 유지했는가 |
| [x] | helper 전용 검증을 별도 축으로 유지했는가 |
| [x] | 신규 fixture를 추가할 경우 별도 검토하기로 했는가 |

## 보안 검수

| 완료 | 항목 |
|---|---|
| [x] | 실제 개인정보를 추가하지 않았는가 |
| [x] | 실제 기관명, 업체명, 담당자명을 추가하지 않았는가 |
| [x] | 실제 문서번호, 민원번호, 사건번호를 추가하지 않았는가 |
| [x] | 실제 날짜, 예산, 실적 수치를 추가하지 않았는가 |
| [x] | 실제 공문 원문 또는 보고서 원문을 추가하지 않았는가 |
| [x] | 실제 HWPX 원본 파일을 추가하지 않았는가 |
| [x] | API, Make.com, Email 자동화 코드를 추가하지 않았는가 |

## 다음 단계 판단

| 완료 | 항목 |
|---|---|
| [x] | helper 전용 검증 케이스를 파일 기반 fixture로 분리할지 검토할 수 있는가 |
| [x] | 기존 routing 회귀 테스트와 섞지 않는 원칙을 유지할 수 있는가 |
