# Quick Start 리허설 경계

## 목적

`docs/143_user_quick_start.md` 기준으로 지금 문서만으로 확인 가능한 항목과 실제 HWPX 열람이 필요한 항목을 분리합니다.

이 문서는 실제 업무용 HWPX 파일 생성 지시가 아닙니다. 실제 원문, 개인정보, 기관명, 문서번호, 실제 표 데이터, 실제 HWPX/HWP 원본을 기록하지 않습니다.

## 지금 문서만으로 확인 가능

| 구분 | 확인 항목 | 기준 |
|---|---|---|
| 사용자 흐름 | 처음 열 파일 순서 | `CURRENT_STATUS.md` -> `docs/140_user_operation_atoz_guide.md` -> `checklists/user_operation_atoz_rehearsal_checklist.md` -> `docs/141_user_rehearsal_prompt_examples.md` |
| 역할 구분 | `[사용자 확인 필요]`, `[Codex 처리 가능]`, `[보류]` | 세 표시가 같은 의미로 유지됨 |
| 요청 예시 | 보고서 4종 비식별 예시 | 실제값 없이 placeholder 유지 |
| 보안 원칙 | 실제 원문, 개인정보, 기관정보, 문서번호 제외 | 문서 기준으로 확인 가능 |
| 표 데이터 | 실제 표 데이터 자동 작성 보류 | `[표 데이터 별도 확인 필요]` 또는 `해당 없음` 후보만 사용 |
| 외부 연동 | Email/API/Make.com 보류 | no-send 원칙 유지 |
| Git 제외 원칙 | output과 local template은 Git 제외 대상 | `.gitignore` 기준으로 확인 가능 |

## Codex가 확인할 수 있는 것

| 구분 | 확인 항목 | 방식 |
|---|---|---|
| 문서 정합성 | 진입점 문서와 사용자 안내 문서 연결 | 파일 내용 확인 |
| 민감정보 패턴 | 전화번호, 이메일 등 의심 패턴 | `rg` 검색 |
| Git 제외 | local template, output ignored 여부 | `git check-ignore`, `git status --ignored --short` |
| 코드 미변경 | renderer, normalizer, fixture 변경 여부 | `git status --short` |

## 사용자가 직접 확인해야 하는 것

아래 항목은 Codex가 대신 확정하지 않습니다.

| 구분 | 확인 항목 | 필요한 상황 |
|---|---|---|
| 실제 양식 적용 여부 | 기관 양식 후보를 사용할지 여부 | 사용자가 저장소 밖 비식별 작업 복사본을 준비할 때 |
| 한컴 열람 | 파일이 열리는지 | `docs/150_manual_preview_resume_gate.md` 조건 충족 후 |
| 글자 겹침 | 본문, 표, 번호체계의 겹침 여부 | 수동 preview 재개 게이트 충족 후 |
| 문단 배치 | 줄바꿈, 여백, 행 높이 | 수동 preview 재개 게이트 충족 후 |
| 표 틀 | 표 폭, 표 위치, 표 안 여백 | 표가 있는 HWPX 파일을 게이트 충족 후 열람할 때 |
| 기관 표준 서식값 | 글꼴, 자간, 줄간격, 문단 간격 | 실제 기관 기준 확인 시 |

## 현재 단계에서 하지 않는 것

- 실제 HWPX/HWP 원본 저장소 추가
- 실제 업무용 HWPX output 재생성
- 실제 Excel/한셀 파일 생성
- 실제 표 데이터, 수량, 금액, 대상 목록 작성
- 실제 이메일 발송
- API, Make.com, Gmail, Outlook 실제 연동
- 실제 발송, 결재, 계약, 예산 집행, 법률 판단 자동화

## 진행 판단

현재는 문서만으로 다음을 할 수 있습니다.

1. 사용자가 처음 열 문서 확인
2. 보고서 4종 비식별 요청 예시 확인
3. 실제값을 넣으면 안 되는 항목 확인
4. HWPX 열람이 필요한 지점과 아닌 지점 분리
5. GitHub Desktop Changes에서 HWPX 원본 또는 Git 추적 대상 output 파일이 보이면 중단해야 함을 확인

실제 HWPX 수동 preview는 사용자가 저장소 밖 비식별 작업 복사본을 준비하고, `docs/150_manual_preview_resume_gate.md` 조건을 충족한 뒤 한컴 열람 검수를 요청할 때 재개합니다.

## 완료 기준

- 문서만으로 가능한 리허설 항목이 분리됨
- HWPX 열람이 필요한 항목이 `[사용자 확인 필요]`로 남음
- Codex가 대신 확정할 수 없는 항목이 명확함
- 실제 개인정보, 기관정보, 문서번호, 표 데이터 요구 없음
- 실제 업무용 HWPX 파일 생성이나 외부 연동 없음
