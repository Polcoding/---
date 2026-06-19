# 다음 작업

## 목표

문서 유형별 사용자 입력 템플릿을 정리합니다.

## 현재 완료 상태

- `one_page_report`: 로컬 placeholder 치환 및 수동 검수 완료
- `project_plan`: 로컬 placeholder 치환 및 수동 검수 완료
- `result_report`: 로컬 placeholder 치환 및 수동 검수 완료
- `review_report`: 로컬 placeholder 치환 및 수동 검수 완료
- HWPX 보고서 4종 완료 상태 및 안전 리허설 문서화 완료
- 저장소 밖 HWPX placeholder 변환 절차 문서화 완료
- Phase 1 완료 기준 및 Phase 2 진입 조건 문서화 완료
- HWPX 보고서 4종 입력 요구사항 문서화 완료
- 입력 정규화 스키마 초안 문서화 완료
- Phase 2 보안 필터 요구사항 문서화 완료
- 입력 정규화 테스트 케이스 문서화 완료
- HWPX 보고서 4종별 정규화 예시 문서화 완료
- 입력 정규화 최소 구현 범위 문서화 완료
- `normalizers/` 최소 PoC 골격 작성 완료
- 입력 정규화 PoC fixture 5종 통과
- 정규화 결과와 HWPX 렌더러 입력 JSON 매핑 범위 문서화 완료
- HWPX payload mapper PoC fixture 5종 통과
- HWPX payload validation PoC fixture 5종 통과
- HWPX 렌더러 연결 dry-run 범위 문서화 완료
- HWPX 렌더러 연결 dry-run PoC 스크립트 작성 완료
- HWPX 렌더러 연결 dry-run PoC fixture 5종 통과
- dry-run 결과 보관 정책 문서화 완료
- 실제 HWPX 렌더링 연결 여부 문서화 완료
- mapped one_page_report HWPX 1건 렌더링 완료
- `remaining_placeholders` 0 확인
- mapped project_plan HWPX 1건 렌더링 완료
- mapped project_plan `remaining_placeholders` 0 확인
- mapped result_report HWPX 1건 렌더링 완료
- mapped result_report `remaining_placeholders` 0 확인
- mapped review_report 렌더링 정책 문서화 완료
- approved review_report fixture 추가 완료
- approved review_report validation 및 dry-run 통과
- approved review_report HWPX 1건 렌더링 완료
- approved review_report `remaining_placeholders` 0 확인
- approved review_report 한컴 수동 검수 완료
- HWPX 4종 mapped 렌더링 한컴 수동 검수 완료
- HWPX 4종 mapped 렌더링 완료 상태 통합 문서화 완료
- normalizers 회귀 테스트 묶음 문서화 완료
- Phase 2 최소 운영 흐름 문서화 완료
- 사용자 입력 체크리스트와 운영 전 수동 점검표 문서화 완료

## 확인 대상

- `docs/59_phase1_completion_and_phase2_entry_criteria.md`
- `docs/60_hwpx_report_input_requirements.md`
- `checklists/hwpx_report_input_requirements_checklist.md`
- `docs/61_input_normalization_schema.md`
- `checklists/input_normalization_schema_checklist.md`
- `docs/62_security_filter_requirements.md`
- `checklists/security_filter_requirements_checklist.md`
- `docs/63_input_normalization_test_cases.md`
- `checklists/input_normalization_test_cases_checklist.md`
- `docs/64_hwpx_report_normalized_input_examples.md`
- `checklists/hwpx_report_normalized_input_examples_checklist.md`
- `docs/65_input_normalization_minimal_poc_scope.md`
- `checklists/input_normalization_minimal_poc_scope_checklist.md`
- `docs/66_input_normalization_poc_result.md`
- `checklists/input_normalization_poc_result_checklist.md`
- `docs/67_normalized_to_hwpx_payload_mapping_scope.md`
- `checklists/normalized_to_hwpx_payload_mapping_scope_checklist.md`
- `docs/68_hwpx_payload_mapper_poc_result.md`
- `checklists/hwpx_payload_mapper_poc_result_checklist.md`
- `docs/69_hwpx_payload_validation_poc_result.md`
- `checklists/hwpx_payload_validation_poc_result_checklist.md`
- `docs/70_hwpx_renderer_dry_run_scope.md`
- `checklists/hwpx_renderer_dry_run_scope_checklist.md`
- `docs/71_hwpx_renderer_dry_run_result.md`
- `checklists/hwpx_renderer_dry_run_result_checklist.md`
- `docs/72_dry_run_artifact_retention_policy.md`
- `checklists/dry_run_artifact_retention_policy_checklist.md`
- `docs/73_hwpx_render_connection_decision.md`
- `checklists/hwpx_render_connection_decision_checklist.md`
- `docs/74_mapped_one_page_hwpx_render_result.md`
- `checklists/mapped_one_page_hwpx_render_result_checklist.md`
- `renderers/hwpx_renderer/output/mapped_safe_one_page_report_poc.hwpx`
- `docs/75_mapped_project_plan_hwpx_render_result.md`
- `checklists/mapped_project_plan_hwpx_render_result_checklist.md`
- `renderers/hwpx_renderer/output/mapped_missing_project_plan_poc.hwpx`
- `docs/76_mapped_result_report_hwpx_render_result.md`
- `checklists/mapped_result_report_hwpx_render_result_checklist.md`
- `renderers/hwpx_renderer/output/mapped_missing_result_report_poc.hwpx`
- `docs/77_mapped_review_report_render_policy.md`
- `checklists/mapped_review_report_render_policy_checklist.md`
- `docs/78_approved_review_report_dry_run_result.md`
- `checklists/approved_review_report_dry_run_result_checklist.md`
- `docs/79_mapped_review_report_hwpx_render_result.md`
- `checklists/mapped_review_report_hwpx_render_result_checklist.md`
- `docs/80_mapped_hwpx_4types_completion_summary.md`
- `checklists/mapped_hwpx_4types_completion_checklist.md`
- `docs/81_normalizers_regression_test_suite.md`
- `checklists/normalizers_regression_test_suite_checklist.md`
- `docs/82_phase2_minimal_operation_flow.md`
- `checklists/phase2_minimal_operation_flow_checklist.md`
- `docs/83_phase2_user_input_and_manual_operation_checkpoints.md`
- `checklists/phase2_user_input_and_manual_operation_checklist.md`
- `renderers/hwpx_renderer/output/mapped_approved_review_report_poc.hwpx`
- `normalizers/fixtures/approved_review_report_request.json`
- `normalizers/README.md`
- `normalizers/input_normalizer_poc.py`
- `normalizers/security_filter_poc.py`
- `normalizers/hwpx_payload_mapper_poc.py`
- `normalizers/validate_hwpx_payload_poc.py`
- `normalizers/hwpx_renderer_dry_run_poc.py`
- `normalizers/fixtures/`
- `renderers/hwpx_renderer/validation.py`
- `docs/58_external_hwpx_placeholder_conversion_runbook.md`
- `checklists/external_hwpx_placeholder_conversion_checklist.md`
- `docs/57_hwpx_report_4types_completion_and_safety_rehearsal.md`
- `docs/18_ai_output_json_schema.md`
- `examples/json/sample_one_page_report.json`
- `examples/json/sample_project_plan.json`
- `examples/json/sample_result_report.json`
- `examples/json/sample_review_report.json`

## 확인 항목

1. HWPX 보고서 4종별 사용자 입력 템플릿이 있는지
2. 각 템플릿이 실제값 대신 placeholder와 `[확인 필요]`를 사용하도록 되어 있는지
3. `review_report` 템플릿에 보안 검토 조건이 반영되는지
4. 자동 발송, 결재, 계약, 예산 집행 금지 문구가 유지되는지
5. 실제 원문이나 실제 승인정보 없이 진행되는지

## 작업 제한

- 실제 기관 양식 사용 금지
- 실제 문서 원문 사용 금지
- 실제 개인정보 또는 내부 운영정보 사용 금지
- 실제 HWPX 템플릿 Git 추가 금지
- Email/API/Make.com 연동 금지
- 확인되지 않은 서식값 임의 생성 금지

## 완료 조건

- HWPX 보고서 4종별 입력 템플릿 문서화
- placeholder 기반 입력 예시 정리
- 금지 입력 예시 정리
- HWPX 4종 우선 흐름 유지
- 실제 원본 미사용 확인
- 다음 단계 진행 여부 판단

## 다음 단계 후보

현재 추천은 `one_page_report`, `project_plan`, `result_report`, `review_report`별 사용자 입력 템플릿을 placeholder 기반으로 정리하는 것입니다.
