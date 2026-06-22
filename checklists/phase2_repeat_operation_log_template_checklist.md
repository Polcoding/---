# Phase 2 반복 운영 로그 템플릿 체크리스트

## 목적

`docs/101_phase2_repeat_operation_log_template.md`가 Phase 2 반복 운영 결과를 안전하게 기록할 수 있는지 확인합니다.

## 기본 정보 확인

| 완료 | 항목 |
|---|---|
| [x] | 실행일을 placeholder로 기록하게 했는가 |
| [x] | 실행 목적과 범위를 기록하게 했는가 |
| [x] | 실제 원문, 개인정보, 기관 양식 원본 미사용 여부를 기록하게 했는가 |

## 실행 명령 확인

| 완료 | 항목 |
|---|---|
| [x] | helper fixture 검증 명령을 포함했는가 |
| [x] | input normalizer 명령을 포함했는가 |
| [x] | HWPX payload mapper 명령을 포함했는가 |
| [x] | HWPX payload validation 명령을 포함했는가 |
| [x] | HWPX renderer dry-run 명령을 포함했는가 |
| [x] | mapped HWPX render 명령을 포함했는가 |

## 상태별 중단 확인

| 완료 | 항목 |
|---|---|
| [x] | `needs_security_review` 렌더링 중단 확인란을 포함했는가 |
| [x] | `blocked` 처리 중단 확인란을 포함했는가 |
| [x] | `template_required` 안전 중단 확인란을 포함했는가 |
| [x] | validation 실패 시 렌더링 중단 확인란을 포함했는가 |
| [x] | `remaining_placeholders` 잔여 시 preview 중단 확인란을 포함했는가 |
| [x] | output 잠금 처리 확인란을 포함했는가 |
| [x] | GitHub Desktop Changes에 HWPX 표시 시 중단 확인란을 포함했는가 |

## HWPX 및 사용자 검수 확인

| 완료 | 항목 |
|---|---|
| [x] | HWPX output 4종 확인란을 포함했는가 |
| [x] | `missing_fields` 확인 섹션을 포함했는가 |
| [x] | HWPX 본문과 검토용 확인 목록 분리 확인란을 포함했는가 |
| [x] | `missing_fields`를 본문 실제값으로 확정하지 않는다고 명시했는가 |
| [x] | 사용자 한컴 검수 항목을 포함했는가 |
| [x] | 이상 발생 시 파일명, 항목 번호, 증상 기록 형식을 포함했는가 |

## Git 제외와 보안 확인

| 완료 | 항목 |
|---|---|
| [x] | GitHub Desktop Changes 확인란을 포함했는가 |
| [x] | output 산출물 Git 제외 확인을 포함했는가 |
| [x] | 로컬 HWPX 템플릿 Git 제외 확인을 포함했는가 |
| [x] | 보안 검수 항목을 포함했는가 |

## 보류 범위 확인

| 완료 | 항목 |
|---|---|
| [x] | 실제 기관 양식 원본 사용을 금지했는가 |
| [x] | 실제 문서 원문 사용을 금지했는가 |
| [x] | Email/API/Make.com 연동을 추가하지 않았는가 |
| [x] | `missing_fields` 자동 제외를 추가하지 않았는가 |
| [x] | `placeholder_confirmed_values` routing 연결을 계속 보류했는가 |

## 보안 검수

| 완료 | 항목 |
|---|---|
| [x] | 실제 개인정보를 추가하지 않았는가 |
| [x] | 실제 기관명, 업체명, 담당자명을 추가하지 않았는가 |
| [x] | 실제 문서번호, 민원번호, 사건번호를 추가하지 않았는가 |
| [x] | 실제 날짜, 예산, 실적 수치를 추가하지 않았는가 |
| [x] | 실제 공문 원문 또는 보고서 원문을 추가하지 않았는가 |
| [x] | 실제 HWPX 원본 파일을 추가하지 않았는가 |
