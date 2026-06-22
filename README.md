# 공공기관 행정문서 AI 자동화 시스템

## 프로젝트 한 줄 정의

비식별화된 업무 지시를 받아 공공기관 행정문서 초안을 만들고, 사람이 최종 검토ㆍ수정ㆍ승인하는 행정 비서형 AI 시스템의 Phase 1 완료 및 Phase 2 최소 PoC 준비 저장소입니다.

## 이번 저장소의 목적

이 저장소는 실제 업무 자동화 운영물이 아닙니다. 안전한 Custom GPT 테스트판, placeholder 기반 샘플 JSON, 로컬 PoC 렌더러, 입력 정규화 PoC, 테스트 결과 문서, 보안 기준을 정리합니다.

핵심 메시지는 다음과 같습니다.

> 이 프로젝트는 AI가 공문을 마음대로 작성하는 시스템이 아니라, 비식별 업무 지시를 받아 공공기관 행정문서 초안을 만들고 사람이 최종 승인하는 시스템입니다.

## 현재 저장소에서 하는 일

- Custom GPT에 붙여넣을 Instructions v0.1 작성
- GPT 이름, 설명, 대화 시작 문구 정리
- 처리 가능 업무와 처리 금지 업무 기준 정리
- 개인정보와 민감정보 비식별화 규칙 정리
- 테스트용 업무 지시 샘플과 모범 출력 예시 작성
- 테스트 결과 평가표 작성
- placeholder 기반 HWPX/XLSX/Markdown/Email 로컬 PoC 렌더러 검증
- HWPX 보고서 템플릿 자동화 우선순위 검증
- HWPX 보고서 4종 placeholder 템플릿 치환 및 한컴 수동 검수
- 비식별 입력 정규화, 보안 필터, HWPX payload 매핑, renderer dry-run 최소 PoC 검증
- Phase 2 최소 운영 흐름과 사용자 입력 템플릿 정리
- 향후 Make.com 또는 OpenAI API 연동 전 점검할 항목 정리

## 현재 자동화 우선순위

이 저장소의 최우선 자동화 대상은 Email이 아니라 HWPX 기반 보고서 템플릿입니다.

우선순위는 다음과 같이 관리합니다.

| 우선순위 | 대상 | 출력 형식 | 비고 |
|---|---|---|---|
| 1 | 원페이지 보고서 | HWPX | 최우선 자동화 대상 |
| 2 | 추진계획서 | HWPX | 핵심 계획 문서 |
| 3 | 결과보고서 | HWPX | 기존 계획 대비 결과 정리 |
| 4 | 검토보고서 | HWPX | 내부 검토자료 |
| 5 | 조사표 | XLSX | 보조 자동화 대상 |
| 6 | 협조 요청 메일 | Email | 보조 초안 작성, 정중한 실무 메일체 |

결과보고서는 가능한 경우 기존 추진계획서의 추진개요, 세부계획, 일정, 예산, 기대효과 항목과 대응되도록 정리합니다.

협조 요청 메일은 공문체가 아니라 정중한 실무 메일체로 작성하며, 실제 자동 발송이 아니라 사람이 검토하는 초안으로만 관리합니다.

## 현재 진행 위치

- Phase 1 문서화와 placeholder 기반 HWPX 보고서 4종 검증은 완료된 상태입니다.
- 현재는 Phase 2 최소 PoC 단계입니다.
- Phase 2는 API, Make.com, Email 자동화가 아니라 비식별 입력 정규화, 보안 필터, HWPX payload 매핑, dry-run, 한컴 수동 검토 흐름을 다듬는 단계입니다.
- 다음 검토 후보는 `placeholder_confirmed_values` fixture schema 확장 여부입니다.

## 1단계에서 하지 않는 일

- 실제 이메일 발송 자동화
- Make.com, Gmail, Outlook, OpenAI API 실제 연동 코드 작성
- 실제 공공기관 원문 문서 업로드 또는 학습
- 실제 개인정보, 민감정보, 내부자료, 대외비 자료 사용
- 결재, 계약, 업체 선정, 예산 집행, 법률 판단, 민원 처리 결론 자동화
- 실제 기관 양식 원본 기반 문서 서식 렌더링 엔진 구현

## 전체 시스템 아키텍처 개요

```text
사용자 입력
→ 입력 정규화
→ 보안ㆍ개인정보 필터
→ 업무 유형 분류
→ AI 초안 생성
→ 문서 템플릿 렌더링
→ 사용자 검토
→ 사람 승인 후 실무 적용
```

현재 단계에서는 위 흐름 중 Custom GPT Instructions, 테스트 입력, 평가 기준, 보안 원칙, 개발 문서, placeholder 기반 로컬 PoC 렌더러, 입력 정규화 PoC, dry-run 검증만 다룹니다.

## 폴더 구조

```text
.
├── README.md
├── AGENTS.md
├── docs/
├── prompts/
├── examples/
├── checklists/
├── templates/
├── renderers/
├── normalizers/
└── tasks/
```

## 빠른 시작 방법

1. `prompts/custom_gpt_instructions_v0.1.md`의 내용을 Custom GPT Instructions에 붙여넣습니다.
2. `prompts/conversation_starters.md`의 문구를 Conversation Starters에 등록합니다.
3. Custom GPT의 Knowledge는 비워 둡니다.
4. Capabilities와 Actions/Apps는 초기 테스트에서 사용하지 않습니다.
5. `docs/08_custom_gpt_test_execution_guide.md`에 따라 Preview에서 테스트 1~5를 실행합니다.
6. `docs/05_evaluation_sheet.md`로 결과를 채점합니다.
7. `checklists/custom_gpt_manual_test_checklist.md`로 실행 상태를 확인합니다.
8. `checklists/security_review_checklist.md`로 민감정보 포함 여부를 확인합니다.

## Custom GPT 테스트 흐름

```text
Instructions 복사
→ Conversation Starters 복사
→ Knowledge 비워 둠
→ Capabilities 비활성 권장
→ Actions/Apps 미사용
→ Preview 테스트 1~5 실행
→ 평가표 채점
→ 위험 응답 기록
→ Instructions 개선
→ 재테스트
```

## 문서 목록

- `AGENTS.md`: Codex 작업 규칙
- `docs/00_chatgpt_handoff.md`: ChatGPT 프로젝트 인수인계
- `docs/00_project_overview.md`: 전체 프로젝트 설명
- `docs/01_custom_gpt_setup.md`: Custom GPT 설정 절차
- `docs/02_security_policy.md`: 처리 가능 업무와 금지 업무 기준
- `docs/03_deidentification_rules.md`: 비식별화 규칙
- `docs/04_test_cases.md`: 테스트 케이스
- `docs/05_evaluation_sheet.md`: 평가표
- `docs/06_future_architecture.md`: 향후 아키텍처
- `docs/07_make_api_next_steps.md`: 자동화 전 준비사항
- `docs/08_custom_gpt_test_execution_guide.md`: Custom GPT Preview 수동 테스트 절차
- `docs/09_phase1_review_and_next_steps.md`: 1단계 검수 후 다음 스텝
- `docs/11_document_inventory.md`: 원천 문서 인벤토리 기준
- `docs/12_security_classification.md`: 문서 보안 분류 기준
- `docs/13_deidentified_style_samples.md`: 비식별 문체 샘플
- `docs/14_document_pattern_library.md`: 문서 패턴 라이브러리
- `docs/15_style_specification.md`: 문체 명세
- `docs/16_knowledge_candidate_review.md`: Knowledge 후보 검토 기준
- `docs/18_ai_output_json_schema.md`: AI 출력 JSON 스키마 정의
- `docs/19_xlsx_template_poc_plan.md`: XLSX 조사표 템플릿 PoC 설계
- `docs/20_hwpx_template_poc_plan.md`: HWPX 공문 템플릿 PoC 설계
- `docs/21_template_renderer_requirements.md`: 템플릿 렌더러 요구사항
- `docs/22_renderer_validation_samples.md`: 렌더러 검증용 샘플 JSON
- `docs/23_poc_readiness_review.md`: PoC 구현 전 통합 검수
- `docs/24_sample_json_validation_report.md`: 샘플 JSON 세부 검수 보고서
- `docs/25_xlsx_renderer_poc_result.md`: XLSX 렌더러 PoC 결과
- `docs/26_markdown_renderer_poc_result.md`: Markdown 미리보기 렌더러 PoC 결과
- `docs/27_email_renderer_poc_result.md`: Email 초안 렌더러 PoC 결과
- `docs/28_local_poc_integration_test_report.md`: 로컬 PoC 통합 검수 보고서
- `docs/29_xlsx_renderer_v02_result.md`: XLSX 렌더러 v0.2 결과
- `docs/30_hwpx_renderer_preimplementation_review.md`: HWPX 렌더러 PoC 구현 전 재검수
- `docs/31_hwpx_style_and_language_requirements.md`: HWPX 서식 및 공문체 요구사항
- `docs/32_hwpx_placeholder_template_strategy.md`: HWPX placeholder 템플릿 전략
- `docs/33_hwpx_minimal_poc_scope.md`: HWPX 최소 PoC 구현 범위
- `docs/34_hwpx_minimal_poc_result.md`: HWPX 최소 PoC 결과
- `docs/35_hwpx_test_template_preparation_guide.md`: HWPX 테스트 템플릿 준비 가이드
- `docs/36_hwpx_placeholder_render_test_result.md`: HWPX placeholder 렌더링 테스트 결과
- `docs/37_hwpx_placeholder_actual_render_test_result.md`: HWPX placeholder 실제 치환 테스트 결과
- `docs/38_hwpx_rendered_output_review.md`: HWPX 렌더링 결과 수동 검수 보고서
- `docs/39_hwpx_paragraph_rendering_improvement.md`: HWPX 본문 문단 렌더링 개선
- `docs/40_hwpx_institution_style_values_review.md`: HWPX 기관 표준 서식값 확인 기준
- `docs/42_channel_style_policy.md`: 채널별 문체 정책
- `docs/43_report_template_automation_priority.md`: HWPX 보고서 템플릿 자동화 우선순위
- `docs/44_report_sample_json_set.md`: HWPX 보고서용 샘플 JSON 세트
- `docs/45_one_page_report_hwpx_template_strategy.md`: 원페이지 보고서 HWPX 템플릿 전략
- `docs/46_one_page_report_hwpx_render_test_result.md`: 원페이지 보고서 HWPX 렌더링 테스트 결과
- `docs/47_result_review_report_hwpx_support_check.md`: 결과보고서ㆍ검토보고서 HWPX 렌더러 지원 확인
- `docs/48_git_push_timing_and_summary.md`: GitHub Desktop push 타이밍과 summary 기준
- `docs/49_result_report_hwpx_template_preparation.md`: 결과보고서 HWPX 최소 템플릿 준비
- `docs/50_result_report_hwpx_render_test_result.md`: 결과보고서 HWPX 렌더링 테스트 결과
- `docs/51_review_report_hwpx_template_preparation.md`: 검토보고서 HWPX 최소 템플릿 준비
- `docs/52_review_report_hwpx_render_test_result.md`: 검토보고서 HWPX 렌더링 테스트 결과
- `docs/53_real_hwpx_template_intake_safety_procedure.md`: 실제 HWPX 양식 투입 전 안전 절차
- `docs/54_hwpx_common_placeholder_design.md`: HWPX 공통 placeholder 설계
- `docs/55_project_plan_hwpx_template_preparation.md`: 추진계획서 HWPX 최소 템플릿 준비
- `docs/56_project_plan_hwpx_render_test_result.md`: 추진계획서 HWPX 렌더링 테스트 결과
- `docs/57_hwpx_report_4types_completion_and_safety_rehearsal.md`: HWPX 보고서 4종 완료 상태 및 안전 리허설
- `docs/58_external_hwpx_placeholder_conversion_runbook.md`: 저장소 밖 HWPX placeholder 변환 절차
- `docs/59_phase1_completion_and_phase2_entry_criteria.md`: Phase 1 완료 기준 및 Phase 2 진입 조건
- `docs/60_hwpx_report_input_requirements.md`: HWPX 보고서 4종 입력 요구사항
- `docs/61_input_normalization_schema.md`: 입력 정규화 스키마 초안
- `docs/62_security_filter_requirements.md`: Phase 2 보안 필터 요구사항
- `docs/63_input_normalization_test_cases.md`: 입력 정규화 테스트 케이스
- `docs/64_hwpx_report_normalized_input_examples.md`: HWPX 보고서 4종 정규화 예시
- `docs/65_input_normalization_minimal_poc_scope.md`: 입력 정규화 최소 PoC 범위
- `docs/66_input_normalization_poc_result.md`: 입력 정규화 PoC 결과
- `docs/67_normalized_to_hwpx_payload_mapping_scope.md`: 정규화 결과와 HWPX 렌더러 입력 매핑 범위
- `docs/68_hwpx_payload_mapper_poc_result.md`: HWPX payload mapper PoC 결과
- `docs/69_hwpx_payload_validation_poc_result.md`: HWPX payload validation PoC 결과
- `docs/70_hwpx_renderer_dry_run_scope.md`: HWPX 렌더러 연결 dry-run 범위
- `docs/71_hwpx_renderer_dry_run_result.md`: HWPX 렌더러 연결 dry-run 결과
- `docs/72_dry_run_artifact_retention_policy.md`: dry-run 결과 보관 정책
- `docs/73_hwpx_render_connection_decision.md`: 실제 HWPX 렌더링 연결 여부 결정
- `docs/74_mapped_one_page_hwpx_render_result.md`: mapped one_page_report HWPX 렌더링 결과
- `docs/75_mapped_project_plan_hwpx_render_result.md`: mapped project_plan HWPX 렌더링 결과
- `docs/76_mapped_result_report_hwpx_render_result.md`: mapped result_report HWPX 렌더링 결과
- `docs/77_mapped_review_report_render_policy.md`: mapped review_report 렌더링 정책
- `docs/78_approved_review_report_dry_run_result.md`: approved review_report dry-run 결과
- `docs/79_mapped_review_report_hwpx_render_result.md`: mapped review_report HWPX 렌더링 결과
- `docs/80_mapped_hwpx_4types_completion_summary.md`: HWPX 4종 mapped 렌더링 완료 요약
- `docs/81_normalizers_regression_test_suite.md`: normalizers 회귀 테스트 묶음
- `docs/82_phase2_minimal_operation_flow.md`: Phase 2 최소 운영 흐름
- `docs/83_phase2_user_input_and_manual_operation_checkpoints.md`: Phase 2 사용자 입력 및 수동 운영 점검표
- `docs/84_hwpx_report_user_input_templates.md`: HWPX 보고서 4종 사용자 입력 템플릿
- `docs/85_normalizers_fixture_expansion_review.md`: normalizers fixture 확장 후보 검토
- `docs/86_missing_fields_rule_improvement_review.md`: missing_fields 생성 규칙 개선 검토
- `docs/87_placeholder_confirmed_values_design_review.md`: placeholder_confirmed_values 도입 검토
- `docs/88_placeholder_pattern_collision_rules.md`: placeholder 형식 판정 및 실제값 충돌 규칙
- `docs/89_placeholder_confirmed_values_code_adoption_decision.md`: placeholder_confirmed_values 코드 도입 여부 재검토
- `docs/90_project_reorganization_after_superpowers.md`: Superpowers 재적용 후 프로젝트 재정비 요약
- `docs/91_placeholder_confirmed_values_helper_result.md`: placeholder_confirmed_values read-only helper 구현 결과
- `docs/92_placeholder_confirmed_values_fixture_schema_review.md`: placeholder_confirmed_values fixture schema 검토
- `docs/93_placeholder_confirmed_values_file_fixture_result.md`: placeholder_confirmed_values 파일 기반 fixture 분리 결과
- `docs/94_placeholder_confirmed_values_normalizer_connection_policy.md`: placeholder_confirmed_values normalizer 연결 정책
- `docs/95_placeholder_confirmed_values_readonly_metadata_schema.md`: placeholder_confirmed_values read-only metadata schema
- `docs/96_placeholder_confirmed_values_metadata_retention_decision.md`: placeholder_confirmed_values metadata 유지 결정
- `docs/97_phase2_minimal_poc_checkpoint.md`: Phase 2 최소 PoC checkpoint
- `docs/98_phase2_manual_rehearsal_runbook.md`: Phase 2 수동 리허설 runbook
- `docs/99_phase2_manual_rehearsal_result.md`: Phase 2 수동 리허설 실행 결과
- `prompts/`: GPT 프롬프트와 대화 시작 문구
- `examples/`: 안전한 요청, 제한 요청, 모범 출력 예시
- `examples/json/README.md`: 렌더러 검증용 JSON 샘플 안내
- [비식별 문체 샘플 작성 템플릿](templates/deidentified_sample_template.md)
- `templates/hwpx/template_manifest.md`: HWPX 템플릿 manifest
- `templates/hwpx/local_template_policy.md`: HWPX 로컬 템플릿 보관 정책
- `templates/hwpx/style_profile_manifest.md`: HWPX style profile manifest
- `checklists/phase1_completion_checklist.md`: 1단계 완료 체크리스트
- `checklists/security_review_checklist.md`: 보안 검토 체크리스트
- `checklists/before_automation_checklist.md`: 자동화 전 체크리스트
- `checklists/custom_gpt_manual_test_checklist.md`: Custom GPT 수동 테스트 체크리스트
- `checklists/codex_second_review_checklist.md`: Codex 2차 검수 체크리스트
- `checklists/source_document_review_checklist.md`: 원천 문서 검토 체크리스트
- `checklists/deidentification_review_checklist.md`: 비식별화 검토 체크리스트
- `checklists/knowledge_candidate_checklist.md`: Knowledge 후보 체크리스트
- `checklists/poc_implementation_readiness_checklist.md`: PoC 구현 준비 체크리스트
- `checklists/sample_json_validation_checklist.md`: 샘플 JSON 검수 체크리스트
- `checklists/local_poc_integration_checklist.md`: 로컬 PoC 통합 검수 체크리스트
- `checklists/hwpx_style_fidelity_checklist.md`: HWPX 서식 충실도 체크리스트
- `checklists/official_document_language_checklist.md`: 공공기관 문체 체크리스트
- `checklists/hwpx_placeholder_template_review_checklist.md`: HWPX placeholder 템플릿 검수 체크리스트
- `checklists/hwpx_minimal_poc_approval_checklist.md`: HWPX 최소 PoC 구현 승인 체크리스트
- `checklists/hwpx_test_template_safety_checklist.md`: HWPX 테스트 템플릿 안전 체크리스트
- `checklists/hwpx_rendered_output_manual_review_checklist.md`: HWPX 렌더링 결과 수동 검수 체크리스트
- `checklists/hwpx_institution_style_value_collection_checklist.md`: HWPX 기관 표준 서식값 수집 체크리스트
- `checklists/report_sample_json_validation_checklist.md`: 보고서 샘플 JSON 검수 체크리스트
- `checklists/one_page_report_hwpx_template_checklist.md`: 원페이지 보고서 HWPX 템플릿 검수 체크리스트
- `checklists/real_hwpx_template_intake_checklist.md`: 실제 HWPX 양식 투입 전 체크리스트
- `checklists/external_hwpx_placeholder_conversion_checklist.md`: 저장소 밖 HWPX placeholder 변환 체크리스트
- `checklists/hwpx_report_input_requirements_checklist.md`: HWPX 보고서 입력 요구사항 체크리스트
- `checklists/input_normalization_schema_checklist.md`: 입력 정규화 스키마 체크리스트
- `checklists/security_filter_requirements_checklist.md`: 보안 필터 요구사항 체크리스트
- `checklists/input_normalization_test_cases_checklist.md`: 입력 정규화 테스트 케이스 체크리스트
- `checklists/hwpx_report_normalized_input_examples_checklist.md`: HWPX 보고서 정규화 예시 체크리스트
- `checklists/input_normalization_minimal_poc_scope_checklist.md`: 입력 정규화 최소 PoC 범위 체크리스트
- `checklists/input_normalization_poc_result_checklist.md`: 입력 정규화 PoC 결과 체크리스트
- `checklists/normalized_to_hwpx_payload_mapping_scope_checklist.md`: 정규화 결과와 HWPX payload 매핑 범위 체크리스트
- `checklists/hwpx_payload_mapper_poc_result_checklist.md`: HWPX payload mapper PoC 결과 체크리스트
- `checklists/hwpx_payload_validation_poc_result_checklist.md`: HWPX payload validation PoC 결과 체크리스트
- `checklists/hwpx_renderer_dry_run_scope_checklist.md`: HWPX 렌더러 연결 dry-run 범위 체크리스트
- `checklists/hwpx_renderer_dry_run_result_checklist.md`: HWPX 렌더러 연결 dry-run 결과 체크리스트
- `checklists/dry_run_artifact_retention_policy_checklist.md`: dry-run 결과 보관 정책 체크리스트
- `checklists/hwpx_render_connection_decision_checklist.md`: 실제 HWPX 렌더링 연결 여부 체크리스트
- `checklists/mapped_one_page_hwpx_render_result_checklist.md`: mapped one_page_report HWPX 렌더링 결과 체크리스트
- `checklists/mapped_project_plan_hwpx_render_result_checklist.md`: mapped project_plan HWPX 렌더링 결과 체크리스트
- `checklists/mapped_result_report_hwpx_render_result_checklist.md`: mapped result_report HWPX 렌더링 결과 체크리스트
- `checklists/mapped_review_report_render_policy_checklist.md`: mapped review_report 렌더링 정책 체크리스트
- `checklists/approved_review_report_dry_run_result_checklist.md`: approved review_report dry-run 결과 체크리스트
- `checklists/mapped_review_report_hwpx_render_result_checklist.md`: mapped review_report HWPX 렌더링 결과 체크리스트
- `checklists/mapped_hwpx_4types_completion_checklist.md`: HWPX 4종 mapped 렌더링 완료 체크리스트
- `checklists/normalizers_regression_test_suite_checklist.md`: normalizers 회귀 테스트 묶음 체크리스트
- `checklists/phase2_minimal_operation_flow_checklist.md`: Phase 2 최소 운영 흐름 체크리스트
- `checklists/phase2_user_input_and_manual_operation_checklist.md`: Phase 2 사용자 입력 및 수동 운영 체크리스트
- `checklists/hwpx_report_user_input_templates_checklist.md`: HWPX 보고서 사용자 입력 템플릿 체크리스트
- `checklists/normalizers_fixture_expansion_review_checklist.md`: normalizers fixture 확장 후보 검토 체크리스트
- `checklists/missing_fields_rule_improvement_review_checklist.md`: missing_fields 생성 규칙 개선 검토 체크리스트
- `checklists/placeholder_confirmed_values_design_review_checklist.md`: placeholder_confirmed_values 도입 검토 체크리스트
- `checklists/placeholder_pattern_collision_rules_checklist.md`: placeholder 형식 및 충돌 규칙 체크리스트
- `checklists/placeholder_confirmed_values_code_adoption_decision_checklist.md`: placeholder_confirmed_values 코드 도입 여부 체크리스트
- `checklists/project_reorganization_after_superpowers_checklist.md`: 프로젝트 재정비 검수 체크리스트
- `checklists/placeholder_confirmed_values_helper_result_checklist.md`: placeholder_confirmed_values helper 구현 결과 체크리스트
- `checklists/placeholder_confirmed_values_fixture_schema_review_checklist.md`: placeholder_confirmed_values fixture schema 검토 체크리스트
- `checklists/placeholder_confirmed_values_file_fixture_result_checklist.md`: placeholder_confirmed_values 파일 기반 fixture 분리 체크리스트
- `checklists/placeholder_confirmed_values_normalizer_connection_policy_checklist.md`: placeholder_confirmed_values normalizer 연결 정책 체크리스트
- `checklists/placeholder_confirmed_values_readonly_metadata_schema_checklist.md`: placeholder_confirmed_values read-only metadata schema 체크리스트
- `checklists/placeholder_confirmed_values_metadata_retention_decision_checklist.md`: placeholder_confirmed_values metadata 유지 결정 체크리스트
- `checklists/phase2_minimal_poc_checkpoint_checklist.md`: Phase 2 최소 PoC checkpoint 체크리스트
- `checklists/phase2_manual_rehearsal_runbook_checklist.md`: Phase 2 수동 리허설 runbook 체크리스트
- `checklists/phase2_manual_rehearsal_result_checklist.md`: Phase 2 수동 리허설 실행 결과 체크리스트
- `templates/`: 비식별 샘플, 문서 인벤토리, 문체 명세 작성 템플릿
- `renderers/markdown_renderer/README.md`: Markdown 미리보기 렌더러 안내
- `renderers/email_renderer/README.md`: Email 초안 렌더러 안내
- `renderers/hwpx_renderer/README.md`: HWPX 최소 PoC 렌더러 안내
- `normalizers/README.md`: 입력 정규화 최소 PoC 안내
- `tasks/NEXT_STEP.md`: 다음 작업 목록

## 보안 주의사항

- 비식별화된 업무 지시만 사용합니다.
- 원문 학습이 아니라 서식ㆍ문체ㆍ구조 추출을 목표로 합니다.
- AI는 초안만 작성합니다.
- 사람이 최종 검토ㆍ승인합니다.
- 민감정보가 포함된 경우 처리 제한합니다.
- 확인되지 않은 정보는 `[확인 필요]`로 표시합니다.

## 다음 단계

1. `tasks/NEXT_STEP.md`를 기준으로 Phase 2 최소 PoC의 반복 운영 기준을 정리합니다.
2. 다음 최소 개선 후보를 정하되, API/Make.com/Email 자동화와 실제 기관 양식 원본 사용은 계속 보류합니다.
3. helper 결과와 metadata는 아직 normalizer 흐름에 연결하지 않습니다.
4. GitHub Desktop에서 변경 파일을 검수한 뒤 push합니다.
5. 실제 원본이 필요한 경우 저장소 밖에서 복사본을 만들고, 실제 내용과 식별 요소를 제거한 뒤 로컬 placeholder 템플릿 후보로만 검토합니다.
