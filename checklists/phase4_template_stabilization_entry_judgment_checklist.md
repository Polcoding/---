# Phase 4 문서 템플릿 안정화 진입 판단 체크리스트

## 목적

`docs/123_phase4_template_stabilization_entry_judgment.md` 기준으로 Phase 4를 실제 구현이 아닌 HWPX 보고서 4종 문서 템플릿 안정화 검토로 시작할 수 있는지 확인합니다.

## 기준 문서 확인

| 완료 | 항목 |
|---|---|
| [x] | `docs/122_phase3_closeout_and_phase4_entry_decision.md`를 확인했는가 |
| [x] | `checklists/phase3_closeout_and_phase4_entry_decision_checklist.md`를 확인했는가 |
| [x] | 외부 연동 구현 보류 판단을 확인했는가 |
| [x] | `docs/54_hwpx_common_placeholder_design.md`를 확인했는가 |
| [x] | `docs/60_hwpx_report_input_requirements.md`를 확인했는가 |
| [x] | `docs/84_hwpx_report_user_input_templates.md`를 확인했는가 |
| [x] | HWPX template manifest와 local template policy를 확인했는가 |
| [x] | style profile manifest의 미확정 값 유지 기준을 확인했는가 |

## 진입 가능 범위 확인

| 완료 | 항목 |
|---|---|
| [x] | Phase 4를 HWPX 보고서 4종 문서 템플릿 안정화로 제한했는가 |
| [x] | 실제 기관 HWPX 원본 없이 placeholder와 manifest 기준으로 점검 가능하다고 판단했는가 |
| [x] | 공통 placeholder와 문서 유형별 placeholder 정합성 점검을 다음 후보로 두었는가 |
| [x] | 누락값, `[확인 필요]`, `missing_fields` 기준 점검을 허용 범위로 두었는가 |
| [x] | style profile의 확인되지 않은 값을 임의 확정하지 않기로 했는가 |
| [x] | local template policy와 Git 제외 원칙 점검을 허용 범위로 두었는가 |

## 계속 보류할 범위 확인

| 완료 | 항목 |
|---|---|
| [x] | 실제 기관 HWPX 원본 Git 추가를 계속 금지했는가 |
| [x] | 실제 HWPX output 재생성을 금지했는가 |
| [x] | 실제 원문 또는 개인정보 기반 검증을 금지했는가 |
| [x] | 확인되지 않은 서식값 임의 확정을 금지했는가 |
| [x] | renderer 코드 변경을 이번 단계 범위에서 제외했는가 |
| [x] | normalizer 코드 변경을 이번 단계 범위에서 제외했는가 |
| [x] | routing, fixture, HWPX payload 변경을 제외했는가 |
| [x] | Email, API, Make.com 실제 연동 구현을 계속 보류했는가 |

## 문서 정합성 점검 후보 확인

| 완료 | 항목 |
|---|---|
| [x] | `docs/54` 공통 placeholder 설계 점검을 다음 후보로 두었는가 |
| [x] | `docs/60` 입력 요구사항 점검을 다음 후보로 두었는가 |
| [x] | `docs/84` 사용자 입력 템플릿 점검을 다음 후보로 두었는가 |
| [x] | `templates/hwpx/template_manifest.md` 점검을 다음 후보로 두었는가 |
| [x] | `templates/hwpx/local_template_policy.md` 점검을 다음 후보로 두었는가 |
| [x] | `templates/hwpx/style_profile_manifest.md` 점검을 다음 후보로 두었는가 |

## 변경 제한 확인

| 완료 | 항목 |
|---|---|
| [x] | `normalizers/` 코드를 변경하지 않았는가 |
| [x] | `renderers/` 코드를 변경하지 않았는가 |
| [x] | `examples/json/` fixture를 변경하지 않았는가 |
| [x] | HWPX payload mapper를 변경하지 않았는가 |
| [x] | HWPX renderer output을 재생성하지 않았는가 |
| [x] | local HWPX template을 Git에 추가하지 않았는가 |
| [x] | API 키, 토큰, 인증정보 예시값을 만들지 않았는가 |

## 보안 검수

| 완료 | 항목 |
|---|---|
| [x] | 실제 개인정보를 추가하지 않았는가 |
| [x] | 실제 기관명, 업체명, 담당자명을 추가하지 않았는가 |
| [x] | 실제 문서번호, 민원번호, 사건번호를 추가하지 않았는가 |
| [x] | 실제 날짜, 예산, 실적 수치를 추가하지 않았는가 |
| [x] | 실제 공문 원문 또는 보고서 원문을 추가하지 않았는가 |
| [x] | 실제 HWPX 원본 파일을 추가하지 않았는가 |
| [x] | 실제 수신자, 참조자, 첨부 파일명을 추가하지 않았는가 |
| [x] | API 키, 토큰, 인증정보 예시값을 추가하지 않았는가 |

## 다음 단계 확인

| 완료 | 항목 |
|---|---|
| [x] | 다음 단계가 코드 변경이 아닌 문서 정합성 점검인가 |
| [x] | HWPX 보고서 4종 template manifest와 공통 placeholder 정합성 점검이 후속 반영되었는가 |
| [x] | 저장소 밖 실제 양식 후보 수동 절차와 보류 조건이 후속 반영되었는가 |
| [x] | local template policy와 Git 제외 상태 반복 검증 기준이 후속 반영되었는가 |
| [x] | Phase 4 문서 템플릿 안정화 통합 점검이 후속 반영되었는가 |
| [x] | 다음 단계가 실제 양식 수동 리허설 사용자 확인 패킷과 gap log 빈 양식 정리인가 |
| [x] | 실제 HWPX 원본, output, 외부 연동 구현을 다음 단계로 두지 않았는가 |
