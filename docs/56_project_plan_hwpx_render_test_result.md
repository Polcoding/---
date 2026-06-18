# 추진계획서 HWPX 렌더링 테스트 결과

## 목적

이 문서는 `project_plan` 문서 유형의 로컬 HWPX placeholder 템플릿 치환 결과를 기록합니다.

실제 기관 양식, 실제 추진계획서 원문, 실제 개인정보는 사용하지 않았습니다.

## 확인 대상

- `examples/json/sample_project_plan.json`
- `templates/hwpx/placeholder_project_plan.hwpx`
- `renderers/hwpx_renderer/template_package.py`
- `renderers/hwpx_renderer/render_hwpx_poc.py`
- `renderers/hwpx_renderer/output/sample_project_plan_poc.hwpx`

## 로컬 템플릿 상태

- 파일명: `templates/hwpx/placeholder_project_plan.hwpx`
- 상태: 로컬 생성 완료
- Git 상태: ignored
- 생성 방식: 기존 placeholder-only HWPX 템플릿을 기반으로 추진계획서 placeholder 문단 구성으로 변환
- 실제 기관 양식 원본 사용 여부: 사용하지 않음

## 포함 placeholder

다음 placeholder가 템플릿에서 확인되었습니다.

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

## 렌더링 결과

HWPX 최소 PoC 렌더러 실행 결과는 다음과 같습니다.

| 입력 JSON | 상태 | remaining_placeholders |
|---|---|---|
| `sample_one_page_report.json` | `rendered` | 0 |
| `sample_official_letter.json` | `rendered` | 0 |
| `sample_project_plan.json` | `rendered` | 0 |
| `sample_result_report.json` | `rendered` | 0 |
| `sample_review_report.json` | `rendered` | 0 |

`project_plan` 렌더링 산출물:

- `renderers/hwpx_renderer/output/sample_project_plan_poc.hwpx`

## Git 제외 확인

다음 파일은 Git 추적 대상이 아니라 ignored 상태입니다.

- `templates/hwpx/placeholder_project_plan.hwpx`
- `renderers/hwpx_renderer/output/sample_project_plan_poc.hwpx`
- `renderers/hwpx_renderer/output/hwpx_render_summary.json`

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명 추가 없음
- 실제 문서번호 추가 없음
- 실제 추진계획서 원문 추가 없음
- 실제 HWPX 양식 원본 추가 없음
- Email/API/Make.com 연동 없음

## 수동 열람 검수

1차 한컴 수동 열람에서 다음 문제가 확인되었습니다.

- 1~10번 항목 순서는 정상
- 항목 제목이 `?? ??` 형태로 표시됨
- 3번 항목 내용 글자 겹침 심함
- 7번 항목 내용 글자 겹침 일부 발생

## 조치 결과

다음 조치를 적용했습니다.

- `templates/hwpx/placeholder_project_plan.hwpx`의 항목 제목을 정상 한글로 재생성
- `project_plan` 전용 placeholder map 추가
- `overview_table`, `schedule_table`, `budget_table`, `detailed_plan`은 표/목록 전체를 길게 펼치지 않고 검토용 한 줄 문구로 축약
- `main_contents`, `expected_effects`, `review_items`도 다른 항목과 맞춰 앞의 `-` 없이 한 줄 문구로 통일
- HWPX 렌더러 재실행

재실행 후 output 내부 텍스트 기준으로 다음 사항을 확인했습니다.

- 항목 제목 `?? ??` 제거
- `3. 추진 개요` 치환값 축약
- `7. 소요 예산` 치환값 축약
- `4. 주요 내용`, `8. 기대 효과`, `9. 검토 사항` 내용란의 앞쪽 `-` 제거
- `sample_project_plan.json`: `rendered`
- `remaining_placeholders`: 0
- 기존 문서 유형 회귀 결과: 모두 `rendered`, `remaining_placeholders` 0

## 재검수 필요 항목

한컴 재검수 결과 다음 항목이 확인되었습니다.

- output HWPX 정상 열람
- 항목 제목 정상 한글 표시
- 3번 항목 글자 겹침 해소
- 7번 항목 글자 겹침 해소
- 4번, 8번, 9번 내용란 앞쪽 `-` 제거 확인
- 전체 항목 배치 정상
- 수동 열람 기준 추가 수정 필요 없음

## 결론

`project_plan` HWPX 렌더러 지원은 자동 치환 기준으로 확인되었습니다.

수동 열람 기준에서도 제목 깨짐, 글자 겹침, 내용란 표기 불일치 문제가 해소되었습니다.

원페이지 보고서, 추진계획서, 결과보고서, 검토보고서의 핵심 HWPX 보고서 4종은 로컬 placeholder 템플릿 기준으로 치환과 수동 검수가 완료되었습니다.
