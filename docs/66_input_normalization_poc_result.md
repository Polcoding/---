# 입력 정규화 PoC 결과

## 목적

`normalizers/` 최소 PoC가 HWPX 보고서 4종 후보 판정과 보안 라우팅을 placeholder fixture 기준으로 수행하는지 확인합니다.

이번 단계에서는 기존 HWPX 렌더러와 연결하지 않습니다.

## 구현 파일

- `normalizers/README.md`
- `normalizers/input_normalizer_poc.py`
- `normalizers/security_filter_poc.py`
- `normalizers/fixtures/*.json`
- `normalizers/output/.gitignore`
- `normalizers/output/.gitkeep`

## fixture

| fixture | 목적 | 기대 결과 |
|---|---|---|
| `safe_one_page_report_request.json` | 안전 원페이지 보고서 요청 | `one_page_report`, `ready_for_draft` |
| `missing_project_plan_request.json` | 일정ㆍ예산 누락 추진계획서 요청 | `project_plan`, `needs_more_input` |
| `missing_result_report_request.json` | 실적ㆍ예산 정보 누락 결과보고서 요청 | `result_report`, `needs_more_input` |
| `review_report_needs_security_review.json` | 검토보고서 보안 검토 요청 | `review_report`, `needs_security_review` |
| `blocked_real_value_like_request.json` | 실제 원문ㆍ자동화 금지 요청 차단 | `unknown`, `blocked` |

## 실행 결과

Codex 번들 Python으로 `normalizers/input_normalizer_poc.py`를 실행했습니다.

| fixture | 실제 document_type | 실제 routing | 판정 |
|---|---|---|---|
| `blocked_real_value_like_request.json` | `unknown` | `blocked` | 통과 |
| `missing_project_plan_request.json` | `project_plan` | `needs_more_input` | 통과 |
| `missing_result_report_request.json` | `result_report` | `needs_more_input` | 통과 |
| `review_report_needs_security_review.json` | `review_report` | `needs_security_review` | 통과 |
| `safe_one_page_report_request.json` | `one_page_report` | `ready_for_draft` | 통과 |

## 실행 중 보정한 사항

- 차단 요청은 문서 유형 키워드보다 금지 자동화 신호를 먼저 보도록 조정했습니다.
- `one_page_report`는 누락값이 `missing_fields`로 분리되어 있으면 `ready_for_draft`로 진행할 수 있도록 조정했습니다.
- fixture 기대값과 실제 결과를 비교해 `passed` 여부를 출력하도록 했습니다.
- output 쓰기 권한 문제가 있어도 stdout 검증 결과는 확인할 수 있도록 했습니다.

## Git 제외 확인

- `normalizers/output/normalization_summary.json`은 `normalizers/output/.gitignore`에 따라 Git 제외 대상입니다.
- `normalizers/output/.gitignore`와 `.gitkeep`은 Git 포함 대상입니다.
- fixture JSON은 placeholder 기반이므로 Git 포함 대상입니다.

## 보안 검수

- 실제 기관 양식 사용 여부: 사용하지 않음
- 실제 문서 원문 사용 여부: 사용하지 않음
- 실제 개인정보 사용 여부: 사용하지 않음
- 실제 기관명, 업체명, 담당자명 사용 여부: 사용하지 않음
- 실제 문서번호, 민원번호, 접수번호, 사건번호 사용 여부: 사용하지 않음
- 실제 예산액, 실적 수치, 담당자, 수량 생성 여부: 생성하지 않음
- Email/API/Make.com 연동 여부: 수행하지 않음

## 결론

입력 정규화 최소 PoC는 HWPX 보고서 4종 후보 판정과 기본 보안 라우팅을 placeholder fixture 기준으로 수행할 수 있습니다.

다음 단계는 정규화 결과를 HWPX 렌더러 입력 JSON으로 변환하는 매핑 범위를 결정하는 것입니다.
