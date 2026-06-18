# 보고서 샘플 JSON 검수 체크리스트

## 공통 필드

- [ ] request_id가 있는가
- [ ] document_type이 있는가
- [ ] output_targets가 있는가
- [ ] security_review가 있는가
- [ ] missing_fields가 있는가
- [ ] draft_status가 draft인가
- [ ] human_review_required가 true인가
- [ ] renderer_hints가 있는가

## 보고서 유형별 필드

- [ ] one_page_report 필수 필드가 있는가
- [ ] project_plan 필수 필드가 있는가
- [ ] result_report 필수 필드가 있는가
- [ ] review_report 필수 필드가 있는가

## 보안

- [ ] 실제 원문이 없는가
- [ ] 실제 개인정보가 없는가
- [ ] 실제 기관명, 업체명, 담당자명이 없는가
- [ ] 실제 문서번호, 민원번호, 차량번호가 없는가
- [ ] 실제 예산액, 실적 수치, 참여 인원이 없는가
- [ ] 실제 HWP/HWPX 파일을 추가하지 않았는가

## 자동화 범위

- [ ] 구현 코드를 작성하지 않았는가
- [ ] API 호출을 하지 않았는가
- [ ] 이메일 자동화를 하지 않았는가
- [ ] Make.com 연동을 하지 않았는가
- [ ] 실제 HWP/HWPX 파일을 생성하지 않았는가
