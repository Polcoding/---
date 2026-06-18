# PoC 구현 전 통합 검수

## 목적

- XLSX/HWPX 렌더러 PoC 구현 전에 문서, 스키마, 샘플, 보안 기준의 준비 상태를 검토합니다.
- 이번 단계에서는 실제 구현 코드를 작성하지 않습니다.
- 실제 업무자료, 실제 공문 원문, 실제 개인정보는 사용하지 않습니다.
- 구현 가능 여부가 아니라 구현 전 준비 상태를 점검합니다.

## 현재 기준 안내

이 문서는 PoC 구현 전 단계의 기록입니다.

현재 저장소에서는 XLSX, Markdown, Email, HWPX 로컬 PoC 렌더러가 작성되었고, HWPX 보고서 4종의 로컬 placeholder 치환과 한컴 수동 열람 검수가 완료되었습니다.

현재 진행 상태는 `docs/59_phase1_completion_and_phase2_entry_criteria.md`, `docs/60_hwpx_report_input_requirements.md`, `docs/61_input_normalization_schema.md`를 우선 확인합니다.

## 검수 대상 문서

| 문서 | 존재 여부 | 비고 |
|---|---|---|
| docs/12_security_classification.md | 확인됨 | 보안등급 기준 |
| docs/13_deidentified_style_samples.md | 확인됨 | 비식별 문체 샘플 |
| docs/14_document_pattern_library.md | 확인됨 | 문서 패턴 라이브러리 |
| docs/15_style_specification.md | 확인됨 | 문서 서식 명세표 |
| docs/18_ai_output_json_schema.md | 확인됨 | AI 출력 JSON 스키마 |
| docs/19_xlsx_template_poc_plan.md | 확인됨 | XLSX 템플릿 PoC 설계 |
| docs/20_hwpx_template_poc_plan.md | 확인됨 | HWPX 템플릿 PoC 설계 |
| docs/21_template_renderer_requirements.md | 확인됨 | 템플릿 렌더러 요구사항 |
| docs/22_renderer_validation_samples.md | 확인됨 | 렌더러 검증용 샘플 JSON 설명 |
| examples/json/README.md | 확인됨 | JSON 샘플 폴더 안내 |
| examples/json/sample_official_letter.json | 확인됨 | 공문 샘플 JSON |
| examples/json/sample_project_plan.json | 확인됨 | 추진계획서 샘플 JSON |
| examples/json/sample_vendor_email.json | 확인됨 | 업체 메일 샘플 JSON |
| examples/json/sample_survey_table.json | 확인됨 | 조사표 샘플 JSON |
| examples/json/sample_blocked_security_case.json | 확인됨 | 보안 차단 샘플 JSON |

## 문서 간 일관성 점검

| 점검 항목 | 검수 기준 | 현재 판단 |
|---|---|---|
| JSON 스키마와 샘플 JSON 필드가 일치하는가 | 공통 필드, security_review, missing_fields, renderer_hints 포함 여부 | 일치 |
| XLSX PoC 설계가 sample_survey_table.json을 사용할 수 있는가 | sheet_name, title, columns, rows, privacy_notice, checklist 포함 여부 | 사용 가능 |
| HWPX PoC 설계가 sample_official_letter.json과 sample_project_plan.json을 사용할 수 있는가 | body_sections, attachments, overview, schedule, budget 포함 여부 | 사용 가능 |
| 업체 메일 샘플이 email 렌더링 요구사항과 맞는가 | subject, purpose, request_items, caution_notes, signature 포함 여부 | 일치 |
| blocked 보안 샘플이 렌더링 차단 조건과 맞는가 | risk_level blocked, allowed_processing 제한, documents 빈 배열 여부 | 일치 |
| 보안등급 기준과 렌더러 차단 조건이 충돌하지 않는가 | high/blocked 및 개인정보 포함 시 차단 또는 사람 검토 | 충돌 없음 |
| 문서 서식 명세표와 HWPX/XLSX PoC 설계가 충돌하지 않는가 | 서식은 템플릿 담당, 확인되지 않은 값은 [확인 필요] 유지 | 충돌 없음 |

## 구현 전 보안 게이트

PoC 구현 전 반드시 만족해야 할 조건은 다음과 같습니다.

- 실제 원문 없음
- 실제 개인정보 없음
- 실제 기관명 없음
- 실제 차량번호 없음
- 실제 장비명과 수량 없음
- 실제 견적 금액 없음
- API 키 없음
- 자동 발송 없음
- Custom GPT Knowledge 업로드 없음
- 모든 샘플 JSON이 placeholder 기반
- blocked 샘플이 렌더링 차단 테스트용으로만 사용됨

## 작성 당시 구현 우선순위

1. XLSX 렌더러 PoC
2. Markdown 미리보기 렌더러
3. Email 초안 렌더러
4. HWPX 렌더러 PoC

이유:
- XLSX는 조사표 구조 검증이 상대적으로 단순합니다.
- Markdown은 디버깅과 검토가 쉽습니다.
- Email은 자동 발송 없이 초안 렌더링만 검증할 수 있습니다.
- 당시 기준 HWPX PoC는 서식 복잡도 때문에 후순위로 두었습니다.

## 작성 당시 결론

현재 판단:

- 일부 문서 보강 후 구현 가능

판단 사유:

- 핵심 설계 문서, JSON 스키마, 샘플 JSON, 보안 기준은 준비되어 있습니다.
- 작성 당시에는 실제 구현 코드가 작성되기 전이었습니다.
- 현재는 placeholder 기반 로컬 PoC 구현과 검수가 진행되었습니다.
- 구현 시작 시에도 실제 업무자료가 아니라 placeholder 기반 샘플 JSON만 사용해야 합니다.
