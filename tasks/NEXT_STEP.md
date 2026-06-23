# 다음 작업

## 현재 상태

사용자 운영 A-to-Z 안내 문서, 리허설 체크리스트, 문서 유형별 비식별 요청 예시, 사용자 안내 3종 통합 점검 문서, 사용자 quick start, quick start 리허설 경계 문서, 사용자 안내 묶음 closeout 문서, 수동 preview 또는 리허설 유지 판단 문서, 문서 기반 사용자 리허설 결과 문서, 문서 기반 리허설 closeout 문서, 문서 기반 리허설 hold 상태 문서를 작성하고 주요 진입점 문서에 연결했습니다.

사용자 피드백에 따라 commit/push는 한 번에 묶습니다. 앞으로는 단일 closeout 또는 작은 문구 정리마다 멈추지 않고, 여러 관련 작업을 묶어서 검증한 뒤 commit/push 후보를 판단합니다.

Git 추적 대상에 남아 있던 Python 캐시 파일은 저장소 산출물이 아니므로 추적 해제하고, 루트 `.gitignore`에 `__pycache__/`와 `*.pyc` 제외 규칙을 추가한 상태입니다. 이 정리는 renderer나 normalizer 동작 변경이 아니라 Git 위생 정리입니다.

normalizers 회귀 테스트 기준은 `normalizers/README.md`와 `docs/109_normalizers_regression_recheck_result.md`에 맞춰 `validate_placeholder_confirmed_values_poc.py`를 실행 순서에 포함하도록 정리했습니다.

최근 검증 묶음에서 normalizers 회귀 스크립트 6개를 재실행했고, mapped HWPX PoC output과 summary output은 Git 제외 상태로 유지되는지 확인했습니다.

현재 사용자 진입점 문서에서는 실제 업무용 HWPX output과 ignored 로컬 PoC HWPX output이 혼동되지 않도록 표현을 정리했습니다.

README와 AGENTS의 현재 진행 위치 요약은 사용자 quick start, 문서 기반 hold, 결과물 지도, 보안ㆍGit 제외 검증, 현황판 진행률 점검까지 반영했습니다.

사용자 안내 문서와 수동 preview 관련 체크리스트에서도 실제 업무용 HWPX output, 로컬 output HWPX, Git 추적 대상 output 표현을 구분하도록 정리했습니다.

HWPX 템플릿 폴더 안내와 로컬 템플릿 보관 정책도 최신 사용자 안내, 결과물 지도, 보안ㆍGit 제외 검증 기준에 맞춰 정리했습니다.

`docs/00_chatgpt_handoff.md`, `docs/00_project_overview.md`, `AGENTS.md`의 현재 작업 축 표현은 결과물 지도ㆍ구형 문구 점검 완료 이후의 최신 상태에 맞춰, 검증 상태 유지와 수동 preview 재개 조건 대기 단계로 정리했습니다.

push 빈도 기준은 작은 확인마다 멈추지 않고, 같은 단계 안의 여러 소작업을 하나의 변경 묶음으로 모은 뒤 판단하는 방향으로 정리했습니다. 파일 또는 폴더 삭제처럼 되돌리기 어려운 작업 외에는 Codex가 계속 진행하고, commit/push는 한 번에 묶는 기준을 우선합니다.

push할 만한 기준점이 아직 없으면 최종 보고로 끊지 않고, 같은 변경 묶음 안에서 다음 추천 작업을 계속 진행합니다.

수동 preview 재개 게이트와 체크리스트를 추가하고 closeout까지 정리해, 사용자가 나중에 비식별 작업 복사본을 준비했다고 명시했을 때만 수동 preview로 넘어가도록 정리했습니다.

현재 사용자는 `docs/140_user_operation_atoz_guide.md`에서 직접 확인할 일, Codex가 처리할 일, 현재 보류할 일을 한 번에 볼 수 있습니다.

`docs/143_user_quick_start.md`에서는 처음 열 파일, 가장 짧은 진행 순서, 바로 멈출 지점을 1페이지로 볼 수 있습니다.

`docs/144_quick_start_rehearsal_boundary.md`에서는 문서만으로 가능한 확인과 HWPX 열람이 필요한 확인을 분리합니다.

`docs/145_user_guidance_closeout.md`에서는 사용자 안내 묶음이 문서 산출물로 정리되었는지 확인할 수 있습니다.

`docs/146_next_manual_preview_or_rehearsal_decision.md`에서는 현재는 실제 HWPX 수동 preview가 아니라 문서 기반 리허설 유지가 추천됨을 확인할 수 있습니다.

`docs/147_document_only_user_rehearsal_result.md`에서는 실제 HWPX 없이 quick start와 체크리스트를 따라간 결과를 확인할 수 있습니다.

`docs/148_document_only_rehearsal_closeout.md`에서는 문서 기반 리허설 묶음이 문서 산출물로 정리되었는지 확인할 수 있습니다.

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

결과물 지도와 사용자 가시 산출물 closeout에서도 `docs/141_user_rehearsal_prompt_examples.md`를 바로 볼 산출물로 연결했습니다.

GitHub Desktop Changes 관련 사용자 안내에서는 실제 HWPX 원본, 로컬 output HWPX, Git 추적 대상 output 파일을 구분하도록 표현을 정리했습니다.

최소 demo 결과, A-to-Z 안내, HWPX 로컬 템플릿 정책, HWPX renderer 안내에서도 output 보관 표현을 Git 추적 대상 기준으로 맞췄습니다.

실제 양식 수동 리허설 준비 확인 기록과 이후 비식별 작업 복사본 없음 보류 기록이 모순처럼 읽히지 않도록, 현재 기준은 `docs/134_actual_hwpx_manual_rehearsal_no_copy_hold.md`와 `docs/150_manual_preview_resume_gate.md`를 우선하도록 정리했습니다.

인수인계 문서와 프로젝트 개요에도 같은 우선순위를 반영해, 과거 준비 확인 기록보다 후속 보류 기록과 재개 게이트를 우선하도록 정리했습니다.

구형 다음 단계 문구 점검과 사용자 가시 산출물 보안ㆍGit 제외 검증 범위에도 `docs/132`와 `docs/134`의 준비 확인/후속 보류 관계를 추가했습니다.

구형 진입점 문서 중 "현재/최신 다음 단계"처럼 읽히는 문구는 `docs/134_actual_hwpx_manual_rehearsal_no_copy_hold.md`와 `docs/150_manual_preview_resume_gate.md` 우선 기준으로 보정했습니다.

`README.md`와 `CURRENT_STATUS.md`도 이 문서와 체크리스트를 현재 사용자 안내 진입점으로 연결합니다.

현재 공통 표시는 다음과 같습니다.

- `[사용자 확인 필요]`: 사람이 직접 판단하거나 확인해야 하는 값
- `[Codex 처리 가능]`: 비식별 placeholder 입력을 바탕으로 구조화 가능한 항목
- `[보류]`: 현재 단계에서 자동화하지 않는 항목

## 목표

불필요한 새 문서 생성을 늘리지 않되 기존 문서 정합성 보강과 검증은 계속 진행하고, 파일 또는 폴더 삭제, 실제 HWPX 수동 preview 재개, 실제 원본ㆍ개인정보 노출 가능성이 생길 때만 멈춥니다.

## 확인 대상

- `docs/140_user_operation_atoz_guide.md`
- `docs/139_minimum_demo_run_result.md`
- `docs/00_chatgpt_handoff.md`
- `docs/00_project_overview.md`
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
- `docs/81_normalizers_regression_test_suite.md`
- `checklists/normalizers_regression_test_suite_checklist.md`
- `docs/129_local_template_gitignore_repeat_verification_criteria.md`
- `docs/130_phase4_template_stabilization_integrated_review.md`
- `docs/150_manual_preview_resume_gate.md`
- `docs/151_manual_preview_resume_gate_closeout.md`
- `docs/152_project_result_artifact_map.md`
- `docs/153_project_result_artifact_map_review.md`
- `docs/154_user_visible_artifact_bundle_closeout.md`
- `docs/155_legacy_next_step_language_review.md`
- `docs/156_user_visible_artifact_security_and_git_check.md`
- `docs/157_current_status_progress_review.md`
- `checklists/manual_preview_resume_gate_checklist.md`
- `checklists/local_template_gitignore_repeat_verification_checklist.md`
- `templates/hwpx/README.md`
- `templates/hwpx/local_template_policy.md`
- `renderers/hwpx_renderer/README.md`
- `docs/84_hwpx_report_user_input_templates.md`
- `checklists/user_operation_atoz_rehearsal_checklist.md`
- `docs/101_phase2_repeat_operation_log_template.md`
- `docs/104_missing_fields_user_display_guidance.md`
- `CURRENT_STATUS.md`
- `README.md`
- `AGENTS.md`
- `.gitignore`

## 생성 후보

- 필요 시 새 문서 생성 없이 기존 검증 문서와 다음 작업 지시서만 보강

## 확인 항목

1. 새 변경이 생기면 최종 보안 검색에 실제값 의심 패턴이 없는지
2. local HWPX template과 output이 Git 제외 상태인지
3. Python 캐시 파일이 Git 추적 대상에서 제외되었는지
4. 실제 HWPX 수동 preview와 실제 운영 연동이 보류 항목으로 남는지
5. 사용자가 직접 확인해야 하는 HWPX 파일이 생겼는지
6. commit/push로 묶을 만한 의미 있는 변경 단위가 쌓였는지

## 작업 제한

- 실제 기관 양식 사용 금지
- 실제 기관 HWPX/HWP 원본 Git 추가 금지
- 실제 업무용 HWPX output 생성 금지
- 실제 Excel/한셀 파일 생성 금지
- 실제 표 데이터, 물품명, 수량, 금액, 대상 목록 기록 금지
- 실제 문서 원문 사용 금지
- 실제 개인정보 또는 내부 운영정보 사용 금지
- 실제 문서번호, 기관명, 담당자명, 수신자명 기록 금지
- Email/API/Make.com 연동 금지
- normalizer, renderer, fixture, routing 코드 변경 금지

## 완료 조건

- 현재 변경 묶음의 보안ㆍGit 제외 검증 상태 유지
- 기존 사용자 입력 안내 문서와 모순 없음
- 실제 구현물과 보류 항목 분리 유지
- output과 local HWPX 파일의 Git 제외 상태 유지 여부 확인
- Python 캐시 파일의 Git 제외 상태 확인
- 다음 추천 작업을 `tasks/NEXT_STEP.md`에 갱신

## 다음 단계 후보

추천 방향은 불필요한 새 문서 생성을 늘리지 않되, 기존 문서 정합성 보강과 검증은 계속 진행하는 것입니다. 파일 또는 폴더 삭제, 실제 HWPX 수동 확인, 실제 원본ㆍ개인정보 노출 가능성이 생길 때만 사용자 확인 지점으로 분리합니다.

이 작업은 문서 산출물 중심이며, 실제 업무용 HWPX 파일 생성이나 외부 연동은 포함하지 않습니다. 필요 시 로컬 PoC 렌더링은 ignored output 상태 검증과 함께만 수행합니다.
