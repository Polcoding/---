# 다음 작업

## 현재 상태

사용자 운영 A-to-Z 안내 문서, 리허설 체크리스트, 문서 유형별 비식별 요청 예시, 사용자 안내 3종 통합 점검 문서, 사용자 quick start, quick start 리허설 경계 문서, 사용자 안내 묶음 closeout 문서, 수동 preview 또는 리허설 유지 판단 문서, 문서 기반 사용자 리허설 결과 문서, 문서 기반 리허설 closeout 문서, 문서 기반 리허설 hold 상태 문서를 작성하고 주요 진입점 문서에 연결했습니다.

사용자 피드백에 따라 push 권장 빈도는 줄입니다. 앞으로는 단일 closeout 또는 작은 문구 정리마다 push를 권하지 않고, 여러 관련 작업을 묶어서 검증한 뒤 push 여부를 판단합니다.

수동 preview 재개 게이트와 체크리스트를 추가하고 closeout까지 정리해, 사용자가 나중에 비식별 작업 복사본을 준비했다고 명시했을 때만 수동 preview로 넘어가도록 정리했습니다.

현재 사용자는 `docs/140_user_operation_atoz_guide.md`에서 직접 확인할 일, Codex가 처리할 일, 현재 보류할 일을 한 번에 볼 수 있습니다.

`docs/143_user_quick_start.md`에서는 처음 열 파일, 가장 짧은 진행 순서, 바로 멈출 지점을 1페이지로 볼 수 있습니다.

`docs/144_quick_start_rehearsal_boundary.md`에서는 문서만으로 가능한 확인과 HWPX 열람이 필요한 확인을 분리합니다.

`docs/145_user_guidance_closeout.md`에서는 사용자 안내 묶음이 push 가능한 문서 산출물인지 판단할 수 있습니다.

`docs/146_next_manual_preview_or_rehearsal_decision.md`에서는 현재는 실제 HWPX 수동 preview가 아니라 문서 기반 리허설 유지가 추천됨을 확인할 수 있습니다.

`docs/147_document_only_user_rehearsal_result.md`에서는 실제 HWPX 없이 quick start와 체크리스트를 따라간 결과를 확인할 수 있습니다.

`docs/148_document_only_rehearsal_closeout.md`에서는 문서 기반 리허설 묶음이 push 가능한 산출물인지 확인할 수 있습니다.

`docs/149_document_only_rehearsal_hold_state.md`에서는 비식별 작업 복사본 준비 전까지 수동 preview를 보류하고 문서 기반 리허설 상태를 유지하는 기준을 확인할 수 있습니다.

`docs/150_manual_preview_resume_gate.md`와 `checklists/manual_preview_resume_gate_checklist.md`에서는 수동 preview 재개 조건을 확인할 수 있습니다.

`docs/151_manual_preview_resume_gate_closeout.md`에서는 재개 게이트 검증 결과와 push 빈도 판단을 확인할 수 있습니다.

`docs/152_project_result_artifact_map.md`에서는 현재 확인 가능한 결과물, 사용자 확인 필요 지점, 보류 항목을 한 번에 확인할 수 있습니다.

`docs/153_project_result_artifact_map_review.md`에서는 결과물 지도와 주요 진입점 정합성 점검 결과를 확인할 수 있습니다.

`docs/154_user_visible_artifact_bundle_closeout.md`에서는 사용자가 바로 볼 수 있는 산출물 묶음과 아직 결과물이 아닌 항목을 확인할 수 있습니다.

`docs/155_legacy_next_step_language_review.md`에서는 구형 다음 단계 문구가 최신 진입점과 충돌하지 않는지 점검한 결과를 확인할 수 있습니다.

`docs/156_user_visible_artifact_security_and_git_check.md`에서는 사용자 가시 산출물 묶음의 보안 검색, Git 제외 확인, 참조 파일 존재 여부 검증 결과를 확인할 수 있습니다.

`docs/157_current_status_progress_review.md`에서는 현황판 진행률을 과장하지 않고 유지한 이유를 확인할 수 있습니다.

`checklists/user_operation_atoz_rehearsal_checklist.md`에서는 실제 HWPX 없이도 현재 단계 확인을 체크박스로 리허설할 수 있습니다.

`docs/141_user_rehearsal_prompt_examples.md`에서는 보고서 4종 요청 예시를 실제값 없이 확인할 수 있습니다.

`docs/142_user_guidance_integrated_review.md`에서는 사용자 안내 3종의 정합성 점검 결과를 볼 수 있습니다.

`README.md`와 `CURRENT_STATUS.md`도 이 문서와 체크리스트를 현재 사용자 안내 진입점으로 연결합니다.

현재 공통 표시는 다음과 같습니다.

- `[사용자 확인 필요]`: 사람이 직접 판단하거나 확인해야 하는 값
- `[Codex 처리 가능]`: 비식별 placeholder 입력을 바탕으로 구조화 가능한 항목
- `[보류]`: 현재 단계에서 자동화하지 않는 항목

## 목표

새 문서 생성 없이 현재 변경 묶음의 검증 상태를 유지하고, 사용자 확인 필요 지점이나 실제 HWPX 수동 preview 지점이 생길 때만 멈춥니다.

## 확인 대상

- `docs/140_user_operation_atoz_guide.md`
- `docs/141_user_rehearsal_prompt_examples.md`
- `docs/142_user_guidance_integrated_review.md`
- `docs/143_user_quick_start.md`
- `docs/144_quick_start_rehearsal_boundary.md`
- `docs/145_user_guidance_closeout.md`
- `docs/146_next_manual_preview_or_rehearsal_decision.md`
- `docs/147_document_only_user_rehearsal_result.md`
- `docs/148_document_only_rehearsal_closeout.md`
- `docs/149_document_only_rehearsal_hold_state.md`
- `docs/48_git_push_timing_and_summary.md`
- `docs/150_manual_preview_resume_gate.md`
- `docs/151_manual_preview_resume_gate_closeout.md`
- `docs/152_project_result_artifact_map.md`
- `docs/153_project_result_artifact_map_review.md`
- `docs/154_user_visible_artifact_bundle_closeout.md`
- `docs/155_legacy_next_step_language_review.md`
- `docs/156_user_visible_artifact_security_and_git_check.md`
- `docs/157_current_status_progress_review.md`
- `checklists/manual_preview_resume_gate_checklist.md`
- `docs/84_hwpx_report_user_input_templates.md`
- `checklists/user_operation_atoz_rehearsal_checklist.md`
- `docs/101_phase2_repeat_operation_log_template.md`
- `docs/104_missing_fields_user_display_guidance.md`
- `CURRENT_STATUS.md`
- `README.md`
- `AGENTS.md`

## 생성 후보

- 필요 시 새 문서 생성 없이 검증 결과만 보고

## 확인 항목

1. 새 변경이 생기면 최종 보안 검색에 실제값 의심 패턴이 없는지
2. local HWPX template과 output이 Git 제외 상태인지
3. 실제 HWPX 수동 preview와 실제 운영 연동이 보류 항목으로 남는지
4. 사용자가 직접 확인해야 하는 HWPX 파일이 생겼는지
5. push가 필요한 의미 있는 묶음 또는 주요 방향 전환이 생겼는지

## 작업 제한

- 실제 기관 양식 사용 금지
- 실제 기관 HWPX/HWP 원본 Git 추가 금지
- 실제 HWPX output 재생성 금지
- 실제 Excel/한셀 파일 생성 금지
- 실제 표 데이터, 물품명, 수량, 금액, 대상 목록 기록 금지
- 실제 문서 원문 사용 금지
- 실제 개인정보 또는 내부 운영정보 사용 금지
- 실제 문서번호, 기관명, 담당자명, 수신자명 기록 금지
- Email/API/Make.com 연동 금지
- normalizer, renderer, fixture, routing 코드 변경 금지

## 완료 조건

- 현재 변경 묶음 최종 검증 상태 유지
- 기존 사용자 입력 안내 문서와 모순 없음
- 실제 구현물과 보류 항목 분리 유지
- output과 local HWPX 파일의 Git 제외 상태 유지 여부 확인
- 다음 추천 작업을 `tasks/NEXT_STEP.md`에 갱신

## 다음 단계 후보

추천 방향은 추가 문서 생성을 멈추고, push 필요 지점이나 사용자 HWPX 확인 지점이 생길 때까지 현재 기준을 유지하는 것입니다.

이 작업은 문서 산출물 중심이며, 실제 HWPX 파일 생성이나 외부 연동은 포함하지 않습니다.
