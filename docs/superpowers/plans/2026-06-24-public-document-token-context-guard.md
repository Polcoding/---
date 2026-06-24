# Public Document Token Context Guard Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a lightweight context guard that keeps future public-document automation work focused on current entry documents while preserving security, HWPX hold, and human-approval rules.

**Architecture:** The implementation is documentation-first and non-blocking. `docs/token_context_map.md` defines what to read first and when to expand, `context_guard.json` stores the policy in structured form, and `scripts/show_context_guard.ps1` prints recommended entry files, exclusions, user-confirmation stops, and expansion triggers without opening HWPX or output files.

**Tech Stack:** Markdown, JSON, PowerShell 5+ built-ins, Git.

## Global Constraints

- Safety rules outrank token savings.
- Always treat `README.md`, `AGENTS.md`, `CURRENT_STATUS.md`, and `tasks/NEXT_STEP.md` as the current entry set.
- Do not delete old phase documents or checklists.
- Do not weaken HWPX manual preview hold criteria.
- Do not open real HWP, HWPX, source documents, or institution forms without explicit user confirmation.
- Do not add actual public-document originals, personal data, internal data, real institution forms, or real output HWPX files.
- Do not introduce external integration, email sending, Make.com, or operational API code.
- Missing paths must produce warnings, not script failures.

---

## File Structure

Create or modify these files:

```text
README.md
AGENTS.md
context_guard.json
docs/token_context_map.md
scripts/show_context_guard.ps1
tasks/NEXT_STEP.md
```

Responsibilities:

- `README.md`: Public entry point; points workers to the context guard before broad document scans.
- `AGENTS.md`: Codex operating rules; adds context guard as a mandatory start step without weakening existing security rules.
- `tasks/NEXT_STEP.md`: Current handoff; records that token guard implementation is the next approved work.
- `docs/token_context_map.md`: Human-readable current-context policy.
- `context_guard.json`: Machine-readable entry files, excludes, confirmation stops, and task profiles.
- `scripts/show_context_guard.ps1`: Prints the context policy without reading file bodies or HWPX/output files.

## Task 1: Add Public-Document Context Map and Guard Config

**Files:**
- Create: `docs/token_context_map.md`
- Create: `context_guard.json`

**Interfaces:**
- Produces: `docs/token_context_map.md`, the human-readable policy for current entry files, expansion rules, and stop conditions.
- Produces: `context_guard.json`, a JSON object with `project`, `last_reviewed`, `default_entry_files`, `default_exclude_globs`, `always_confirm_before`, `expand_when_global`, and `task_profiles`.

- [ ] **Step 1: Run the pre-check**

Run:

```powershell
Test-Path docs/token_context_map.md
Test-Path context_guard.json
```

Expected before this task is implemented:

```text
False
False
```

- [ ] **Step 2: Create `docs/token_context_map.md`**

Create `docs/token_context_map.md` with this content:

```markdown
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
```

- [ ] **Step 3: Create `context_guard.json`**

Create `context_guard.json` with this exact content:

```json
{
  "project": "public-document-automation",
  "last_reviewed": "2026-06-24",
  "default_entry_files": [
    "README.md",
    "AGENTS.md",
    "CURRENT_STATUS.md",
    "tasks/NEXT_STEP.md",
    "docs/token_context_map.md"
  ],
  "default_exclude_globs": [
    "docs/**",
    "checklists/**",
    "renderers/**/output/**",
    "normalizers/output/**",
    "templates/**/*.hwp",
    "templates/**/*.hwpx",
    "**/*.hwp",
    "**/*.hwpx",
    "**/__pycache__/**",
    "**/*.pyc"
  ],
  "always_confirm_before": [
    "real HWPX preview or Hancom manual viewing",
    "opening source documents",
    "using real institution forms",
    "processing possible personal or internal data",
    "deleting files or folders",
    "external integration",
    "email sending",
    "Make.com or operational API connection",
    "real work HWPX or XLSX output generation"
  ],
  "expand_when_global": [
    "current entry documents conflict with older phase documents",
    "security, de-identification, or original-document handling changes",
    "HWPX hold or manual preview criteria changes",
    "placeholder, output, or local template policy changes",
    "README, AGENTS, CURRENT_STATUS, or NEXT_STEP changes"
  ],
  "task_profiles": {
    "default": {
      "entry_files": [],
      "inspect_commands": [
        "git status --short",
        "git diff --stat"
      ],
      "expand_when": []
    },
    "docs": {
      "entry_files": [],
      "inspect_commands": [
        "git status --short",
        "git diff --stat",
        "rg -n \"현재|다음 단계|보류|수동 preview|HWPX\" README.md CURRENT_STATUS.md tasks/NEXT_STEP.md"
      ],
      "expand_when": [
        "README link changes",
        "CURRENT_STATUS progress wording changes",
        "new document or checklist is created"
      ]
    },
    "hwpx-policy": {
      "entry_files": [
        "docs/150_manual_preview_resume_gate.md",
        "checklists/manual_preview_resume_gate_checklist.md",
        "templates/hwpx/local_template_policy.md",
        "renderers/hwpx_renderer/README.md"
      ],
      "inspect_commands": [
        "rg -n \"수동 preview|재개 게이트|local template|output|Git 제외\" docs/150_manual_preview_resume_gate.md checklists/manual_preview_resume_gate_checklist.md templates/hwpx/local_template_policy.md renderers/hwpx_renderer/README.md"
      ],
      "expand_when": [
        "manual preview resume criteria changes",
        "local HWPX template policy changes",
        "placeholder or style profile policy changes"
      ]
    },
    "normalizer": {
      "entry_files": [
        "normalizers/README.md",
        "docs/109_normalizers_regression_recheck_result.md",
        "checklists/normalizers_regression_test_suite_checklist.md"
      ],
      "inspect_commands": [
        "rg --files normalizers | rg \"\\.py$|README\\.md$\""
      ],
      "expand_when": [
        "placeholder policy changes",
        "security filter behavior changes",
        "fixture schema changes"
      ]
    },
    "renderer": {
      "entry_files": [
        "renderers/README.md",
        "renderers/hwpx_renderer/README.md",
        "templates/hwpx/local_template_policy.md"
      ],
      "inspect_commands": [
        "rg --files renderers templates/hwpx | rg \"README\\.md$|\\.py$|\\.gitignore$\""
      ],
      "expand_when": [
        "output retention policy changes",
        "HWPX template handling changes",
        "actual work output risk appears"
      ]
    },
    "security": {
      "entry_files": [
        "docs/02_security_policy.md",
        "docs/03_deidentification_rules.md"
      ],
      "inspect_commands": [
        "rg -n \"개인정보|민감정보|원문|Knowledge|외부 AI|실제\" AGENTS.md docs/02_security_policy.md docs/03_deidentification_rules.md"
      ],
      "expand_when": [
        "real-value pattern appears",
        "Custom GPT Knowledge wording changes",
        "external AI input wording changes"
      ]
    },
    "review": {
      "entry_files": [],
      "inspect_commands": [
        "git diff --stat",
        "git diff --name-only"
      ],
      "expand_when": [
        "security or HWPX hold policy changes",
        "entry documents conflict",
        "changed file has no direct checklist or test"
      ]
    }
  }
}
```

- [ ] **Step 4: Verify JSON parses**

Run:

```powershell
$config = Get-Content -Raw -Encoding utf8 context_guard.json | ConvertFrom-Json
$config.project
$config.task_profiles.PSObject.Properties.Name -join ","
```

Expected output includes:

```text
public-document-automation
default,docs,hwpx-policy,normalizer,renderer,security,review
```

- [ ] **Step 5: Commit**

Run:

```powershell
git add docs/token_context_map.md context_guard.json
git commit -m "docs: add public document context guard map"
```

## Task 2: Add Context Guard Script

**Files:**
- Create: `scripts/show_context_guard.ps1`

**Interfaces:**
- Consumes: `context_guard.json`
- Produces: Console output listing task type, recommended entry files, missing path warnings, inspect commands, default exclusions, user-confirmation stops, and expansion triggers.

- [ ] **Step 1: Run the pre-check**

Run:

```powershell
Test-Path scripts/show_context_guard.ps1
```

Expected before this task is implemented:

```text
False
```

- [ ] **Step 2: Create the script directory**

Run:

```powershell
New-Item -ItemType Directory -Force scripts | Out-Null
```

Expected: command completes without output.

- [ ] **Step 3: Create `scripts/show_context_guard.ps1`**

Create `scripts/show_context_guard.ps1` with this content:

```powershell
param(
    [ValidateSet("default", "docs", "hwpx-policy", "normalizer", "renderer", "security", "review")]
    [string]$TaskType = "default"
)

$ErrorActionPreference = "Stop"
$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
$ConfigPath = Join-Path $Root "context_guard.json"

if (-not (Test-Path -LiteralPath $ConfigPath)) {
    Write-Error "Missing context_guard.json at $ConfigPath"
    exit 2
}

$Config = Get-Content -Raw -Encoding utf8 -LiteralPath $ConfigPath | ConvertFrom-Json
$Profiles = $Config.task_profiles
$ProfileNames = @($Profiles.PSObject.Properties.Name)

if ($ProfileNames -notcontains $TaskType) {
    Write-Error "Unknown task type '$TaskType'. Available: $($ProfileNames -join ', ')"
    exit 2
}

$Profile = $Profiles.$TaskType
$EntryFiles = @()
$EntryFiles += @($Config.default_entry_files)
$EntryFiles += @($Profile.entry_files)
$EntryFiles = $EntryFiles | Where-Object { $_ } | Select-Object -Unique

function Test-ContextPath {
    param([string]$RelativePath)

    if ($RelativePath.Contains("*")) {
        return "GLOB"
    }

    $FullPath = Join-Path $Root $RelativePath
    if (Test-Path -LiteralPath $FullPath) {
        return "OK"
    }

    return "MISSING"
}

Write-Host "Project: $($Config.project)"
Write-Host "Task type: $TaskType"
Write-Host "Last reviewed: $($Config.last_reviewed)"
Write-Host ""

Write-Host "Recommended entry files:"
foreach ($Entry in $EntryFiles) {
    $Status = Test-ContextPath -RelativePath $Entry
    Write-Host "[$Status] $Entry"
}

Write-Host ""
Write-Host "Inspect commands:"
foreach ($Command in @($Profile.inspect_commands)) {
    Write-Host "- $Command"
}

Write-Host ""
Write-Host "Default excludes:"
foreach ($Exclude in @($Config.default_exclude_globs)) {
    Write-Host "- $Exclude"
}

Write-Host ""
Write-Host "Stop and ask the user before:"
foreach ($StopRule in @($Config.always_confirm_before)) {
    Write-Host "- $StopRule"
}

Write-Host ""
Write-Host "Always expand when:"
foreach ($Rule in @($Config.expand_when_global)) {
    Write-Host "- $Rule"
}
foreach ($Rule in @($Profile.expand_when)) {
    Write-Host "- $Rule"
}
```

- [ ] **Step 4: Verify default output**

Run:

```powershell
.\scripts\show_context_guard.ps1
```

Expected output includes:

```text
Project: public-document-automation
Task type: default
Recommended entry files:
[OK] README.md
[OK] AGENTS.md
[OK] CURRENT_STATUS.md
[OK] tasks/NEXT_STEP.md
[OK] docs/token_context_map.md
Stop and ask the user before:
- real HWPX preview or Hancom manual viewing
```

- [ ] **Step 5: Verify HWPX policy profile**

Run:

```powershell
.\scripts\show_context_guard.ps1 -TaskType hwpx-policy
```

Expected output includes:

```text
Task type: hwpx-policy
[OK] docs/150_manual_preview_resume_gate.md
[OK] checklists/manual_preview_resume_gate_checklist.md
```

- [ ] **Step 6: Commit**

Run:

```powershell
git add scripts/show_context_guard.ps1
git commit -m "tool: add public document context guard script"
```

## Task 3: Link Guard From Current Entry Points

**Files:**
- Modify: `README.md`
- Modify: `AGENTS.md`
- Modify: `tasks/NEXT_STEP.md`

**Interfaces:**
- Consumes: `docs/token_context_map.md`, `scripts/show_context_guard.ps1`
- Produces: Entry-point instructions that direct future workers to the guard before broad scans.

- [ ] **Step 1: Insert README guard section**

In `README.md`, insert this section after the paragraph that says `현재 실제로 작동 확인된 범위와 아직 결과물이 아닌 범위는 CURRENT_STATUS.md를 먼저 확인합니다.`

````markdown
## Codex 작업 시작 전 토큰 가드

새 작업을 시작할 때는 전체 `docs/` 또는 `checklists/`를 먼저 훑지 말고, 토큰 컨텍스트 가드를 먼저 확인합니다.

```powershell
.\scripts\show_context_guard.ps1
```

작업 유형이 분명하면 다음 중 하나를 사용합니다.

```powershell
.\scripts\show_context_guard.ps1 -TaskType docs
.\scripts\show_context_guard.ps1 -TaskType hwpx-policy
.\scripts\show_context_guard.ps1 -TaskType normalizer
.\scripts\show_context_guard.ps1 -TaskType renderer
.\scripts\show_context_guard.ps1 -TaskType security
.\scripts\show_context_guard.ps1 -TaskType review
```

가드는 파일 접근을 막는 장치가 아닙니다. 최신 진입점부터 작게 읽고, 보안ㆍHWPXㆍ실제 원본 가능성이 있으면 즉시 사용자 확인 또는 컨텍스트 확장으로 전환하기 위한 안내입니다.
````

- [ ] **Step 2: Insert AGENTS guard rule**

In `AGENTS.md`, under `## Codex 작업 방식 보강`, add this bullet group after the existing bullet that begins `작업 전에는 관련 문서와 실제 파일 상태를 먼저 확인하고`.

```markdown
- 새 작업 시작 시 전체 `docs/` 또는 `checklists/`를 먼저 훑지 않고 `docs/token_context_map.md`와 `scripts/show_context_guard.ps1`의 추천 진입 파일을 먼저 확인합니다.
- 토큰 컨텍스트 가드는 파일 접근 금지가 아니라 기본 탐색 범위를 줄이는 안내입니다. 테스트 실패, 보안 기준 변경, HWPX 수동 preview, 실제 원본 가능성, output 정책 변경이 보이면 즉시 관련 문서와 체크리스트로 범위를 넓힙니다.
- HWP/HWPX 파일, output 폴더, 실제 원본 후보는 기본 컨텍스트에 포함하지 않으며, 열람 또는 처리 필요성이 생기면 기존 사용자 확인 절차를 우선합니다.
```

- [ ] **Step 3: Insert NEXT_STEP guard status**

In `tasks/NEXT_STEP.md`, add this paragraph near the end of `## 현재 상태`, before `## 목표`.

```markdown
토큰 사용량 절감을 위해 `docs/token_context_map.md`, `context_guard.json`, `scripts/show_context_guard.ps1`를 도입합니다. 이 가드는 전체 문서 탐색을 막는 장치가 아니라, 최신 진입점부터 작게 읽고 보안ㆍHWPXㆍ실제 원본 위험이 보이면 즉시 범위를 넓히거나 사용자 확인으로 전환하는 작업 시작 절차입니다.
```

- [ ] **Step 4: Verify entry-point links**

Run:

```powershell
rg -n "show_context_guard|token_context_map|토큰 컨텍스트|토큰 가드" README.md AGENTS.md tasks/NEXT_STEP.md
```

Expected output includes matches in all three files.

- [ ] **Step 5: Commit**

Run:

```powershell
git add README.md AGENTS.md tasks/NEXT_STEP.md
git commit -m "docs: link public document context guard"
```

## Task 4: Verify Security and Guard Integrity

**Files:**
- Modify: none expected

**Interfaces:**
- Consumes: `README.md`, `AGENTS.md`, `tasks/NEXT_STEP.md`, `context_guard.json`, `docs/token_context_map.md`, `scripts/show_context_guard.ps1`
- Produces: Verification evidence only.

- [ ] **Step 1: Run JSON validation**

Run:

```powershell
$config = Get-Content -Raw -Encoding utf8 context_guard.json | ConvertFrom-Json
if ($config.project -ne "public-document-automation") { throw "Unexpected project name" }
if (-not $config.default_entry_files.Contains("AGENTS.md")) { throw "AGENTS.md must be a default entry" }
if (-not $config.always_confirm_before.Contains("real HWPX preview or Hancom manual viewing")) { throw "Missing HWPX stop rule" }
```

Expected: command completes without output.

- [ ] **Step 2: Run all task profiles**

Run:

```powershell
foreach ($task in "default","docs","hwpx-policy","normalizer","renderer","security","review") {
    .\scripts\show_context_guard.ps1 -TaskType $task
}
```

Expected: each profile prints a context guard report and exits successfully.

- [ ] **Step 3: Verify HWP/HWPX files are not default entry files**

Run:

```powershell
$config = Get-Content -Raw -Encoding utf8 context_guard.json | ConvertFrom-Json
$allEntries = @($config.default_entry_files)
foreach ($profile in $config.task_profiles.PSObject.Properties) {
    $allEntries += @($profile.Value.entry_files)
}
if ($allEntries | Where-Object { $_ -match "\.hwp$|\.hwpx$|output/" }) {
    throw "HWP/HWPX/output paths must not be default entry files"
}
```

Expected: command completes without output.

- [ ] **Step 4: Run security keyword scan on new guard files and modified entry points**

Run:

```powershell
rg -n "010|주민등록|계좌|차량번호|문서번호|민원번호|접수번호|사건번호|대외비|비공개|내부망|비밀번호|API 키|실명|주소|감사|징계|수사|업체 견적|관서별|장비현황" docs/token_context_map.md context_guard.json scripts/show_context_guard.ps1 README.md AGENTS.md tasks/NEXT_STEP.md
```

Expected: matches may appear only as policy terms in `AGENTS.md` or explanatory safety lists. No actual personal, institutional, case, account, address, phone, budget, or internal-operation values should appear.

- [ ] **Step 5: Check Git status**

Run:

```powershell
git status --short
```

Expected:

```text
```

- [ ] **Step 6: Commit if verification required a correction**

If any correction was needed, commit it:

```powershell
git add README.md AGENTS.md tasks/NEXT_STEP.md context_guard.json docs/token_context_map.md scripts/show_context_guard.ps1
git commit -m "fix: align public document context guard"
```

If no correction was needed, do not create an empty commit.

## Self-Review Notes

Spec coverage:

- `docs/token_context_map.md` implements the human-readable policy.
- `context_guard.json` implements default entry files, excludes, stop rules, and task profiles.
- `scripts/show_context_guard.ps1` prints guidance without reading file bodies.
- README, AGENTS, and NEXT_STEP link the guard from current entry points.
- HWP/HWPX, output, and real-origin risks remain excluded from default entry files.
- User confirmation remains required for HWPX preview, source documents, real institution forms, destructive file operations, and external integration.

Known residual risk:

- When new current-entry documents are created, both `docs/token_context_map.md` and `context_guard.json` must be updated in the same change set.
