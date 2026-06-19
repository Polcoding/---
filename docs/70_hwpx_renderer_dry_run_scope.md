# HWPX 렌더러 연결 dry-run 범위

## 목적

이 문서는 normalizer mapper payload를 기존 HWPX 렌더러 흐름에 연결하기 전, 어느 수준까지 dry-run으로 확인할지 정합니다.

이번 단계의 목표는 실제 HWPX 파일 생성이 아니라, mapper payload가 HWPX 렌더러의 입력 조건, 템플릿 후보, 라우팅 기준을 만족하는지 확인하는 것입니다.

## 결론

dry-run에서는 실제 HWPX 파일을 생성하지 않습니다.

허용 범위:

- mapper payload 생성
- HWPX validation 통과 여부 확인
- placeholder map 생성 가능 여부 확인
- 문서 유형별 template 후보 경로 계산
- template 존재 여부 확인
- 렌더링을 진행했다면 어떤 상태가 되었을지 요약

금지 범위:

- `replace_placeholders_in_hwpx` 호출
- 실제 HWPX output 생성
- 실제 HWPX 템플릿 추가
- 실제 기관 양식 사용
- 기존 renderer output 덮어쓰기

## 라우팅 기준

| routing | dry-run 상태 | 실제 HWPX 생성 |
|---|---|---|
| `ready_for_draft` | `dry_run_ready` 또는 `template_required` | 생성하지 않음 |
| `needs_more_input` | `dry_run_ready_with_missing_fields` 또는 `template_required` | 생성하지 않음 |
| `needs_security_review` | `skipped_security_review` | 생성하지 않음 |
| `blocked` | `skipped_blocked` | 생성하지 않음 |

`needs_more_input`은 실제값을 채우지 않고 `[확인 필요]` 중심 placeholder map 생성 가능 여부만 확인합니다.

## 확인 항목

dry-run은 각 fixture별로 다음을 확인합니다.

- 정규화 결과의 `routing_decision.status`
- HWPX payload 생성 여부
- `validate_for_hwpx_rendering` 통과 여부
- `build_placeholder_map` 성공 여부
- template 후보 파일명
- template 존재 여부
- 실제 렌더링 없이 예상 상태 산출

## template 후보

| document_type | template 후보 |
|---|---|
| `one_page_report` | `templates/hwpx/placeholder_one_page_report.hwpx` |
| `project_plan` | `templates/hwpx/placeholder_project_plan.hwpx` |
| `result_report` | `templates/hwpx/placeholder_result_report.hwpx` |
| `review_report` | `templates/hwpx/placeholder_review_report.hwpx` |

로컬 템플릿은 Git 제외 대상입니다. dry-run은 템플릿 존재 여부만 기록하고 파일 내용은 읽지 않습니다.

## output 정책

dry-run summary는 `normalizers/output/hwpx_renderer_dry_run_summary.json`에 생성합니다.

이 output은 Git 제외 대상입니다.

## 완료 조건

- `ready_for_draft` 케이스가 validation과 placeholder map 생성을 통과
- `needs_more_input` 케이스가 validation과 placeholder map 생성을 통과
- `needs_security_review` 케이스가 렌더링 대상에서 제외
- `blocked` 케이스가 렌더링 대상에서 제외
- 실제 HWPX 파일 생성 없음
- 실제 원문, 개인정보, 기관 양식 사용 없음

## 다음 단계

dry-run이 통과하면, 이후 별도 단계에서 사용자가 허용한 로컬 placeholder 템플릿에 한해 실제 HWPX 렌더링 연결 테스트를 검토할 수 있습니다.
