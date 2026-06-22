# missing_fields 생성 규칙 재검토 결과 체크리스트

## 목적

`docs/103_missing_fields_rule_decision_after_helper.md` 기준으로 `missing_fields` 생성 규칙을 최신 상태에서 재검토했는지 확인합니다.

## 현재 상태 확인

| 완료 | 항목 |
|---|---|
| [x] | `make_missing_fields()`가 문서 유형별 고정 누락값을 생성하는지 확인했는가 |
| [x] | `known_values`가 현재 빈 객체로 유지되는지 확인했는가 |
| [x] | `placeholder_confirmed_values` helper가 read-only 검증용인지 확인했는가 |
| [x] | helper fixture가 기존 routing fixture와 분리되어 있는지 확인했는가 |
| [x] | metadata schema가 문서 기준 후보로만 유지되는지 확인했는가 |

## 정책 결정 확인

| 완료 | 항목 |
|---|---|
| [x] | `project_plan`의 `needs_more_input` 경로를 유지하기로 했는가 |
| [x] | `result_report`의 `needs_more_input` 경로를 유지하기로 했는가 |
| [x] | `missing_fields` 자동 제외 금지 원칙을 유지했는가 |
| [x] | placeholder-confirmed 값을 개념상 구분하되 코드에는 반영하지 않기로 했는가 |
| [x] | `placeholder_confirmed_values`를 routing에 연결하지 않기로 했는가 |
| [x] | HWPX payload 구조를 바꾸지 않기로 했는가 |

## 코드 및 fixture 판단

| 완료 | 항목 |
|---|---|
| [x] | normalizer 코드 변경이 불필요하다고 판단했는가 |
| [x] | fixture JSON 추가가 불필요하다고 판단했는가 |
| [x] | 기존 routing fixture 6종을 유지하기로 했는가 |
| [x] | helper fixture 2종을 별도 검증용으로 유지하기로 했는가 |
| [x] | renderer dry-run 구조를 바꾸지 않기로 했는가 |

## 다음 단계 확인

| 완료 | 항목 |
|---|---|
| [x] | 사용자 표시 기준 문서화가 다음 최소 작업인지 정리했는가 |
| [x] | HWPX 본문과 검토용 확인 목록 분리 필요성을 확인했는가 |
| [x] | placeholder-confirmed 값 표시 표현을 다음 검토 대상으로 남겼는가 |
| [x] | 실제값 입력 금지 안내 문구를 다음 검토 대상으로 남겼는가 |
| [x] | 후속 사용자 확인 표시 기준 문서를 연결했는가 |

## 보안 검수

| 완료 | 항목 |
|---|---|
| [x] | 실제 개인정보를 추가하지 않았는가 |
| [x] | 실제 기관명, 업체명, 담당자명을 추가하지 않았는가 |
| [x] | 실제 문서번호, 민원번호, 사건번호를 추가하지 않았는가 |
| [x] | 실제 날짜, 예산, 실적 수치를 추가하지 않았는가 |
| [x] | 실제 공문 원문 또는 보고서 원문을 추가하지 않았는가 |
| [x] | 실제 HWPX 원본 파일을 추가하지 않았는가 |
| [x] | Email, API, Make.com 연동을 하지 않았는가 |
