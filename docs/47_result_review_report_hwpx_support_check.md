# 결과보고서ㆍ검토보고서 HWPX 렌더러 지원 확인

## 현재 기준 안내

이 문서는 결과보고서와 검토보고서 로컬 템플릿을 만들기 전 지원 여부를 확인한 기록입니다.

현재는 `result_report`와 `review_report` 모두 로컬 placeholder HWPX 템플릿 치환과 한컴 수동 열람 검수가 완료되었습니다. 최신 결과는 `docs/50_result_report_hwpx_render_test_result.md`, `docs/52_review_report_hwpx_render_test_result.md`, `docs/57_hwpx_report_4types_completion_and_safety_rehearsal.md`를 우선 확인합니다.

## 목적

실제 기관 양식을 투입하기 전에 `result_report`와 `review_report` 샘플 JSON이 HWPX 렌더러에서 처리 가능한지 확인합니다.

이번 단계에서는 실제 HWPX 템플릿을 만들거나 실제 기관 양식을 사용하지 않습니다.

## 확인 대상

- `examples/json/sample_result_report.json`
- `examples/json/sample_review_report.json`
- `renderers/hwpx_renderer/template_package.py`
- `renderers/hwpx_renderer/render_hwpx_poc.py`
- `renderers/hwpx_renderer/validation.py`

## 보강 내용

### result_report placeholder

다음 placeholder를 허용하고 전용 map을 구성했습니다.

- `{{title}}`
- `{{linked_plan_reference}}`
- `{{overview_table}}`
- `{{planned_items}}`
- `{{actual_results}}`
- `{{comparison_to_plan}}`
- `{{main_outcomes}}`
- `{{issues}}`
- `{{improvements}}`
- `{{future_plan}}`
- `{{missing_fields}}`
- `{{checklist}}`
- `{{security_review}}`
- `{{draft_status}}`
- `{{human_review_required}}`

### review_report placeholder

다음 placeholder를 허용하고 전용 map을 구성했습니다.

- `{{title}}`
- `{{review_background}}`
- `{{review_scope}}`
- `{{review_items}}`
- `{{review_opinion}}`
- `{{risks}}`
- `{{required_reviews}}`
- `{{next_actions}}`
- `{{missing_fields}}`
- `{{checklist}}`
- `{{security_review}}`
- `{{draft_status}}`
- `{{human_review_required}}`

## 보안 검증 보정

`sample_result_report.json`의 `예산 집행액`은 확정된 예산 집행을 의미하는 값이 아니라 누락 필드명입니다.

따라서 `예산 집행액` 문구는 확정 표현 차단에서 제외하도록 보정했습니다. 실제 금액이나 실제 집행 사실을 생성하거나 허용한 것은 아닙니다.

## 테스트 결과

| 샘플 | placeholder map | 보안 검증 | 렌더링 결과 | 판정 |
|---|---|---|---|---|
| `sample_result_report.json` | 필수 placeholder 누락 없음 | 통과 | `rendered` | 로컬 placeholder 템플릿 치환 및 수동 검수 완료 |
| `sample_review_report.json` | 필수 placeholder 누락 없음 | 통과 | `rendered` | 로컬 placeholder 템플릿 치환 및 수동 검수 완료 |

기존 샘플 회귀 확인:

| 샘플 | 결과 | 판정 |
|---|---|---|
| `sample_one_page_report.json` | `rendered` | 통과 |
| `sample_official_letter.json` | `rendered` | 통과 |
| `sample_project_plan.json` | `rendered` | 로컬 placeholder 템플릿 치환 및 수동 검수 완료 |

## Git 제외 확인

- `renderers/hwpx_renderer/output/hwpx_render_summary.json`: output `.gitignore`로 제외
- `renderers/hwpx_renderer/output/sample_result_report_poc.hwpx`: output `.gitignore`로 제외
- `renderers/hwpx_renderer/output/sample_review_report_poc.hwpx`: output `.gitignore`로 제외
- `templates/hwpx/placeholder_result_report.hwpx`: `templates/hwpx/.gitignore`로 제외
- `templates/hwpx/placeholder_review_report.hwpx`: `templates/hwpx/.gitignore`로 제외

## 보안 검수

- 실제 기관 양식 사용 여부: 사용하지 않음
- 실제 원문 사용 여부: 사용하지 않음
- 실제 개인정보 사용 여부: 사용하지 않음
- 실제 예산액, 실적 수치, 참여 인원 생성 여부: 생성하지 않음
- Email/API/Make.com 연동 여부: 수행하지 않음

## 결론

`result_report`와 `review_report`는 코드 수준 지원 확인 이후 로컬 placeholder HWPX 템플릿 치환과 수동 열람 검수까지 완료되었습니다.

다음 단계는 실제 기관 양식이 아닌 외부 복사본 기반 placeholder 전환 절차와 Phase 2 입력 정규화ㆍ보안 필터 설계를 이어가는 것입니다.
