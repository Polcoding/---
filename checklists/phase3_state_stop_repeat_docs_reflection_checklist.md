# Phase 3 상태별 중단 기준 반복 운영 문서 반영 체크리스트

## 목적

`docs/113_phase3_state_stop_repeat_docs_reflection.md` 기준으로 Phase 3 상태별 중단 기준이 반복 운영 문서에 안전하게 반영되었는지 확인합니다.

## 반영 필요성 확인

| 완료 | 항목 |
|---|---|
| [x] | `docs/112`의 상태별 중단 기준을 확인했는가 |
| [x] | `docs/100`에 반복 실행 기준으로 반영할 필요가 있다고 판단했는가 |
| [x] | `docs/101`에 반복 실행 기록 양식으로 반영할 필요가 있다고 판단했는가 |
| [x] | `docs/83`은 이번 직접 보강 대상에서 제외한 이유를 정리했는가 |

## 상태별 기준 반영 확인

| 완료 | 항목 |
|---|---|
| [x] | `ready_for_draft` 처리 기준을 정리했는가 |
| [x] | `needs_more_input` 처리 기준을 정리했는가 |
| [x] | `needs_security_review` 렌더링 중단 기준을 정리했는가 |
| [x] | `blocked` 처리 중단 기준을 정리했는가 |
| [x] | `template_required` 안전 중단 기준을 정리했는가 |
| [x] | validation 실패 시 렌더링 중단 기준을 정리했는가 |
| [x] | `remaining_placeholders` 잔여 시 preview 중단 기준을 정리했는가 |
| [x] | output 잠금 시 처리 기준을 정리했는가 |
| [x] | GitHub Desktop Changes에 HWPX 표시 시 중단 기준을 정리했는가 |

## 문서 반영 확인

| 완료 | 항목 |
|---|---|
| [x] | `docs/100_phase2_repeat_operation_criteria.md`에 상태별 중단 기준 표를 추가했는가 |
| [x] | `docs/101_phase2_repeat_operation_log_template.md`에 상태별 중단 확인 섹션을 추가했는가 |
| [x] | `checklists/phase2_repeat_operation_criteria_checklist.md`를 갱신했는가 |
| [x] | `checklists/phase2_repeat_operation_log_template_checklist.md`를 갱신했는가 |
| [x] | README와 AGENTS의 현재 진행 상태를 갱신했는가 |
| [x] | NEXT_STEP을 다음 추천 작업으로 갱신했는가 |

## 변경 제한 확인

| 완료 | 항목 |
|---|---|
| [x] | normalizer 코드를 변경하지 않았는가 |
| [x] | renderer 코드를 변경하지 않았는가 |
| [x] | fixture JSON을 변경하지 않았는가 |
| [x] | routing 결과를 변경하지 않았는가 |
| [x] | HWPX payload 구조를 변경하지 않았는가 |
| [x] | HWPX output을 재생성하지 않았는가 |
| [x] | `placeholder_confirmed_values`를 normalizer에 연결하지 않았는가 |

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

## 다음 단계 확인

| 완료 | 항목 |
|---|---|
| [x] | Phase 3 운영 문서 묶음 통합 점검이 `docs/114`에 반영되었는가 |
| [x] | 외부 연동을 계속 후순위로 유지했는가 |
