# mapped review_report HWPX 렌더링 결과 체크리스트

## 목적

`docs/79_mapped_review_report_hwpx_render_result.md`와 실제 렌더링 결과가 안전하게 생성되었는지 확인합니다.

## 실행 확인

| 완료 | 항목 |
|---|---|
| [x] | `approved_review_report_request.json`만 mapped review_report 렌더링 대상으로 추가했는가 |
| [x] | routing이 `ready_for_draft`였는가 |
| [x] | HWPX 렌더링 상태가 `rendered`인가 |
| [x] | `remaining_placeholders`가 0인가 |
| [x] | 렌더링 errors가 없는가 |

## Git 제외 확인

| 완료 | 항목 |
|---|---|
| [x] | output HWPX가 Git 제외 대상인가 |
| [x] | summary JSON이 Git 제외 대상인가 |
| [x] | 로컬 HWPX 템플릿이 Git 제외 대상인가 |

## 보안 검수

| 완료 | 항목 |
|---|---|
| [x] | 실제 개인정보를 포함하지 않았는가 |
| [x] | 실제 기관명, 업체명, 담당자명을 포함하지 않았는가 |
| [x] | 실제 승인자명, 결재번호, 문서번호를 포함하지 않았는가 |
| [x] | 실제 공문 또는 보고서 원문을 포함하지 않았는가 |
| [x] | 실제 검토의견 원문을 포함하지 않았는가 |
| [x] | 실제 예산액, 일정, 실적 수치를 생성하지 않았는가 |
| [x] | Email/API/Make.com 연동을 하지 않았는가 |

## 사용자 수동 검수

| 완료 | 항목 |
|---|---|
| [x] | 한컴에서 output HWPX를 열어보았는가 |
| [x] | 글자 겹침이 없는가 |
| [x] | 1~10번 항목 제목이 정상 표시되는가 |
| [x] | 검토 배경, 검토 범위, 검토 항목, 검토 의견, 위험 요소, 필요 검토, 향후 조치가 적절히 표시되는가 |
| [x] | 내용 앞 `-` 표기가 일관적인가 |
| [x] | 남은 `{{placeholder}}`가 없는가 |

## 다음 단계 판단

| 완료 | 항목 |
|---|---|
| [x] | 사용자 수동 검수 후 HWPX 4종 mapped 렌더링 완료 상태를 확정할 수 있는가 |
