# HWPX style profile manifest

## 목적

이 문서는 향후 HWPX 템플릿 렌더러가 사용할 style_profile 후보를 관리하기 위한 manifest입니다.

현재 단계에서는 실제 서식값을 확정하지 않습니다.

최신 `[확인 필요]` 유지 기준은 `docs/126_style_profile_confirmation_value_collection_criteria.md`를 따릅니다.

## style profile 목록

| style_profile_id | 문서유형 | 상태 | 비고 |
|---|---|---|---|
| style_official_letter_basic | 일반 공문 | 확인 필요 | 실제 값 미확정 |
| style_survey_request_letter | 현황조사 지시 공문 | 확인 필요 | 실제 값 미확정 |
| style_one_page_report_basic | 원페이지 보고서 | 확인 필요 | 실제 값 미확정 |
| style_project_plan_basic | 추진계획서 | 확인 필요 | 실제 값 미확정 |
| style_result_report_basic | 결과보고서 | 확인 필요 | 실제 값 미확정 |
| style_review_report_basic | 검토보고서 | 확인 필요 | 실제 값 미확정 |

## 보관 원칙

- 실제 폰트 파일을 보관하지 않습니다.
- 실제 기관 HWPX 양식 원본을 보관하지 않습니다.
- style_profile에는 확인된 서식값만 기록합니다.
- 확인되지 않은 값은 [확인 필요]로 둡니다.

## 상태 전환 원칙

style profile 값은 다음 조건을 모두 만족하기 전까지 `확인 필요` 상태를 유지합니다.

- 사람이 저장소 밖 로컬 환경에서 서식값을 직접 확인
- 실제 기관명, 실제 문서번호, 실제 파일명, 실제 원문을 기록하지 않음
- 폰트 파일, HWP/HWPX 원본, 이미지 원본을 저장소에 추가하지 않음
- 확인값의 적용 대상 문서유형과 서식 항목이 명확함
- 사용자가 반영 가능 여부를 별도로 승인

이번 단계에서는 `normalizers/`, `renderers/`, fixture, routing, HWPX payload에 style profile 값을 연결하지 않습니다.
