# missing_fields 수동 운영 점검표 반영 결과

## 목적

`docs/104_missing_fields_user_display_guidance.md`와 `docs/105_missing_fields_repeat_log_reflection_result.md` 기준을 `docs/83_phase2_user_input_and_manual_operation_checkpoints.md`에 반영한 결과를 기록합니다.

이 문서는 코드 변경 지시서가 아닙니다. 현재 단계에서는 사용자 입력 및 수동 운영 점검표만 보강하고 normalizer, routing, HWPX payload, HWPX output은 변경하지 않습니다.

## 검토 결론

Phase 2 사용자 입력 및 수동 운영 점검표에 `missing_fields` 표시 기준을 반영했습니다.

반영 이유:

- 반복 운영 로그에는 `missing_fields 확인` 섹션이 추가되었습니다.
- 사용자 수동 운영 점검표에도 같은 기준이 있어야 실제 HWPX output 확인 시 누락값을 오해하지 않습니다.
- 기존 `[확인 필요]` 확인 항목은 placeholder 오인 방지에 가깝고, `missing_fields`가 검토용 목록이라는 기준은 별도로 필요합니다.
- 입력 전 단계에서도 `[확인 필요]`가 실제값이 아니라는 의미를 명확히 해야 합니다.

## 반영 위치

`docs/83_phase2_user_input_and_manual_operation_checkpoints.md`에 다음 위치로 반영했습니다.

| 위치 | 반영 내용 |
|---|---|
| 입력 전 사용자 체크리스트 | `[확인 필요]`가 `missing_fields` 검토용 항목으로 분리될 수 있음을 추가 |
| HWPX output 생성 전 수동 점검 | `missing_fields`를 검토용 목록으로 유지하고 자동 제외하지 않는 기준 추가 |
| HWPX output 생성 후 사용자 검수 | HWPX 본문과 검토용 확인 목록 분리 확인 추가 |
| 이상 발견 시 처리 | `missing_fields`를 실제값처럼 확정하면 중단하도록 추가 |
| 완료 판단 | `missing_fields`가 검토용 확인 목록으로 분리되어 있는지 추가 |

## 기존 항목과의 중복 여부

중복이 아니라 역할이 다릅니다.

| 기존 항목 | 역할 |
|---|---|
| 확인 필요값 | `[확인 필요]`가 실제값처럼 보이지 않는지 확인 |
| `missing_fields` 표시 | 본문과 검토용 확인 목록이 분리되어 있는지 확인 |
| 검토용 목록 | 누락값을 본문 실제값으로 확정하지 않는지 확인 |

## 입력 전 체크리스트 반영 판단

입력 전 체크리스트에는 `missing_fields`라는 내부 필드를 직접 작성하라고 안내하지 않았습니다.

대신 `[확인 필요]`는 실제값이 아니며, 이후 `missing_fields` 검토용 항목으로 분리될 수 있다고만 안내했습니다.

이유:

- 사용자가 normalizer 내부 구조를 직접 작성할 필요는 없습니다.
- 실제 일정, 예산, 실적, 담당자, 수량을 임의로 채우지 않게 하는 것이 더 중요합니다.
- `missing_fields`는 코드 생성 결과이자 사람 검토용 목록입니다.

## 코드 변경 판단

현재 단계에서는 코드 변경이 필요하지 않습니다.

변경하지 않은 항목:

- `make_missing_fields()` 생성 규칙
- `routing_decision.status`
- HWPX payload 구조
- renderer dry-run 구조
- fixture JSON
- `placeholder_confirmed_values` helper 연결
- HWPX output

## 다음 작업 후보

다음 단계에서는 Phase 2 운영 문서 묶음에서 `missing_fields` 표시 기준이 중복 없이 정리되었는지 통합 점검합니다.

확인 대상 후보:

- `docs/83_phase2_user_input_and_manual_operation_checkpoints.md`
- `docs/101_phase2_repeat_operation_log_template.md`
- `docs/104_missing_fields_user_display_guidance.md`
- `docs/105_missing_fields_repeat_log_reflection_result.md`
- `docs/106_missing_fields_manual_operation_checkpoints_reflection.md`

검토 질문:

- 같은 기준이 서로 다른 문서에서 모순 없이 표현되는지
- 반복 운영 로그와 수동 운영 점검표의 역할이 분리되어 있는지
- `missing_fields` 자동 제외 금지 원칙이 유지되는지
- 코드 변경 없이 문서 기준만으로 충분한지

후속 작업에서 통합 점검 결과는 `docs/107_missing_fields_phase2_docs_integrated_review.md`에 정리했습니다.

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX 원본 파일 추가 없음
- Email, API, Make.com 연동 없음

## 결론

`missing_fields` 표시 기준은 Phase 2 사용자 입력 및 수동 운영 점검표에 반영했습니다.

반영 범위는 문서와 체크리스트에 한정했습니다. 코드, fixture, routing, HWPX payload, HWPX output은 변경하지 않았습니다.
