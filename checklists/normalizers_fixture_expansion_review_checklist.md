# normalizers fixture 확장 후보 검토 체크리스트

## 목적

`docs/85_normalizers_fixture_expansion_review.md` 기준으로 fixture 확장 여부를 검토했는지 확인합니다.

## 현재 범위 확인

| 완료 | 항목 |
|---|---|
| [x] | 기존 fixture 6종을 확인했는가 |
| [x] | HWPX 보고서 4종 document_type을 모두 커버하는가 |
| [x] | `ready_for_draft` 경로가 포함되는가 |
| [x] | `needs_more_input` 경로가 포함되는가 |
| [x] | `needs_security_review` 경로가 포함되는가 |
| [x] | `blocked` 경로가 포함되는가 |
| [x] | `review_report` 승인/미승인 경로가 모두 포함되는가 |

## 확장 후보 확인

| 완료 | 항목 |
|---|---|
| [x] | one_page_report 템플릿 기반 fixture 후보를 검토했는가 |
| [x] | project_plan 템플릿 기반 fixture 후보를 검토했는가 |
| [x] | result_report 템플릿 기반 fixture 후보를 검토했는가 |
| [x] | review_report 템플릿 기반 fixture 후보를 검토했는가 |
| [x] | blocked fixture 확장 후보를 검토했는가 |

## 판단 확인

| 완료 | 항목 |
|---|---|
| [x] | 즉시 fixture 추가가 필요한지 판단했는가 |
| [x] | fixture 추가 전 선행 조건을 정리했는가 |
| [x] | 중복 fixture를 보류했는가 |
| [x] | 향후 추가 우선순위를 정리했는가 |

## 보안 검수

| 완료 | 항목 |
|---|---|
| [x] | 실제 개인정보를 포함하지 않았는가 |
| [x] | 실제 기관명, 업체명, 담당자명을 포함하지 않았는가 |
| [x] | 실제 승인자명, 결재번호, 문서번호를 포함하지 않았는가 |
| [x] | 실제 공문 또는 보고서 원문을 포함하지 않았는가 |
| [x] | 실제 예산액, 일정, 실적 수치를 생성하지 않았는가 |
| [x] | Email/API/Make.com 연동을 하지 않았는가 |

## 다음 단계 판단

| 완료 | 항목 |
|---|---|
| [x] | 현재 fixture 6종을 회귀 기준으로 유지할 수 있는가 |
| [ ] | `missing_fields` 생성 규칙 개선 여부를 검토할 수 있는가 |
