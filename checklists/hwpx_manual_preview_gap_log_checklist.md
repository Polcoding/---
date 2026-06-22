# HWPX 수동 preview 서식 gap log 체크리스트

## 목적

`docs/127_hwpx_manual_preview_gap_log_criteria.md` 기준으로 HWPX 보고서 4종 수동 preview에서 발견되는 서식 차이를 실제값 없이 기록할 수 있는지 확인합니다.

## 기준 문서 확인

| 완료 | 항목 |
|---|---|
| [x] | `docs/126_style_profile_confirmation_value_collection_criteria.md`를 확인했는가 |
| [x] | `checklists/style_profile_confirmation_value_collection_checklist.md`를 확인했는가 |
| [x] | `checklists/hwpx_rendered_output_manual_review_checklist.md`를 확인했는가 |
| [x] | `docs/112_phase3_external_hwpx_and_manual_preview_criteria.md`를 확인했는가 |
| [x] | `docs/119_phase3_user_preview_and_human_approval_integration.md`를 확인했는가 |
| [x] | `docs/57_hwpx_report_4types_completion_and_safety_rehearsal.md`를 확인했는가 |

## gap log 구조 확인

| 완료 | 항목 |
|---|---|
| [x] | gap log 필드를 문서화했는가 |
| [x] | 문서유형, 항목, 증상, 심각도, 후속 조치를 분리했는가 |
| [x] | gap 유형을 글자 겹침, 줄바꿈, 번호 들여쓰기, 기호 표기, 표 폭, 여백 등으로 구분했는가 |
| [x] | 심각도를 `차단`, `수정 필요`, `관찰`, `문제 없음`으로 구분했는가 |
| [x] | style profile `[확인 필요]`와 preview gap을 구분했는가 |

## 사용자 확인 필요 항목

| 완료 | 항목 |
|---|---|
| [x] | one_page_report 수동 확인 항목을 정리했는가 |
| [x] | project_plan 수동 확인 항목을 정리했는가 |
| [x] | result_report 수동 확인 항목을 정리했는가 |
| [x] | review_report 수동 확인 항목을 정리했는가 |
| [x] | `[사용자 확인 필요]` 표시가 눈에 보이도록 남아 있는가 |

## 기록 제한 확인

| 완료 | 항목 |
|---|---|
| [x] | 실제 기관명을 기록하지 않도록 했는가 |
| [x] | 실제 문서번호를 기록하지 않도록 했는가 |
| [x] | 실제 파일명 또는 내부 경로를 기록하지 않도록 했는가 |
| [x] | 실제 원문 또는 원문 요약을 기록하지 않도록 했는가 |
| [x] | 실제 예산, 일정, 실적 수치를 기록하지 않도록 했는가 |

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
| [x] | 저장소 밖 실제 양식 후보 수동 절차와 보류 조건 재정렬이 `docs/128`에 반영되었는가 |
| [x] | local template policy와 Git 제외 상태 반복 검증 기준이 `docs/129`에 반영되었는가 |
| [x] | 다음 단계가 Phase 4 문서 템플릿 안정화 통합 점검과 실제 양식 수동 리허설 진입 여부 판단인가 |
| [x] | 실제 양식 투입, output 재생성, 외부 연동 구현을 다음 단계로 두지 않았는가 |
