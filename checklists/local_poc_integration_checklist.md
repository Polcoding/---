# 로컬 PoC 통합 검수 체크리스트

## 실행 검수

- [x] XLSX 렌더러를 실행했는가
- [x] Markdown 렌더러를 실행했는가
- [x] Email 렌더러를 실행했는가
- [x] examples/json의 placeholder 샘플만 입력으로 사용했는가
- [x] XLSX 렌더러가 sample_survey_table.json을 처리했는가
- [x] Markdown 렌더러가 샘플 JSON을 처리했는가
- [x] Email 렌더러가 sample_vendor_email.json을 처리했는가
- [x] blocked 샘플이 일반 산출물이 아니라 차단 보고로 처리되었는가

## 산출물 검수

- [x] XLSX 산출물이 생성되었는가
- [x] Markdown preview 산출물이 생성되었는가
- [x] Email Markdown 초안 산출물이 생성되었는가
- [x] Email TXT 초안 산출물이 생성되었는가
- [x] output 산출물이 로컬 테스트 산출물로만 관리되는가

## Git 제외 검수

- [x] renderers/xlsx_renderer/output/*.xlsx가 Git 제외 대상인가
- [x] renderers/xlsx_renderer/output/*.xlsm이 Git 제외 대상인가
- [x] renderers/xlsx_renderer/output/*.xls가 Git 제외 대상인가
- [x] renderers/markdown_renderer/output/*.md가 Git 제외 대상인가
- [x] renderers/email_renderer/output/*.md가 Git 제외 대상인가
- [x] renderers/email_renderer/output/*.txt가 Git 제외 대상인가
- [x] renderers/email_renderer/output/*.eml이 Git 제외 대상인가
- [x] 각 output 폴더의 .gitkeep은 유지되는가

## 보안 검수

- [x] 실제 업무자료를 사용하지 않았는가
- [x] 실제 공문 원문을 사용하지 않았는가
- [x] 실제 개인정보를 사용하지 않았는가
- [x] 실제 기관명, 업체명, 담당자명을 사용하지 않았는가
- [x] 실제 차량번호, 장비명, 수량을 사용하지 않았는가
- [x] 실제 예산액, 견적 금액을 사용하지 않았는가
- [x] API 호출을 하지 않았는가
- [x] Make.com 연동을 하지 않았는가
- [x] Gmail/Outlook/SMTP 연결을 하지 않았는가
- [x] 실제 이메일 발송을 하지 않았는가
- [x] HWPX 구현을 하지 않았는가
- [x] Custom GPT Knowledge 업로드를 하지 않았는가

## Step 19 완료 체크리스트

- [x] 로컬 PoC 통합 검수 보고서가 작성되었는가
- [x] 로컬 PoC 통합 검수 체크리스트가 작성되었는가
- [x] README 링크가 반영되었는가
- [x] 새로운 기능 구현 없이 기존 PoC 실행 결과만 문서화했는가
- [x] 보안 위험 항목이 발견되지 않았는가
- [x] Step 20 진행 가능 여부를 판단했는가
