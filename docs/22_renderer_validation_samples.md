# 렌더러 검증용 샘플 JSON

## 목적

- 향후 HWPX, XLSX, Email, Markdown 렌더러를 테스트하기 위한 placeholder 기반 샘플 JSON을 정의합니다.
- 실제 원문이나 실제 개인정보를 사용하지 않습니다.
- 모든 샘플은 docs/18_ai_output_json_schema.md 구조를 따르는 테스트용 초안입니다.
- 샘플은 렌더러의 정상 출력, missing_fields 처리, 보안 차단 조건을 검증하기 위한 용도입니다.

## 기본 원칙

- 실제 원문을 사용하지 않습니다.
- 실제 기관명, 업체명, 담당자명, 연락처를 사용하지 않습니다.
- 실제 문서번호, 민원번호, 접수번호, 차량번호를 사용하지 않습니다.
- 실제 장비명, 수량, 금액, 계약 조건을 사용하지 않습니다.
- 확인되지 않은 값은 [확인 필요] 또는 null로 표시합니다.
- 모든 산출물은 초안이며 사람이 최종 검토해야 합니다.

## 샘플 목록

| 파일 | 목적 | 예상 target_format |
|---|---|---|
| examples/json/sample_official_letter.json | 공문 HWPX 렌더링 검증 | hwpx |
| examples/json/sample_project_plan.json | 추진계획서 HWPX 렌더링 검증 | hwpx |
| examples/json/sample_vendor_email.json | 업체 메일 렌더링 검증 | email |
| examples/json/sample_survey_table.json | 조사표 XLSX 렌더링 검증 | xlsx |
| examples/json/sample_blocked_security_case.json | 보안 차단 로직 검증 | blocked |

## 각 샘플의 검증 목적

### sample_official_letter.json

- 검증 렌더러: HWPX 공문 렌더러
- 검증 필드: document_type, body_sections, attachments, checklist, missing_fields, renderer_hints
- missing_fields: 있음
- security_review: low
- 사람 최종 검토 이유: 수신처, 제출기한, 붙임 목록 등 확인 필요 항목이 남아 있음

### sample_project_plan.json

- 검증 렌더러: HWPX 추진계획서 렌더러
- 검증 필드: background, purpose, overview, schedule, budget, expected_effects
- missing_fields: 있음
- security_review: low
- 사람 최종 검토 이유: 추진기간, 소요예산, 일정 등 확정되지 않은 값이 있음

### sample_vendor_email.json

- 검증 렌더러: Email 렌더러
- 검증 필드: subject, purpose, request_items, caution_notes, signature
- missing_fields: 있음
- security_review: medium
- 사람 최종 검토 이유: 외부 발송 전 개인정보 제외 문구와 계약ㆍ선정 미확정 문구 확인 필요

### sample_survey_table.json

- 검증 렌더러: XLSX 조사표 렌더러
- 검증 필드: sheet_name, title, columns, rows, notes, privacy_notice, checklist
- missing_fields: 있음
- security_review: low
- 사람 최종 검토 이유: 조사 기준일, 제출 단위, 조사 항목 범위 확인 필요

### sample_blocked_security_case.json

- 검증 렌더러: 보안 차단 로직
- 검증 필드: security_review, blocked_items, allowed_processing, notes
- missing_fields: 있음
- security_review: blocked
- 사람 최종 검토 이유: 렌더링 차단 대상인지 확인하고 입력을 폐기 또는 비식별 재요청해야 함

## 사용 금지

- 이 샘플을 실제 업무자료로 사용하지 않습니다.
- 이 샘플을 외부 발송하지 않습니다.
- 이 샘플에 실제 개인정보를 추가하지 않습니다.
- 이 샘플을 Custom GPT Knowledge에 바로 업로드하지 않습니다.

## Step 13 완료 체크리스트

- [x] 공문 샘플 JSON이 작성되었는가
- [x] 추진계획서 샘플 JSON이 작성되었는가
- [x] 업체 메일 샘플 JSON이 작성되었는가
- [x] 조사표 샘플 JSON이 작성되었는가
- [x] 보안 차단 테스트 샘플 JSON이 작성되었는가
- [x] 모든 샘플이 placeholder 기반인가
- [x] 실제 원문, 개인정보, 내부 운영정보가 포함되지 않았는가
- [x] 실제 렌더러 코드를 작성하지 않았는가
- [x] README 링크가 반영되었는가
