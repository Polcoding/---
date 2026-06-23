# 사용자 안내 3종 통합 점검

## 목적

`docs/140_user_operation_atoz_guide.md`, `checklists/user_operation_atoz_rehearsal_checklist.md`, `docs/141_user_rehearsal_prompt_examples.md`가 같은 기준으로 사용자에게 안내되는지 점검합니다.

이 문서는 실제 업무값, 실제 개인정보, 실제 기관명, 실제 문서번호, 실제 HWPX/HWP 원본, 실제 표 데이터를 기록하지 않습니다.

## 점검 대상

- `docs/140_user_operation_atoz_guide.md`
- `checklists/user_operation_atoz_rehearsal_checklist.md`
- `docs/141_user_rehearsal_prompt_examples.md`
- `docs/84_hwpx_report_user_input_templates.md`
- `docs/101_phase2_repeat_operation_log_template.md`
- `docs/104_missing_fields_user_display_guidance.md`
- `CURRENT_STATUS.md`
- `README.md`
- `AGENTS.md`
- `tasks/NEXT_STEP.md`

## 통합 기준

| 기준 | 점검 결과 |
|---|---|
| `[사용자 확인 필요]` | 사람이 직접 판단하거나 확인해야 하는 값으로 유지 |
| `[Codex 처리 가능]` | 비식별 placeholder 기반 구조화 가능 항목으로 유지 |
| `[보류]` | 실제 HWPX 원본, 실제 표 데이터, 외부 연동 제외 항목으로 유지 |
| HWPX 열람 지점 | 한컴에서 사람이 직접 확인해야 하는 항목으로 분리 |
| 실제값 처리 | 실제값 입력 또는 자동 확정 지시 없음 |

## 문서별 역할

| 문서 | 역할 | 점검 결과 |
|---|---|---|
| `docs/140_user_operation_atoz_guide.md` | 사용자 흐름 전체 안내 | 직접 확인, Codex 처리, 보류 항목 분리됨 |
| `checklists/user_operation_atoz_rehearsal_checklist.md` | 실제 HWPX 없는 리허설 체크 | 단계별 체크 항목이 역할 구분을 유지함 |
| `docs/141_user_rehearsal_prompt_examples.md` | 문서 유형별 비식별 요청 예시 | 보고서 4종 예시가 실제값 없이 유지됨 |
| `docs/84_hwpx_report_user_input_templates.md` | 상세 입력 템플릿 | 사용자 확인 지점과 보류 항목이 유지됨 |
| `docs/101_phase2_repeat_operation_log_template.md` | 반복 운영 로그 | 실제 업무값 기록 금지와 역할 구분 유지 |
| `docs/104_missing_fields_user_display_guidance.md` | missing_fields 표시 기준 | 본문 실제값과 검토용 목록 분리 유지 |

## 보고서 4종 예시 점검

| document_type | 예시 포함 | 실제값 금지 유지 | 사용자 확인 지점 |
|---|---|---|---|
| `one_page_report` | 포함 | 유지 | 보고 목적, 주요 내용, 향후 계획, 한컴 배치 확인 |
| `project_plan` | 포함 | 유지 | 일정, 예산, 추진대상, 표 폭 확인 |
| `result_report` | 포함 | 유지 | 실적, 계획 대비 결과, 예산 집행 정보 확인 |
| `review_report` | 포함 | 유지 | 검토 범위, 필요 검토 주체, 보안 승인 여부 확인 |

## 보류 항목 유지

아래 항목은 사용자 안내 3종에서 현재 단계 실행 대상으로 다루지 않습니다.

- 실제 기관 HWPX/HWP 원본 사용
- 실제 업무 원문 기반 작성
- 실제 개인정보, 기관정보, 문서번호 입력
- 실제 표 데이터, 수량, 금액, 대상 목록 자동 작성
- 실제 Email/API/Make.com 연동
- 실제 발송, 결재, 계약, 예산 집행, 법률 판단

## HWPX 열람 지점 분리

HWPX 파일을 직접 열어봐야 하는 항목은 `[사용자 확인 필요]`로 남깁니다.

- 파일 열림
- 글자 겹침
- 항목 순서
- 줄바꿈과 문단 배치
- 표 폭, 여백, 행 높이
- 남은 `{{placeholder}}`
- bullet 또는 번호 표기 일관성

현재 단계에서는 실제 HWPX output을 새로 생성하지 않습니다.

## Git 제외 기준

아래 파일군은 Git에 추가하지 않는 대상으로 유지합니다.

- `templates/hwpx/*.hwpx`
- `renderers/hwpx_renderer/output/*.hwpx`
- `normalizers/output/*`

Git 제외 여부는 작업 완료 전 `git check-ignore`와 `git status --ignored --short`로 재확인합니다.

## 판단

사용자 안내 3종은 현재 기준에서 서로 모순되지 않습니다.

다음 단계는 실제 HWPX 파일 생성이 아니라, 사용자가 이 안내를 보고 실제로 따라 하기 쉬운지 문구와 진입 순서를 더 줄이는 것입니다.

실제 HWPX 수동 preview는 비식별 작업 복사본이 준비되고 사용자가 한컴 열람을 요청할 때만 재개합니다.

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 표 데이터, 물품명, 수량, 금액, 대상 목록 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX/HWP 원본 파일 추가 없음
- Email, API, Make.com 연동 없음
