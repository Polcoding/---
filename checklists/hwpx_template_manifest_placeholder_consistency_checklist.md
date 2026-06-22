# HWPX template manifest와 공통 placeholder 정합성 체크리스트

## 목적

`docs/125_hwpx_template_manifest_placeholder_consistency_review.md` 기준으로 HWPX 보고서 4종의 template manifest, 공통 placeholder, 입력 요구사항, 사용자 입력 템플릿, style profile, local template policy 정합성을 확인합니다.

## 기준 문서 확인

| 완료 | 항목 |
|---|---|
| [x] | `docs/123_phase4_template_stabilization_entry_judgment.md`를 확인했는가 |
| [x] | `docs/124_project_direction_and_legacy_update_review.md`를 확인했는가 |
| [x] | `docs/54_hwpx_common_placeholder_design.md`를 확인했는가 |
| [x] | `docs/60_hwpx_report_input_requirements.md`를 확인했는가 |
| [x] | `docs/84_hwpx_report_user_input_templates.md`를 확인했는가 |
| [x] | HWPX template manifest, local template policy, style profile manifest를 확인했는가 |

## manifest 정합성 확인

| 완료 | 항목 |
|---|---|
| [x] | `one_page_report` template_id와 placeholder 그룹이 대응되는가 |
| [x] | `project_plan` template_id와 placeholder 그룹이 대응되는가 |
| [x] | `result_report` template_id와 placeholder 그룹이 대응되는가 |
| [x] | `review_report` template_id와 placeholder 그룹이 대응되는가 |
| [x] | 실제 HWPX 파일명을 manifest에 기록하지 않았는가 |
| [x] | 로컬 placeholder 파일은 Git 등록 안 함 상태로 유지했는가 |

## placeholder 매핑 확인

| 완료 | 항목 |
|---|---|
| [x] | 공통 메타 placeholder를 유지했는가 |
| [x] | one_page_report 입력 필드가 placeholder와 대응되는가 |
| [x] | project_plan의 `overview`, `schedule`, `budget`을 `overview_table`, `schedule_table`, `budget_table`로 명시 매핑했는가 |
| [x] | result_report의 `overview`를 `overview_table`로 명시 매핑했는가 |
| [x] | review_report 보안 검토 조건을 유지했는가 |
| [x] | `missing_fields`, `[확인 필요]`, 안전한 빈 문자열 처리 기준을 유지했는가 |

## style profile 확인

| 완료 | 항목 |
|---|---|
| [x] | one_page_report style profile 후보를 `[확인 필요]` 상태로 추가했는가 |
| [x] | project_plan style profile 후보를 유지했는가 |
| [x] | result_report style profile 후보를 유지했는가 |
| [x] | review_report style profile 후보를 유지했는가 |
| [x] | 확인되지 않은 서식값을 임의 확정하지 않았는가 |

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
| [x] | API 키, 토큰, 인증정보 예시값을 추가하지 않았는가 |

## 다음 단계 확인

| 완료 | 항목 |
|---|---|
| [x] | style profile `[확인 필요]` 값 유지 기준과 수집 체크리스트가 후속 반영되었는가 |
| [x] | 저장소 밖 실제 양식 후보 수동 절차와 보류 조건이 후속 반영되었는가 |
| [x] | local template policy와 Git 제외 상태 반복 검증 기준이 후속 반영되었는가 |
| [x] | Phase 4 문서 템플릿 안정화 통합 점검이 후속 반영되었는가 |
| [x] | 실제 양식 수동 리허설 사용자 확인 패킷이 후속 반영되었는가 |
| [x] | 다음 단계가 저장소 밖 한컴 preview 결과의 실제값 없는 gap log 기록인가 |
| [x] | 실제 양식 투입, output 재생성, 외부 연동 구현을 다음 단계로 두지 않았는가 |
