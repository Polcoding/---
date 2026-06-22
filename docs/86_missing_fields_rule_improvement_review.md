# missing_fields 생성 규칙 개선 검토

## 목적

`normalizers/input_normalizer_poc.py`의 `missing_fields` 생성 규칙을 개선할 필요가 있는지 검토합니다.

이 문서는 즉시 코드 수정을 전제로 하지 않습니다. 현재 fixture 6종 회귀 기준을 유지하면서, 어떤 조건에서 `missing_fields` 생성 규칙을 바꿀지 판단합니다.

## 현재 동작

현재 `make_missing_fields(document_type)`는 문서 유형만 보고 고정 누락값을 생성합니다.

| document_type | 현재 missing_fields |
|---|---|
| `one_page_report` | `purpose` |
| `project_plan` | `schedule`, `budget` |
| `result_report` | `results_or_metrics`, `budget` |
| `review_report` | `review_scope`, `required_reviews` |

## 현재 방식의 장점

- 구현이 단순합니다.
- fixture 6종 회귀 테스트가 안정적입니다.
- 실제값이 들어오지 않아도 `[확인 필요]` 중심 초안을 만들 수 있습니다.
- 예산, 일정, 실적, 담당자, 수량을 임의 생성하지 않는 원칙을 강하게 유지합니다.

## 현재 방식의 한계

- 사용자가 placeholder-confirmed 값을 제공해도 누락값이 줄어들지 않습니다.
- `project_plan`과 `result_report`는 현재 구조상 대부분 `needs_more_input`으로 유지됩니다.
- `docs/84_hwpx_report_user_input_templates.md`의 문서 유형별 입력 템플릿을 fixture로 직접 확장하기 어렵습니다.
- `known_values`가 항상 빈 객체라서 안전하게 제공된 값과 미확정 값을 구분하지 못합니다.

## 개선 필요 여부

현재 단계에서는 즉시 코드 개선하지 않습니다.

이유:

- 현재 회귀 기준은 HWPX 보고서 4종 렌더링 흐름을 충분히 검증합니다.
- 실제값과 placeholder-confirmed 값을 구분하는 구조가 아직 정의되지 않았습니다.
- missing_fields를 줄이는 규칙을 잘못 열면 실제 일정, 예산, 실적을 확정값처럼 취급할 위험이 있습니다.
- fixture 확장보다 입력 구조 정책 확정이 먼저입니다.

## 개선 전 선행 조건

코드를 개선하려면 먼저 다음 구조를 문서로 확정해야 합니다.

### placeholder-confirmed 값

사용자가 실제값이 아니라 placeholder로 명시 확인한 값입니다.

예:

```json
{
  "placeholder_confirmed_values": {
    "schedule": "[추진 일정 확인 필요]",
    "budget": "[예산 확인 필요]"
  }
}
```

이 값은 실제 일정이나 예산이 아니며, `[확인 필요]` 상태를 의도적으로 유지한다는 표시입니다.

### known_values와의 구분

`known_values`는 사용자가 명확히 제공했고 보안상 허용되는 값만 넣습니다.

다만 현재 단계에서는 실제 일정, 실제 예산액, 실제 담당자명은 `known_values`에 넣지 않는 것이 원칙입니다.

## 개선 후보

| 후보 | 설명 | 현재 판단 |
|---|---|---|
| 고정 missing_fields 유지 | 현재 방식 그대로 유지 | 채택 |
| placeholder_confirmed_values 도입 | placeholder로 확인된 항목은 missing_fields에서 제외 | 보류 |
| known_values 기반 missing_fields 조정 | 안전한 known_values가 있으면 누락값 제외 | 보류 |
| 문서 유형별 ready fixture 추가 | project_plan/result_report ready 경로 검증 | 보류 |

## 최소 코드 개선 조건

향후 개선한다면 최소 범위는 다음과 같습니다.

1. fixture schema에 `placeholder_confirmed_values`를 추가
2. `make_missing_fields(document_type, placeholder_confirmed_values)` 형태로 확장
3. 실제값처럼 보이는 값은 security filter에서 계속 차단
4. 기존 fixture 6종 기대 결과 유지
5. 신규 fixture는 실제값 없이 placeholder만 사용

## 회귀 테스트 조건

개선 시 다음은 반드시 유지되어야 합니다.

- `safe_one_page_report_request.json`: `ready_for_draft`
- `missing_project_plan_request.json`: `needs_more_input`
- `missing_result_report_request.json`: `needs_more_input`
- `review_report_needs_security_review.json`: `needs_security_review`
- `approved_review_report_request.json`: `ready_for_draft`
- `blocked_real_value_like_request.json`: `blocked`

## 보안 조건

- 실제 원문 사용 금지
- 실제 개인정보 사용 금지
- 실제 기관명, 부서명, 담당자명 사용 금지
- 실제 문서번호, 민원번호, 사건번호 사용 금지
- 실제 예산액, 일정, 실적 수치 사용 금지
- 실제 승인자명, 결재번호, 검토의견 원문 사용 금지

## 결론

현재는 `missing_fields` 생성 규칙을 코드로 개선하지 않고, 고정 누락값 정책을 유지합니다.

이 문서 작성 시점의 다음 단계는 `placeholder_confirmed_values` 도입 여부를 별도 설계로 검토하는 것이었습니다.

후속 작업에서 `placeholder_confirmed_values`는 read-only helper, helper fixture, metadata 후보까지 정리되었고, `missing_fields`, routing, HWPX payload에는 연결하지 않기로 결정했습니다.

최신 재검토 결과는 `docs/103_missing_fields_rule_decision_after_helper.md`를 기준으로 관리합니다.
