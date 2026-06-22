# Phase 3 상태별 중단 기준 반복 운영 문서 반영 결과

## 목적

`docs/112_phase3_external_hwpx_and_manual_preview_criteria.md`의 상태별 중단 기준을 Phase 2 반복 운영 문서에 반영할지 검토하고, 반영 결과를 기록합니다.

이 문서는 코드 변경 지시서가 아닙니다. 현재 단계에서는 반복 운영 기준과 반복 운영 로그 템플릿만 보강하고 normalizer, renderer, routing, HWPX payload, fixture, HWPX output은 변경하지 않습니다.

## 검토 결론

상태별 중단 기준은 반복 운영 문서에 반영하는 것이 필요하다고 판단했습니다.

반영 이유:

- `docs/112`에는 Phase 3 preview 기준이 정리되어 있지만, 실제 반복 실행 시 기록 양식은 `docs/100`과 `docs/101`입니다.
- `template_required`, `needs_security_review`, `blocked`, validation 실패, `remaining_placeholders` 잔여, output 잠금, Git Changes HWPX 표시를 반복 실행마다 같은 기준으로 처리해야 합니다.
- 사용자 수동 preview에서 이상이 발생했을 때 실제 원문이나 실제 파일명을 기록하지 않고 상태와 증상만 남겨야 합니다.
- 상태별 기준은 코드 변경 없이 운영 문서와 로그 템플릿만으로도 반영할 수 있습니다.

## 반영 대상 판단

| 문서 | 판단 |
|---|---|
| `docs/100_phase2_repeat_operation_criteria.md` | 반복 실행 기준이므로 상태별 중단 기준 표를 추가 |
| `docs/101_phase2_repeat_operation_log_template.md` | 반복 실행 결과를 남기는 양식이므로 상태별 중단 확인 섹션을 추가 |
| `docs/83_phase2_user_input_and_manual_operation_checkpoints.md` | 사용자 입력과 한컴 검수 중심 문서이므로 이번에는 직접 보강하지 않음 |

`docs/83`은 이미 사용자 수동 검수와 이상 발견 시 처리 기준을 갖고 있습니다. 이번 작업은 반복 실행 기준과 로그 기록 기준을 맞추는 범위로 제한했습니다.

## 반영한 상태별 기준

| 상태 또는 증상 | 반복 운영 처리 |
|---|---|
| `ready_for_draft` | placeholder 기반 HWPX 초안 생성 가능 |
| `needs_more_input` | `[확인 필요]`와 `missing_fields`를 유지한 상태로 초안 생성 가능 |
| `needs_security_review` | 사람 보안 검토 전 HWPX 렌더링 중단 |
| `blocked` | 처리 중단, 실제값 제거 요청 |
| `template_required` | 로컬 템플릿 준비 전 안전 중단, output 생성 시도하지 않음 |
| validation 실패 | 렌더링 중단, payload 또는 placeholder map 확인 |
| `remaining_placeholders` 있음 | preview 중단, placeholder map 또는 템플릿 오탈자 확인 |
| output 잠금 | 한컴에서 output 파일을 닫은 뒤 재시도 |
| GitHub Desktop Changes에 HWPX 표시 | 작업 중단, `.gitignore`와 파일 위치 확인 |

## 로그 템플릿 반영 위치

`docs/101_phase2_repeat_operation_log_template.md`의 로그 템플릿 안에서 다음 순서로 배치했습니다.

1. 실행 명령 결과
2. 상태별 중단 확인
3. HWPX output 확인
4. `missing_fields` 확인
5. 사용자 한컴 검수

상태별 중단 확인을 HWPX output 확인보다 앞에 둔 이유는, 중단 상태가 발생한 경우 output 확인 단계로 넘어가지 않아야 하기 때문입니다.

## 중복 여부 판단

이번 보강은 중복이 아니라 역할 분리입니다.

| 문서 | 역할 |
|---|---|
| `docs/112` | Phase 3 기준 정의 |
| `docs/100` | 반복 실행 전후 기준 |
| `docs/101` | 반복 실행 결과 기록 양식 |
| `docs/83` | 사용자 입력과 수동 검수 체크포인트 |

같은 상태명이 여러 문서에 등장하더라도, 기준 정의와 실행 기록의 역할이 다르므로 유지합니다.

## 코드 변경 판단

현재 단계에서는 코드 변경이 필요하지 않습니다.

변경하지 않은 항목:

- normalizer 코드
- renderer 코드
- routing 결과
- HWPX payload 구조
- fixture JSON
- HWPX output
- 로컬 HWPX 템플릿
- `placeholder_confirmed_values` normalizer 연결

## 계속 보류할 범위

- 실제 기관 HWPX 양식 원본 Git 추가
- 실제 공문 또는 보고서 원문 처리
- 실제 개인정보, 민원정보, 내부 운영정보 처리
- `missing_fields` 자동 제외
- `placeholder_confirmed_values` routing 연결
- HWPX payload metadata 자동 반영
- Email, API, Make.com 실제 연동

## 후속 반영 상태

Phase 3 운영 문서 묶음 통합 점검은 `docs/114_phase3_operating_docs_integrated_review.md`에 반영했습니다.

확인 대상:

- `docs/111_phase3_entry_safety_gate.md`
- `docs/112_phase3_external_hwpx_and_manual_preview_criteria.md`
- `docs/113_phase3_state_stop_repeat_docs_reflection.md`
- `docs/100_phase2_repeat_operation_criteria.md`
- `docs/101_phase2_repeat_operation_log_template.md`
- 관련 체크리스트

통합 점검 질문:

- Phase 3 안전 게이트와 반복 운영 기준이 같은 상태명을 같은 의미로 쓰는지
- 사용자 수동 preview 기준과 반복 로그 항목이 서로 빠짐없이 연결되는지
- Git 제외와 실제 원문 금지 기준이 문서마다 일관되는지
- 코드 변경 없이 문서 기준만으로 충분한지

다음 단계는 실제 연동 구현이 아니라, 외부 전송 없는 no-send dry-run 기준을 문서로 점검하는 것입니다.

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX 원본 파일 추가 없음
- Email, API, Make.com 연동 없음

## 결론

Phase 3 상태별 중단 기준은 반복 운영 기준과 반복 운영 로그 템플릿에 반영했습니다.

외부 연동 필요성과 보류 기준은 `docs/115`에, 로그와 감사 추적 기준은 `docs/116`에, 테스트 계정과 테스트 데이터 기준은 `docs/117`에, 실제 원문 차단과 비식별 입력 확인 절차는 `docs/118`에, 사용자 preview와 사람 승인 지점 통합 기준은 `docs/119`에 후속 반영했습니다.

반영 범위는 문서와 체크리스트에 한정했습니다. 코드, fixture, routing, HWPX payload, HWPX output은 변경하지 않았습니다.
