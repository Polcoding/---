# fixture 확장 후보 재검토 결과 체크리스트

## 목적

`docs/102_fixture_expansion_decision_after_repeat_run.md` 기준으로 fixture 확장 여부를 안전하게 재검토했는지 확인합니다.

## 현재 fixture 확인

| 완료 | 항목 |
|---|---|
| [x] | 일반 routing fixture 6종을 확인했는가 |
| [x] | helper fixture 2종을 별도 폴더로 확인했는가 |
| [x] | 기존 routing 상태 4종을 모두 커버하는지 확인했는가 |
| [x] | review_report 승인/미승인 경로를 확인했는가 |

## 확장 후보 판단

| 완료 | 항목 |
|---|---|
| [x] | one_page_report 확장 후보를 검토했는가 |
| [x] | project_plan ready fixture 후보를 검토했는가 |
| [x] | result_report ready fixture 후보를 검토했는가 |
| [x] | review_report 승인 fixture 후보를 검토했는가 |
| [x] | unknown needs_more_input fixture 후보를 검토했는가 |
| [x] | blocked 변형 fixture 후보를 검토했는가 |
| [x] | placeholder_confirmed_values routing fixture 후보를 보류했는가 |

## 결정 확인

| 완료 | 항목 |
|---|---|
| [x] | fixture JSON을 즉시 추가하지 않기로 했는가 |
| [x] | normalizer 코드를 변경하지 않기로 했는가 |
| [x] | routing 결과를 변경하지 않기로 했는가 |
| [x] | HWPX payload 반영을 하지 않기로 했는가 |
| [x] | helper fixture와 일반 routing fixture 분리를 유지했는가 |

## 다음 단계 확인

| 완료 | 항목 |
|---|---|
| [x] | missing_fields 생성 규칙 개선 여부를 다음 후보로 정리했는가 |
| [x] | placeholder-confirmed 값 구분 문제를 다음 검토 대상으로 남겼는가 |
| [x] | project_plan/result_report ready 경로 개방을 보류했는가 |

## 보안 검수

| 완료 | 항목 |
|---|---|
| [x] | 실제 개인정보를 추가하지 않았는가 |
| [x] | 실제 기관명, 업체명, 담당자명을 추가하지 않았는가 |
| [x] | 실제 문서번호, 민원번호, 사건번호를 추가하지 않았는가 |
| [x] | 실제 날짜, 예산, 실적 수치를 추가하지 않았는가 |
| [x] | 실제 공문 원문 또는 보고서 원문을 추가하지 않았는가 |
| [x] | 실제 HWPX 원본 파일을 추가하지 않았는가 |
