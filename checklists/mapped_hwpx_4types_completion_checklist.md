# HWPX 4종 mapped 렌더링 완료 체크리스트

## 목적

`docs/80_mapped_hwpx_4types_completion_summary.md` 기준으로 보고서 4종 mapped HWPX 렌더링 완료 상태를 확인합니다.

## 렌더링 확인

| 완료 | 항목 |
|---|---|
| [x] | `one_page_report` mapped HWPX 렌더링이 완료되었는가 |
| [x] | `project_plan` mapped HWPX 렌더링이 완료되었는가 |
| [x] | `result_report` mapped HWPX 렌더링이 완료되었는가 |
| [x] | `review_report` approved fixture mapped HWPX 렌더링이 완료되었는가 |
| [x] | 4종 모두 `remaining_placeholders`가 0인가 |
| [x] | 4종 모두 렌더링 errors가 없는가 |

## 사용자 수동 검수

| 완료 | 항목 |
|---|---|
| [x] | `one_page_report`를 한컴에서 수동 검수했는가 |
| [x] | `project_plan`을 한컴에서 수동 검수했는가 |
| [x] | `result_report`를 한컴에서 수동 검수했는가 |
| [x] | `review_report`를 한컴에서 수동 검수했는가 |
| [x] | 글자 겹침 문제가 없는가 |
| [x] | 내용 앞 `-` 표기 문제가 보정되었는가 |

## review_report 보안 조건

| 완료 | 항목 |
|---|---|
| [x] | 승인 없는 `review_report`가 `needs_security_review`로 유지되는가 |
| [x] | placeholder 보안 승인 신호가 있는 경우만 렌더링하는가 |
| [x] | 실제 승인자명, 결재번호, 검토의견 원문을 사용하지 않았는가 |

## Git 제외 확인

| 완료 | 항목 |
|---|---|
| [x] | output HWPX가 Git 제외 대상인가 |
| [x] | normalizers output summary가 Git 제외 대상인가 |
| [x] | 로컬 HWPX 템플릿이 Git 제외 대상인가 |

## 보안 검수

| 완료 | 항목 |
|---|---|
| [x] | 실제 개인정보를 포함하지 않았는가 |
| [x] | 실제 기관명, 업체명, 담당자명을 포함하지 않았는가 |
| [x] | 실제 문서번호, 민원번호, 접수번호, 사건번호를 포함하지 않았는가 |
| [x] | 실제 공문 또는 보고서 원문을 포함하지 않았는가 |
| [x] | 실제 예산액, 일정, 실적 수치를 생성하지 않았는가 |
| [x] | Email/API/Make.com 연동을 하지 않았는가 |

## 다음 단계 판단

| 완료 | 항목 |
|---|---|
| [x] | HWPX 4종 mapped 렌더링 PoC 완료 상태를 확정할 수 있는가 |
| [ ] | 입력 정규화와 보안 필터 회귀 테스트 묶음 정리로 넘어갈 수 있는가 |
