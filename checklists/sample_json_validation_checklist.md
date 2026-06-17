# 샘플 JSON 검수 체크리스트

## 공통 필드 검수

- [x] request_id가 있는가
- [x] input_summary가 있는가
- [x] task_type이 있는가
- [x] document_type이 있는가
- [x] output_targets가 있는가
- [x] security_review가 있는가
- [x] missing_fields가 있는가
- [x] assumptions가 있는가
- [x] draft_status가 있는가
- [x] human_review_required가 있는가
- [x] renderer_hints가 있는가

## security_review 검수

- [x] risk_level이 있는가
- [x] contains_personal_info가 있는가
- [x] contains_sensitive_info가 있는가
- [x] contains_internal_info가 있는가
- [x] blocked_items가 있는가
- [x] allowed_processing이 있는가
- [x] required_review가 있는가
- [x] notes가 있는가
- [x] risk_level이 low, medium, high, blocked 중 하나인가

## 샘플별 검수

- [x] 공문 샘플이 HWPX 렌더링 검증용으로 적절한가
- [x] 추진계획서 샘플이 HWPX 렌더링 검증용으로 적절한가
- [x] 업체 메일 샘플이 Email 렌더링 검증용으로 적절한가
- [x] 조사표 샘플이 XLSX 렌더링 검증용으로 적절한가
- [x] blocked 샘플이 보안 차단 검증용으로 적절한가

## 보안 검수

- [x] 실제 원문이 없는가
- [x] 실제 개인정보가 없는가
- [x] 실제 기관명이나 업체명이 없는가
- [x] 실제 담당자명, 연락처, 이메일이 없는가
- [x] 실제 문서번호, 민원번호, 접수번호, 사건번호가 없는가
- [x] 실제 차량번호, 장비명, 수량이 없는가
- [x] 실제 예산액, 견적 금액, 계약 조건이 없는가
- [x] blocked 샘플의 blocked_items가 placeholder 기반인가

## 구현 금지 확인

- [x] HWPX 생성 코드를 작성하지 않았는가
- [x] XLSX 생성 코드를 작성하지 않았는가
- [x] openpyxl 코드를 작성하지 않았는가
- [x] Python 코드를 작성하지 않았는가
- [x] API 코드를 작성하지 않았는가
- [x] Make.com 자동화 코드를 작성하지 않았는가
- [x] 이메일 자동화 코드를 작성하지 않았는가
- [x] 실제 HWPX/XLSX 파일을 생성하지 않았는가
