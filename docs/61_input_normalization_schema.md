# 입력 정규화 스키마 초안

## 목적

이 문서는 사용자의 짧은 업무 지시를 AI 출력 JSON으로 보내기 전에 표준 입력 구조로 정리하기 위한 초안입니다.

입력 정규화는 실제 원문을 저장하거나 외부 AI에 그대로 보내기 위한 절차가 아닙니다. 사용자의 지시에서 문서 유형, 목적, 확인 필요 값, 보안 위험을 분리하기 위한 중간 단계입니다.

## 기본 원칙

- 실제 원문 전체를 저장하지 않습니다.
- 실제 개인정보, 민감정보, 내부 운영정보는 정규화 입력에 포함하지 않습니다.
- 위험하거나 애매한 값은 `security_flags`와 `missing_fields`로 분리합니다.
- 예산, 일정, 실적, 담당자, 수량은 사용자가 명확히 제공하지 않으면 임의 생성하지 않습니다.
- 정규화 결과는 초안 생성 전 사람 검토 또는 보안 필터 검토를 통과해야 합니다.

## 표준 입력 구조

```json
{
  "normalized_request_id": "[정규화 요청 ID placeholder]",
  "source_channel": "[manual_input]",
  "raw_input_retention": "not_stored",
  "user_intent_summary": "[비식별 업무 지시 요약]",
  "requested_task": "draft_document",
  "candidate_document_type": "project_plan",
  "output_targets": ["hwpx", "markdown"],
  "content_inputs": {},
  "known_values": {},
  "missing_fields": [],
  "security_flags": {},
  "routing_decision": {},
  "human_review_required": true
}
```

## 필드 정의

| 필드 | 설명 | 비고 |
|---|---|---|
| `normalized_request_id` | 정규화 요청 식별자 | 실제 접수번호나 문서번호 금지 |
| `source_channel` | 입력 경로 | `manual_input`, `memo`, `email_summary` 등 |
| `raw_input_retention` | 원문 저장 여부 | 기본값 `not_stored` |
| `user_intent_summary` | 비식별 업무 지시 요약 | 실제 원문 복사 금지 |
| `requested_task` | 요청 작업 | `draft_document`, `draft_email`, `create_table` |
| `candidate_document_type` | 후보 문서 유형 | HWPX 보고서 4종 우선 |
| `output_targets` | 희망 출력 | `hwpx`, `markdown`, `xlsx`, `email` |
| `content_inputs` | 본문 구성에 필요한 입력 | 비식별 값만 |
| `known_values` | 사용자가 명확히 제공한 값 | 실제 민감정보 제외 |
| `missing_fields` | 확인 필요 값 | 누락값 본문 혼입 방지 |
| `security_flags` | 보안 위험 신호 | 보안 필터 입력 |
| `routing_decision` | 다음 처리 흐름 | 생성, 보류, 차단 |
| `human_review_required` | 사람 검토 필요 여부 | 기본값 `true` |

## 문서 유형 분류 기준

| 후보 유형 | 주요 신호 | 비고 |
|---|---|---|
| `one_page_report` | "간단히 보고", "원페이지", "요약 보고", "검토해서 보고" | 짧은 보고용 |
| `project_plan` | "추진계획", "계획서", "추진하려고 함", "일정/예산/추진내용" | 계획 수립 |
| `result_report` | "결과보고", "추진 결과", "실적", "계획 대비" | 기존 계획과 연결 |
| `review_report` | "검토보고", "검토 의견", "위험요소", "법무/계약/개인정보 검토" | 확정 판단 금지 |
| `survey_table` | "조사표", "현황표", "엑셀", "취합" | XLSX 우선 |
| `vendor_email` | "업체에 메일", "자료 요청", "견적 문의" | 자동 발송 금지 |

문서 유형이 애매하면 `candidate_document_type`을 `unknown`으로 두고 `missing_fields`에 확인 필요 항목을 추가합니다.

## content_inputs 구조

HWPX 보고서 4종은 다음 공통 입력을 우선 수집합니다.

```json
{
  "title_hint": "[제목 힌트 확인 필요]",
  "purpose": "[목적 확인 필요]",
  "background": "[배경 확인 필요]",
  "main_points": ["[주요 내용 확인 필요]"],
  "schedule": "[일정 확인 필요]",
  "budget": "[예산 확인 필요]",
  "department": "[담당부서 확인 필요]",
  "results_or_metrics": "[실적 수치 확인 필요]",
  "risks": ["[위험요소 확인 필요]"],
  "next_steps": ["[후속조치 확인 필요]"]
}
```

실제 값이 없는 항목은 생성하지 않고 `[확인 필요]` 또는 `missing_fields`로 분리합니다.

## known_values 구조

`known_values`에는 사용자가 명확히 제공했고 보안상 허용되는 값만 넣습니다.

허용 예:

- 비식별 사업명 placeholder
- 일반적인 목적 설명
- 공개 가능한 일정 범위 placeholder
- 사용자가 제공한 비식별 대상 범위

금지 예:

- 실제 사람 이름
- 실제 연락처
- 실제 이메일
- 실제 문서번호
- 실제 민원번호
- 실제 차량번호
- 실제 내부 시스템명
- 실제 예산액 또는 견적 금액

## missing_fields 구조

```json
[
  {
    "field_name": "[확인 필요 항목명]",
    "reason": "[필요 사유]",
    "required_for": "[문서 유형 또는 섹션]",
    "suggested_placeholder": "[확인 필요]"
  }
]
```

누락값은 본문에 자연스럽게 꾸며 넣지 않고 `missing_fields`에 분리합니다.

## security_flags 구조

```json
{
  "suspected_personal_info": false,
  "suspected_sensitive_info": false,
  "suspected_internal_info": false,
  "suspected_real_document_number": false,
  "suspected_real_case_number": false,
  "suspected_budget_or_contract_value": false,
  "risk_level_hint": "low",
  "requires_security_review": true,
  "block_reason": null
}
```

## routing_decision 구조

| 값 | 의미 |
|---|---|
| `ready_for_draft` | 초안 생성 가능 |
| `needs_more_input` | 필수값 부족 |
| `needs_security_review` | 보안 검토 필요 |
| `blocked` | 처리 중단 |

예시:

```json
{
  "status": "needs_more_input",
  "reason": "[예산과 추진기간 확인 필요]",
  "next_action": "ask_user_for_missing_fields"
}
```

## 차단 조건

다음이 감지되면 `routing_decision.status`를 `blocked` 또는 `needs_security_review`로 둡니다.

- 실제 개인정보 포함 의심
- 민원번호, 접수번호, 사건번호 포함 의심
- 실제 문서번호 포함 의심
- 차량번호, 장비현황, 내부 운영정보 포함 의심
- 감사, 징계, 인사, 수사, 보안 관련 문서
- 대외비, 비공개, 내부전용 표시 문서
- 실제 계약 조건, 견적 금액, 업체 평가 의견 포함 의심

## HWPX 보고서 4종 연결

정규화 결과는 `docs/60_hwpx_report_input_requirements.md`의 필수 입력값으로 매핑합니다.

| 정규화 필드 | one_page_report | project_plan | result_report | review_report |
|---|---|---|---|---|
| `title_hint` | `title` | `title` | `title` | `title` |
| `purpose` | `report_summary` | `purpose` | `overview` | `review_scope` |
| `background` | `background` | `background` | `linked_plan_reference` | `review_background` |
| `main_points` | `main_points` | `main_contents` | `planned_items` | `review_items` |
| `schedule` | `next_steps` | `schedule` | `comparison_to_plan` | `next_actions` |
| `budget` | `issues_or_considerations` | `budget` | `actual_results` | `risks` |
| `results_or_metrics` | `review_opinion` | `review_items` | `actual_results` | `review_opinion` |
| `risks` | `issues_or_considerations` | `review_items` | `issues` | `risks` |
| `next_steps` | `next_steps` | `future_plan` | `future_plan` | `next_actions` |

## 다음 단계

이 스키마를 기준으로 다음 문서를 작성합니다.

- 보안 필터 요구사항
- 입력 정규화 테스트 케이스
- HWPX 보고서 4종별 정규화 예시
- `needs_more_input` 상황에서 사용자에게 되묻는 질문 목록
