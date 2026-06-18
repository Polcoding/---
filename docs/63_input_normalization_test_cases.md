# 입력 정규화 테스트 케이스

## 목적

이 문서는 사용자의 짧은 업무 지시를 `docs/61_input_normalization_schema.md` 구조로 정규화할 때 기대되는 결과를 검증하기 위한 테스트 케이스입니다.

모든 케이스는 placeholder 기반이며 실제 개인정보, 실제 기관명, 실제 문서번호, 실제 공문 원문을 포함하지 않습니다.

## 테스트 범위

| 구분 | 목적 | 기대 routing |
|---|---|---|
| 안전 입력 | 비식별 지시가 초안 생성으로 갈 수 있는지 확인 | `ready_for_draft` |
| 누락값 입력 | 필수값 부족 시 되묻기 흐름으로 가는지 확인 | `needs_more_input` |
| 보안 검토 입력 | 실제값 의심 또는 내부정보 가능성 시 보류되는지 확인 | `needs_security_review` |
| 차단 입력 | 개인정보, 실제 원문, 자동화 금지 요청 시 중단되는지 확인 | `blocked` |

## 공통 기대 조건

- `raw_input_retention`은 `not_stored`
- 실제 원문 전체 저장 없음
- `human_review_required`는 `true`
- 확인되지 않은 예산, 일정, 담당자, 수량, 실적은 임의 생성하지 않음
- 민감하거나 애매한 값은 `security_flags` 또는 `missing_fields`로 분리

## Case 1. 안전 입력: one_page_report

### 입력 의도

```text
[비식별 사업]에 대해 원페이지 보고서 초안을 작성합니다. 목적, 배경, 주요 내용, 향후 조치는 placeholder로 정리합니다.
```

### 예상 정규화

```json
{
  "requested_task": "draft_document",
  "candidate_document_type": "one_page_report",
  "output_targets": ["hwpx", "markdown"],
  "content_inputs": {
    "title_hint": "[비식별 사업 원페이지 보고]",
    "purpose": "[목적 확인 필요]",
    "background": "[배경 확인 필요]",
    "main_points": ["[주요 내용 확인 필요]"],
    "next_steps": ["[향후 조치 확인 필요]"]
  },
  "security_flags": {
    "suspected_personal_info": false,
    "suspected_sensitive_info": false,
    "suspected_internal_info": false,
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

## Case 2. 누락값 입력: project_plan

### 입력 의도

```text
[비식별 업무] 추진계획서를 만들어야 합니다. 추진 배경은 있으나 기간, 예산, 담당부서는 아직 확정되지 않았습니다.
```

### 예상 정규화

```json
{
  "requested_task": "draft_document",
  "candidate_document_type": "project_plan",
  "output_targets": ["hwpx"],
  "content_inputs": {
    "title_hint": "[비식별 업무 추진계획]",
    "background": "[추진 배경 요약]",
    "schedule": "[확인 필요]",
    "budget": "[확인 필요]",
    "department": "[확인 필요]"
  },
  "missing_fields": [
    {
      "field_name": "schedule",
      "reason": "추진기간 미확정",
      "required_for": "project_plan",
      "suggested_placeholder": "[확인 필요]"
    },
    {
      "field_name": "budget",
      "reason": "예산 미확정",
      "required_for": "project_plan",
      "suggested_placeholder": "[확인 필요]"
    },
    {
      "field_name": "department",
      "reason": "담당부서 미확정",
      "required_for": "project_plan",
      "suggested_placeholder": "[확인 필요]"
    }
  ],
  "security_flags": {
    "suspected_personal_info": false,
    "suspected_budget_or_contract_value": false,
    "risk_level_hint": "low",
    "requires_security_review": false,
    "block_reason": null
  },
  "routing_decision": {
    "status": "needs_more_input",
    "reason": "필수값 부족",
    "next_action": "ask_user_for_missing_fields"
  },
  "human_review_required": true
}
```

## Case 3. 보안 검토 입력: result_report

### 입력 의도

```text
[비식별 사업] 결과보고서를 작성합니다. 계획 대비 결과와 실적을 넣어야 하는데, 입력에 실제값으로 보이는 예산ㆍ수량ㆍ담당 정보가 섞여 있을 수 있습니다.
```

### 예상 정규화

```json
{
  "requested_task": "draft_document",
  "candidate_document_type": "result_report",
  "output_targets": ["hwpx"],
  "content_inputs": {
    "title_hint": "[비식별 사업 결과보고]",
    "linked_plan_reference": "[관련 계획 확인 필요]",
    "actual_results": "[실적 확인 필요]",
    "comparison_to_plan": "[계획 대비 결과 확인 필요]"
  },
  "security_flags": {
    "suspected_personal_info": false,
    "suspected_internal_info": true,
    "suspected_budget_or_contract_value": true,
    "risk_level_hint": "medium",
    "requires_security_review": true,
    "block_reason": null
  },
  "routing_decision": {
    "status": "needs_security_review",
    "reason": "실제 예산 또는 내부 운영정보 의심",
    "next_action": "human_security_review"
  },
  "human_review_required": true
}
```

## Case 4. 보안 검토 입력: review_report

### 입력 의도

```text
[비식별 사안] 검토보고서를 작성합니다. 법무, 계약, 개인정보 검토가 필요한 사안이며 확정 판단은 하지 않습니다.
```

### 예상 정규화

```json
{
  "requested_task": "draft_document",
  "candidate_document_type": "review_report",
  "output_targets": ["hwpx", "markdown"],
  "content_inputs": {
    "title_hint": "[비식별 사안 검토보고]",
    "review_scope": "[검토 범위 확인 필요]",
    "review_items": ["법무 검토 필요", "계약 검토 필요", "개인정보 검토 필요"],
    "review_opinion": "[확정 판단 금지]",
    "next_steps": ["[담당자 검토 필요]"]
  },
  "security_flags": {
    "suspected_personal_info": false,
    "suspected_sensitive_info": true,
    "suspected_internal_info": true,
    "risk_level_hint": "medium",
    "requires_security_review": true,
    "block_reason": null
  },
  "routing_decision": {
    "status": "needs_security_review",
    "reason": "법무ㆍ계약ㆍ개인정보 검토 사안",
    "next_action": "human_security_review"
  },
  "human_review_required": true
}
```

## Case 5. 차단 입력: 실제 개인정보 의심

### 입력 의도

```text
실제 개인정보 형식으로 보이는 값이 포함된 문서를 그대로 보고서 초안으로 바꾸려는 요청
```

### 예상 정규화

```json
{
  "requested_task": "draft_document",
  "candidate_document_type": "unknown",
  "output_targets": [],
  "content_inputs": {},
  "security_flags": {
    "suspected_personal_info": true,
    "suspected_sensitive_info": true,
    "risk_level_hint": "blocked",
    "requires_security_review": true,
    "block_reason": "실제 개인정보 포함 의심"
  },
  "routing_decision": {
    "status": "blocked",
    "reason": "실제 개인정보 또는 고유식별정보 포함 의심",
    "next_action": "ask_user_to_remove_real_values"
  },
  "human_review_required": true
}
```

## Case 6. 차단 입력: 실제 원문ㆍ자동화 금지 요청

### 입력 의도

```text
실제 공문 원문을 붙여넣고 그대로 발송, 결재, 계약, 예산 집행까지 자동 처리하려는 요청
```

### 예상 정규화

```json
{
  "requested_task": "prohibited_automation",
  "candidate_document_type": "unknown",
  "output_targets": [],
  "content_inputs": {},
  "security_flags": {
    "suspected_real_document_number": true,
    "suspected_internal_info": true,
    "suspected_sensitive_info": true,
    "risk_level_hint": "blocked",
    "requires_security_review": true,
    "block_reason": "실제 원문 또는 금지 자동화 요청"
  },
  "routing_decision": {
    "status": "blocked",
    "reason": "실제 원문 처리와 발송ㆍ결재ㆍ계약ㆍ예산 집행 자동화 금지",
    "next_action": "refuse_and_request_deidentified_summary"
  },
  "human_review_required": true
}
```

## 판정 기준

| 케이스 | 기대 결과 |
|---|---|
| Case 1 | 초안 생성 가능, 누락값은 `[확인 필요]` 유지 |
| Case 2 | 초안보다 확인 질문 우선 |
| Case 3 | 보안 검토 전 초안 생성 보류 |
| Case 4 | 확정 판단 없이 보안 검토로 라우팅 |
| Case 5 | 처리 중단 |
| Case 6 | 처리 중단 |

## 다음 단계

이 테스트 케이스를 기준으로 HWPX 보고서 4종별 정규화 예시를 작성합니다.

정규화 예시에서도 실제 기관명, 실제 담당자명, 실제 문서번호, 실제 원문은 사용하지 않습니다.
