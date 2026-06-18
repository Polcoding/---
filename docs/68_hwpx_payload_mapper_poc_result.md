# HWPX payload mapper PoC 결과

## 목적

`normalizers/hwpx_payload_mapper_poc.py`가 정규화 결과를 HWPX 렌더러 입력 JSON 형태로 변환할 수 있는지 확인합니다.

이번 단계에서는 실제 HWPX 렌더러를 호출하지 않습니다.

## 구현 파일

- `normalizers/hwpx_payload_mapper_poc.py`
- `normalizers/input_normalizer_poc.py`
- `normalizers/security_filter_poc.py`
- `normalizers/fixtures/*.json`

## 매핑 원칙

| routing | payload 생성 여부 |
|---|---|
| `ready_for_draft` | 생성 |
| `needs_more_input` | 생성 |
| `needs_security_review` | 미생성 |
| `blocked` | 미생성 |

`needs_more_input`은 실제값을 채우는 것이 아니라 `[확인 필요]` 중심 payload를 만드는 범위에서만 허용합니다.

## 실행 결과

Codex 번들 Python으로 `normalizers/hwpx_payload_mapper_poc.py`를 실행했습니다.

| fixture | routing | payload | 판정 |
|---|---|---|---|
| `blocked_real_value_like_request.json` | `blocked` | 미생성 | 통과 |
| `missing_project_plan_request.json` | `needs_more_input` | 생성 | 통과 |
| `missing_result_report_request.json` | `needs_more_input` | 생성 | 통과 |
| `review_report_needs_security_review.json` | `needs_security_review` | 미생성 | 통과 |
| `safe_one_page_report_request.json` | `ready_for_draft` | 생성 | 통과 |

## Git 제외 확인

- `normalizers/output/hwpx_payload_mapping_summary.json`은 Git 제외 대상입니다.
- `normalizers/output/normalization_summary.json`도 Git 제외 대상입니다.
- fixture JSON과 PoC 코드는 Git 포함 대상입니다.

## 보안 검수

- 실제 기관 양식 사용 여부: 사용하지 않음
- 실제 문서 원문 사용 여부: 사용하지 않음
- 실제 개인정보 사용 여부: 사용하지 않음
- 실제 기관명, 업체명, 담당자명 사용 여부: 사용하지 않음
- 실제 문서번호, 민원번호, 접수번호, 사건번호 사용 여부: 사용하지 않음
- 실제 예산액, 실적 수치, 수량 생성 여부: 생성하지 않음
- Email/API/Make.com 연동 여부: 수행하지 않음

## 결론

정규화 결과를 HWPX 렌더러 입력 JSON 형태로 변환하는 독립 mapper PoC가 통과했습니다.

다음 단계는 mapper가 생성한 payload를 기존 HWPX 렌더러 검증 규칙에 통과시키는지 확인하는 것입니다. 이때도 실제 HWPX 템플릿이나 실제 원문은 사용하지 않습니다.
