# HWPX 보고서 4종 template manifest와 공통 placeholder 정합성 점검

## 목적

HWPX 보고서 4종의 template manifest, 공통 placeholder 설계, 입력 요구사항, 사용자 입력 템플릿, local template policy, style profile manifest가 서로 충돌하지 않는지 문서 기준으로 점검합니다.

이 문서는 구현 지시서가 아닙니다. 실제 HWPX 원본, 실제 output 재생성, renderer 코드 변경, normalizer 변경, fixture 추가, APIㆍMake.comㆍEmail 연동 구현은 계속 보류합니다.

## 확인 대상

- `docs/123_phase4_template_stabilization_entry_judgment.md`
- `docs/124_project_direction_and_legacy_update_review.md`
- `docs/54_hwpx_common_placeholder_design.md`
- `docs/60_hwpx_report_input_requirements.md`
- `docs/84_hwpx_report_user_input_templates.md`
- `docs/40_hwpx_institution_style_values_review.md`
- `templates/hwpx/template_manifest.md`
- `templates/hwpx/local_template_policy.md`
- `templates/hwpx/style_profile_manifest.md`
- `checklists/before_automation_checklist.md`
- `renderers/hwpx_renderer/template_package.py`
- `normalizers/hwpx_payload_mapper_poc.py`

## 점검 결론

현재 저장소 기준으로 HWPX 보고서 4종 template manifest와 공통 placeholder 설계는 대체로 정합합니다.

다만 문서 기준으로 다음 보강이 필요했습니다.

| 항목 | 확인 내용 | 조치 |
|---|---|---|
| one_page_report style profile | template manifest에는 원페이지 보고서가 있으나 style profile manifest에는 전용 후보가 없었음 | `style_one_page_report_basic`을 `[확인 필요]` 상태로 추가 |
| 입력 필드와 placeholder 이름 차이 | `docs/60`의 `overview`, `schedule`, `budget`은 HWPX placeholder에서 `overview_table`, `schedule_table`, `budget_table`로 표현됨 | 입력 필드와 placeholder 매핑 표 추가 |
| `docs/84` 다음 단계 문구 | 과거 normalizers fixture 확장 후보로 남아 있었음 | 이번 점검 대상인 manifest-placeholder 정합성 점검으로 보정 |

위 조치는 문서 정합성 보강이며, 코드 동작이나 렌더링 결과를 바꾸지 않습니다.

## 문서 유형별 manifest 정합성

| document_type | template_id | template manifest 상태 | placeholder 그룹 | style_profile_id | 판단 |
|---|---|---|---|---|---|
| `one_page_report` | `hwpx_one_page_report_basic` | 로컬 검증 완료, Git 등록 안 함 | 원페이지 보고서 | `style_one_page_report_basic` | 정합 |
| `project_plan` | `hwpx_project_plan_basic` | 로컬 검증 완료, Git 등록 안 함 | 추진계획서 | `style_project_plan_basic` | 정합 |
| `result_report` | `hwpx_result_report_basic` | 로컬 검증 완료, Git 등록 안 함 | 결과보고서 | `style_result_report_basic` | 정합 |
| `review_report` | `hwpx_review_report_basic` | 로컬 검증 완료, Git 등록 안 함 | 검토보고서 | `style_review_report_basic` | 정합, 보안 검토 조건 유지 |

## 공통 메타 placeholder 정합성

다음 메타 placeholder는 HWPX 보고서 4종에 공통으로 유지합니다.

| placeholder | 입력 기준 | 판단 |
|---|---|---|
| `{{title}}` | `documents[0].title` 또는 문서 유형별 제목 필드 | 유지 |
| `{{missing_fields}}` | `missing_fields` | 유지, 자동 제외 금지 |
| `{{checklist}}` | `documents[0].checklist` 또는 `checklist` | 유지 |
| `{{security_review}}` | `security_review` | 유지, 누락 시 렌더링 중단 권장 |
| `{{draft_status}}` | `draft_status` | 유지 |
| `{{human_review_required}}` | `human_review_required` | 유지, 사람 검토 전제 |

`{{document_number}}`, `{{execution_date}}`, `{{recipient}}`, `{{reference}}`, `{{attachments}}`는 공문 또는 일부 템플릿에서 사용할 수 있으나 실제값을 임의 생성하지 않습니다.

## 입력 필드와 placeholder 매핑

### one_page_report

| 입력 필드 | HWPX placeholder | 판단 |
|---|---|---|
| `title` | `{{title}}` | 정합 |
| `report_summary` | `{{report_summary}}` | 정합 |
| `background` | `{{background}}` | 정합 |
| `main_points` | `{{main_points}}` | 정합 |
| `review_opinion` | `{{review_opinion}}` | 정합 |
| `issues_or_considerations` | `{{issues_or_considerations}}` | 정합 |
| `next_steps` | `{{next_steps}}` | 정합 |
| `action_items` | `{{action_items}}` | 정합 |

### project_plan

| 입력 필드 | HWPX placeholder | 판단 |
|---|---|---|
| `title` | `{{title}}` | 정합 |
| `background` | `{{background}}` | 정합 |
| `purpose` | `{{purpose}}` | 정합 |
| `overview` | `{{overview_table}}` | 명시 매핑 필요, 보강 |
| `main_contents` | `{{main_contents}}` | 정합 |
| `detailed_plan` | `{{detailed_plan}}` | 정합 |
| `schedule` | `{{schedule_table}}` | 명시 매핑 필요, 보강 |
| `budget` | `{{budget_table}}` | 명시 매핑 필요, 보강 |
| `expected_effects` | `{{expected_effects}}` | 정합 |
| `review_items` | `{{review_items}}` | 정합 |
| `future_plan` | `{{future_plan}}` | 정합 |

### result_report

| 입력 필드 | HWPX placeholder | 판단 |
|---|---|---|
| `title` | `{{title}}` | 정합 |
| `linked_plan_reference` | `{{linked_plan_reference}}` | 정합 |
| `overview` | `{{overview_table}}` | 명시 매핑 필요, 보강 |
| `planned_items` | `{{planned_items}}` | 정합 |
| `actual_results` | `{{actual_results}}` | 정합 |
| `comparison_to_plan` | `{{comparison_to_plan}}` | 정합 |
| `main_outcomes` | `{{main_outcomes}}` | 정합 |
| `issues` | `{{issues}}` | 정합 |
| `improvements` | `{{improvements}}` | 정합 |
| `future_plan` | `{{future_plan}}` | 정합 |

### review_report

| 입력 필드 | HWPX placeholder | 판단 |
|---|---|---|
| `title` | `{{title}}` | 정합 |
| `review_background` | `{{review_background}}` | 정합 |
| `review_scope` | `{{review_scope}}` | 정합 |
| `review_items` | `{{review_items}}` | 정합 |
| `review_opinion` | `{{review_opinion}}` | 정합 |
| `risks` | `{{risks}}` | 정합 |
| `required_reviews` | `{{required_reviews}}` | 정합 |
| `next_actions` | `{{next_actions}}` | 정합 |

`review_report`는 승인 없는 입력을 `needs_security_review`로 멈추는 조건을 유지합니다. placeholder 렌더링은 사람이 보안 검토 완료 신호를 준 경우에만 허용합니다.

## 누락값 처리 기준

누락값 기준은 문서 간 충돌 없이 유지합니다.

| 상황 | 기준 |
|---|---|
| 제목 누락 | 문서 유형별 `[확인 필요]` 제목 사용 |
| 본문 핵심값 누락 | `[확인 필요]` 포함 문구 사용 |
| 배열 누락 | `[확인 필요]` 또는 템플릿별 안전한 빈 문자열 |
| 메타 검토값 누락 | `missing_fields`에 기록 |
| 보안 검토값 누락 | 렌더링 중단 권장 |
| 예산, 일정, 실적, 담당자, 수량 누락 | 임의 생성 금지, `[확인 필요]` 유지 |
| C/D등급 또는 실제 원문 포함 | 렌더링 및 외부 AI 처리 중단 |

## policy와 Git 제외 정합성

local template policy와 template manifest는 다음 원칙을 일관되게 유지합니다.

- 실제 기관 HWPX 원본은 저장소 밖에서만 다룸
- 로컬 placeholder HWPX 템플릿은 Git 제외 상태 유지
- output HWPX와 summary output은 Git 제외 상태 유지
- GitHub Desktop Changes에 HWP/HWPX 파일이 나타나면 작업 중단
- 실제 파일명, 실제 기관 양식명, 실제 문서번호는 manifest에 기록하지 않음

## 코드 변경 판단

이번 점검에서는 코드 변경이 필요하지 않습니다.

변경하지 않는 항목:

- `normalizers/`
- `renderers/`
- `examples/json/`
- routing fixture
- HWPX payload mapper
- HWPX renderer output
- local HWPX template
- API, Make.com, Email 연동 코드

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX 원본 파일 추가 없음
- 실제 계정명, 이메일 주소, 결제정보 추가 없음
- 실제 수신자, 참조자, 첨부 파일명 추가 없음
- API 키, 토큰, 인증정보 예시값 추가 없음
- Email, API, Make.com 연동 구현 없음

## 결론

HWPX 보고서 4종의 template manifest와 공통 placeholder 설계는 문서 기준으로 정합합니다.

style profile의 `[확인 필요]` 값 유지 기준과 수집 체크리스트는 `docs/126_style_profile_confirmation_value_collection_criteria.md`에 후속 반영했습니다.

HWPX 보고서 4종 수동 preview 서식 gap log 기준은 `docs/127_hwpx_manual_preview_gap_log_criteria.md`에 후속 반영했습니다.

저장소 밖 실제 양식 후보 수동 절차와 보류 조건은 `docs/128_external_hwpx_candidate_manual_procedure_and_hold_criteria.md`에 후속 반영했습니다.

local template policy와 Git 제외 상태 반복 검증 기준은 `docs/129_local_template_gitignore_repeat_verification_criteria.md`에 후속 반영했습니다.

다음 단계는 Phase 4 문서 템플릿 안정화 통합 점검과 실제 양식 수동 리허설 진입 여부를 문서로 판단하는 것입니다. 실제 기관 양식 원본, HWPX output 재생성, renderer 코드 변경, 외부 연동 구현은 계속 보류합니다.
