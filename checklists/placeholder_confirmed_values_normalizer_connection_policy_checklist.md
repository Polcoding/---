# placeholder_confirmed_values normalizer 연결 정책 체크리스트

## 목적

`docs/94_placeholder_confirmed_values_normalizer_connection_policy.md` 기준으로 helper 결과의 normalizer 연결 허용 조건과 금지 조건을 안전하게 정리했는지 확인합니다.

## 연결 판단

| 완료 | 항목 |
|---|---|
| [x] | 현재 단계에서 normalizer 연결을 보류했는가 |
| [x] | 연결 허용 조건을 read-only metadata로 제한했는가 |
| [x] | 연결 금지 조건을 명시했는가 |
| [x] | 보안 필터 우선 원칙을 유지했는가 |

## 변경 금지 확인

| 완료 | 항목 |
|---|---|
| [x] | `missing_fields` 변경 금지를 명시했는가 |
| [x] | routing 결과 변경 금지를 명시했는가 |
| [x] | `security_flags` 변경 금지를 명시했는가 |
| [x] | HWPX payload 변경 금지를 명시했는가 |
| [x] | HWPX output 변경 금지를 명시했는가 |

## 보류 범위

| 완료 | 항목 |
|---|---|
| [x] | invalid finding을 즉시 blocked로 바꾸지 않기로 했는가 |
| [x] | `project_plan` ready 경로 개방을 보류했는가 |
| [x] | `result_report` ready 경로 개방을 보류했는가 |
| [x] | API/Make.com/Email 연동을 제외했는가 |

## 보안 검수

| 완료 | 항목 |
|---|---|
| [x] | 실제 개인정보를 추가하지 않았는가 |
| [x] | 실제 기관명, 업체명, 담당자명을 추가하지 않았는가 |
| [x] | 실제 문서번호, 민원번호, 사건번호를 추가하지 않았는가 |
| [x] | 실제 날짜, 예산, 실적 수치를 추가하지 않았는가 |
| [x] | 실제 공문 원문 또는 보고서 원문을 추가하지 않았는가 |
| [x] | 실제 HWPX 원본 파일을 추가하지 않았는가 |

## 다음 단계 판단

| 완료 | 항목 |
|---|---|
| [x] | read-only metadata schema 후보를 다음 단계로 검토할 수 있는가 |
| [x] | 기존 6종 회귀 기준을 유지할 수 있는가 |
