# HWPX style profile 확인 필요 값 유지와 서식값 수집 기준 체크리스트

## 목적

`docs/126_style_profile_confirmation_value_collection_criteria.md` 기준으로 style profile의 `[확인 필요]` 값 유지 기준과 기관 표준 서식값 수집 체크리스트 보강 여부를 확인합니다.

## 기준 문서 확인

| 완료 | 항목 |
|---|---|
| [x] | `docs/125_hwpx_template_manifest_placeholder_consistency_review.md`를 확인했는가 |
| [x] | `docs/40_hwpx_institution_style_values_review.md`를 확인했는가 |
| [x] | `templates/hwpx/style_profile_manifest.md`를 확인했는가 |
| [x] | `checklists/hwpx_institution_style_value_collection_checklist.md`를 확인했는가 |
| [x] | `templates/hwpx/local_template_policy.md`를 확인했는가 |
| [x] | `templates/hwpx/template_manifest.md`를 확인했는가 |

## `[확인 필요]` 유지 기준 확인

| 완료 | 항목 |
|---|---|
| [x] | 실제 서식값을 이번 단계에서 확정하지 않았는가 |
| [x] | 확인되지 않은 글꼴, 자간, 줄간격, 문단 간격을 `[확인 필요]`로 유지했는가 |
| [x] | 확인되지 않은 표 서식과 번호 들여쓰기 값을 `[확인 필요]`로 유지했는가 |
| [x] | style profile 상태 전환 기준을 문서화했는가 |
| [x] | 애매한 값은 `[확인 필요]`로 되돌린다는 기준을 유지했는가 |

## style profile 후보 확인

| 완료 | 항목 |
|---|---|
| [x] | `style_one_page_report_basic`을 미확정 상태로 유지했는가 |
| [x] | `style_project_plan_basic`을 미확정 상태로 유지했는가 |
| [x] | `style_result_report_basic`을 미확정 상태로 유지했는가 |
| [x] | `style_review_report_basic`을 미확정 상태로 유지했는가 |
| [x] | 공문 계열 style profile도 실제값을 임의 확정하지 않았는가 |

## 수집 체크리스트 보강 확인

| 완료 | 항목 |
|---|---|
| [x] | 수집 전 중단 조건을 추가했는가 |
| [x] | 실제 원본과 수집 기록을 분리하도록 했는가 |
| [x] | 실제 파일명, 실제 기관명, 실제 문서번호를 기록하지 않도록 했는가 |
| [x] | 폰트 파일을 저장소에 추가하지 않도록 했는가 |
| [x] | 수집값을 바로 renderer나 normalizer에 연결하지 않도록 했는가 |

## 변경 제한 확인

| 완료 | 항목 |
|---|---|
| [x] | renderer 코드를 변경하지 않았는가 |
| [x] | normalizer 코드를 변경하지 않았는가 |
| [x] | fixture JSON을 추가하거나 변경하지 않았는가 |
| [x] | routing 결과를 변경하지 않았는가 |
| [x] | HWPX payload 구조를 변경하지 않았는가 |
| [x] | HWPX output을 재생성하지 않았는가 |
| [x] | 실제 HWPX/HWP 파일을 Git에 추가하지 않았는가 |

## 보안 검수

| 완료 | 항목 |
|---|---|
| [x] | 실제 개인정보를 추가하지 않았는가 |
| [x] | 실제 기관명, 업체명, 담당자명을 추가하지 않았는가 |
| [x] | 실제 문서번호, 민원번호, 사건번호를 추가하지 않았는가 |
| [x] | 실제 날짜, 예산, 실적 수치를 추가하지 않았는가 |
| [x] | 실제 공문 원문 또는 보고서 원문을 추가하지 않았는가 |
| [x] | 실제 HWPX 원본 파일을 추가하지 않았는가 |
| [x] | 실제 내부 경로나 파일명을 추가하지 않았는가 |
| [x] | API 키, 토큰, 인증정보 예시값을 추가하지 않았는가 |

## 다음 단계 확인

| 완료 | 항목 |
|---|---|
| [x] | HWPX 보고서 4종 수동 preview 서식 gap log 기준이 `docs/127`에 후속 반영되었는가 |
| [x] | 실제 양식 투입, output 재생성, 외부 연동 구현을 다음 단계로 두지 않았는가 |
