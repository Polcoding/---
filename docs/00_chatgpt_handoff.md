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

다음 단계는 API/Make.com 연동이 아니라 local template policy와 Git 제외 상태 반복 검증 기준을 정리하는 것입니다.

이미 추가된 read-only helper는 `missing_fields` 생성 결과와 routing 결과를 즉시 바꾸지 않습니다.

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
- `tasks/NEXT_STEP.md`
- `examples/json/sample_one_page_report.json`
- `examples/json/sample_result_report.json`
- `examples/json/sample_review_report.json`
- `renderers/hwpx_renderer/render_hwpx_poc.py`
- `renderers/hwpx_renderer/template_package.py`
- `templates/hwpx/local_template_policy.md`
- `checklists/one_page_report_hwpx_template_checklist.md`
- `checklists/external_hwpx_candidate_manual_procedure_checklist.md`
