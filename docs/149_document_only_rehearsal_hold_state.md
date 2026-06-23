# 문서 기반 리허설 Hold 상태

## 목적

비식별 작업 복사본이 준비되기 전까지 실제 HWPX 수동 preview를 보류하고, 문서 기반 리허설 상태를 유지한다는 현재 기준을 기록합니다.

이 문서는 실제 HWPX 파일 생성, 실제 HWPX 열람, 실제 업무값 입력을 요구하지 않습니다.

## 현재 상태

현재 상태는 단순 중단이 아니라 문서 기반 리허설 유지 상태입니다.

| 구분 | 상태 | 기준 |
|---|---|---|
| 실제 HWPX 수동 preview | 보류 | 비식별 작업 복사본 준비 전 |
| 문서 기반 사용자 리허설 | 유지 | quick start와 체크리스트 기준 가능 |
| 비식별 요청 예시 확인 | 가능 | 보고서 4종 placeholder 예시 유지 |
| Git 제외 확인 | 유지 | local template, output, normalizers output 제외 |
| 외부 연동 | 보류 | no-send 원칙 유지 |

## hold 유지 조건

아래 조건 중 하나라도 해당하면 hold 상태를 유지합니다.

- 비식별 작업 복사본 준비 여부가 확인되지 않음
- 실제 HWPX/HWP 원본이 저장소 안에 들어올 위험이 있음
- 실제 원문, 개인정보, 기관명, 문서번호가 포함될 가능성이 있음
- 사용자가 한컴 열람 검수를 진행할 수 없는 상태임
- 표 내부 실제 데이터 자동화 요구가 섞임
- Email/API/Make.com 등 외부 연동 요구가 섞임

## hold 중 가능한 작업

- `docs/143_user_quick_start.md` 기준으로 처음 볼 순서 확인
- `checklists/user_operation_atoz_rehearsal_checklist.md` 기준으로 문서 기반 리허설
- `docs/141_user_rehearsal_prompt_examples.md` 기준으로 비식별 요청 예시 확인
- `docs/144_quick_start_rehearsal_boundary.md` 기준으로 문서만 가능한 확인과 HWPX 열람 필요 지점 분리
- `git check-ignore`와 `git status --ignored --short`로 local template과 output 제외 상태 확인

## hold 중 하지 않는 작업

- 실제 HWPX/HWP 원본 저장소 추가
- 실제 HWPX output 재생성
- 실제 Excel/한셀 파일 생성
- 실제 표 데이터, 수량, 금액, 대상 목록 작성
- 실제 이메일 발송
- API, Make.com, Gmail, Outlook 실제 연동
- 실제 발송, 결재, 계약, 예산 집행, 법률 판단 자동화

## hold 해제 조건

hold를 해제하고 수동 preview 준비로 넘어가려면 아래 조건이 모두 필요합니다.

1. 사용자가 저장소 밖 비식별 작업 복사본을 준비했다고 명시
2. 실제 원문, 개인정보, 기관명, 문서번호, 실제 표 데이터 제거 확인
3. GitHub Desktop Changes에 실제 HWPX 원본과 output이 보이지 않음
4. 사용자가 한컴에서 파일 열람 검수를 진행할 수 있음
5. 검수 범위가 표 내부 실제값이 아니라 글자 겹침, 줄바꿈, 표 폭, 여백임

## 다음 추천

hold 상태에서는 실제 HWPX 수동 preview를 재촉하지 않습니다.

다음 추천은 문서 기반 hold 상태를 push 가능한 단위로 확정하는 것입니다.

사용자가 이후 비식별 작업 복사본 준비를 명시하면, 그때 수동 preview 준비 문서로 전환합니다.

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 표 데이터, 물품명, 수량, 금액, 대상 목록 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX/HWP 원본 파일 추가 없음
- Email, API, Make.com 연동 없음
