# 정규화 결과와 HWPX 렌더러 입력 매핑 범위

## 목적

이 문서는 `normalizers/` PoC가 만든 정규화 결과를 기존 HWPX 렌더러가 받는 AI 출력 JSON 구조로 변환할 때의 최소 매핑 범위를 정합니다.

현재 단계에서는 정규화 결과를 HWPX 렌더러에 직접 연결하지 않습니다. 먼저 변환 계층의 필드 대응과 중단 조건을 확정합니다.

## 결론

정규화 결과와 HWPX 렌더러 입력 사이에는 별도 변환 계층을 둡니다.

```text
normalized_request
→ security_filter
→ hwpx_payload_mapper
→ renderers/hwpx_renderer
```

이유:

- 정규화 스키마와 렌더러 입력 JSON의 목적이 다릅니다.
- `routing_decision`이 안전하지 않은 입력은 렌더러로 넘기지 않아야 합니다.
- `security_flags`를 기존 `security_review` 구조로 명확히 변환해야 합니다.
- 나중에 Markdown 미리보기 또는 Email 초안으로 확장할 때도 같은 정규화 결과를 재사용할 수 있습니다.

## 매핑 대상

이번 매핑 PoC는 HWPX 보고서 4종만 대상으로 합니다.

- `one_page_report`
- `project_plan`
- `result_report`
- `review_report`

공문, XLSX 조사표, Email 초안은 이번 매핑 범위에서 제외합니다.

## 라우팅 기준

| `routing_decision.status` | HWPX payload 생성 | 이유 |
|---|---|---|
| `ready_for_draft` | 생성 가능 | placeholder 기반 초안 생성 가능 |
| `needs_more_input` | 제한 생성 가능 | `[확인 필요]` 중심 payload 생성 가능 |
| `needs_security_review` | 생성하지 않음 | 사람 보안 검토 전 렌더링 보류 |
| `blocked` | 생성하지 않음 | 처리 중단 |

`needs_more_input`은 실제값이 아니라 확인 필요 placeholder를 렌더링하는 목적에 한해 허용합니다.

## 공통 필드 매핑

| 정규화 필드 | HWPX 렌더러 입력 필드 | 비고 |
|---|---|---|
| `normalized_request_id` | `request_id` | 실제 접수번호 금지 |
| `user_intent_summary` | `input_summary` | 비식별 요약만 |
| `requested_task` | `task_type` | `draft_document` |
| `candidate_document_type` | `document_type` | HWPX 보고서 4종 |
| `output_targets` | `output_targets` | `hwpx` 포함 필요 |
| `security_flags` | `security_review` | 별도 변환 |
| `missing_fields` | `missing_fields` | 그대로 유지 |
| `human_review_required` | `human_review_required` | 항상 `true` |
| `content_inputs` | `documents[0]` | 문서 유형별 매핑 |
| `routing_decision` | `draft_status`, `assumptions`, `checklist` | 상태와 검토 항목에 반영 |

## security_flags → security_review

| `security_flags` | `security_review` |
|---|---|
| `risk_level_hint` | `risk_level` |
| `suspected_personal_info` | `contains_personal_info` |
| `suspected_sensitive_info` | `contains_sensitive_info` |
| `suspected_internal_info` | `contains_internal_info` |
| `block_reason` | `blocked_items`, `notes` |
| `requires_security_review` | `required_review` |

변환 규칙:

- `routing_decision.status`가 `blocked`이면 `allowed_processing`은 `false`
- `routing_decision.status`가 `needs_security_review`이면 `allowed_processing`은 `false`
- `routing_decision.status`가 `ready_for_draft` 또는 `needs_more_input`이면 `allowed_processing`은 `true`
- `required_review`에는 항상 `human_review`를 포함
- 보안 검토가 필요하면 `security_review`를 추가

## draft_status 매핑

| routing | draft_status |
|---|---|
| `ready_for_draft` | `draft` |
| `needs_more_input` | `needs_input` |
| `needs_security_review` | `blocked` |
| `blocked` | `blocked` |

`needs_security_review`는 렌더링 보류를 강제하기 위해 HWPX payload를 생성하지 않는 것이 원칙입니다.

## documents[0] 매핑

### one_page_report

| `content_inputs` | `documents[0]` |
|---|---|
| `title_hint` | `title` |
| `purpose` | `report_summary` |
| `background` | `background` |
| `main_points` | `main_points` |
| `risks` | `issues_or_considerations` |
| `next_steps` | `next_steps`, `action_items` |

기본값:

- `review_opinion`: `[검토 의견 확인 필요]`
- `checklist`: placeholder 기반 검토 항목

### project_plan

| `content_inputs` | `documents[0]` |
|---|---|
| `title_hint` | `title` |
| `background` | `background` |
| `purpose` | `purpose` |
| `main_points` | `main_contents` |
| `schedule` | `schedule` |
| `budget` | `budget` |
| `next_steps` | `future_plan` |
| `risks` | `review_items` |

기본값:

- `overview`: `[사업명ㆍ추진기간ㆍ추진대상ㆍ추진방식ㆍ소요예산 확인 필요]`
- `detailed_plan`: `[단계별 세부 추진내용 확인 필요]`
- `expected_effects`: `[기대효과 확인 필요]`

### result_report

| `content_inputs` | `documents[0]` |
|---|---|
| `title_hint` | `title` |
| `background` | `linked_plan_reference` |
| `purpose` | `overview` |
| `main_points` | `planned_items` |
| `results_or_metrics` | `actual_results` |
| `schedule` | `comparison_to_plan` |
| `risks` | `issues` |
| `next_steps` | `future_plan` |

기본값:

- `main_outcomes`: `[주요성과 확인 필요]`
- `improvements`: `[개선사항 확인 필요]`

### review_report

검토보고서는 기본적으로 `needs_security_review`로 라우팅되므로 HWPX payload 생성 대상이 아닙니다.

향후 사람이 보안 검토 후 허용한 경우에만 다음 매핑을 적용합니다.

| `content_inputs` | `documents[0]` |
|---|---|
| `title_hint` | `title` |
| `background` | `review_background` |
| `purpose` | `review_scope` |
| `main_points` | `review_items` |
| `risks` | `risks` |
| `next_steps` | `next_actions` |

기본값:

- `review_opinion`: `[검토 의견 확인 필요]`
- `required_reviews`: `[법무ㆍ계약ㆍ개인정보 검토 필요 여부 확인]`

## renderer_hints 매핑

HWPX payload에는 다음 힌트를 포함합니다.

```json
{
  "target_format": "hwpx",
  "template_id": "[템플릿 ID 확인 필요]",
  "requires_hwpx": true,
  "requires_manual_review": true
}
```

템플릿 ID는 문서 유형별 로컬 placeholder 템플릿 후보와 연결합니다.

| document_type | template_id |
|---|---|
| `one_page_report` | `placeholder_one_page_report` |
| `project_plan` | `placeholder_project_plan` |
| `result_report` | `placeholder_result_report` |
| `review_report` | `placeholder_review_report` |

## 매핑 fixture 기준

매핑 fixture는 Git에 포함할 수 있습니다.

조건:

- 정규화 fixture와 동일하게 placeholder 기반
- 실제 원문, 개인정보, 기관명, 문서번호 없음
- `needs_security_review`와 `blocked`는 payload 미생성 결과를 검증
- output 산출물은 Git 제외

## 다음 단계

다음 작업은 `normalizers/hwpx_payload_mapper_poc.py`를 작성하고, 정규화 결과를 HWPX 렌더러 입력 JSON 구조로 변환하는 최소 PoC를 검증하는 것입니다.
