# 다음 작업

## 목표

HWPX 렌더러 연결 dry-run 범위를 결정합니다.

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
- `normalizers/README.md`
- `normalizers/input_normalizer_poc.py`
- `normalizers/security_filter_poc.py`
- `normalizers/hwpx_payload_mapper_poc.py`
- `normalizers/validate_hwpx_payload_poc.py`
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

1. mapper payload를 기존 HWPX 렌더러에 직접 넘길지
2. dry-run에서 실제 HWPX 파일을 생성할지, validation까지만 할지
3. `needs_more_input` payload도 HWPX 생성 대상으로 둘지
4. `needs_security_review`와 `blocked`는 계속 미생성/미렌더링으로 둘지
5. output HWPX와 summary JSON이 Git 제외 상태인지
6. 실제 원문이나 실제 식별값 없이 dry-run할 수 있는지

## 작업 제한

- 실제 기관 양식 사용 금지
- 실제 문서 원문 사용 금지
- 실제 개인정보 또는 내부 운영정보 사용 금지
- 실제 HWPX 템플릿 Git 추가 금지
- Email/API/Make.com 연동 금지
- 확인되지 않은 서식값 임의 생성 금지

## 완료 조건

- HWPX 렌더러 연결 dry-run 범위 문서화
- 실제 HWPX 생성 여부 판단
- `needs_more_input` payload 렌더링 허용 여부 판단
- 미렌더링 라우팅 기준 재확인
- output 산출물 Git 제외 확인
- 실제 원본 미사용 확인
- 다음 단계 진행 여부 판단

## 다음 단계 후보

현재 추천은 실제 HWPX 파일 생성으로 바로 연결하지 말고, dry-run 범위를 먼저 문서화한 뒤 허용된 케이스만 별도 테스트하는 것입니다.
