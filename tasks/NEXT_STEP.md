# 다음 작업

## 목표

`project_plan` 렌더링 산출물을 한컴에서 열어 수동 열람 검수를 진행합니다.

## 확인할 로컬 파일

- `renderers/hwpx_renderer/output/sample_project_plan_poc.hwpx`

이 파일은 로컬 검증용 output HWPX이며 Git에 추가하지 않습니다.

## 현재 자동 검수 결과

- `templates/hwpx/placeholder_project_plan.hwpx` 생성 완료
- 로컬 템플릿 Git 제외 확인
- output HWPX Git 제외 확인
- 렌더러 실행 결과: `rendered`
- `remaining_placeholders`: `[]`
- 기존 문서 유형 회귀 결과: 모두 `rendered`

## 확인 대상

- `renderers/hwpx_renderer/output/sample_project_plan_poc.hwpx`
- `docs/56_project_plan_hwpx_render_test_result.md`

## 확인 항목

1. output HWPX가 한컴에서 정상적으로 열리는지
2. 제목과 1~10번 항목이 순서대로 표시되는지
3. 각 치환 결과가 서로 다른 문단에 표시되는지
4. 글자 겹침이 없는지
5. 줄간격과 문단 간격이 지나치게 좁지 않은지
6. `overview_table`, `schedule_table`, `budget_table` 치환 결과를 읽을 수 있는지
7. 실제 기관 양식, 실제 원문, 실제 개인정보가 포함되지 않았는지

## 작업 제한

- 실제 기관 양식 사용 금지
- 실제 문서 원문 사용 금지
- 실제 개인정보 또는 내부 운영정보 사용 금지
- 실제 HWPX 템플릿 Git 추가 금지
- Email/API/Make.com 연동 금지
- 확인되지 않은 서식값 임의 생성 금지

## 완료 조건

- `project_plan` HWPX 수동 열람 결과 보고
- 글자 겹침 여부 확인
- 문단 간격과 번호체계 확인
- 수동 열람 검수 결과 문서화
