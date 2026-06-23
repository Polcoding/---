# ChatGPT 프로젝트 인수인계

## 저장소 상태 확인 결과

이 문서는 ChatGPT에서 진행하던 프로젝트를 Codex에서 이어가기 위한 인수인계 문서입니다.

작성 전 `AGENTS.md`, `README.md`, `docs/`, `examples/`, `checklists/`, `templates/`, `renderers/`의 현재 파일 상태를 확인했습니다.

확인 결과, 사용자가 제공한 인수인계 내용과 현재 저장소 상태 사이에 새 문서 생성을 중단해야 할 핵심 모순은 확인되지 않았습니다.

현재 `AGENTS.md`와 `README.md`는 로컬 PoC 렌더러가 이미 존재하는 저장소 상태를 반영하도록 갱신되었습니다. 이후 작업에서는 저장소의 실제 파일 상태와 최신 결과 문서를 우선 사실로 취급해야 합니다.

## 프로젝트 목표

공공기관 행정업무를 지원하는 AI 초안 생성 시스템을 구축합니다.

최우선 자동화 대상:

1. HWPX 원페이지 보고서
2. HWPX 추진계획서
3. HWPX 결과보고서
4. HWPX 검토보고서
5. XLSX 조사표
6. Email 초안

AI는 초안만 생성하며 실제 발송, 결재, 계약, 업체 선정, 예산 집행, 법률 판단은 사람이 수행합니다.

## 핵심 구현 방향

- 기존 HWP/HWPX 정형 양식의 복사본을 placeholder 템플릿으로 변환
- AI 출력 JSON을 HWPX/XLSX/Markdown/Email 렌더러가 처리
- 템플릿이 폰트, 자간, 줄간격, 표, 문단 배치를 담당
- AI는 내용과 구조를 담당
- 실제 원문, 개인정보, 기관정보는 저장소에 포함하지 않음
- output 산출물과 로컬 HWPX 템플릿은 Git에서 제외
- HWPX 보고서 안의 표는 현재 단계에서 표 틀과 배치만 검수하고, 표 내부 데이터 자동화는 향후 Excel/한셀 연동 후보로 분리
- 비식별 HWPX 작업 복사본이 없으면 실제 양식 수동 preview 결과를 임의로 만들지 않고 보류

## 문체 정책

- HWPX 보고서: 개조식, 짧은 문장, 명사형, 불필요한 조사 최소화
- 공문: 공문체, 번호체계와 붙임 형식 유지
- Email: 지나치게 딱딱한 공문체가 아닌 정중한 실무 메일체
- 협조 요청 공문과 협조 요청 메일의 문체를 구분
- 확인되지 않은 값은 `[확인 필요]` 또는 `null`
- 예산, 일정, 실적, 담당자, 수량 임의 생성 금지

## 보안 원칙

- 실제 공문 원문 외부 AI 입력 금지
- 실제 개인정보, 민원정보, 차량번호, 내부 운영정보 사용 금지
- 실제 기관 HWPX 양식 원본 Git 추가 금지
- A/B등급만 비식별 샘플 후보
- C등급은 내부 참고만 가능
- D등급은 외부 처리 금지
- 판단이 애매하면 더 보수적으로 분류

## 현재까지 완료한 주요 작업

- Custom GPT v0.1 Instructions 및 수동 테스트
- 보안등급 A/B/C/D 기준
- 비식별 샘플 작성 기준
- 문서 패턴 라이브러리
- 서식 명세표
- AI 출력 JSON 스키마
- XLSX 렌더러 PoC
- Markdown 미리보기 렌더러 PoC
- Email 초안 렌더러 PoC
- HWPX placeholder 치환 렌더러 PoC
- HWPX 공문 템플릿 실제 치환 성공
- 원페이지 보고서 HWPX 로컬 placeholder 템플릿 실제 치환 성공
- HWPX 본문 문단 분리와 번호체계 개선
- HWPX 기관 표준 서식값 확인 구조
- 보고서 중심 자동화 우선순위 재정렬
- `one_page_report`, `project_plan`, `result_report`, `review_report` 샘플 JSON 세트
- `result_report`, `review_report` HWPX 렌더러 입력 지원 확인

## HWPX에서 확인된 사항

- placeholder 기반 로컬 HWPX 템플릿 치환 성공
- `remaining_placeholders` 0 확인
- 문단별 placeholder 적용 후 본문 문단 분리 정상
- 하위 항목 표시 정상
- 글자 겹침 문제 개선
- 붙임 표시 정상
- 원페이지 보고서 `remaining_placeholders` 0 확인
- 원페이지 보고서 `보고 개요` 겹침 문제는 치환값 축소로 개선
- 실제 기관 표준 글꼴, 자간, 줄간격, 문단 간격 값은 아직 확인 필요

## 현재 핵심 상태

현재 저장소 기준으로 원페이지 보고서, 추진계획서, 결과보고서, 검토보고서 4종의 로컬 placeholder HWPX 템플릿 치환과 한컴 수동 열람 검수는 완료되었습니다.

저장소 코드 및 문서 기준 최신 상태:

- HWPX 보고서 4종 전용 placeholder map 또는 문서 유형별 처리 흐름이 `renderers/hwpx_renderer/template_package.py`에 반영됨
- `renderers/hwpx_renderer/render_hwpx_poc.py`에서 4종 샘플과 템플릿 후보를 함께 관리함
- `hwpx_render_summary.json` 기준 HWPX 보고서 4종과 공문 샘플은 모두 `rendered`, `remaining_placeholders` 0
- 로컬 HWPX 템플릿과 output HWPX는 Git 제외 상태임
- 실제 기관 양식 원본, 실제 원문, 실제 개인정보는 저장소에 추가하지 않음
- Phase 1 완료 기준과 Phase 2 진입 조건은 `docs/59_phase1_completion_and_phase2_entry_criteria.md`에 정리됨
- HWPX 보고서 4종 입력 요구사항은 `docs/60_hwpx_report_input_requirements.md`에 정리됨
- 입력 정규화 스키마 초안은 `docs/61_input_normalization_schema.md`에 정리됨
- 보안 필터 요구사항은 `docs/62_security_filter_requirements.md`에 정리됨
- 입력 정규화, 보안 필터, HWPX payload mapper, payload validation, renderer dry-run 최소 PoC가 `normalizers/`에 있음
- mapped HWPX 보고서 4종은 로컬 output으로 렌더링 및 수동 검수 완료 상태임
- Phase 2 최소 운영 흐름은 `docs/82_phase2_minimal_operation_flow.md`에 정리됨
- 사용자 입력 템플릿은 `docs/84_hwpx_report_user_input_templates.md`에 정리됨
- `placeholder_confirmed_values` 설계와 충돌 규칙, 코드 도입 여부는 `docs/87`~`docs/89`에 정리됨
- Phase 3 외부 연동 보류 기준과 no-send dry-run 기준은 `docs/115`~`docs/122`에 정리됨
- Phase 4 문서 템플릿 안정화 진입 판단은 `docs/123_phase4_template_stabilization_entry_judgment.md`에 정리됨
- 프로젝트 방향 재확인과 구형 문서 업데이트 기준은 `docs/124_project_direction_and_legacy_update_review.md`에 정리됨
- HWPX 보고서 4종 template manifest와 공통 placeholder 정합성은 `docs/125_hwpx_template_manifest_placeholder_consistency_review.md`에 정리됨
- style profile `[확인 필요]` 값 유지 기준과 서식값 수집 체크리스트는 `docs/126_style_profile_confirmation_value_collection_criteria.md`에 정리됨
- HWPX 보고서 4종 수동 preview 서식 gap log 기준은 `docs/127_hwpx_manual_preview_gap_log_criteria.md`에 정리됨
- 저장소 밖 실제 양식 후보 수동 절차와 보류 조건은 `docs/128_external_hwpx_candidate_manual_procedure_and_hold_criteria.md`에 정리됨
- local template policy와 Git 제외 상태 반복 검증 기준은 `docs/129_local_template_gitignore_repeat_verification_criteria.md`에 정리됨
- Phase 4 문서 템플릿 안정화 통합 점검은 `docs/130_phase4_template_stabilization_integrated_review.md`에 정리됨
- 실제 양식 수동 리허설 사용자 확인 패킷과 gap log 빈 양식은 `docs/131_actual_hwpx_manual_rehearsal_user_confirmation_packet.md`에 정리됨
- 실제 양식 수동 리허설 전 사용자 준비 확인 기록은 `docs/132_actual_hwpx_manual_rehearsal_readiness_confirmation.md`에 정리됨
- HWPX 일원화 유지와 표 데이터 Excel/한셀 연동 후보 분리 결정은 `docs/133_hwpx_only_table_frame_decision.md`에 정리됨
- 후속 비식별 HWPX 작업 복사본 없음에 따른 수동 리허설 보류 기록은 `docs/134_actual_hwpx_manual_rehearsal_no_copy_hold.md`에 정리됨
- HWPX 보고서와 Excel/한셀 표 데이터 역할 분리 범위는 `docs/135_hwp_report_and_hancell_table_data_scope.md`에 정리됨
- HWPX 보고서 사용자 입력 템플릿의 표 데이터 후보 표시 기준은 `docs/136_table_data_candidate_user_input_display_criteria.md`에 정리됨
- 보고서 샘플 JSON 4종의 표 데이터 후보 직접 반영 보류 결정은 `docs/137_report_sample_json_table_data_candidate_review.md`에 정리됨
- renderer와 normalizer 안내 문서의 표 데이터 후보 오해 가능성 점검은 `docs/138_renderer_normalizer_table_data_candidate_scope_review.md`에 정리됨
- 최소 demo 실행 결과 요약은 `docs/139_minimum_demo_run_result.md`에 정리됨
- 사용자 운영 A-to-Z 안내는 `docs/140_user_operation_atoz_guide.md`에 정리됨
- 문서 유형별 비식별 요청 예시는 `docs/141_user_rehearsal_prompt_examples.md`에 정리됨
- 사용자 안내 3종 통합 점검은 `docs/142_user_guidance_integrated_review.md`에 정리됨
- 사용자 quick start는 `docs/143_user_quick_start.md`에 정리됨
- quick start 리허설 경계는 `docs/144_quick_start_rehearsal_boundary.md`에 정리됨
- 사용자 안내 묶음 closeout은 `docs/145_user_guidance_closeout.md`에 정리됨
- 수동 preview 또는 리허설 유지 판단은 `docs/146_next_manual_preview_or_rehearsal_decision.md`에 정리됨
- 문서 기반 사용자 리허설 결과는 `docs/147_document_only_user_rehearsal_result.md`에 정리됨
- 문서 기반 리허설 closeout은 `docs/148_document_only_rehearsal_closeout.md`에 정리됨
- 문서 기반 리허설 hold 상태는 `docs/149_document_only_rehearsal_hold_state.md`에 정리됨
- 수동 preview 재개 게이트는 `docs/150_manual_preview_resume_gate.md`에 정리됨
- 수동 preview 재개 게이트 closeout은 `docs/151_manual_preview_resume_gate_closeout.md`에 정리됨
- 현재 확인 가능한 결과물 지도는 `docs/152_project_result_artifact_map.md`에 정리됨
- 결과물 지도와 주요 진입점 정합성 점검은 `docs/153_project_result_artifact_map_review.md`에 정리됨
- 사용자 가시 산출물 묶음 closeout은 `docs/154_user_visible_artifact_bundle_closeout.md`에 정리됨
- 구형 다음 단계 문구 점검은 `docs/155_legacy_next_step_language_review.md`에 정리됨
- 사용자 가시 산출물 보안ㆍGit 제외 검증은 `docs/156_user_visible_artifact_security_and_git_check.md`에 정리됨
- 현황판 진행률 점검은 `docs/157_current_status_progress_review.md`에 정리됨
- 사용자 운영 A-to-Z 리허설 체크리스트는 `checklists/user_operation_atoz_rehearsal_checklist.md`에 정리됨
- 수동 preview 재개 게이트 체크리스트는 `checklists/manual_preview_resume_gate_checklist.md`에 정리됨
- 현재 상태판은 `CURRENT_STATUS.md`를 우선 확인함
- 반복 운영 로그 템플릿은 `docs/101_phase2_repeat_operation_log_template.md`에 정리됨
- missing_fields 사용자 표시 기준은 `docs/104_missing_fields_user_display_guidance.md`에 정리됨

현재 사용자 안내 기준:

- `[사용자 확인 필요]`: 사람이 직접 판단하거나 확인해야 하는 값
- `[Codex 처리 가능]`: 비식별 placeholder 입력을 바탕으로 구조화 가능한 항목
- `[보류]`: 현재 단계에서 자동화하지 않는 항목

다음 단계는 API/Make.com 연동이 아니라, 현재 검증 상태를 유지하면서 사용자가 저장소 밖 비식별 HWPX 작업 복사본을 준비했다고 명시할 때만 수동 preview 재개 조건을 확인하는 것입니다.

실제 양식 수동 리허설 상태를 판단할 때는 과거 준비 확인 기록보다 후속 보류 기록인 `docs/134_actual_hwpx_manual_rehearsal_no_copy_hold.md`와 재개 게이트인 `docs/150_manual_preview_resume_gate.md`를 우선합니다.

최신 작업 순서는 `tasks/NEXT_STEP.md`, `CURRENT_STATUS.md`, `docs/152_project_result_artifact_map.md`를 우선합니다.

이미 추가된 read-only helper는 `missing_fields` 생성 결과와 routing 결과를 즉시 바꾸지 않습니다.

작업 운영 기준은 작은 확인마다 멈추지 않고, 파일 또는 폴더 삭제처럼 되돌리기 어려운 작업 외에는 Codex가 저장소 범위 안에서 계속 진행하는 것입니다. commit/push는 여러 관련 수정과 검증을 한 번에 묶는 기준을 우선하며, 아직 push할 기준점이 없으면 보고만 하고 멈추지 않고 다음 추천 작업을 계속 진행합니다.

## 향후 참고자료

사용자가 추후 "공문서 작성 요령" PDF를 제공할 예정입니다.

반영 원칙:

- PDF 원문을 그대로 저장하거나 학습시키지 않음
- 작성 원칙, 권장 표현, 지양 표현, 번호체계, 예시 구조만 패턴화
- 보고서체, 공문체, 이메일체를 구분
- 민감정보 또는 비공개 정보가 있으면 외부 처리 제외

## 이어서 작업할 때 우선 확인할 파일

- `AGENTS.md`
- `README.md`
- `docs/43_report_template_automation_priority.md`
- `docs/44_report_sample_json_set.md`
- `docs/45_one_page_report_hwpx_template_strategy.md`
- `docs/46_one_page_report_hwpx_render_test_result.md`
- `docs/47_result_review_report_hwpx_support_check.md`
- `docs/57_hwpx_report_4types_completion_and_safety_rehearsal.md`
- `docs/59_phase1_completion_and_phase2_entry_criteria.md`
- `docs/60_hwpx_report_input_requirements.md`
- `docs/61_input_normalization_schema.md`
- `docs/82_phase2_minimal_operation_flow.md`
- `docs/84_hwpx_report_user_input_templates.md`
- `docs/87_placeholder_confirmed_values_design_review.md`
- `docs/88_placeholder_pattern_collision_rules.md`
- `docs/89_placeholder_confirmed_values_code_adoption_decision.md`
- `docs/90_project_reorganization_after_superpowers.md`
- `docs/123_phase4_template_stabilization_entry_judgment.md`
- `docs/124_project_direction_and_legacy_update_review.md`
- `docs/125_hwpx_template_manifest_placeholder_consistency_review.md`
- `docs/126_style_profile_confirmation_value_collection_criteria.md`
- `docs/127_hwpx_manual_preview_gap_log_criteria.md`
- `docs/128_external_hwpx_candidate_manual_procedure_and_hold_criteria.md`
- `docs/129_local_template_gitignore_repeat_verification_criteria.md`
- `docs/130_phase4_template_stabilization_integrated_review.md`
- `docs/131_actual_hwpx_manual_rehearsal_user_confirmation_packet.md`
- `docs/132_actual_hwpx_manual_rehearsal_readiness_confirmation.md`
- `docs/133_hwpx_only_table_frame_decision.md`
- `docs/134_actual_hwpx_manual_rehearsal_no_copy_hold.md`
- `docs/135_hwp_report_and_hancell_table_data_scope.md`
- `docs/136_table_data_candidate_user_input_display_criteria.md`
- `docs/137_report_sample_json_table_data_candidate_review.md`
- `docs/138_renderer_normalizer_table_data_candidate_scope_review.md`
- `docs/139_minimum_demo_run_result.md`
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
- `docs/150_manual_preview_resume_gate.md`
- `docs/151_manual_preview_resume_gate_closeout.md`
- `docs/152_project_result_artifact_map.md`
- `docs/153_project_result_artifact_map_review.md`
- `docs/154_user_visible_artifact_bundle_closeout.md`
- `docs/155_legacy_next_step_language_review.md`
- `docs/156_user_visible_artifact_security_and_git_check.md`
- `docs/157_current_status_progress_review.md`
- `CURRENT_STATUS.md`
- `docs/101_phase2_repeat_operation_log_template.md`
- `docs/104_missing_fields_user_display_guidance.md`
- `tasks/NEXT_STEP.md`
- `examples/json/sample_one_page_report.json`
- `examples/json/sample_project_plan.json`
- `examples/json/sample_result_report.json`
- `examples/json/sample_review_report.json`
- `renderers/hwpx_renderer/render_hwpx_poc.py`
- `renderers/hwpx_renderer/template_package.py`
- `templates/hwpx/local_template_policy.md`
- `checklists/one_page_report_hwpx_template_checklist.md`
- `checklists/external_hwpx_candidate_manual_procedure_checklist.md`
- `checklists/user_operation_atoz_rehearsal_checklist.md`
- `checklists/manual_preview_resume_gate_checklist.md`
- `checklists/local_template_gitignore_repeat_verification_checklist.md`
