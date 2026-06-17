# Markdown 미리보기 렌더러 PoC 결과

## 목적
JSON 샘플을 사람이 검토하기 쉬운 Markdown 초안으로 변환하는 PoC입니다.

이번 단계는 실제 외부 발송용 문서 생성이 아니라, 렌더러 검증용 미리보기 생성입니다.

## 실행 방법
python renderers/markdown_renderer/render_markdown_poc.py

## 입력 파일
- examples/json/sample_official_letter.json
- examples/json/sample_project_plan.json
- examples/json/sample_vendor_email.json
- examples/json/sample_survey_table.json
- examples/json/sample_blocked_security_case.json

## 출력 파일
- renderers/markdown_renderer/output/sample_official_letter_preview.md
- renderers/markdown_renderer/output/sample_project_plan_preview.md
- renderers/markdown_renderer/output/sample_vendor_email_preview.md
- renderers/markdown_renderer/output/sample_survey_table_preview.md
- renderers/markdown_renderer/output/sample_blocked_security_case_blocked.md

## 보안 검증 결과

| 샘플 | 예상 결과 | 실제 결과 | 판정 |
|---|---|---|---|
| sample_official_letter.json | Markdown 미리보기 생성 | sample_official_letter_preview.md 생성 | 통과 |
| sample_project_plan.json | Markdown 미리보기 생성 | sample_project_plan_preview.md 생성 | 통과 |
| sample_vendor_email.json | Markdown 미리보기 생성 | sample_vendor_email_preview.md 생성 | 통과 |
| sample_survey_table.json | Markdown 미리보기 생성 | sample_survey_table_preview.md 생성 | 통과 |
| sample_blocked_security_case.json | 차단 보고 Markdown 생성 | sample_blocked_security_case_blocked.md 생성 | 통과 |

## 이번 단계에서 하지 않은 것
- 실제 이메일 발송
- HWPX 생성
- XLSX 생성
- API 호출
- Make.com 자동화
- 실제 업무자료 사용

## Step 17 완료 체크리스트

- [x] Markdown 렌더러 README가 작성되었는가
- [x] Markdown 렌더러 코드가 작성되었는가
- [x] 보안 검증 코드가 작성되었는가
- [x] output .gitignore가 작성되었는가
- [x] 샘플 JSON 5개를 처리했는가
- [x] blocked 샘플은 차단 보고로 처리했는가
- [x] 실제 원문, 개인정보, 내부 운영정보를 사용하지 않았는가
- [x] 외부 발송이나 API 호출을 하지 않았는가
