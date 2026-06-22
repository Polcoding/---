# missing_fields 생성 규칙 재검토 결과

## 목적

`placeholder_confirmed_values` helper, helper fixture, metadata 문서화가 끝난 뒤에도 `missing_fields` 생성 규칙을 바꿀 필요가 있는지 재검토합니다.

이 문서는 코드 변경 지시서가 아닙니다. 현재 저장소 상태를 기준으로 `missing_fields` 유지 여부, 자동 제외 금지 원칙, 다음 문서화 후보를 정리합니다.

## 확인한 현재 상태

현재 normalizer 흐름은 다음 기준을 유지합니다.

| 항목 | 현재 상태 |
|---|---|
| `make_missing_fields()` | 문서 유형별 고정 누락값 생성 |
| `known_values` | 빈 객체 유지 |
| `placeholder_confirmed_values` helper | read-only 검증용 |
| helper fixture | 기존 routing fixture 6종과 분리 |
| metadata schema | 문서 기준 후보로만 유지 |
| routing 결과 | helper 결과와 연결하지 않음 |
| HWPX payload | helper 결과와 연결하지 않음 |

현재 고정 누락값은 다음과 같습니다.

| document_type | 유지하는 missing_fields |
|---|---|
| `one_page_report` | `purpose` |
| `project_plan` | `schedule`, `budget` |
| `result_report` | `results_or_metrics`, `budget` |
| `review_report` | `review_scope`, `required_reviews` |

## 재검토 질문별 판단

| 질문 | 판단 |
|---|---|
| project_plan/result_report의 필수값 누락을 계속 `needs_more_input`으로 둘지 | 유지 |
| placeholder-confirmed 값을 `[확인 필요]`와 구분할지 | 개념상 구분하되 코드에는 미반영 |
| `missing_fields` 자동 제외 금지 원칙을 유지할지 | 유지 |
| 사용자에게 더 보기 좋게 표시하는 문서 기준이 필요한지 | 필요 |
| 지금 단계에서 코드 변경이 필요한지 | 불필요 |
| fixture 확장 없이 문서 기준으로 충분한지 | 충분 |
| `placeholder_confirmed_values`를 아직 연결하지 않을지 | 연결 보류 |

## 결정

현재 단계에서는 `missing_fields` 생성 규칙을 코드로 개선하지 않습니다.

결정 사항:

- `make_missing_fields(document_type)` 구조 유지
- `project_plan`과 `result_report`의 `needs_more_input` 경로 유지
- `placeholder_confirmed_values`로 `missing_fields` 자동 제외 금지
- `placeholder_confirmed_values`로 `ready_for_draft` 경로 개방 금지
- 기존 routing fixture 6종 변경 없음
- helper fixture 2종은 별도 검증용으로 유지
- HWPX payload 구조 변경 없음
- renderer dry-run 구조 변경 없음

## 이유

`missing_fields`는 단순 표시 필드가 아니라 routing에 직접 영향을 줄 수 있습니다.

특히 `project_plan`과 `result_report`에서 일정, 예산, 실적 값을 잘못 제외하면 실제값이 확인된 것처럼 보일 위험이 있습니다. 현재 프로젝트 원칙상 예산, 일정, 실적, 담당자, 수량은 임의 생성하거나 확정 처리하지 않습니다.

따라서 `placeholder_confirmed_values`가 안전한 placeholder 형식으로 검증되더라도, 그 값은 "실제값 확인 완료"가 아니라 "placeholder 유지 의사 확인"으로만 봅니다.

## placeholder-confirmed 값과 [확인 필요] 구분

구분 기준은 다음과 같습니다.

| 구분 | 의미 | 현재 코드 반영 |
|---|---|---|
| `[확인 필요]` | 값이 비어 있거나 아직 확인되지 않음 | 본문 placeholder와 missing_fields에 사용 |
| `placeholder_confirmed_values` | 사용자가 실제값 대신 placeholder 유지 의사를 밝힘 | helper 검증만 수행 |
| `known_values` | 사용자가 안전하게 제공했고 사용 가능한 값 | 현재 비워 둠 |

현재 단계에서는 이 구분을 코드 흐름에 연결하지 않습니다.

다만 사용자 확인 화면이나 운영 로그에서는 다음처럼 의미를 구분해 적을 수 있습니다.

| 표시 항목 | 권장 표현 |
|---|---|
| 아직 확인할 값 | 사용자 확인 필요 |
| placeholder 유지 의사가 있는 값 | placeholder 유지 확인 |
| 실제값처럼 쓰면 안 되는 값 | 실제값 입력 금지 |

## 사용자 표시 기준 필요성

코드 변경보다 먼저 필요한 것은 사용자에게 `missing_fields`를 어떻게 보여줄지 정하는 문서 기준입니다.

필요한 이유:

- `missing_fields`가 본문 내용인지 검토용 목록인지 혼동될 수 있음
- `[확인 필요]`와 placeholder-confirmed 값이 같은 의미로 보일 수 있음
- HWPX 보고서 본문과 사람 검토용 확인 목록을 분리해야 함
- 다음 수동 리허설에서 사용자가 확인할 항목을 더 빠르게 찾을 수 있음

따라서 다음 최소 작업은 코드 변경이 아니라 `missing_fields` 사용자 확인 표시 기준 문서화입니다.

## 다음 작업 후보

다음 작업에서는 다음 기준을 문서화합니다.

1. `missing_fields` 항목을 사용자에게 표시하는 순서
2. `field_name`, `reason`, `required_for`, `suggested_placeholder` 표시 방식
3. HWPX 본문과 검토용 확인 목록의 분리 기준
4. placeholder-confirmed 값의 표시 표현
5. 실제값 입력 금지 안내 문구
6. 운영 로그에서 누락값 확인 결과를 적는 방식

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX 원본 파일 추가 없음
- Email, API, Make.com 연동 없음

## 결론

`missing_fields` 생성 규칙은 현재 고정 정책을 유지합니다.

`placeholder_confirmed_values`는 계속 read-only helper와 문서 기준 metadata 후보로만 유지하고, `missing_fields`, routing, HWPX payload에는 연결하지 않습니다.

다음 단계는 `missing_fields`를 사용자에게 더 명확하게 보여주는 표시 기준을 문서화하는 것입니다.

후속 작업에서 사용자 확인 표시 기준은 `docs/104_missing_fields_user_display_guidance.md`에 정리했습니다.
