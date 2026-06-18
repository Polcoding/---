# 결과보고서 HWPX 최소 템플릿 준비

## 목적

`result_report` 샘플 JSON을 HWPX로 치환하기 위한 최소 placeholder 템플릿 준비 기준을 정리합니다.

이번 단계에서는 실제 기관 양식이나 실제 추진계획서 원문을 사용하지 않습니다.

## 준비 파일

- `templates/hwpx/placeholder_result_report.hwpx`

이 파일은 로컬 테스트 템플릿이며 Git 제외 대상입니다.

## 최소 템플릿 내용

한컴에서 새 HWPX 문서를 만들고 아래 내용을 배치합니다.

각 placeholder는 가능하면 서로 다른 문단에 둡니다.

```text
{{title}}

1. 추진 개요
{{overview_table}}

2. 기존 계획 참조
{{linked_plan_reference}}

3. 계획 항목
{{planned_items}}

4. 추진 결과
{{actual_results}}

5. 계획 대비 결과
{{comparison_to_plan}}

6. 주요 성과
{{main_outcomes}}

7. 문제점
{{issues}}

8. 개선사항
{{improvements}}

9. 향후 계획
{{future_plan}}
```

## placeholder별 의미

| placeholder | JSON 경로 | 주의 |
|---|---|---|
| `{{title}}` | `documents[0].title` | 실제 사업명은 사용하지 않음 |
| `{{overview_table}}` | `documents[0].overview` | 추진기간, 대상, 담당부서는 placeholder 유지 |
| `{{linked_plan_reference}}` | `documents[0].linked_plan_reference` | 실제 계획서 원문을 넣지 않음 |
| `{{planned_items}}` | `documents[0].planned_items` | 계획 항목은 placeholder 기반 |
| `{{actual_results}}` | `documents[0].actual_results` | 실적 수치, 참여 인원, 예산 집행액 임의 생성 금지 |
| `{{comparison_to_plan}}` | `documents[0].comparison_to_plan` | 계획 대비 결과는 확인 필요로 유지 |
| `{{main_outcomes}}` | `documents[0].main_outcomes` | 성과 과장 금지 |
| `{{issues}}` | `documents[0].issues` | 문제점 확인 필요로 유지 |
| `{{improvements}}` | `documents[0].improvements` | 개선사항 확인 필요로 유지 |
| `{{future_plan}}` | `documents[0].future_plan` | 향후계획 확인 필요로 유지 |

## 수동 검수 포인트

- 각 항목이 별도 문단으로 보이는가
- 여러 줄 개조식 치환 후 글자가 겹치지 않는가
- 계획 항목, 추진 결과, 계획 대비 결과 영역이 너무 빽빽하지 않은가
- 실제 수치나 실제 사업명이 들어가지 않았는가
- output HWPX가 GitHub Desktop Changes에 나타나지 않는가

## 다음 단계

한컴에서 `placeholder_result_report.hwpx`를 준비한 뒤 렌더러를 실행하고, 결과를 `docs/50_result_report_hwpx_render_test_result.md`에 기록합니다.
