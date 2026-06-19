# placeholder_confirmed_values read-only metadata schema 체크리스트

## 목적

`docs/95_placeholder_confirmed_values_readonly_metadata_schema.md` 기준으로 read-only metadata schema 후보가 안전하게 정리되었는지 확인합니다.

## schema 확인

| 완료 | 항목 |
|---|---|
| [x] | metadata 필드명을 정했는가 |
| [x] | top-level 필드 후보로 정했는가 |
| [x] | `security_flags` 안에 넣지 않기로 했는가 |
| [x] | `checked`, `valid`, `invalid_count`, `findings`를 정의했는가 |
| [x] | 영향 여부 flag를 모두 `false`로 두었는가 |

## 변경 금지 확인

| 완료 | 항목 |
|---|---|
| [x] | `missing_fields` 변경 금지를 명시했는가 |
| [x] | routing 결과 변경 금지를 명시했는가 |
| [x] | `security_flags` 변경 금지를 명시했는가 |
| [x] | HWPX payload 변경 금지를 명시했는가 |
| [x] | HWPX output 변경 금지를 명시했는가 |

## 보안 우선 원칙

| 완료 | 항목 |
|---|---|
| [x] | 보안 필터 판단이 helper 판단보다 우선임을 명시했는가 |
| [x] | invalid finding을 즉시 blocked로 바꾸지 않기로 했는가 |
| [x] | invalid finding은 검토용 metadata로만 남기기로 했는가 |

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
| [x] | metadata를 코드에 연결하지 않고 문서 기준으로 유지할지 검토할 수 있는가 |
| [x] | dry-run preview 전용 출력 여부를 별도 검토할 수 있는가 |
