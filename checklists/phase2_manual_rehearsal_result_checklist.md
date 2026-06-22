# Phase 2 수동 리허설 실행 결과 체크리스트

## 목적

`docs/99_phase2_manual_rehearsal_result.md` 기준으로 Phase 2 수동 리허설 1회 실행 결과가 안전하게 기록되었는지 확인합니다.

## Codex 실행 확인

| 완료 | 항목 |
|---|---|
| [x] | helper fixture 검증을 실행했는가 |
| [x] | 입력 정규화 fixture 6종을 실행했는가 |
| [x] | HWPX payload mapper를 실행했는가 |
| [x] | HWPX payload validation을 실행했는가 |
| [x] | HWPX renderer dry-run을 실행했는가 |
| [x] | mapped HWPX 렌더링을 실행했는가 |

## 렌더링 결과 확인

| 완료 | 항목 |
|---|---|
| [x] | mapped HWPX 4종이 `rendered` 상태인가 |
| [x] | mapped HWPX 4종의 `remaining_placeholders`가 0인가 |
| [x] | blocked fixture가 HWPX output으로 생성되지 않았는가 |
| [x] | `needs_security_review` fixture가 HWPX output으로 생성되지 않았는가 |
| [x] | sandbox 쓰기 제한과 실제 렌더 결과를 분리해서 기록했는가 |

## Git 제외 확인

| 완료 | 항목 |
|---|---|
| [x] | `normalizers/output/*.json`이 ignored 상태인가 |
| [x] | `renderers/hwpx_renderer/output/*.hwpx`가 ignored 상태인가 |
| [x] | `renderers/hwpx_renderer/output/*.json`이 ignored 상태인가 |
| [x] | `templates/hwpx/*.hwpx`가 ignored 상태인가 |
| [x] | Python cache를 tracked 변경에 포함하지 않았는가 |

## 사용자 확인 완료

| 완료 | 항목 |
|---|---|
| [x] | 사용자가 `mapped_safe_one_page_report_poc.hwpx`를 한컴에서 확인했는가 |
| [x] | 사용자가 `mapped_missing_project_plan_poc.hwpx`를 한컴에서 확인했는가 |
| [x] | 사용자가 `mapped_missing_result_report_poc.hwpx`를 한컴에서 확인했는가 |
| [x] | 사용자가 `mapped_approved_review_report_poc.hwpx`를 한컴에서 확인했는가 |
| [x] | 글자 겹침, 항목 순서, bullet 표기, placeholder 잔여, 민감정보 여부를 확인했는가 |

## 보안 검수

| 완료 | 항목 |
|---|---|
| [x] | 실제 개인정보를 추가하지 않았는가 |
| [x] | 실제 기관명, 업체명, 담당자명을 추가하지 않았는가 |
| [x] | 실제 문서번호, 민원번호, 사건번호를 추가하지 않았는가 |
| [x] | 실제 날짜, 예산, 실적 수치를 추가하지 않았는가 |
| [x] | 실제 공문 원문 또는 보고서 원문을 추가하지 않았는가 |
| [x] | 실제 HWPX 원본 파일을 추가하지 않았는가 |
