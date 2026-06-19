# placeholder_confirmed_values 파일 기반 fixture 분리 체크리스트

## 목적

`docs/93_placeholder_confirmed_values_file_fixture_result.md` 기준으로 helper 전용 fixture 분리가 안전하게 완료되었는지 확인합니다.

## fixture 분리

| 완료 | 항목 |
|---|---|
| [x] | helper 전용 fixture 하위 폴더를 사용했는가 |
| [x] | safe fixture를 파일로 분리했는가 |
| [x] | invalid fixture를 파일로 분리했는가 |
| [x] | 기존 routing fixture 6종 위치를 바꾸지 않았는가 |
| [x] | 기존 routing fixture 6종 schema를 바꾸지 않았는가 |

## 검증 스크립트

| 완료 | 항목 |
|---|---|
| [x] | helper 검증 스크립트가 파일 기반 fixture를 읽는가 |
| [x] | mapping 검증과 단일 값 검증을 모두 지원하는가 |
| [x] | helper safe fixture가 통과했는가 |
| [x] | helper invalid fixture가 통과했는가 |
| [x] | 기존 routing fixture 6종이 통과했는가 |

## 보류 범위

| 완료 | 항목 |
|---|---|
| [x] | `missing_fields` 자동 제외를 하지 않았는가 |
| [x] | routing 결과를 변경하지 않았는가 |
| [x] | HWPX payload 반영을 하지 않았는가 |
| [x] | `project_plan` ready 경로를 열지 않았는가 |
| [x] | `result_report` ready 경로를 열지 않았는가 |

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
| [x] | helper 결과를 normalizer 흐름에 연결할지 별도 판단할 수 있는가 |
| [x] | 연결 전 허용 조건과 금지 조건을 먼저 문서화할 수 있는가 |
