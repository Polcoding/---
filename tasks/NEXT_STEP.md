# 다음 작업

## 목표

입력 정규화 로직의 최소 구현 범위를 결정합니다.

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
- `docs/58_external_hwpx_placeholder_conversion_runbook.md`
- `checklists/external_hwpx_placeholder_conversion_checklist.md`
- `docs/57_hwpx_report_4types_completion_and_safety_rehearsal.md`
- `docs/18_ai_output_json_schema.md`
- `examples/json/sample_one_page_report.json`
- `examples/json/sample_project_plan.json`
- `examples/json/sample_result_report.json`
- `examples/json/sample_review_report.json`

## 확인 항목

1. 입력 정규화 로직을 문서 기준으로만 둘지 코드 PoC로 만들지
2. 코드 PoC를 만든다면 대상 범위를 HWPX 보고서 4종으로 제한할지
3. 테스트 fixture를 문서 예시에서 분리해 JSON 파일로 둘지
4. 보안 필터를 정규화 로직 안에 둘지 별도 단계로 둘지
5. blocked/needs_security_review 케이스를 코드 테스트에 포함할지
6. 실제 원문이나 실제 식별값 없이 구현할 수 있는지

## 작업 제한

- 실제 기관 양식 사용 금지
- 실제 문서 원문 사용 금지
- 실제 개인정보 또는 내부 운영정보 사용 금지
- 실제 HWPX 템플릿 Git 추가 금지
- Email/API/Make.com 연동 금지
- 확인되지 않은 서식값 임의 생성 금지

## 완료 조건

- 입력 정규화 최소 구현 범위 문서화
- 코드 PoC 여부 판단
- fixture 위치와 Git 포함 여부 판단
- 보안 필터와 정규화 로직의 경계 판단
- 실제 원본 미사용 확인
- 다음 단계 진행 여부 판단

## 다음 단계 후보

현재 추천은 입력 정규화 로직을 곧바로 크게 구현하지 말고, HWPX 보고서 4종에 한정한 최소 PoC 범위를 먼저 문서로 확정하는 것입니다.
