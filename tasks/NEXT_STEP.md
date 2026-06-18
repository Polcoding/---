# 다음 작업

## 목표

Phase 2 보안 필터 요구사항을 작성합니다.

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

## 확인 대상

- `docs/59_phase1_completion_and_phase2_entry_criteria.md`
- `docs/60_hwpx_report_input_requirements.md`
- `checklists/hwpx_report_input_requirements_checklist.md`
- `docs/61_input_normalization_schema.md`
- `checklists/input_normalization_schema_checklist.md`
- `docs/58_external_hwpx_placeholder_conversion_runbook.md`
- `checklists/external_hwpx_placeholder_conversion_checklist.md`
- `docs/57_hwpx_report_4types_completion_and_safety_rehearsal.md`
- `docs/18_ai_output_json_schema.md`
- `examples/json/sample_one_page_report.json`
- `examples/json/sample_project_plan.json`
- `examples/json/sample_result_report.json`
- `examples/json/sample_review_report.json`

## 확인 항목

1. `security_flags`를 어떻게 판정할지
2. A/B/C/D 등급과 `risk_level`을 어떻게 연결할지
3. 차단해야 할 패턴과 키워드는 무엇인지
4. 안전한 설명 문맥과 실제값 의심 문맥을 어떻게 구분할지
5. `blocked`, `needs_security_review`, `ready_for_draft` 기준을 어떻게 둘지
6. 실제 원문이나 개인정보 없이 요구사항을 작성할 수 있는지

## 작업 제한

- 실제 기관 양식 사용 금지
- 실제 문서 원문 사용 금지
- 실제 개인정보 또는 내부 운영정보 사용 금지
- 실제 HWPX 템플릿 Git 추가 금지
- Email/API/Make.com 연동 금지
- 확인되지 않은 서식값 임의 생성 금지

## 완료 조건

- 보안 필터 요구사항 작성
- 차단 패턴과 키워드 기준 작성
- A/B/C/D 등급과 `risk_level` 연결 기준 작성
- 라우팅 결정 기준 작성
- 실제 원본 미사용 확인
- 다음 단계 진행 여부 판단

## 다음 단계 후보

현재 추천은 보안 필터 요구사항을 문서로 먼저 확정하고, 이후 입력 정규화 테스트 케이스를 작성하는 것입니다.
