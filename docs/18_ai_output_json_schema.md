# AI 출력 JSON 스키마 정의

## 목적

이 문서는 AI가 생성한 행정문서 초안을 HWPX, XLSX, 이메일, Markdown 등으로 변환하기 위한 JSON 출력 구조를 정의합니다.

AI는 문장과 구조를 생성하고, 템플릿 렌더러는 폰트, 자간, 줄간격, 표 양식, 셀 서식 등을 적용합니다.

본 문서는 실제 코드 구현이 아니라 향후 개발을 위한 설계 문서입니다.

실제 원문, 실제 개인정보, 실제 내부 운영정보는 포함하지 않습니다.

## 기본 원칙

- 모든 출력은 초안입니다.
- 확인되지 않은 값은 "[확인 필요]" 또는 null로 표시합니다.
- AI는 날짜, 예산, 수신처, 담당자, 업체명, 수량을 임의 생성하지 않습니다.
- 개인정보와 민감정보는 출력 JSON에 직접 포함하지 않습니다.
- 보안 위험이 있는 경우 security_review 필드에 표시합니다.
- 사용자가 채워야 할 항목은 missing_fields에 분리합니다.
- HWPX와 XLSX의 서식은 JSON이 아니라 템플릿 엔진이 담당합니다.
- JSON은 문서 내용과 구조만 표현합니다.
- 모든 문서 결과물은 사람이 최종 검토해야 합니다.
- HWPX 생성 코드, XLSX 생성 코드, OpenAI API 코드, Make.com 자동화 코드, 이메일 자동화 코드는 이 문서에 작성하지 않습니다.

## 공통 최상위 JSON 구조

| 필드 | 유형 | 설명 |
|---|---|---|
| request_id | string 또는 null | 요청 식별용 placeholder입니다. 실제 접수번호나 문서번호를 넣지 않습니다. |
| input_summary | string | 입력 내용을 원문 요약이 아니라 비식별 업무 요청 수준으로 정리합니다. |
| task_type | string | draft_document, draft_email, create_table 등 작업 유형입니다. |
| document_type | string | 공문, 추진계획서, 결과보고서, 검토보고서, 조사표, 업체 메일 등 문서 유형입니다. |
| output_targets | array | markdown, hwpx, xlsx, email 등 희망 출력 대상입니다. |
| security_review | object | 개인정보, 민감정보, 내부정보 포함 여부와 처리 가능 여부를 표시합니다. |
| missing_fields | array | 사용자가 추가 확인해야 하는 값을 분리합니다. |
| assumptions | array | AI가 추론한 사항을 본문과 분리해 표시합니다. |
| draft_status | string | draft, needs_input, blocked 등 초안 상태입니다. |
| human_review_required | boolean | 사람 검토 필요 여부입니다. |
| documents | array | 생성할 문서 본문 구조입니다. |
| attachments | array | 붙임 또는 참고자료 placeholder 목록입니다. |
| email_draft | object 또는 null | 이메일 초안이 필요한 경우 사용합니다. |
| checklist | array | 문서 생성 후 검토 항목입니다. |
| renderer_hints | object | 템플릿 렌더러가 참고할 출력 형식 힌트입니다. |

## document_type 후보

보고서 중심 HWPX 자동화를 위해 다음 document_type 후보를 사용합니다.

- one_page_report
- project_plan
- result_report
- review_report
- survey_request_letter
- survey_table
- vendor_email

document_type은 실제 문서명이나 실제 파일명이 아니라 렌더러와 템플릿 선택을 위한 분류값입니다.

공통 예시:

```json
{
  "request_id": "[요청 ID placeholder]",
  "input_summary": "[비식별 업무 요청 요약]",
  "task_type": "draft_document",
  "document_type": "[문서 유형]",
  "output_targets": ["markdown", "hwpx"],
  "security_review": {
    "risk_level": "low",
    "contains_personal_info": false,
    "contains_sensitive_info": false,
    "contains_internal_info": false,
    "blocked_items": [],
    "allowed_processing": true,
    "required_review": ["human_review"],
    "notes": "[보안 검토 메모]"
  },
  "missing_fields": [
    {
      "field_name": "[확인 필요 항목]",
      "reason": "[필요 사유]",
      "required_for": "[문서 섹션]",
      "suggested_placeholder": "[확인 필요]"
    }
  ],
  "assumptions": [],
  "draft_status": "needs_input",
  "human_review_required": true,
  "documents": [],
  "attachments": [],
  "email_draft": null,
  "checklist": ["[검토 항목]"],
  "renderer_hints": {
    "target_format": "hwpx",
    "template_id": "[템플릿 ID 확인 필요]",
    "style_profile": "[확인 필요]",
    "requires_manual_review": true
  }
}
```

## security_review 필드

| 하위 필드 | 유형 | 설명 |
|---|---|---|
| risk_level | string | low, medium, high, blocked 중 하나를 사용합니다. |
| contains_personal_info | boolean | 개인정보 포함 여부입니다. 실제 개인정보를 값으로 넣지 않습니다. |
| contains_sensitive_info | boolean | 민감정보 포함 여부입니다. |
| contains_internal_info | boolean | 내부 운영정보 포함 여부입니다. |
| blocked_items | array | 처리 제외가 필요한 항목명을 placeholder로 표시합니다. |
| allowed_processing | boolean | 현재 입력으로 초안 생성이 가능한지 표시합니다. |
| required_review | array | human_review, privacy_review, security_review 등 필요한 검토입니다. |
| notes | string | 금지 기준 설명 또는 검토 메모입니다. |

risk_level 값:

- low
- medium
- high
- blocked

예시:

```json
{
  "risk_level": "medium",
  "contains_personal_info": false,
  "contains_sensitive_info": false,
  "contains_internal_info": false,
  "blocked_items": ["[실제 식별정보 제외 필요]"],
  "allowed_processing": true,
  "required_review": ["human_review", "privacy_review"],
  "notes": "[실제 개인정보 없이 placeholder 기준으로 검토]"
}
```

## missing_fields 필드

missing_fields는 사용자가 채워야 할 값을 본문과 분리하기 위한 배열입니다.

| 하위 필드 | 설명 |
|---|---|
| field_name | 확인이 필요한 항목명입니다. |
| reason | 해당 값이 필요한 이유입니다. |
| required_for | 필요한 문서 위치 또는 출력 대상입니다. |
| suggested_placeholder | 본문에 표시할 placeholder입니다. |

예시 항목:

```json
[
  {
    "field_name": "조사기준일",
    "reason": "조사표 기준 시점 확인 필요",
    "required_for": "현황조사표",
    "suggested_placeholder": "[조사기준일 확인 필요]"
  },
  {
    "field_name": "제출기한",
    "reason": "회신 요청 문구 작성에 필요",
    "required_for": "공문 본문",
    "suggested_placeholder": "[제출기한 확인 필요]"
  },
  {
    "field_name": "수신처",
    "reason": "공문 수신 영역 확인 필요",
    "required_for": "공문",
    "suggested_placeholder": "[수신처 확인 필요]"
  },
  {
    "field_name": "담당부서",
    "reason": "문의처 안내에 필요",
    "required_for": "본문 및 이메일 서명",
    "suggested_placeholder": "[담당부서 확인 필요]"
  },
  {
    "field_name": "예산",
    "reason": "예산 항목은 임의 생성 금지",
    "required_for": "추진계획서",
    "suggested_placeholder": "[소요예산 확인 필요]"
  },
  {
    "field_name": "행사일시",
    "reason": "행사 안내 일정 확인 필요",
    "required_for": "추진계획서",
    "suggested_placeholder": "[행사일시 확인 필요]"
  },
  {
    "field_name": "회신기한",
    "reason": "업체 메일 회신 요청에 필요",
    "required_for": "업체 연락 메일",
    "suggested_placeholder": "[회신기한 확인 필요]"
  }
]
```

## assumptions 필드

assumptions는 AI가 추론한 내용을 문서 본문과 분리해 명시하기 위한 필드입니다.

| 하위 필드 | 설명 |
|---|---|
| assumption | 추론한 내용입니다. |
| confidence | low, medium, high 등 추론 신뢰도입니다. |
| reason | 추론 근거입니다. |
| needs_confirmation | 사용자 확인 필요 여부입니다. |

추론은 확정 사실이 아니며, 문서 본문에서는 [확인 필요]로 표시해야 합니다.

```json
[
  {
    "assumption": "[추진기간은 별도 확인이 필요하다고 추정]",
    "confidence": "low",
    "reason": "[입력에 기간 정보가 없음]",
    "needs_confirmation": true
  }
]
```

## 공문 JSON 스키마

| 필드 | 설명 |
|---|---|
| document_id | 문서 내부 ID placeholder입니다. 실제 문서번호가 아닙니다. |
| document_type | 공문 유형입니다. |
| title | 제목 문구입니다. |
| document_number | 실제 문서번호가 없으면 null 또는 [확인 필요]입니다. |
| execution_date | 실제 시행일자가 없으면 null 또는 [확인 필요]입니다. |
| recipient | 수신처 placeholder입니다. |
| reference | 참조 placeholder입니다. |
| body_sections | 본문 번호 구조 배열입니다. |
| sub_sections | 부가 섹션 배열입니다. |
| attachments | 붙임 목록입니다. |
| closing | 끝 표시입니다. |
| notes | 검토 메모입니다. |
| checklist | 검토 체크리스트입니다. |

body_sections 구조:

| 필드 | 설명 |
|---|---|
| number | 1., 가., 1), 가) 등 번호입니다. |
| content | 본문 문장입니다. |
| children | 하위 번호 구조입니다. |

번호 체계:

- 1.
- 가.
- 1)
- 가)

붙임 형식:

```text
붙임  1. [문서명] 1부.
      2. [문서명] 1부.  끝.
```

예시:

```json
{
  "document_id": "[문서 ID placeholder]",
  "document_type": "공문",
  "title": "[조사 대상] 현황 조사 요청",
  "document_number": null,
  "execution_date": null,
  "recipient": "[수신처 확인 필요]",
  "reference": "[참조 확인 필요]",
  "body_sections": [
    {
      "number": "1.",
      "content": "[업무 발생 배경]에 따라 [대상 기관/부서]의 [조사 대상] 현황을 확인하고자 합니다.",
      "children": []
    },
    {
      "number": "2.",
      "content": "각 [대상 기관/부서]에서는 [조사 기준일] 현재의 자료를 [제출기한]까지 제출하여 주시기 바랍니다.",
      "children": [
        {
          "number": "가.",
          "content": "제출방법: [제출방법 확인 필요]",
          "children": []
        }
      ]
    }
  ],
  "sub_sections": [],
  "attachments": [
    {
      "number": "1.",
      "title": "[문서명]",
      "copies": "[부수 확인 필요]"
    }
  ],
  "closing": "끝.",
  "notes": "[실제 문서번호와 시행일자는 사용자가 확인]",
  "checklist": ["개인정보 제외 여부 확인", "붙임 목록 확인"]
}
```

## 추진계획서 JSON 스키마

필드:

- title
- background
- purpose
- overview
- main_contents
- detailed_plan
- schedule
- budget
- expected_effects
- review_items
- future_plan
- attachments
- checklist

overview 필드 예:

- 사업명
- 추진기간
- 추진대상
- 추진방식
- 소요예산
- 담당부서

schedule은 배열로 정의합니다.

budget은 금액을 임의 생성하지 않고 [확인 필요]로 표시합니다.

예시:

```json
{
  "title": "[사업명] 추진계획",
  "background": "[업무 발생 배경]",
  "purpose": "[활용 목적]",
  "overview": {
    "사업명": "[사업명 확인 필요]",
    "추진기간": "[추진기간 확인 필요]",
    "추진대상": "[추진대상 확인 필요]",
    "추진방식": "[추진방식 확인 필요]",
    "소요예산": "[소요예산 확인 필요]",
    "담당부서": "[담당부서 확인 필요]"
  },
  "main_contents": ["[주요 내용 확인 필요]"],
  "detailed_plan": [
    {
      "step": "[단계명]",
      "description": "[세부 추진내용 확인 필요]"
    }
  ],
  "schedule": [
    {
      "phase": "[추진 단계]",
      "period": "[확인 필요]",
      "details": "[일정 세부내용 확인 필요]"
    }
  ],
  "budget": {
    "total": "[소요예산 확인 필요]",
    "items": [
      {
        "name": "[예산 항목]",
        "amount": "[확인 필요]",
        "basis": "[산출 기준 확인 필요]"
      }
    ]
  },
  "expected_effects": ["[기대효과 확인 필요]"],
  "review_items": ["[검토사항 확인 필요]"],
  "future_plan": "[향후계획 확인 필요]",
  "attachments": [],
  "checklist": ["예산 임의 생성 여부 확인", "일정 확인 필요 표시 확인"]
}
```

## 결과보고서 JSON 스키마

필드:

- title
- overview
- results
- main_outcomes
- issues
- improvements
- future_plan
- attachments
- checklist

참여 인원, 실적 수치, 예산 집행액은 임의 생성하지 않습니다.

```json
{
  "title": "[사업명] 결과보고",
  "overview": {
    "사업명": "[사업명 확인 필요]",
    "추진기간": "[추진기간 확인 필요]",
    "추진대상": "[추진대상 확인 필요]"
  },
  "results": ["[추진결과 확인 필요]"],
  "main_outcomes": ["[주요성과 확인 필요]"],
  "issues": ["[문제점 확인 필요]"],
  "improvements": ["[개선사항 확인 필요]"],
  "future_plan": "[향후계획 확인 필요]",
  "attachments": [],
  "checklist": ["실제 수치 임의 생성 금지", "개인정보 제외 여부 확인"]
}
```

## 검토보고서 JSON 스키마

필드:

- title
- review_background
- review_scope
- review_items
- review_opinion
- risks
- required_reviews
- next_actions
- checklist

법률적으로 문제없다고 단정하지 않고, 법무ㆍ계약ㆍ개인정보 담당자 검토 필요 여부를 required_reviews에 표시합니다.

```json
{
  "title": "[검토 대상] 검토보고",
  "review_background": "[검토배경 확인 필요]",
  "review_scope": "[검토범위 확인 필요]",
  "review_items": ["[검토항목 확인 필요]"],
  "review_opinion": "[검토의견은 확정 판단이 아니며 확인 필요]",
  "risks": ["[위험요소 확인 필요]"],
  "required_reviews": ["법무 검토 필요 여부 확인", "계약 검토 필요 여부 확인", "개인정보 검토 필요 여부 확인"],
  "next_actions": ["[후속조치 확인 필요]"],
  "checklist": ["확정 표현 여부 확인", "관련 부서 검토 필요 표시 확인"]
}
```

## 현황조사표 JSON 스키마

XLSX 템플릿 렌더링을 고려한 구조입니다.

필드:

- sheet_name
- title
- standard_date
- submitting_unit
- columns
- rows
- notes
- validation_rules
- privacy_notice
- checklist

columns 예:

- 연번
- 구분
- 항목
- 상태
- 보완 필요 여부
- 조치 필요사항
- 비고

rows는 placeholder 기반 배열로 작성합니다.

실제 관서명, 차량번호, 장비명, 수량, 운영정보는 포함하지 않습니다.

```json
{
  "sheet_name": "[시트명 확인 필요]",
  "title": "[조사 대상] 현황조사표",
  "standard_date": "[조사기준일 확인 필요]",
  "submitting_unit": "[비식별 제출 단위 코드]",
  "columns": ["연번", "구분", "항목", "상태", "보완 필요 여부", "조치 필요사항", "비고"],
  "rows": [
    {
      "연번": "[연번]",
      "구분": "[구분]",
      "항목": "[항목]",
      "상태": "[확인 필요]",
      "보완 필요 여부": "[확인 필요]",
      "조치 필요사항": "[확인 필요]",
      "비고": "[비고]"
    }
  ],
  "notes": "[실제 운영정보 제외]",
  "validation_rules": ["개인정보 입력 금지", "실제 차량번호 입력 금지"],
  "privacy_notice": "[개인정보 제외 안내 문구]",
  "checklist": ["실제 수량 입력 여부 확인", "내부 운영정보 제외 여부 확인"]
}
```

## 업체 연락 메일 JSON 스키마

필드:

- subject
- greeting
- sender
- purpose
- request_items
- response_deadline
- response_method
- caution_notes
- closing
- signature
- checklist

caution_notes에는 다음 취지가 포함되어야 합니다.

- 본 요청은 사전 검토 목적입니다.
- 계약 또는 업체 선정이 확정된 사항은 아닙니다.
- 개인정보, 내부자료, 민감정보는 제외하여 회신해 주시기 바랍니다.
- 세부 추진 여부는 내부 검토 및 관련 절차에 따라 결정됩니다.

sender와 signature에는 개인 연락처보다 [담당부서 공용 연락처] 또는 [공용 이메일]을 우선 사용합니다.

```json
{
  "subject": "[사업명] 관련 [자료 요청 항목] 확인 요청",
  "greeting": "안녕하세요. [담당부서]입니다.",
  "sender": "[담당부서]",
  "purpose": "[활용 목적]을 위한 사전 검토",
  "request_items": ["[자료 요청 항목]"],
  "response_deadline": "[회신기한 확인 필요]",
  "response_method": "[회신방법 확인 필요]",
  "caution_notes": [
    "본 요청은 사전 검토 목적입니다.",
    "계약 또는 업체 선정이 확정된 사항은 아닙니다.",
    "개인정보, 내부자료, 민감정보는 제외하여 회신해 주시기 바랍니다.",
    "세부 추진 여부는 내부 검토 및 관련 절차에 따라 결정됩니다."
  ],
  "closing": "감사합니다.",
  "signature": {
    "department": "[담당부서]",
    "contact": "[담당부서 공용 연락처]",
    "email": "[공용 이메일]"
  },
  "checklist": ["개인 연락처 사용 여부 확인", "계약 확정 표현 여부 확인"]
}
```

## 민원 관련 외부 전달문 JSON 스키마

이 섹션은 보수적으로 작성합니다.

필드:

- title
- purpose
- deidentified_complaint_summary
- request_items
- prohibited_items
- contact_policy
- required_internal_review
- attachments
- checklist

prohibited_items에는 다음을 포함합니다.

- 민원인 실명
- 연락처
- 주소
- 민원번호
- 접수번호
- 사건번호
- 특정 개인을 식별할 수 있는 내용

contact_policy에는 다음 취지를 포함합니다.

- 업체가 민원인에게 직접 연락하지 않음
- 기관 담당부서 또는 공용 연락처를 통해 협의

attachments는 "비식별 처리된 민원 요지 자료" 형태로만 표현합니다.

```json
{
  "title": "[비식별 민원 관련 검토 요청]",
  "purpose": "[활용 목적]",
  "deidentified_complaint_summary": "[비식별 처리된 민원 요지]",
  "request_items": ["[자료 요청 항목]"],
  "prohibited_items": ["민원인 실명", "연락처", "주소", "민원번호", "접수번호", "사건번호", "특정 개인을 식별할 수 있는 내용"],
  "contact_policy": {
    "direct_contact_allowed": false,
    "coordination_channel": "[담당부서 또는 공용 연락처]"
  },
  "required_internal_review": ["개인정보 보호 담당부서 검토", "내부 승인 필요 여부 확인"],
  "attachments": [
    {
      "title": "[비식별 처리된 민원 요지 자료]",
      "contains_personal_info": false
    }
  ],
  "checklist": ["민원인 직접 식별정보 제외", "외부 전달 가능 여부 검토"]
}
```

## renderer_hints 필드

renderer_hints는 HWPX와 XLSX 렌더러가 참고할 수 있는 힌트 필드입니다.

| 하위 필드 | 설명 |
|---|---|
| target_format | hwpx, xlsx, markdown, email 등 출력 대상입니다. |
| template_id | 적용할 템플릿 ID placeholder입니다. |
| style_profile | 서식 프로필 placeholder입니다. |
| table_template | 표 템플릿 placeholder입니다. |
| placeholder_map | JSON 필드와 템플릿 placeholder 매핑입니다. |
| requires_xlsx | XLSX 렌더링 필요 여부입니다. |
| requires_hwpx | HWPX 렌더링 필요 여부입니다. |
| requires_manual_review | 수동 검토 필요 여부입니다. |

renderer_hints는 서식 적용 힌트일 뿐 실제 서식값은 docs/15_style_specification.md를 참고해야 합니다.

```json
{
  "target_format": "xlsx",
  "template_id": "[템플릿 ID 확인 필요]",
  "style_profile": "[서식 프로필 확인 필요]",
  "table_template": "[표 템플릿 확인 필요]",
  "placeholder_map": {
    "[문서 제목]": "documents[0].title",
    "[조사기준일]": "documents[0].standard_date"
  },
  "requires_xlsx": true,
  "requires_hwpx": false,
  "requires_manual_review": true
}
```

## 출력 예시

### 1. 조사 지시 공문 예시

```json
{
  "request_id": "[요청 ID placeholder]",
  "task_type": "draft_document",
  "document_type": "조사 지시 공문",
  "output_targets": ["markdown", "hwpx"],
  "security_review": {
    "risk_level": "low",
    "contains_personal_info": false,
    "contains_sensitive_info": false,
    "contains_internal_info": false,
    "blocked_items": [],
    "allowed_processing": true,
    "required_review": ["human_review"],
    "notes": "[placeholder 기반 초안]"
  },
  "missing_fields": [
    {
      "field_name": "조사기준일",
      "reason": "조사 기준 확인 필요",
      "required_for": "본문",
      "suggested_placeholder": "[조사기준일 확인 필요]"
    }
  ],
  "assumptions": [],
  "draft_status": "needs_input",
  "human_review_required": true,
  "documents": [
    {
      "document_id": "[문서 ID placeholder]",
      "document_type": "공문",
      "title": "[조사 대상] 현황 조사 요청",
      "recipient": "[수신처 확인 필요]",
      "body_sections": [
        {
          "number": "1.",
          "content": "[업무 발생 배경]에 따라 [조사 대상] 현황을 확인하고자 합니다.",
          "children": []
        }
      ],
      "attachments": [
        {
          "number": "1.",
          "title": "[조사표 문서명]",
          "copies": "[부수 확인 필요]"
        }
      ],
      "closing": "끝."
    }
  ],
  "attachments": [],
  "email_draft": null,
  "checklist": ["수신처 확인", "개인정보 제외 확인"],
  "renderer_hints": {
    "target_format": "hwpx",
    "template_id": "[템플릿 ID 확인 필요]",
    "requires_hwpx": true,
    "requires_manual_review": true
  }
}
```

### 2. 추진계획서 예시

```json
{
  "request_id": "[요청 ID placeholder]",
  "task_type": "draft_document",
  "document_type": "추진계획서",
  "output_targets": ["markdown", "hwpx"],
  "security_review": {
    "risk_level": "low",
    "contains_personal_info": false,
    "contains_sensitive_info": false,
    "contains_internal_info": false,
    "blocked_items": [],
    "allowed_processing": true,
    "required_review": ["human_review"],
    "notes": "[확인되지 않은 값은 placeholder 처리]"
  },
  "missing_fields": [
    {
      "field_name": "소요예산",
      "reason": "예산 임의 생성 금지",
      "required_for": "budget",
      "suggested_placeholder": "[소요예산 확인 필요]"
    }
  ],
  "assumptions": [],
  "draft_status": "needs_input",
  "human_review_required": true,
  "documents": [
    {
      "title": "[사업명] 추진계획",
      "background": "[업무 발생 배경]",
      "purpose": "[활용 목적]",
      "overview": {
        "사업명": "[사업명 확인 필요]",
        "추진기간": "[추진기간 확인 필요]",
        "추진대상": "[추진대상 확인 필요]",
        "추진방식": "[추진방식 확인 필요]",
        "소요예산": "[소요예산 확인 필요]",
        "담당부서": "[담당부서 확인 필요]"
      },
      "schedule": [],
      "budget": {
        "total": "[소요예산 확인 필요]",
        "items": []
      },
      "expected_effects": ["[기대효과 확인 필요]"],
      "checklist": ["예산 확인", "일정 확인", "사람 검토"]
    }
  ],
  "attachments": [],
  "email_draft": null,
  "checklist": ["확정 표현 여부 확인"],
  "renderer_hints": {
    "target_format": "hwpx",
    "template_id": "[템플릿 ID 확인 필요]",
    "requires_hwpx": true,
    "requires_manual_review": true
  }
}
```

### 3. 업체 견적 요청 메일 예시

```json
{
  "request_id": "[요청 ID placeholder]",
  "task_type": "draft_email",
  "document_type": "업체 견적 요청 메일",
  "output_targets": ["email", "markdown"],
  "security_review": {
    "risk_level": "medium",
    "contains_personal_info": false,
    "contains_sensitive_info": false,
    "contains_internal_info": false,
    "blocked_items": ["[실제 견적 금액 입력 금지]", "[실제 계약 조건 입력 금지]"],
    "allowed_processing": true,
    "required_review": ["human_review", "contract_review"],
    "notes": "[계약 또는 업체 선정 미확정 문구 필요]"
  },
  "missing_fields": [
    {
      "field_name": "회신기한",
      "reason": "메일 회신 요청에 필요",
      "required_for": "email_draft.response_deadline",
      "suggested_placeholder": "[회신기한 확인 필요]"
    }
  ],
  "assumptions": [],
  "draft_status": "needs_input",
  "human_review_required": true,
  "documents": [],
  "attachments": [],
  "email_draft": {
    "subject": "[사업명] 관련 [자료 요청 항목] 확인 요청",
    "greeting": "안녕하세요. [담당부서]입니다.",
    "sender": "[담당부서]",
    "purpose": "[활용 목적]을 위한 사전 검토",
    "request_items": ["[자료 요청 항목]"],
    "response_deadline": "[회신기한 확인 필요]",
    "response_method": "[회신방법 확인 필요]",
    "caution_notes": [
      "본 요청은 사전 검토 목적입니다.",
      "계약 또는 업체 선정이 확정된 사항은 아닙니다.",
      "개인정보, 내부자료, 민감정보는 제외하여 회신해 주시기 바랍니다."
    ],
    "closing": "감사합니다.",
    "signature": {
      "department": "[담당부서]",
      "contact": "[담당부서 공용 연락처]",
      "email": "[공용 이메일]"
    }
  },
  "checklist": ["계약 확정 표현 금지", "개인 연락처 제외"],
  "renderer_hints": {
    "target_format": "email",
    "template_id": "[메일 템플릿 ID 확인 필요]",
    "requires_manual_review": true
  }
}
```

## 금지되는 JSON 출력

다음 내용은 JSON에 포함하지 않습니다.

- 실제 개인정보
- 실제 내부자료
- 실제 업체 견적 금액
- 실제 계약 조건
- 실제 차량번호
- 실제 관서별 운영정보
- 실제 민원번호 또는 접수번호
- 실제 문서번호
- 실제 담당자 개인 연락처
- 실제 내부망 주소 또는 시스템 정보

## Step 9 완료 체크리스트

- [x] 공통 JSON 구조가 정의되었는가
- [x] security_review 필드가 정의되었는가
- [x] missing_fields 필드가 정의되었는가
- [x] 공문 JSON 스키마가 정의되었는가
- [x] 추진계획서 JSON 스키마가 정의되었는가
- [x] 결과보고서 JSON 스키마가 정의되었는가
- [x] 검토보고서 JSON 스키마가 정의되었는가
- [x] 현황조사표 JSON 스키마가 정의되었는가
- [x] 업체 연락 메일 JSON 스키마가 정의되었는가
- [x] 민원 관련 외부 전달문 JSON 스키마가 정의되었는가
- [x] renderer_hints 필드가 정의되었는가
- [x] 예시 JSON이 모두 placeholder 기반인가
- [x] 실제 원문, 개인정보, 내부 운영정보가 포함되지 않았는가
- [x] HWPX/XLSX 생성 코드를 작성하지 않았는가
