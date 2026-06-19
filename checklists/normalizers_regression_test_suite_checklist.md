# normalizers 회귀 테스트 묶음 체크리스트

## 목적

`docs/81_normalizers_regression_test_suite.md` 기준으로 정규화부터 mapped HWPX 렌더링까지의 회귀 테스트 상태를 확인합니다.

## fixture 범위

| 완료 | 항목 |
|---|---|
| [x] | `safe_one_page_report_request.json`이 포함되는가 |
| [x] | `missing_project_plan_request.json`이 포함되는가 |
| [x] | `missing_result_report_request.json`이 포함되는가 |
| [x] | `review_report_needs_security_review.json`이 포함되는가 |
| [x] | `approved_review_report_request.json`이 포함되는가 |
| [x] | `blocked_real_value_like_request.json`이 포함되는가 |

## 실행 순서

| 완료 | 항목 |
|---|---|
| [x] | `input_normalizer_poc.py`를 실행했는가 |
| [x] | `hwpx_payload_mapper_poc.py`를 실행했는가 |
| [x] | `validate_hwpx_payload_poc.py`를 실행했는가 |
| [x] | `hwpx_renderer_dry_run_poc.py`를 실행했는가 |
| [x] | `render_mapped_hwpx_poc.py`를 실행했는가 |

## 기대 결과

| 완료 | 항목 |
|---|---|
| [x] | 입력 정규화 fixture 6종이 모두 `passed`인가 |
| [x] | 승인 없는 `review_report`가 `needs_security_review`로 유지되는가 |
| [x] | 승인된 `review_report`가 `ready_for_draft`로 라우팅되는가 |
| [x] | blocked fixture가 `blocked`로 라우팅되는가 |
| [x] | `needs_security_review`와 `blocked`가 payload를 생성하지 않는가 |
| [x] | validation 대상 payload가 모두 통과하는가 |
| [x] | dry-run 상태가 문서의 기대값과 일치하는가 |
| [x] | mapped HWPX 렌더링 4종이 모두 `rendered`인가 |
| [x] | mapped HWPX 렌더링 4종의 `remaining_placeholders`가 0인가 |

## Git 제외 확인

| 완료 | 항목 |
|---|---|
| [x] | `normalizers/output/*`가 Git 제외 대상인가 |
| [x] | `renderers/hwpx_renderer/output/*.hwpx`가 Git 제외 대상인가 |
| [x] | `templates/hwpx/*.hwpx`가 Git 제외 대상인가 |

## 보안 검수

| 완료 | 항목 |
|---|---|
| [x] | 실제 개인정보를 포함하지 않았는가 |
| [x] | 실제 기관명, 업체명, 담당자명을 포함하지 않았는가 |
| [x] | 실제 승인자명, 결재번호, 문서번호를 포함하지 않았는가 |
| [x] | 실제 공문 또는 보고서 원문을 포함하지 않았는가 |
| [x] | 실제 예산액, 일정, 실적 수치를 생성하지 않았는가 |
| [x] | Email/API/Make.com 연동을 하지 않았는가 |

## 다음 단계 판단

| 완료 | 항목 |
|---|---|
| [x] | normalizers 회귀 테스트 묶음을 기준 문서로 사용할 수 있는가 |
| [ ] | 다음 단계로 Phase 2 최소 운영 흐름을 정리할 수 있는가 |
