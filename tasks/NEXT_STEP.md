# 다음 작업

## 목표

`placeholder_confirmed_values` 코드 도입 여부를 재검토합니다.

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
- HWPX 보고서 4종별 사용자 입력 템플릿 문서화 완료
- `normalizers/` fixture 확장 후보 검토 완료
- `missing_fields` 생성 규칙 개선 여부 검토 완료
- `placeholder_confirmed_values` 도입 여부 검토 완료
- placeholder 형식 판정 기준과 실제값 의심 패턴 충돌 처리 규칙 문서화 완료

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
- `docs/84_hwpx_report_user_input_templates.md`
- `checklists/hwpx_report_user_input_templates_checklist.md`
- `docs/85_normalizers_fixture_expansion_review.md`
- `checklists/normalizers_fixture_expansion_review_checklist.md`
- `docs/86_missing_fields_rule_improvement_review.md`
- `checklists/missing_fields_rule_improvement_review_checklist.md`
- `docs/87_placeholder_confirmed_values_design_review.md`
- `checklists/placeholder_confirmed_values_design_review_checklist.md`
- `docs/88_placeholder_pattern_collision_rules.md`
- `checklists/placeholder_pattern_collision_rules_checklist.md`
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

1. 문서 기준만으로 충분한지, 코드 도입이 필요한지
2. 도입한다면 placeholder 판정 함수를 어디에 둘지
3. 도입한다면 `missing_fields` 생성 규칙을 어느 범위까지 바꿀지
4. 신규 fixture를 추가할지
5. 기존 fixture 6종 회귀 테스트가 깨지지 않는지
6. 실제 원문이나 실제 승인정보 없이 진행되는지

## 작업 제한

- 실제 기관 양식 사용 금지
- 실제 문서 원문 사용 금지
- 실제 개인정보 또는 내부 운영정보 사용 금지
- 실제 HWPX 템플릿 Git 추가 금지
- Email/API/Make.com 연동 금지
- 확인되지 않은 서식값 임의 생성 금지

## 완료 조건

- 코드 도입 여부 판단
- 도입 시 최소 구현 범위 정의
- 미도입 시 문서 기준 유지 사유 정리
- HWPX 4종 우선 흐름 유지
- 실제 원본 미사용 확인
- 다음 단계 진행 여부 판단

## 다음 단계 후보

현재 추천은 `docs/87`과 `docs/88` 기준으로 `placeholder_confirmed_values`를 코드에 도입할지 재검토하는 것입니다.
