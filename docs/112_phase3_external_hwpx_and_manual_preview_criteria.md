# Phase 3 저장소 밖 HWPX 취급 및 수동 preview 기준

## 목적

Phase 3 안전 게이트 이후 실제 HWPX 양식 복사본을 저장소 밖에서 어떻게 다룰지, 그리고 사용자가 HWPX output을 어떻게 수동 preview할지 구체화합니다.

이 문서는 실제 기관 HWPX 원본을 저장소에 추가하거나 자동화하는 문서가 아닙니다. 실제 원문, 개인정보, 기관정보, 문서번호는 계속 제외합니다.

## 기준 문서

- `docs/53_real_hwpx_template_intake_safety_procedure.md`
- `docs/58_external_hwpx_placeholder_conversion_runbook.md`
- `docs/83_phase2_user_input_and_manual_operation_checkpoints.md`
- `docs/98_phase2_manual_rehearsal_runbook.md`
- `docs/100_phase2_repeat_operation_criteria.md`
- `docs/101_phase2_repeat_operation_log_template.md`
- `docs/111_phase3_entry_safety_gate.md`

## 적용 범위

포함:

- 저장소 밖 로컬 작업 폴더에서 실제 HWPX 양식 복사본을 다루는 기준
- 복사본을 placeholder 후보로 바꾸는 기준
- GitHub Desktop Changes 확인 기준
- HWPX output 사용자 수동 preview 기준
- `template_required`, `needs_security_review`, `blocked` 중단 기준

제외:

- 실제 기관 HWPX 원본 Git 추가
- 실제 공문 또는 보고서 원문 저장
- 실제 개인정보, 민원정보, 내부 운영정보 처리
- 한컴 프로그램 자동 제어
- API, Make.com, Email 실제 연동

## 저장소 밖 HWPX 양식 취급 기준

### 1. 작업 위치

실제 원본 또는 작업 복사본은 저장소 밖 로컬 폴더에서만 다룹니다.

허용 예시:

```text
[사용자 로컬 작업 폴더]\hwpx_template_intake\
```

금지:

- 저장소 내부에 실제 원본 복사
- 저장소 내부에 실제 기관명 또는 실제 문서명이 들어간 폴더 생성
- GitHub Desktop Changes에 실제 원본 표시

### 2. 파일명

파일명에는 실제 기관명, 실제 부서명, 실제 문서명, 실제 문서번호를 쓰지 않습니다.

권장:

```text
source_original_do_not_commit.hwpx
working_copy_deidentified.hwpx
placeholder_candidate_[document_type].hwpx
```

금지:

```text
[실제 기관명]_[실제 문서명].hwpx
[실제 부서명]_[실제 양식명].hwpx
[실제 문서번호].hwpx
```

### 3. 등급 판단

저장소 밖 작업 전 A/B/C/D 등급을 먼저 판단합니다.

| 등급 | Phase 3 처리 |
|---|---|
| A | 공개 가능 자료만 참고 가능 |
| B | 비식별 처리 후 placeholder 후보로 검토 가능 |
| C | 내부 참고만 가능, placeholder 후보 제외 |
| D | 외부 처리 금지, 즉시 중단 |

애매한 경우 더 보수적으로 분류합니다.

### 4. 식별 요소 제거

placeholder 후보로 검토하기 전에 다음 요소를 제거합니다.

- 실제 본문 원문
- 실제 기관명, 관서명, 부서명, 업체명
- 실제 개인명, 담당자명, 연락처, 이메일
- 실제 문서번호, 시행일자, 접수번호, 사건번호, 민원번호
- 실제 결재선, 직인, 로고
- 실제 예산액, 실적 수치, 장비명, 차량번호, 내부 운영정보
- 문서 속성, 미리보기, 마지막 저장자 정보의 실제값

확인이 어려우면 저장소 안으로 옮기지 않고 로컬 참고로만 둡니다.

### 5. placeholder 변환

동적 값은 중립적 placeholder로 바꿉니다.

권장:

- `{{title}}`
- `{{background}}`
- `{{main_points}}`
- `{{review_opinion}}`
- `{{next_steps}}`
- `{{missing_fields}}`

금지:

- 실제 기관명, 실제 부서명, 실제 업무명, 실제 사건명을 암시하는 placeholder
- 실제 금액, 일정, 담당자, 수량을 유추할 수 있는 placeholder
- 여러 줄 값이 한 문단에 과도하게 몰리는 placeholder 배치

## 저장소 반입 판단

기본값은 저장소 반입 금지입니다.

로컬 검증이 필요한 경우에만 `templates/hwpx/placeholder_[document_type].hwpx` 후보로 둘 수 있습니다.

조건:

- 실제 정보 제거 완료
- placeholder 이름 중립성 확인
- `.hwpx` Git 제외 상태 확인
- GitHub Desktop Changes에 `.hwpx`가 보이지 않음
- 실제 원본 파일명 또는 실제 양식명을 README, docs, checklist에 기록하지 않음

중단 기준:

- `templates/hwpx/*.hwpx`가 Changes에 보임
- `templates/hwpx/*.hwp`가 Changes에 보임
- 실제 원본 또는 output 파일이 Changes에 보임
- `__pycache__`, 잠금 파일, 임시 파일이 tracked 변경으로 보임

## 사용자 수동 preview 기준

[사용자 확인 필요]

사용자는 HWPX output을 한컴에서 열고 다음을 확인합니다.

| 확인 | 항목 | 기준 |
|---|---|---|
| [ ] | 파일 열림 | 한컴에서 정상 열림 |
| [ ] | 글자 겹침 | 제목, 번호, 본문, 표 영역에서 겹침 없음 |
| [ ] | 항목 순서 | 문서 유형별 항목 순서 정상 |
| [ ] | 줄바꿈 | 여러 줄 본문이 문단 단위로 분리됨 |
| [ ] | 문단 배치 | 제목, 본문, 검토용 목록이 서로 겹치지 않음 |
| [ ] | bullet 표기 | 내용 앞 기호 표기 일관성 |
| [ ] | placeholder 잔여 | 남은 `{{placeholder}}` 없음 |
| [ ] | 확인 필요값 | `[확인 필요]`가 실제값처럼 보이지 않음 |
| [ ] | missing_fields | 본문 실제값이 아니라 검토용 목록으로 보임 |
| [ ] | 민감정보 | 실제 개인정보, 기관정보, 문서번호 없음 |

## 문서 유형별 preview 중점

| 문서 유형 | 중점 확인 |
|---|---|
| `one_page_report` | 제목, 보고 개요, 주요 내용, 검토 의견 배치 |
| `project_plan` | 추진개요, 세부계획, 일정, 예산의 `[확인 필요]` 처리 |
| `result_report` | 계획 대비 결과, 실적, 예산 집행 정보의 placeholder 유지 |
| `review_report` | 보안 검토 전 렌더링 금지, 승인된 placeholder 검토보고서만 확인 |

## 상태별 중단 기준

| 상태 | Phase 3 처리 |
|---|---|
| `template_required` | 로컬 템플릿 준비 전 안전 중단, output 생성 시도하지 않음 |
| `needs_security_review` | 사람 보안 검토 전 HWPX 렌더링 중단 |
| `blocked` | 처리 중단, 실제값 제거 요청 |
| validation 실패 | 렌더링 중단, payload 또는 placeholder map 확인 |
| `remaining_placeholders` 있음 | preview 중단, placeholder map 또는 템플릿 오탈자 확인 |
| output 잠금 | 한컴에서 파일 닫은 뒤 재시도 |
| Git Changes에 HWPX 표시 | 작업 중단, `.gitignore`와 파일 위치 확인 |

## 이상 발생 기록 기준

이상 발생 시 실제 원문이나 실제 파일명을 기록하지 않습니다.

기록 가능한 정보:

- placeholder 기반 output 파일명
- 문서 유형
- 항목 번호
- 증상
- 처리 상태

예시:

```text
mapped_missing_result_report_poc.hwpx / 5번 / 내용 앞 기호 불일치 / 보류
```

금지:

- 실제 원본 파일명
- 실제 기관명
- 실제 문서번호
- 실제 본문 내용
- 실제 담당자명
- 실제 내부 경로

## GitHub Desktop Changes 확인

[사용자 확인 필요]

보이면 안 되는 항목:

- `templates/hwpx/*.hwpx`
- `templates/hwpx/*.hwp`
- `renderers/hwpx_renderer/output/*`
- `normalizers/output/*`
- 실제 기관 양식 원본
- 실제 공문 또는 보고서 원문
- 잠금 파일 또는 임시 파일

보여도 되는 항목:

- `docs/*.md`
- `checklists/*.md`
- `README.md`
- `AGENTS.md`
- `tasks/NEXT_STEP.md`
- 명시적으로 수정한 PoC 코드
- placeholder 기반 fixture

## 후속 반영 상태

이번 문서에서 저장소 밖 HWPX 취급과 사용자 수동 preview 기준을 Phase 3 기준으로 구체화했습니다.

후속 반영 상태:

1. 상태별 중단 기준은 `docs/113`에서 반복 운영 문서에 반영 완료
2. Phase 3 preview 기준은 `docs/101`의 반복 운영 로그 템플릿과 연결 완료
3. Phase 3 운영 문서 묶음 통합 점검은 `docs/114`에 반영 완료
4. 외부 연동 필요성과 보류 기준은 `docs/115`에 반영 완료
5. 로그와 감사 추적 기준은 `docs/116`에 반영 완료
6. 테스트 계정과 테스트 데이터 기준은 `docs/117`에 반영 완료
7. 실제 원문 차단과 비식별 입력 확인 절차는 `docs/118`에 반영 완료

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX 원본 파일 추가 없음
- Email, API, Make.com 연동 없음

## 결론

Phase 3에서는 실제 원본과 output을 Git에 남기지 않고, 저장소 밖 HWPX 취급과 사용자 수동 preview를 분리해 관리합니다.

다음 단계는 실제 연동 구현이 아니라, 사용자 preview와 사람 승인 지점을 외부 전송 전 절차로 통합 점검하는 것입니다.
