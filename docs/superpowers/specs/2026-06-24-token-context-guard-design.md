# 공공문서 자동화 토큰 컨텍스트 가드 설계

작성일: 2026-06-24

## 1. 목적

이 설계의 목적은 공공문서 자동화 프로젝트에서 Codex가 매 작업마다 방대한 과거 문서와 체크리스트를 전부 다시 읽지 않고, 현재 기준 문서와 필요한 세부 문서만 단계적으로 읽도록 만드는 것이다.

이 프로젝트는 보안, 비식별, HWPX placeholder, 수동 preview 보류 조건이 중요하므로 토큰 절감보다 안전 원칙이 우선한다. 따라서 컨텍스트 가드는 문서를 덜 읽기 위한 장치이면서, 반드시 읽어야 하는 보안 진입점을 고정하는 장치다.

## 2. 현재 문제

공공문서 자동화 프로젝트는 문서와 체크리스트가 매우 많고, 과거 Phase 문서도 현재 기준과 함께 남아 있다. 최근 로그 기준으로 턴당 토큰 사용량이 높았는데, 이는 작업 시작 시 `docs/`, `checklists/`, `templates/`, `renderers/`를 넓게 훑는 경향과 관련이 있다.

주요 낭비 지점:

- `docs/` 전체 또는 `checklists/` 전체를 작업 시작 단계에서 훑음
- 과거 Phase 문서의 당시 판단과 최신 진입점 기준을 동시에 길게 읽음
- HWPX preview 보류 상태인데도 preview 관련 문서를 반복 확인함
- 실제 산출물이 아닌 ignored output 또는 로컬 HWPX 후보까지 탐색 대상에 섞일 위험이 있음

## 3. 목표

1. 기본 시작 문서를 최신 진입점 중심으로 제한한다.
2. 과거 Phase 문서는 현재 작업에 직접 연결될 때만 읽는다.
3. 체크리스트는 해당 작업의 완료 검증에 필요한 것만 연다.
4. HWPX, output, 실제 원본 후보는 기존 보안 규칙에 따라 기본 탐색에서 제외한다.
5. 토큰 절감 때문에 보안ㆍ비식별ㆍ수동 승인 기준을 놓치지 않도록 필수 진입점을 고정한다.

## 4. 비목표

- 과거 문서나 체크리스트를 삭제하지 않는다.
- HWPX 수동 preview 보류 기준을 완화하지 않는다.
- 실제 HWPX 원본, 실제 공문 원문, 개인정보 처리 범위를 넓히지 않는다.
- 기존 renderer, normalizer, fixture 동작을 이 설계 단계에서 변경하지 않는다.
- 외부 HWPX 도구를 운영 의존성으로 도입하지 않는다.

## 5. 권장 산출물

### 5.1 `docs/token_context_map.md`

현재 작업자가 먼저 읽을 토큰 절감 지도다.

포함 내용:

- 기본 진입 문서
- 작업 유형별 추가 문서
- 기본 탐색 제외 경로
- 필수 보안 확인 경로
- 과소 탐색 방지 조건
- HWPX preview 또는 실제 원본 관련 중단 조건

### 5.2 `context_guard.json`

스크립트가 읽을 수 있는 구조화된 설정이다.

권장 필드:

```json
{
  "project": "public-document-automation",
  "default_entry_files": [
    "README.md",
    "AGENTS.md",
    "CURRENT_STATUS.md",
    "tasks/NEXT_STEP.md",
    "docs/token_context_map.md"
  ],
  "default_exclude_globs": [
    "renderers/**/output/**",
    "normalizers/output/**",
    "templates/**/*.hwpx",
    "**/*.hwp",
    "**/*.hwpx",
    "**/__pycache__/**",
    "**/*.pyc"
  ],
  "always_confirm_before": [
    "real HWPX preview",
    "opening source documents",
    "using real institution forms",
    "deleting files or folders",
    "external integration"
  ]
}
```

### 5.3 `scripts/show_context_guard.ps1`

작업 유형별 추천 읽기 목록과 제외 경로를 출력하는 스크립트다.

동작 원칙:

- 파일 내용을 통째로 출력하지 않는다.
- 기본 진입 문서와 작업별 추가 문서만 보여준다.
- HWPX/output/실제 원본 후보는 기본 목록에서 제외한다.
- 보안상 사용자 확인이 필요한 조건을 함께 출력한다.
- 없는 경로는 경고로 표시한다.

예상 사용:

```powershell
.\scripts\show_context_guard.ps1 -TaskType docs
.\scripts\show_context_guard.ps1 -TaskType hwpx-policy
.\scripts\show_context_guard.ps1 -TaskType normalizer
.\scripts\show_context_guard.ps1 -TaskType review
```

## 6. 작업 유형별 컨텍스트 정책

### 6.1 일반 문서 정합성 보강

처음 읽기:

- `README.md`
- `AGENTS.md`
- `CURRENT_STATUS.md`
- `tasks/NEXT_STEP.md`
- `docs/token_context_map.md`
- 사용자가 직접 언급한 문서

기본 제외:

- `docs/` 전체 훑기
- `checklists/` 전체 훑기
- output 폴더
- HWP/HWPX 파일

확장 조건:

- 최신 진입점과 과거 문서가 충돌할 때
- README 링크 또는 CURRENT_STATUS 진행률을 바꿀 때
- 새 문서 생성 여부를 판단해야 할 때

### 6.2 HWPX 정책ㆍpreview 관련 작업

처음 읽기:

- `AGENTS.md`
- `tasks/NEXT_STEP.md`
- `docs/150_manual_preview_resume_gate.md`
- `checklists/manual_preview_resume_gate_checklist.md`
- 관련 HWPX 정책 문서 1~3개

기본 제외:

- 실제 HWPX 열람
- 저장소 밖 실제 양식 접근
- output HWPX 전문 확인

중단 조건:

- 사용자가 비식별 작업 복사본 준비를 명시하지 않았는데 실제 preview를 해야 하는 경우
- 실제 원본, 개인정보, 내부자료 가능성이 있는 파일을 열어야 하는 경우

### 6.3 normalizer 또는 renderer PoC 점검

처음 읽기:

- `AGENTS.md`
- 관련 `normalizers/` 또는 `renderers/` 파일
- 해당 테스트 파일
- 해당 README

확장 조건:

- placeholder 정책 변경
- output 보관 정책 변경
- 실제 업무용 산출물처럼 보일 위험

### 6.4 보안 검토

처음 읽기:

- `AGENTS.md`
- `docs/02_security_policy.md`
- `docs/03_deidentification_rules.md`
- 사용자가 언급한 문서

확장 조건:

- 실제값 의심 패턴 발견
- Custom GPT Knowledge, 외부 AI 입력, 실제 원문 처리 관련 문구 변경
- HWPX 원본 또는 output 처리 기준 변경

## 7. 추후 작업 리스크 점검

### 7.1 최신 기준을 놓칠 위험

완화:

- 기본 진입 세트에 `README.md`, `AGENTS.md`, `CURRENT_STATUS.md`, `tasks/NEXT_STEP.md`를 반드시 포함한다.
- 과거 Phase 문서는 최신 진입점과 충돌할 때만 읽고, 충돌 시 최신 진입점 우선 원칙을 따른다.

### 7.2 보안 기준을 과소 탐색할 위험

완화:

- 보안 관련 작업은 항상 `AGENTS.md`를 먼저 읽는다.
- 실제 원본, 개인정보, 외부 연동, HWPX preview 가능성이 보이면 토큰 절감 규칙보다 사용자 확인 절차를 우선한다.
- HWP/HWPX 파일은 기본 제외하고, 열람 필요 시 중단 조건을 출력한다.

### 7.3 문서 정합성 문제를 못 찾을 위험

완화:

- README, CURRENT_STATUS, NEXT_STEP을 동시에 기본 세트로 둔다.
- 새 문서 또는 새 체크리스트가 생기면 README 링크와 NEXT_STEP 정합성을 완료 조건으로 둔다.
- 전체 `docs/` 스캔 대신 파일명 검색과 직접 관련 문서만 확장한다.

### 7.4 PoC 코드 변경 누락 위험

완화:

- normalizer, renderer 작업은 관련 소스와 테스트를 항상 같이 읽는다.
- output 정책이나 placeholder 정책을 건드리면 AGENTS와 관련 policy 문서를 추가로 읽는다.
- 테스트 실패가 있으면 컨텍스트 가드보다 실패 추적을 우선한다.

### 7.5 컨텍스트 가드가 오래되어 잘못 안내할 위험

완화:

- `docs/token_context_map.md`에 마지막 검토일을 둔다.
- `context_guard.json`의 경로 존재 여부를 스크립트가 경고한다.
- 새 진입점 문서가 생기면 context map 업데이트를 완료 조건에 넣는다.

## 8. 성공 기준

- 일반 문서 작업 시작 시 기본 읽기 파일이 5~8개 수준으로 줄어든다.
- `docs/`와 `checklists/` 전체를 처음부터 훑지 않는다.
- 보안 작업에서는 AGENTS와 보안 문서를 반드시 포함한다.
- HWPX preview, 실제 원본, 개인정보, 외부 연동 가능성이 있으면 토큰 절감보다 중단 조건이 먼저 작동한다.
- 최신 진입점과 과거 문서의 역할이 분리되어, 오래된 다음 단계 문구에 끌려가지 않는다.

## 9. 구현 계획 방향

이 설계가 승인되면 다음 순서로 구현한다.

1. `docs/token_context_map.md` 작성
2. `context_guard.json` 작성
3. `scripts/show_context_guard.ps1` 작성
4. `README.md`, `AGENTS.md`, `tasks/NEXT_STEP.md` 중 필요한 진입점에 토큰 가드 연결
5. 경로 존재 여부와 제외 규칙을 검증
6. HWPX/output/실제 원본 후보가 기본 추천 목록에 들어가지 않는지 확인
