# missing_fields 반복 운영 로그 반영 결과

## 목적

`docs/104_missing_fields_user_display_guidance.md`의 표시 기준을 `docs/101_phase2_repeat_operation_log_template.md`에 반영할지 검토하고, 반영 결과를 기록합니다.

이 문서는 코드 변경 지시서가 아닙니다. 현재 단계에서는 반복 운영 로그 템플릿만 보강하고 normalizer, routing, HWPX payload, HWPX output은 변경하지 않습니다.

## 검토 결론

반복 운영 로그 템플릿에 `missing_fields 확인` 섹션을 반영했습니다.

반영 이유:

- `docs/101`에는 HWPX output 확인과 사용자 한컴 검수는 있었지만, `missing_fields`를 검토용 목록으로 해석하는 별도 확인란은 없었습니다.
- `missing_fields`는 HWPX 본문 값이 아니라 사람 검토용 확인 목록입니다.
- `[확인 필요]`가 실제값처럼 보이지 않는지 매번 확인할 필요가 있습니다.
- placeholder 유지 확인과 실제값 입력 금지를 운영 로그에서 분리해 기록할 필요가 있습니다.

## 반영 위치

`docs/101_phase2_repeat_operation_log_template.md`의 로그 템플릿 안에서 다음 순서로 배치했습니다.

1. 실행 명령 결과
2. HWPX output 확인
3. `missing_fields` 확인
4. 사용자 한컴 검수
5. 이상 발생 기록

이 배치는 HWPX output 생성 결과와 사용자 수동 검수 사이에서 누락값 표시를 먼저 확인하기 위한 것입니다.

## 추가한 확인 항목

반복 운영 로그에 다음 항목을 추가했습니다.

| 확인 항목 | 목적 |
|---|---|
| 확인 필요 항목 개수 확인 | 누락값 존재 여부를 먼저 파악 |
| HWPX 본문과 검토용 확인 목록 분리 확인 | 본문과 검토용 목록 혼동 방지 |
| `[확인 필요]`가 실제값처럼 보이지 않음 | placeholder 오인 방지 |
| placeholder 유지 확인 대상 구분 | placeholder-confirmed 의미 오해 방지 |
| 실제값 입력 금지 안내 포함 | 일정, 예산, 실적 등 임의 작성 방지 |

또한 `missing_fields`는 검토용 목록이며, 본문 실제값으로 확정하지 않는다는 문구를 추가했습니다.

## 사용자 한컴 검수와의 중복 여부

중복이 아니라 역할이 다릅니다.

| 구분 | 역할 |
|---|---|
| `missing_fields 확인` | 누락값 표시와 해석 기준 확인 |
| 사용자 한컴 검수 | 파일 열림, 글자 겹침, 항목 순서, 줄바꿈, placeholder 잔여 확인 |

사용자 한컴 검수의 `[확인 필요]` 확인 항목은 유지합니다.

## 중단 기준 보강

반복 운영 중단 기준에 다음 항목을 추가했습니다.

- `missing_fields`를 실제값처럼 확정하거나 자동 제외

이 기준은 `missing_fields` 자동 제외 금지, routing 변경 금지 원칙을 반복 운영 로그에서도 확인하기 위한 것입니다.

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

다음 단계에서는 같은 기준을 `docs/83_phase2_user_input_and_manual_operation_checkpoints.md`와 해당 체크리스트에 반영할지 검토합니다.

검토 질문:

- HWPX output 생성 후 사용자 검수에 `missing_fields` 확인란을 추가할지
- 입력 전 체크리스트에 `missing_fields` 표시 기준을 넣을지
- 기존 `[확인 필요]` 확인 항목과 중복되지 않게 분리할 수 있는지
- 코드 변경 없이 문서 기준만으로 충분한지

후속 작업에서 Phase 2 사용자 입력 및 수동 운영 점검표 반영 결과는 `docs/106_missing_fields_manual_operation_checkpoints_reflection.md`에 정리했습니다.

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX 원본 파일 추가 없음
- Email, API, Make.com 연동 없음

## 결론

`missing_fields` 표시 기준은 Phase 2 반복 운영 로그 템플릿에 반영했습니다.

반영 범위는 문서 템플릿과 체크리스트에 한정했습니다. 코드, fixture, routing, HWPX payload, HWPX output은 변경하지 않았습니다.
