# 검토보고서 HWPX 최소 템플릿 준비

## 목적

`review_report` 샘플 JSON을 HWPX로 치환하기 위한 최소 placeholder 템플릿 준비 기준을 정리합니다.

이번 단계에서는 실제 기관 양식이나 실제 검토보고서 원문을 사용하지 않습니다.

## 준비 파일

- `templates/hwpx/placeholder_review_report.hwpx`

이 파일은 로컬 테스트 템플릿이며 Git 제외 대상입니다.

## 최소 템플릿 내용

한컴에서 새 HWPX 문서를 만들고 아래 내용을 배치합니다.

각 placeholder는 가능하면 서로 다른 문단에 둡니다.

```text
{{title}}

1. 검토 배경
{{review_background}}

2. 검토 범위
{{review_scope}}

3. 검토 항목
{{review_items}}

4. 검토 의견
{{review_opinion}}

5. 위험요소
{{risks}}

6. 필요 검토
{{required_reviews}}

7. 후속조치
{{next_actions}}
```

## placeholder별 의미

| placeholder | JSON 경로 | 주의 |
|---|---|---|
| `{{title}}` | `documents[0].title` | 실제 검토 대상명은 사용하지 않음 |
| `{{review_background}}` | `documents[0].review_background` | 검토배경은 확인 필요로 유지 |
| `{{review_scope}}` | `documents[0].review_scope` | 검토범위는 확인 필요로 유지 |
| `{{review_items}}` | `documents[0].review_items` | 관련 기준과 검토 상태는 placeholder 기반 |
| `{{review_opinion}}` | `documents[0].review_opinion` | 확정 판단이 아니어야 함 |
| `{{risks}}` | `documents[0].risks` | 위험요소는 확인 필요로 유지 |
| `{{required_reviews}}` | `documents[0].required_reviews` | 법무ㆍ계약ㆍ개인정보 검토 필요 여부 표시 |
| `{{next_actions}}` | `documents[0].next_actions` | 후속조치는 확인 필요로 유지 |

## 수동 검수 포인트

- 각 항목이 별도 문단으로 보이는가
- 여러 줄 개조식 치환 후 글자가 겹치지 않는가
- 검토 항목과 필요 검토 영역이 너무 빽빽하지 않은가
- 법률적으로 문제없다는 확정 표현이 없는가
- 실제 개인정보나 내부 운영정보가 들어가지 않았는가
- output HWPX가 GitHub Desktop Changes에 나타나지 않는가

## 다음 단계

한컴에서 `placeholder_review_report.hwpx`를 준비한 뒤 렌더러를 실행하고, 결과를 `docs/52_review_report_hwpx_render_test_result.md`에 기록합니다.
