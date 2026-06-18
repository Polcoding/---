# 다음 작업

## 목표

`result_report`의 최소 HWPX placeholder 템플릿을 로컬에서 준비하고 실제 치환 결과를 검수합니다.

## 준비할 로컬 파일

- `templates/hwpx/placeholder_result_report.hwpx`

이 파일은 로컬 검증용 HWPX 템플릿이며 Git에 추가하지 않습니다.

## 한컴 템플릿 최소 내용

각 placeholder는 가능한 한 서로 다른 문단에 배치합니다.

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

## 확인 대상

- `renderers/hwpx_renderer/template_package.py`
- `renderers/hwpx_renderer/render_hwpx_poc.py`
- `examples/json/sample_result_report.json`
- `docs/47_result_review_report_hwpx_support_check.md`

## 확인 항목

1. `templates/hwpx/placeholder_result_report.hwpx` 존재 여부
2. 로컬 템플릿이 Git 제외 상태인지 여부
3. HWPX zip 패키지로 열리는지 여부
4. 다음 placeholder가 템플릿에 포함되어 있는지 여부
   - `{{title}}`
   - `{{overview_table}}`
   - `{{linked_plan_reference}}`
   - `{{planned_items}}`
   - `{{actual_results}}`
   - `{{comparison_to_plan}}`
   - `{{main_outcomes}}`
   - `{{issues}}`
   - `{{improvements}}`
   - `{{future_plan}}`
5. 렌더러 실행 결과가 `rendered`인지 여부
6. `remaining_placeholders`가 `[]`인지 여부
7. 한컴 열람 시 글자 겹침, 줄간격, 문단 간격 문제가 있는지 여부

## 작업 제한

- 실제 기관 양식 사용 금지
- 실제 추진계획서 원문 사용 금지
- 실제 실적 수치, 예산 집행액, 참여 인원 사용 금지
- 실제 HWPX 템플릿 Git 추가 금지
- Email/API/Make.com 연동 금지
- 확인되지 않은 서식값 임의 생성 금지

## 완료 조건

- `result_report` HWPX 치환 성공 여부 보고
- output HWPX Git 제외 확인
- 보안 테스트 통과
- 수동 열람 검수 결과 문서화
