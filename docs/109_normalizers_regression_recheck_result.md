# normalizers 회귀 테스트 재검증 결과

## 목적

Phase 2 마무리 전 `normalizers/` 회귀 테스트 묶음이 현재 저장소 상태에서도 유지되는지 재검증합니다.

이 문서는 실행 결과 기록입니다. normalizer, routing, HWPX payload, renderer, fixture 구조를 변경하지 않습니다.

## 실행 기준

기준 문서:

- `docs/81_normalizers_regression_test_suite.md`
- `docs/108_phase2_operating_docs_final_review.md`
- `tasks/NEXT_STEP.md`

실행 대상:

```powershell
python .\normalizers\validate_placeholder_confirmed_values_poc.py
python .\normalizers\input_normalizer_poc.py
python .\normalizers\hwpx_payload_mapper_poc.py
python .\normalizers\validate_hwpx_payload_poc.py
python .\normalizers\hwpx_renderer_dry_run_poc.py
python .\normalizers\render_mapped_hwpx_poc.py
```

## 실행 결과 요약

| 단계 | 결과 | 판단 |
|---|---|---|
| `validate_placeholder_confirmed_values_poc.py` | helper safe/invalid fixture 통과 | 정상 |
| `input_normalizer_poc.py` | routing fixture 6종 통과 | 정상 |
| `hwpx_payload_mapper_poc.py` | 생성 대상 4종 created, 차단 대상 2종 skipped | 정상 |
| `validate_hwpx_payload_poc.py` | 생성 대상 4종 validated, 차단 대상 2종 skipped | 정상 |
| `hwpx_renderer_dry_run_poc.py` | dry-run 상태 기대값과 일치 | 정상 |
| `render_mapped_hwpx_poc.py` | mapped HWPX 4종 rendered | 정상 |

## helper fixture 검증

`placeholder_confirmed_values` helper 검증 결과:

- invalid fixture의 plain text, empty placeholder, actual value marker, non-mapping 사례 차단
- safe fixture의 placeholder 값 허용
- safe single value 허용
- 전체 결과 `all_passed: true`

## routing fixture 검증

| fixture | document_type | routing_status | 판단 |
|---|---|---|---|
| `safe_one_page_report_request.json` | `one_page_report` | `ready_for_draft` | 통과 |
| `missing_project_plan_request.json` | `project_plan` | `needs_more_input` | 통과 |
| `missing_result_report_request.json` | `result_report` | `needs_more_input` | 통과 |
| `review_report_needs_security_review.json` | `review_report` | `needs_security_review` | 통과 |
| `approved_review_report_request.json` | `review_report` | `ready_for_draft` | 통과 |
| `blocked_real_value_like_request.json` | `unknown` | `blocked` | 통과 |

## payload 및 validation 검증

유지된 기준:

- `ready_for_draft`와 `needs_more_input`만 HWPX payload 생성
- `needs_security_review`는 payload 미생성
- `blocked`는 payload 미생성
- 생성된 payload 4종 validation 통과
- 차단 대상 2종 validation skipped 유지

## dry-run 검증

| fixture | 기대 상태 | 확인 상태 |
|---|---|---|
| `safe_one_page_report_request.json` | `dry_run_ready` | 일치 |
| `missing_project_plan_request.json` | `dry_run_ready_with_missing_fields` | 일치 |
| `missing_result_report_request.json` | `dry_run_ready_with_missing_fields` | 일치 |
| `approved_review_report_request.json` | `dry_run_ready` | 일치 |
| `review_report_needs_security_review.json` | `skipped_security_review` | 일치 |
| `blocked_real_value_like_request.json` | `skipped_blocked` | 일치 |

## mapped HWPX 렌더링 검증

| fixture | status | remaining_placeholders | errors |
|---|---|---|---|
| `safe_one_page_report_request.json` | `rendered` | 0 | 0 |
| `missing_project_plan_request.json` | `rendered` | 0 | 0 |
| `missing_result_report_request.json` | `rendered` | 0 | 0 |
| `approved_review_report_request.json` | `rendered` | 0 | 0 |

## output summary 갱신 메모

초기 sandbox 실행에서는 일부 summary JSON 쓰기가 `PermissionError`로 skipped되었습니다.

원인 판단:

- PowerShell temp write는 가능
- sandbox 안의 미승인 Python write에서만 PermissionError 발생
- normalizer 로직 실패가 아니라 실행 권한 차이로 판단

조치:

- summary JSON 갱신이 필요한 앞 단계 스크립트는 권한 승인 후 재실행
- `placeholder_confirmed_values_summary.json`, `normalization_summary.json`, `hwpx_payload_mapping_summary.json`, `hwpx_payload_validation_summary.json` 갱신 확인
- `hwpx_renderer_dry_run_summary.json`, `mapped_hwpx_render_summary.json` 생성 확인

## Git 상태

회귀 테스트 실행 중 tracked Python cache가 일부 변경되었으나 테스트 부산물이므로 원복했습니다.

유지 기준:

- normalizer 코드 변경 없음
- renderer 코드 변경 없음
- fixture JSON 변경 없음
- routing 결과 변경 없음
- HWPX payload 구조 변경 없음
- output과 로컬 HWPX 템플릿은 Git 제외 유지

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX 원본 파일 추가 없음
- Email, API, Make.com 연동 없음

## 결론

normalizers 회귀 테스트 묶음은 현재 저장소 상태에서 유지됩니다.

Phase 2 최소 PoC 흐름은 다음 기준을 만족합니다.

- helper fixture 통과
- routing fixture 6종 통과
- payload 생성 및 차단 기준 유지
- validation 기준 유지
- dry-run 상태 기대값 일치
- mapped HWPX 4종 rendered
- mapped HWPX 4종 remaining placeholders 0

다음 단계는 Phase 2 마무리 판단과 Phase 3 진입 조건 문서화 여부를 결정하는 것입니다.
