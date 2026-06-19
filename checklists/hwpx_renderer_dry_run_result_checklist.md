# HWPX 렌더러 연결 dry-run 결과 체크리스트

## 목적

`docs/71_hwpx_renderer_dry_run_result.md`와 dry-run PoC가 실제 HWPX 생성 없이 안전하게 수행되었는지 확인합니다.

## 실행 확인

| 완료 | 항목 |
|---|---|
| [x] | fixture 5종을 처리했는가 |
| [x] | `ready_for_draft` 케이스가 dry-run ready 상태인가 |
| [x] | `needs_more_input` 케이스가 dry-run ready with missing fields 상태인가 |
| [x] | `needs_security_review` 케이스가 제외되었는가 |
| [x] | `blocked` 케이스가 제외되었는가 |
| [x] | 실제 HWPX 파일을 생성하지 않았는가 |

## Git 제외 확인

| 완료 | 항목 |
|---|---|
| [x] | dry-run summary output이 Git 제외 대상인가 |
| [x] | 기존 HWPX renderer output이 Git 제외 대상인가 |
| [x] | 로컬 HWPX 템플릿이 Git 제외 대상인가 |

## 보안 검수

| 완료 | 항목 |
|---|---|
| [x] | 실제 개인정보를 포함하지 않았는가 |
| [x] | 실제 기관명, 업체명, 담당자명을 포함하지 않았는가 |
| [x] | 실제 문서번호, 민원번호, 접수번호, 사건번호를 포함하지 않았는가 |
| [x] | 실제 공문 또는 보고서 원문을 포함하지 않았는가 |
| [x] | 실제 예산액 또는 실적 수치를 생성하지 않았는가 |
| [x] | Email/API/Make.com 연동을 하지 않았는가 |

## 다음 단계 판단

| 완료 | 항목 |
|---|---|
| [x] | dry-run 결과 보관 방식 결정으로 넘어갈 수 있는가 |
