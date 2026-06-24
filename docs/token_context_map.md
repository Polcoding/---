# 공공문서 자동화 토큰 컨텍스트 지도

마지막 검토일: 2026-06-24

## 목적

이 문서는 공공문서 자동화 프로젝트에서 Codex가 작업을 시작할 때 최신 기준 문서부터 작게 읽고, 필요한 경우에만 과거 문서와 체크리스트로 범위를 넓히기 위한 안내입니다.

토큰 절감보다 보안, 비식별, HWPX 수동 preview 보류, 사람 승인 기준이 우선입니다.

## 기본 시작 세트

항상 먼저 확인합니다.

1. `README.md`
2. `AGENTS.md`
3. `CURRENT_STATUS.md`
4. `tasks/NEXT_STEP.md`
5. `docs/token_context_map.md`

사용자가 특정 문서를 언급하면 위 기본 세트 다음에 그 문서를 읽습니다.

## 기본 탐색 제외

처음부터 전체 탐색하지 않습니다.

- `docs/**` 전체
- `checklists/**` 전체
- `renderers/**/output/**`
- `normalizers/output/**`
- `templates/**/*.hwp`
- `templates/**/*.hwpx`
- `**/*.hwp`
- `**/*.hwpx`
- `**/__pycache__/**`
- `**/*.pyc`

## 사용자 확인 전 중단 조건

아래 조건은 토큰 절감과 무관하게 사용자 확인을 먼저 받습니다.

- 실제 HWPX preview 또는 한컴 수동 열람
- 실제 원본, 실제 공문, 실제 기관 양식, 실제 내부자료 가능성이 있는 파일 열람
- 개인정보, 민감정보, 내부 운영정보 가능성이 있는 파일 처리
- 파일 또는 폴더 삭제
- 외부 연동, 이메일 발송, Make.com, 운영 API 연결
- 실제 업무용 HWPX/XLSX output 생성

## 작업 유형별 읽기 기준

### 일반 문서 정합성 보강

처음 읽기:

- 기본 시작 세트
- 사용자가 언급한 문서
- 변경하려는 문서와 직접 연결된 README 링크 또는 NEXT_STEP 문단

확장 조건:

- 최신 진입점과 과거 Phase 문서가 충돌함
- README 링크 또는 CURRENT_STATUS 진행률을 바꿈
- 새 문서 생성 여부를 판단해야 함

### HWPX 정책 또는 preview 기준

처음 읽기:

- `AGENTS.md`
- `tasks/NEXT_STEP.md`
- `docs/150_manual_preview_resume_gate.md`
- `checklists/manual_preview_resume_gate_checklist.md`
- 사용자가 언급한 HWPX 정책 문서

확장 조건:

- HWPX 수동 preview 재개 조건 변경
- local template Git 제외 정책 변경
- placeholder 또는 style profile 정책 변경

중단 조건:

- 비식별 작업 복사본 준비가 명시되지 않았는데 실제 preview가 필요함
- 실제 원본 또는 개인정보 가능성이 있는 파일을 열어야 함

### normalizer 또는 renderer PoC 점검

처음 읽기:

- `AGENTS.md`
- 관련 `normalizers/` 또는 `renderers/` 파일
- 해당 테스트 파일
- 해당 README

확장 조건:

- placeholder 정책 변경
- output 보관 정책 변경
- 실제 업무용 산출물처럼 보일 위험

### 보안 검토

처음 읽기:

- `AGENTS.md`
- `docs/02_security_policy.md`
- `docs/03_deidentification_rules.md`
- 사용자가 언급한 문서

확장 조건:

- 실제값 의심 패턴 발견
- Custom GPT Knowledge, 외부 AI 입력, 실제 원문 처리 문구 변경
- HWPX 원본 또는 output 처리 기준 변경

### 리뷰

처음 읽기:

- `git diff --stat`
- `git diff --name-only`
- 변경 파일
- 변경 파일과 직접 연결된 체크리스트 또는 테스트

확장 조건:

- 보안, HWPX hold, 실제 원본 처리, output 정책 관련 변경
- README, AGENTS, CURRENT_STATUS, NEXT_STEP 사이에 충돌 가능성
- 테스트나 체크리스트 없이 판단해야 하는 변경

## 완료 전 확인

- 새 문서가 생겼으면 README 링크 필요 여부를 확인합니다.
- 새 체크리스트가 생겼으면 해당 문서와 연결되어 있는지 확인합니다.
- HWP/HWPX 또는 output 파일이 기본 진입 파일에 들어가지 않았는지 확인합니다.
- 실제값 의심 패턴이 생기지 않았는지 확인합니다.
- `tasks/NEXT_STEP.md`가 최신 작업 방향과 충돌하지 않는지 확인합니다.
