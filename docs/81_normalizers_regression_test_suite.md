# normalizers 회귀 테스트 묶음

## 목적

`normalizers/`의 입력 정규화, 보안 필터, HWPX payload 매핑, validation, dry-run, mapped HWPX 렌더링을 같은 fixture 묶음으로 재검증합니다.

이 문서는 HWPX 보고서 4종 mapped 렌더링 완료 이후의 최소 회귀 테스트 기준입니다.

## fixture 범위

| fixture | 기대 document_type | 기대 routing | payload | 비고 |
|---|---|---|---|---|
| `safe_one_page_report_request.json` | `one_page_report` | `ready_for_draft` | 생성 | 원페이지 보고서 정상 초안 |
| `missing_project_plan_request.json` | `project_plan` | `needs_more_input` | 생성 | 추진계획서 확인 필요값 유지 |
| `missing_result_report_request.json` | `result_report` | `needs_more_input` | 생성 | 결과보고서 확인 필요값 유지 |
| `review_report_needs_security_review.json` | `review_report` | `needs_security_review` | 미생성 | 승인 없는 검토보고서 차단 |
| `approved_review_report_request.json` | `review_report` | `ready_for_draft` | 생성 | placeholder 보안 승인 후 허용 |
| `blocked_real_value_like_request.json` | `unknown` | `blocked` | 미생성 | 금지 자동화 요청 차단 |

## 실행 순서

Codex 번들 Python 또는 로컬 Python으로 아래 순서를 실행합니다.

```powershell
python .\normalizers\input_normalizer_poc.py
python .\normalizers\hwpx_payload_mapper_poc.py
python .\normalizers\validate_hwpx_payload_poc.py
python .\normalizers\hwpx_renderer_dry_run_poc.py
python .\normalizers\render_mapped_hwpx_poc.py
```

## 기대 결과

### input_normalizer_poc.py

- fixture 6종 모두 `passed`
- 승인 없는 `review_report`는 `needs_security_review`
- 승인된 `review_report`는 `ready_for_draft`
- blocked fixture는 `blocked`

### hwpx_payload_mapper_poc.py

- `ready_for_draft`, `needs_more_input`만 payload 생성
- `needs_security_review`, `blocked`는 payload 미생성
- `approved_review_report_request.json`은 payload 생성
- `review_report_needs_security_review.json`은 payload 미생성

### validate_hwpx_payload_poc.py

- payload 생성 대상은 validation 통과
- payload 미생성 대상은 skipped 상태 유지
- 보안 승인 없는 검토보고서가 validation 대상으로 넘어가지 않음

### hwpx_renderer_dry_run_poc.py

- `safe_one_page_report_request.json`: `dry_run_ready`
- `missing_project_plan_request.json`: `dry_run_ready_with_missing_fields`
- `missing_result_report_request.json`: `dry_run_ready_with_missing_fields`
- `approved_review_report_request.json`: `dry_run_ready`
- `review_report_needs_security_review.json`: `skipped_security_review`
- `blocked_real_value_like_request.json`: `skipped_blocked`

### render_mapped_hwpx_poc.py

렌더링 대상은 4종으로 제한합니다.

- `safe_one_page_report_request.json`
- `missing_project_plan_request.json`
- `missing_result_report_request.json`
- `approved_review_report_request.json`

각 결과는 다음 조건을 만족해야 합니다.

- `status`: `rendered`
- `remaining_placeholders`: 0
- `errors`: 없음

## 산출물 정책

다음 산출물은 Git에 포함하지 않습니다.

- `normalizers/output/*`
- `renderers/hwpx_renderer/output/*.hwpx`
- `templates/hwpx/*.hwpx`

summary JSON과 HWPX output은 로컬 검증용입니다.

## 보안 검수

- 실제 기관 양식 원본 사용 금지
- 실제 문서 원문 사용 금지
- 실제 개인정보, 민원정보, 내부 운영정보 사용 금지
- 실제 승인자명, 결재번호, 문서번호 사용 금지
- 실제 예산액, 일정, 실적 수치 임의 생성 금지
- Email/API/Make.com 연동 금지

## 결론

현재 `normalizers/` 회귀 테스트 묶음은 fixture 6종을 기준으로 관리합니다.

이 묶음이 통과하면 입력 정규화부터 mapped HWPX 렌더링 전제까지의 최소 PoC 흐름이 유지되는 것으로 봅니다.
