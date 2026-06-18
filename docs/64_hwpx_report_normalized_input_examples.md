# HWPX 보고서 4종 정규화 예시

## 목적

이 문서는 HWPX 보고서 4종의 사용자 지시를 `docs/61_input_normalization_schema.md` 구조로 정규화하는 예시입니다.

예시는 모두 placeholder 기반입니다. 실제 기관명, 실제 담당자명, 실제 문서번호, 실제 원문, 실제 예산액, 실제 실적 수치를 포함하지 않습니다.

## 공통 원칙

- `raw_input_retention`은 `not_stored`로 둡니다.
- 실제값이 없거나 확인되지 않은 값은 `[확인 필요]` 또는 `missing_fields`로 분리합니다.
- `human_review_required`는 항상 `true`입니다.
- HWPX 렌더링은 로컬 placeholder 템플릿을 전제로 합니다.
- 보안 필터 결과가 `ready_for_draft`가 아니면 초안 생성 또는 렌더링을 진행하지 않습니다.

## one_page_report 예시

```json
{
  "normalized_request_id": "[정규화 요청 ID placeholder]",
  "source_channel": "manual_input",
  "raw_input_retention": "not_stored",
  "user_intent_summary": "[비식별 사업의 핵심 내용을 원페이지 보고서로 정리]",
  "requested_task": "draft_document",
  "candidate_document_type": "one_page_report",
  "output_targets": ["hwpx", "markdown"],
  "content_inputs": {
    "title_hint": "[비식별 사업 원페이지 보고]",
    "purpose": "[보고 목적 확인 필요]",
    "background": "[추진 배경 확인 필요]",
    "main_points": [
      "[주요 내용 1 확인 필요]",
      "[주요 내용 2 확인 필요]"
    ],
    "risks": [
      "[문제점 또는 고려사항 확인 필요]"
    ],
    "next_steps": [
      "[향후 조치 확인 필요]"
    ]
  },
  "known_values": {},
  "missing_fields": [
    {
      "field_name": "purpose",
      "reason": "보고 목적 미확정",
      "required_for": "one_page_report.report_summary",
      "suggested_placeholder": "[확인 필요]"
    }
  ],
  "security_flags": {
    "suspected_personal_info": false,
    "suspected_sensitive_info": false,
    "suspected_internal_info": false,
    "suspected_real_document_number": false,
    "suspected_budget_or_contract_value": false,
    "risk_level_hint": "low",
    "requires_security_review": false,
    "block_reason": null
  },
  "routing_decision": {
    "status": "ready_for_draft",
    "reason": "placeholder 기반 비식별 입력",
    "next_action": "draft_with_missing_fields"
  },
  "human_review_required": true
}
```

## project_plan 예시

```json
{
  "normalized_request_id": "[정규화 요청 ID placeholder]",
  "source_channel": "manual_input",
  "raw_input_retention": "not_stored",
  "user_intent_summary": "[비식별 업무의 추진계획서 초안 작성]",
  "requested_task": "draft_document",
  "candidate_document_type": "project_plan",
  "output_targets": ["hwpx", "markdown"],
  "content_inputs": {
    "title_hint": "[비식별 업무 추진계획]",
    "purpose": "[추진 목적 확인 필요]",
    "background": "[추진 배경 확인 필요]",
    "main_points": [
      "[세부 추진내용 확인 필요]"
    ],
    "schedule": "[추진 일정 확인 필요]",
    "budget": "[예산 확인 필요]",
    "department": "[담당부서 확인 필요]",
    "risks": [
      "[검토 필요사항 확인 필요]"
    ],
    "next_steps": [
      "[향후 계획 확인 필요]"
    ]
  },
  "known_values": {},
  "missing_fields": [
    {
      "field_name": "schedule",
      "reason": "추진 일정 미확정",
      "required_for": "project_plan.schedule",
      "suggested_placeholder": "[확인 필요]"
    },
    {
      "field_name": "budget",
      "reason": "예산 미확정",
      "required_for": "project_plan.budget",
      "suggested_placeholder": "[확인 필요]"
    }
  ],
  "security_flags": {
    "suspected_personal_info": false,
    "suspected_sensitive_info": false,
    "suspected_internal_info": false,
    "suspected_real_document_number": false,
    "suspected_budget_or_contract_value": false,
    "risk_level_hint": "low",
    "requires_security_review": false,
    "block_reason": null
  },
  "routing_decision": {
    "status": "needs_more_input",
    "reason": "일정과 예산 확인 필요",
    "next_action": "ask_user_for_missing_fields"
  },
  "human_review_required": true
}
```

## result_report 예시

```json
{
  "normalized_request_id": "[정규화 요청 ID placeholder]",
  "source_channel": "manual_input",
  "raw_input_retention": "not_stored",
  "user_intent_summary": "[비식별 사업의 추진 결과를 계획 대비로 정리]",
  "requested_task": "draft_document",
  "candidate_document_type": "result_report",
  "output_targets": ["hwpx", "markdown"],
  "content_inputs": {
    "title_hint": "[비식별 사업 결과보고]",
    "purpose": "[결과보고 목적 확인 필요]",
    "background": "[관련 추진계획 확인 필요]",
    "main_points": [
      "[계획 항목 확인 필요]"
    ],
    "results_or_metrics": "[실적 수치 확인 필요]",
    "schedule": "[계획 대비 일정 확인 필요]",
    "budget": "[예산 집행 여부 확인 필요]",
    "risks": [
      "[문제점 확인 필요]"
    ],
    "next_steps": [
      "[후속 조치 확인 필요]"
    ]
  },
  "known_values": {},
  "missing_fields": [
    {
      "field_name": "results_or_metrics",
      "reason": "실적 수치 미확정",
      "required_for": "result_report.actual_results",
      "suggested_placeholder": "[확인 필요]"
    },
    {
      "field_name": "budget",
      "reason": "예산 집행 정보 미확정",
      "required_for": "result_report.actual_results",
      "suggested_placeholder": "[확인 필요]"
    }
  ],
  "security_flags": {
    "suspected_personal_info": false,
    "suspected_sensitive_info": false,
    "suspected_internal_info": false,
    "suspected_real_document_number": false,
    "suspected_budget_or_contract_value": false,
    "risk_level_hint": "low",
    "requires_security_review": false,
    "block_reason": null
  },
  "routing_decision": {
    "status": "needs_more_input",
    "reason": "실적과 예산 집행 정보 확인 필요",
    "next_action": "ask_user_for_missing_fields"
  },
  "human_review_required": true
}
```

## review_report 예시

```json
{
  "normalized_request_id": "[정규화 요청 ID placeholder]",
  "source_channel": "manual_input",
  "raw_input_retention": "not_stored",
  "user_intent_summary": "[비식별 사안의 검토보고서 초안 작성]",
  "requested_task": "draft_document",
  "candidate_document_type": "review_report",
  "output_targets": ["hwpx", "markdown"],
  "content_inputs": {
    "title_hint": "[비식별 사안 검토보고]",
    "purpose": "[검토 목적 확인 필요]",
    "background": "[검토 배경 확인 필요]",
    "main_points": [
      "[검토 항목 확인 필요]"
    ],
    "risks": [
      "[위험요소 확인 필요]",
      "[추가 검토 필요사항 확인 필요]"
    ],
    "next_steps": [
      "[후속 검토 절차 확인 필요]"
    ]
  },
  "known_values": {},
  "missing_fields": [
    {
      "field_name": "review_scope",
      "reason": "검토 범위 미확정",
      "required_for": "review_report.review_scope",
      "suggested_placeholder": "[확인 필요]"
    },
    {
      "field_name": "required_reviews",
      "reason": "필요 검토 주체 미확정",
      "required_for": "review_report.required_reviews",
      "suggested_placeholder": "[확인 필요]"
    }
  ],
  "security_flags": {
    "suspected_personal_info": false,
    "suspected_sensitive_info": true,
    "suspected_internal_info": true,
    "suspected_real_document_number": false,
    "suspected_budget_or_contract_value": false,
    "risk_level_hint": "medium",
    "requires_security_review": true,
    "block_reason": null
  },
  "routing_decision": {
    "status": "needs_security_review",
    "reason": "검토보고서는 내부 판단 또는 민감 검토 항목 가능성 확인 필요",
    "next_action": "human_security_review"
  },
  "human_review_required": true
}
```

## 문서 유형별 기본 라우팅

| 문서 유형 | 안전 입력 | 필수값 부족 | 실제값 의심 | 민감정보 의심 |
|---|---|---|---|---|
| `one_page_report` | `ready_for_draft` | `needs_more_input` | `needs_security_review` | `blocked` |
| `project_plan` | `ready_for_draft` | `needs_more_input` | `needs_security_review` | `blocked` |
| `result_report` | `ready_for_draft` | `needs_more_input` | `needs_security_review` | `blocked` |
| `review_report` | `needs_security_review` | `needs_more_input` | `needs_security_review` | `blocked` |

검토보고서는 문서 성격상 내부 판단, 계약, 법무, 개인정보 검토가 섞일 가능성이 높으므로 기본값을 더 보수적으로 둡니다.

## 다음 단계

다음 작업은 입력 정규화 로직의 최소 구현 범위를 결정하는 것입니다.

구현 전에는 이 문서의 예시를 코드 테스트 fixture로 옮길지, 문서 기준으로만 둘지 먼저 결정합니다.
