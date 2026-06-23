# 저장소 밖 실제 양식 후보 수동 절차와 보류 조건 재정렬

## 목적

이 문서는 저장소 밖에서 실제 HWPX 양식 후보를 다룰 때의 수동 절차와 보류 조건을 HWPX 보고서 4종 기준으로 재정렬합니다.

이번 단계는 실제 기관 HWPX 원본을 저장소에 넣거나 실제 HWPX output을 재생성하는 단계가 아닙니다. renderer, normalizer, fixture, routing, HWPX payload, output도 변경하지 않습니다.

## 확인 대상

- `docs/127_hwpx_manual_preview_gap_log_criteria.md`
- `checklists/hwpx_manual_preview_gap_log_checklist.md`
- `docs/53_real_hwpx_template_intake_safety_procedure.md`
- `docs/58_external_hwpx_placeholder_conversion_runbook.md`
- `docs/112_phase3_external_hwpx_and_manual_preview_criteria.md`
- `templates/hwpx/local_template_policy.md`
- `templates/hwpx/README.md`
- `checklists/real_hwpx_template_intake_checklist.md`
- `checklists/external_hwpx_placeholder_conversion_checklist.md`
- `checklists/hwpx_rendered_output_manual_review_checklist.md`
- `README.md`
- `AGENTS.md`
- `tasks/NEXT_STEP.md`

## 점검 결론

현재 저장소 기준으로 실제 기관 HWPX 원본, 로컬 placeholder HWPX 템플릿, output 산출물, 수동 preview gap log를 분리해서 다루는 방향은 서로 충돌하지 않습니다.

다만 실제 양식 후보를 다루기 전 단계에서 다음 구분을 더 분명히 유지해야 합니다.

| 구분 | 위치 | Git 포함 여부 | 처리 원칙 |
|---|---|---|---|
| 실제 원본 | 저장소 밖 로컬 위치 | 금지 | 직접 수정하지 않고 외부 AI 입력 금지 |
| 비식별 작업 복사본 | 저장소 밖 로컬 위치 | 금지 | 실제 내용과 식별 요소 제거 후에도 Git 추가 금지 |
| placeholder 후보 | `templates/hwpx/` 로컬 파일 | 기본 제외 | `.hwpx`, `.hwp`는 GitHub Desktop Changes에 보이면 중단 |
| 렌더링 output | renderer 또는 normalizer output | 제외 | 실제 업무용 산출물 아님 |
| gap log | `docs/`, `checklists/` | 가능 | 실제 원문, 실제 파일명, 실제 기관정보 없이 증상만 기록 |

## 용어 구분

### 실제 원본

실무에서 쓰는 실제 HWP/HWPX 양식 또는 실제 내용이 들어 있는 파일입니다.

- 저장소에 넣지 않습니다.
- 외부 AI, Custom GPT Knowledge, API 입력으로 사용하지 않습니다.
- 파일명, 내부 경로, 문서 속성도 저장소 문서에 기록하지 않습니다.

### 비식별 작업 복사본

실제 원본을 직접 수정하지 않기 위해 저장소 밖에서 만든 작업용 복사본입니다.

- 실제 본문, 실제 기관명, 문서번호, 결재선, 직인, 로고, 담당자 정보 제거 전에는 placeholder 후보가 아닙니다.
- 식별 요소를 제거했더라도 기본적으로 Git에 추가하지 않습니다.
- C/D등급 또는 판단 애매 자료가 섞이면 즉시 보류합니다.

### placeholder 후보

동적 값을 `{{title}}`, `{{background}}` 같은 중립 placeholder로 바꾼 로컬 검증 후보입니다.

- `templates/hwpx/placeholder_[document_type].hwpx` 형태로 로컬에 둘 수 있습니다.
- `.hwpx`, `.hwp` 파일은 Git 제외 상태를 유지합니다.
- GitHub Desktop Changes에 보이면 작업을 중단합니다.

### gap log

한컴 수동 preview에서 확인한 배치, 줄바꿈, 기호, 겹침 등의 차이를 기록하는 문서 기준입니다.

- 실제 원문이나 실제 파일명을 기록하지 않습니다.
- 문서유형, 항목 번호, 증상, 심각도, 후속 조치만 기록합니다.
- 심각도 `차단`이 하나라도 있으면 실제 업무 적용 후보가 아닙니다.

## 수동 절차

### 1. 작업 필요성 판단

- 실제 양식이 꼭 필요한지 먼저 확인합니다.
- placeholder-only 샘플이나 기존 로컬 템플릿으로 확인 가능한 작업이면 실제 원본을 열지 않습니다.
- API, Make.com, Email 자동화 구현 필요성으로 확대하지 않습니다.

### 2. 보안등급 분류

- A/B/C/D 등급을 먼저 판단합니다.
- A/B등급만 비식별 후보로 검토합니다.
- C등급은 내부 참고만 가능하며 placeholder 후보에서 제외합니다.
- D등급은 외부 처리 금지이며 즉시 중단합니다.
- 애매하면 더 보수적으로 분류합니다.

### 3. 저장소 밖 작업 위치 확인

- 실제 원본과 작업 복사본은 저장소 밖 로컬 위치에서만 다룹니다.
- 작업 폴더명과 파일명에 실제 기관명, 실제 문서명, 실제 문서번호를 쓰지 않습니다.
- 저장소 내부에 실제 원본, 비식별 작업 복사본, 실제 output을 만들지 않습니다.

### 4. 작업 복사본 생성

- 실제 원본은 직접 수정하지 않습니다.
- 저장소 밖에서 작업 복사본을 만듭니다.
- 작업 복사본도 Git 추적 대상이 되지 않는 위치에 둡니다.

### 5. 식별 요소 제거

다음 요소를 제거하거나 중립 placeholder로 대체하기 전에는 placeholder 후보로 보지 않습니다.

- 실제 본문 원문
- 실제 기관명, 관서명, 부서명, 업체명
- 실제 개인명, 담당자명, 연락처, 이메일
- 실제 문서번호, 시행일자, 접수번호, 사건번호, 민원번호
- 실제 결재선, 직인, 로고
- 실제 예산액, 실적 수치, 장비명, 차량번호, 내부 운영정보
- 문서 속성, 미리보기, 마지막 저장자 정보의 실제값

확인이 어려우면 저장소 안으로 옮기지 않고 보류합니다.

표 안에 실제 물품명, 수량, 금액, 대상 목록이 많은 경우에도 모든 셀을 길게 placeholder화할 필요는 없습니다. 현재 단계에서는 보안 노출을 막을 정도로 삭제, 공란, 짧은 중립 표기만 사용하고, 표 틀 preview가 가능하면 충분합니다.

### 6. placeholder 후보 전환

- 동적 값은 중립 placeholder로 바꿉니다.
- placeholder 이름으로 실제 기관, 실제 부서, 실제 업무명, 실제 사건을 추정할 수 없어야 합니다.
- 여러 줄 값이 들어갈 placeholder는 가능한 한 서로 다른 문단에 둡니다.
- 예산, 일정, 실적, 담당자, 수량은 임의 생성하지 않고 `[확인 필요]`, `null`, 또는 안전한 빈 문자열로 둡니다.
- 복잡한 표 내부 데이터는 HWPX renderer 대상이 아니라 향후 Excel/한셀 연동 후보로 분리합니다.
- 표 검수는 표 위치, 폭, 줄바꿈, 겹침, 여백 같은 `table_scope: frame_only` 기준으로만 수행합니다.

### 7. Git 제외 확인

다음 항목이 GitHub Desktop Changes에 보이면 즉시 중단합니다.

- 실제 원본 HWP/HWPX 파일
- 저장소 밖 작업 복사본
- `templates/hwpx/*.hwpx`
- `templates/hwpx/*.hwp`
- `renderers/hwpx_renderer/output/*`
- `normalizers/output/*`
- 잠금 파일, 임시 파일, `__pycache__`

Git에 남길 수 있는 것은 문서, 체크리스트, placeholder 기반 샘플, 승인된 PoC 코드뿐입니다.

### 8. 로컬 preview와 gap log 연결

- placeholder 후보는 사용자가 한컴에서 직접 preview합니다.
- 글자 겹침, 줄바꿈, 번호 들여쓰기, 기호 표기, 표 폭, 여백, placeholder 잔여를 확인합니다.
- gap은 `docs/127_hwpx_manual_preview_gap_log_criteria.md` 기준으로 기록합니다.
- 실제 원문, 실제 파일명, 실제 기관명, 실제 문서번호는 gap log에 기록하지 않습니다.

### 9. 보류 또는 다음 단계 판단

- 보류 조건이 없고 Git 제외 상태가 확인된 경우에만 다음 수동 검토로 넘어갑니다.
- 심각도 `차단` 또는 보안 의심이 있으면 실제 업무 적용 후보에서 제외합니다.
- 코드 변경, output 재생성, 외부 연동은 별도 명시 승인 전까지 진행하지 않습니다.

## HWPX 보고서 4종별 중점

| 문서 유형 | 수동 절차 중점 |
|---|---|
| `one_page_report` | 제목, 보고 개요, 주요 내용, 검토 의견이 서로 다른 문단에서 읽히는지 확인 |
| `project_plan` | 추진개요, 세부계획, 일정, 예산의 `[확인 필요]` 값이 실제값처럼 보이지 않는지 확인 |
| `result_report` | 계획 대비 결과, 실적, 예산 집행 정보가 임의 생성되지 않았는지 확인 |
| `review_report` | 보안 검토 조건과 사람 승인 전제, 위험요소와 후속조치 구분 유지 |

## 보류 조건

다음 중 하나라도 있으면 다음 단계로 진행하지 않습니다.

| 보류 조건 | 처리 |
|---|---|
| 실제 원본 또는 작업 복사본이 저장소 안에 있음 | 즉시 중단, 파일 위치 재검토 |
| GitHub Desktop Changes에 HWP/HWPX/output 파일이 보임 | 즉시 중단, `.gitignore`와 위치 확인 |
| C/D등급 또는 판단 애매 자료가 섞임 | 보류, 더 보수적 등급 적용 |
| 실제 개인정보, 문서번호, 기관정보, 내부 운영정보 의심 | 보안 검토 전 중단 |
| 직인, 로고, 결재선 등 식별 요소가 남음 | placeholder 후보 전환 불가 |
| 문서 속성이나 미리보기에 실제값이 남음 | 저장소 반입 금지 |
| placeholder 이름이 실제 대상을 암시함 | placeholder 이름 수정 전 보류 |
| `remaining_placeholders`가 남음 | preview 중단, map 또는 템플릿 확인 |
| gap log 심각도 `차단` 발생 | 실제 업무 적용 후보 제외 |
| style profile 값이 확인되지 않았는데 확정값처럼 기록됨 | `[확인 필요]`로 되돌림 |

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
- 실제 파일명, 내부 경로, 원본 양식명 추가 없음
- 폰트 파일 추가 없음
- API 키, 토큰, 인증정보 예시값 추가 없음
- Email, API, Make.com 연동 구현 없음

## 결론

저장소 밖 실제 양식 후보는 실제 원본, 비식별 작업 복사본, placeholder 후보, gap log를 분리해서 관리합니다.

local template policy와 Git 제외 상태 반복 검증 기준은 `docs/129_local_template_gitignore_repeat_verification_criteria.md`에 반영했습니다.

Phase 4 문서 템플릿 안정화 통합 점검은 `docs/130_phase4_template_stabilization_integrated_review.md`에 반영했습니다.

실제 양식 수동 리허설 사용자 확인 패킷과 gap log 빈 양식은 `docs/131_actual_hwpx_manual_rehearsal_user_confirmation_packet.md`에 반영했습니다.

다음 단계는 비식별 작업 복사본 준비가 명시되기 전까지 문서 기반 검증 상태를 유지하는 것입니다. 저장소 밖 한컴 preview 결과의 실제값 없는 gap log 기록은 `docs/150_manual_preview_resume_gate.md` 조건을 만족할 때만 재개하며, 실제 기관 HWPX 원본 투입, HWPX output 재생성, renderer 코드 변경, 외부 연동 구현은 계속 보류합니다.
