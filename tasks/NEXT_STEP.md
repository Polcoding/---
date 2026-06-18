# 다음 작업

## 목표

`project_plan`의 로컬 HWPX placeholder 템플릿을 준비하고 실제 치환 결과를 검수합니다.

## 준비할 로컬 파일

- `templates/hwpx/placeholder_project_plan.hwpx`

이 파일은 로컬 검증용 HWPX 템플릿이며 Git에 추가하지 않습니다.

## 한컴 템플릿 최소 내용

각 placeholder는 가능한 한 서로 다른 문단에 배치합니다.

```text
{{title}}

1. 추진 배경
{{background}}

2. 추진 목적
{{purpose}}

3. 추진 개요
{{overview_table}}

4. 주요 내용
{{main_contents}}

5. 세부 추진계획
{{detailed_plan}}

6. 추진 일정
{{schedule_table}}

7. 소요 예산
{{budget_table}}

8. 기대 효과
{{expected_effects}}

9. 검토 사항
{{review_items}}

10. 향후 계획
{{future_plan}}
```

## 확인 대상

- `renderers/hwpx_renderer/template_package.py`
- `renderers/hwpx_renderer/render_hwpx_poc.py`
- `examples/json/sample_project_plan.json`
- `docs/55_project_plan_hwpx_template_preparation.md`

## 확인 항목

1. `templates/hwpx/placeholder_project_plan.hwpx` 존재 여부
2. 로컬 템플릿이 Git 제외 상태인지 여부
3. `renderers/hwpx_renderer/output/` 폴더에 렌더러가 새 파일을 쓸 수 있는지 여부
4. HWPX zip 패키지로 열리는지 여부
5. 다음 placeholder가 템플릿에 포함되어 있는지 여부
   - `{{title}}`
   - `{{background}}`
   - `{{purpose}}`
   - `{{overview_table}}`
   - `{{main_contents}}`
   - `{{detailed_plan}}`
   - `{{schedule_table}}`
   - `{{budget_table}}`
   - `{{expected_effects}}`
   - `{{review_items}}`
   - `{{future_plan}}`
6. 렌더러 실행 결과가 `rendered`인지 여부
7. `remaining_placeholders`가 `[]`인지 여부
8. 한컴 열람 시 글자 겹침, 줄간격, 문단 간격 문제가 있는지 여부

## 작업 제한

- 실제 기관 양식 사용 금지
- 실제 문서 원문 사용 금지
- 실제 개인정보 또는 내부 운영정보 사용 금지
- 실제 HWPX 템플릿 Git 추가 금지
- Email/API/Make.com 연동 금지
- 확인되지 않은 서식값 임의 생성 금지

## 완료 조건

- `project_plan` HWPX 치환 성공 여부 보고
- output HWPX Git 제외 확인
- 보안 테스트 통과
- 수동 열람 검수 결과 문서화
