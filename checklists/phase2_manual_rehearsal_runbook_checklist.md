# Phase 2 수동 리허설 runbook 체크리스트

## 목적

`docs/98_phase2_manual_rehearsal_runbook.md`가 Phase 2 최소 PoC를 안전하게 반복 실행할 수 있는 절차로 정리되었는지 확인합니다.

## 범위 확인

| 완료 | 항목 |
|---|---|
| [x] | 비식별 입력부터 HWPX output 확인까지 포함했는가 |
| [x] | API, Make.com, Email 자동화를 제외했는가 |
| [x] | 실제 기관 양식 원본 사용 금지를 유지했는가 |
| [x] | `placeholder_confirmed_values` 코드 연결 보류를 유지했는가 |

## 사용자 확인 지점

| 완료 | 항목 |
|---|---|
| [x] | 입력 전 사용자 확인 항목을 분리했는가 |
| [x] | HWPX output 열람 후 사용자 확인 항목을 분리했는가 |
| [x] | GitHub Desktop Changes 확인 항목을 분리했는가 |
| [x] | 사용자가 이상 보고할 때 필요한 파일명과 항목 번호를 안내했는가 |

## 명령 순서

| 완료 | 항목 |
|---|---|
| [x] | helper fixture 검증 명령을 포함했는가 |
| [x] | 입력 정규화 명령을 포함했는가 |
| [x] | HWPX payload mapper 명령을 포함했는가 |
| [x] | HWPX payload validation 명령을 포함했는가 |
| [x] | HWPX renderer dry-run 명령을 포함했는가 |
| [x] | mapped HWPX render 명령을 포함했는가 |

## output 및 Git 제외

| 완료 | 항목 |
|---|---|
| [x] | `normalizers/output/` Git 제외 확인을 포함했는가 |
| [x] | `renderers/hwpx_renderer/output/` Git 제외 확인을 포함했는가 |
| [x] | `templates/hwpx/*.hwpx` Git 제외 확인을 포함했는가 |
| [x] | output 폴더 쓰기 권한과 파일 잠금 확인을 포함했는가 |

## 중단 기준

| 완료 | 항목 |
|---|---|
| [x] | 실제 개인정보 발견 시 중단 기준을 포함했는가 |
| [x] | 실제 문서번호 등 식별정보 발견 시 중단 기준을 포함했는가 |
| [x] | `review_report` 승인 신호 누락 시 중단 기준을 포함했는가 |
| [x] | blocked fixture output 생성 시 중단 기준을 포함했는가 |
| [x] | HWPX 겹침 또는 placeholder 잔여 시 중단 기준을 포함했는가 |
| [x] | GitHub Desktop Changes에 output 파일이 보일 때 중단 기준을 포함했는가 |

## 보안 검수

| 완료 | 항목 |
|---|---|
| [x] | 실제 개인정보를 추가하지 않았는가 |
| [x] | 실제 기관명, 업체명, 담당자명을 추가하지 않았는가 |
| [x] | 실제 문서번호, 민원번호, 사건번호를 추가하지 않았는가 |
| [x] | 실제 날짜, 예산, 실적 수치를 추가하지 않았는가 |
| [x] | 실제 공문 원문 또는 보고서 원문을 추가하지 않았는가 |
| [x] | 실제 HWPX 원본 파일을 추가하지 않았는가 |
