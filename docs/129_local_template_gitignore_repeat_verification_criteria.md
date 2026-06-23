# local template policy와 Git 제외 상태 반복 검증 기준

## 목적

이 문서는 HWPX 보고서 4종 작업을 반복할 때 로컬 HWPX 템플릿, renderer output, normalizer output이 Git 추적 대상에 들어가지 않도록 확인하는 기준을 정리합니다.

이번 단계는 실제 기관 HWPX 원본을 저장소에 넣거나 실제 HWPX output을 재생성하는 단계가 아닙니다. renderer, normalizer, fixture, routing, HWPX payload, output도 변경하지 않습니다.

## 확인 대상

- `docs/128_external_hwpx_candidate_manual_procedure_and_hold_criteria.md`
- `checklists/external_hwpx_candidate_manual_procedure_checklist.md`
- `templates/hwpx/local_template_policy.md`
- `templates/hwpx/README.md`
- `docs/53_real_hwpx_template_intake_safety_procedure.md`
- `docs/58_external_hwpx_placeholder_conversion_runbook.md`
- `docs/112_phase3_external_hwpx_and_manual_preview_criteria.md`
- `docs/127_hwpx_manual_preview_gap_log_criteria.md`
- `docs/133_hwpx_only_table_frame_decision.md`
- `docs/72_dry_run_artifact_retention_policy.md`
- `checklists/real_hwpx_template_intake_checklist.md`
- `checklists/external_hwpx_placeholder_conversion_checklist.md`
- `checklists/hwpx_rendered_output_manual_review_checklist.md`
- `checklists/before_automation_checklist.md`
- `templates/hwpx/.gitignore`
- `renderers/hwpx_renderer/output/.gitignore`
- `normalizers/output/.gitignore`
- `.gitignore`
- `README.md`
- `AGENTS.md`
- `tasks/NEXT_STEP.md`

## 점검 결론

현재 저장소에는 Python cache 제외를 위한 root `.gitignore`가 있고, HWPX template과 output 제외 규칙은 폴더별 `.gitignore`가 담당합니다.

현재 확인한 제외 구조:

| 위치 | 현재 역할 | 판단 |
|---|---|---|
| `templates/hwpx/.gitignore` | `.hwpx`, `.hwp`, 임시 파일 제외 | 유지 |
| `renderers/hwpx_renderer/output/.gitignore` | renderer output의 HWPX, JSON, MD 제외 | 유지 |
| `normalizers/output/.gitignore` | normalizer output 전체 제외, `.gitignore`, `.gitkeep`만 허용 | 유지 |
| root `.gitignore` | `__pycache__/`, `*.pyc` 제외 | 유지 |

현재 규칙으로 로컬 placeholder HWPX 템플릿, output 산출물, Python cache는 Git 제외 상태를 유지하고 있습니다. 따라서 이번 단계에서는 HWPX/output ignore 규칙을 추가 변경하지 않고, 반복 검증 순서와 중단 조건을 유지합니다.

## Git 제외 대상 구분

| 대상 | 위치 | Git 상태 기준 | 처리 |
|---|---|---|---|
| 로컬 placeholder HWPX 템플릿 | `templates/hwpx/*.hwpx`, `templates/hwpx/*.hwp` | ignored | GitHub Desktop Changes에 보이면 중단 |
| renderer output | `renderers/hwpx_renderer/output/*` | ignored | 재생성 여부와 무관하게 Git 추가 금지 |
| normalizer output | `normalizers/output/*` | ignored | summary JSON도 Git 추가 금지 |
| dry-run summary | `normalizers/output/*.json` | ignored | 필요 시 재생성, 커밋 금지 |
| 문서와 체크리스트 | `docs/*.md`, `checklists/*.md` | tracked 가능 | 실제 원문 없는 기준만 기록 |
| policy/manifest 문서 | `templates/hwpx/*.md` | tracked 가능 | 실제 HWPX 원본 정보 기록 금지 |

## 반복 검증 시점

다음 시점에는 Git 제외 상태를 다시 확인합니다.

1. 로컬 placeholder HWPX 템플릿을 새로 만들거나 교체한 직후
2. renderer output 또는 normalizer output을 생성한 직후
3. 한컴 수동 preview 후 gap log를 기록하기 전
4. README, AGENTS, checklist, NEXT_STEP을 갱신한 후
5. GitHub Desktop에서 commit 또는 push하기 전
6. 네트워크 끊김, Codex 재시작, 작업 탭 전환 후 다시 이어갈 때

## 권장 확인 순서

### 1. 저장소 상태 확인

확인 목적:

- 문서와 체크리스트 외의 파일이 Changes에 올라왔는지 확인
- 의도하지 않은 HWP/HWPX/output/임시 파일이 추적되는지 확인

권장 확인:

```powershell
git status --short --untracked-files=all
```

통과 기준:

- `docs/*.md`, `checklists/*.md`, `README.md`, `AGENTS.md`, `tasks/NEXT_STEP.md`, `templates/hwpx/*.md` 같은 의도한 문서 변경만 보임
- `.hwpx`, `.hwp`, `output/*`, `__pycache__`, 잠금 파일이 tracked 또는 untracked Changes로 보이지 않음

### 2. ignored 상태 확인

확인 목적:

- 로컬 HWPX 템플릿과 output 산출물이 실제로 ignored 상태인지 확인

권장 확인:

```powershell
git status --ignored --short normalizers/output renderers/hwpx_renderer/output templates/hwpx renderers/hwpx_renderer/__pycache__
```

통과 기준:

- 로컬 HWPX 템플릿과 output 산출물은 `!!` ignored로 표시됨
- Python cache도 재생성되면 `!!` ignored로 표시됨
- `.gitignore`, `.gitkeep`, README, manifest, policy 문서는 필요 시 tracked 상태로 남음

### 3. GitHub Desktop Changes 확인

[사용자 확인 필요]

GitHub Desktop에서 보이면 안 되는 항목:

- `templates/hwpx/*.hwpx`
- `templates/hwpx/*.hwp`
- `renderers/hwpx_renderer/output/*`
- `normalizers/output/*`
- 실제 기관 HWPX 원본
- 실제 HWP/HWPX 작업 복사본
- 실제 공문 또는 보고서 원문
- 잠금 파일, 임시 파일, `__pycache__`

보여도 되는 항목:

- `docs/*.md`
- `checklists/*.md`
- `README.md`
- `AGENTS.md`
- `tasks/NEXT_STEP.md`
- `templates/hwpx/*.md`
- 명시 승인된 placeholder 기반 PoC 코드

## 즉시 중단 조건

다음 중 하나라도 있으면 commit 또는 push하지 않습니다.

| 중단 조건 | 처리 |
|---|---|
| `templates/hwpx/*.hwpx` 또는 `.hwp`가 Changes에 보임 | `.gitignore`와 파일 위치 확인 |
| `renderers/hwpx_renderer/output/*`가 Changes에 보임 | output 제외 상태 확인 |
| `normalizers/output/*`가 Changes에 보임 | output 제외 상태 확인 |
| 실제 원본 또는 비식별 작업 복사본이 저장소 안에 있음 | 저장소 밖 위치로 분리, 보안 검토 |
| 실제 파일명, 실제 기관명, 실제 문서번호가 문서에 기록됨 | 문서 수정 전 commit 금지 |
| root `.gitignore`와 폴더별 ignore 기준을 우회해 HWPX 파일을 강제 추가하려 함 | 강제 추가 금지, 폴더별 ignore 기준 유지 |
| `git add -f`가 필요하다고 판단됨 | 사용자 명시 승인 전 중단 |

## `.gitignore` 변경 판단

현재 단계에서는 HWPX template과 output 제외를 위한 `.gitignore` 추가 변경이 필요하지 않습니다.

추가 변경하지 않는 이유:

- root `.gitignore`가 `__pycache__/`, `*.pyc`를 제외합니다.
- `templates/hwpx/.gitignore`가 `.hwpx`, `.hwp`, 임시 파일을 제외합니다.
- `renderers/hwpx_renderer/output/.gitignore`가 renderer output 산출물을 제외합니다.
- `normalizers/output/.gitignore`가 normalizer output 전체를 제외합니다.
- 현재 확인 결과 로컬 HWPX 템플릿과 output 산출물은 ignored 상태입니다.

향후 `.gitignore` 변경을 검토할 수 있는 경우:

- 새 output 폴더가 생김
- 새 로컬 템플릿 폴더가 생김
- GitHub Desktop Changes에 HWP/HWPX/output 파일이 반복 표시됨
- 폴더별 ignore 규칙이 서로 충돌함

다만 이 경우에도 실제 HWP/HWPX 원본을 Git에 추가하는 방향으로 수정하지 않습니다.

## 문서화 원칙

- Git 제외 확인 결과에는 실제 원본 파일명, 실제 기관명, 실제 문서번호를 기록하지 않습니다.
- 로컬 placeholder 파일명은 기존 검증용 중립 파일명만 기록합니다.
- output 파일명은 placeholder 기반 검증 산출물로만 기록합니다.
- 실제 HWPX 파일 내용, 화면 캡처, 원문 일부는 저장소 문서에 넣지 않습니다.
- 표 관련 확인도 `table_scope: frame_only` 기준으로 표 틀만 기록하고 실제 표 데이터는 남기지 않습니다.
- `!!` ignored 상태 확인은 허용하지만 실제 원본 경로나 내부 경로는 기록하지 않습니다.

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
- HWPX/output ignore 규칙
- API, Make.com, Email 연동 코드

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 표 데이터, 물품명, 수량, 금액, 대상 목록 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX 원본 파일 추가 없음
- 실제 파일명, 내부 경로, 원본 양식명 추가 없음
- 폰트 파일 추가 없음
- API 키, 토큰, 인증정보 예시값 추가 없음
- Email, API, Make.com 연동 구현 없음

## 결론

현재 저장소는 root `.gitignore`와 폴더별 `.gitignore` 기준으로 Python cache, local HWPX template, output 산출물을 Git에서 제외하고 있습니다.

Phase 4 문서 템플릿 안정화 통합 점검은 `docs/130_phase4_template_stabilization_integrated_review.md`에 반영했습니다.

실제 양식 수동 리허설 사용자 확인 패킷과 gap log 빈 양식은 `docs/131_actual_hwpx_manual_rehearsal_user_confirmation_packet.md`에 반영했습니다.

HWPX 일원화 유지와 표 데이터 Excel/한셀 연동 후보 분리 결정은 `docs/133_hwpx_only_table_frame_decision.md`에 반영했습니다.

다음 단계는 비식별 작업 복사본 준비가 명시될 때만 저장소 밖 한컴 preview 결과를 `table_scope: frame_only` 포함 실제값 없는 gap log로 기록하는 것입니다. 실제 기관 HWPX 원본 투입, HWPX output 재생성, renderer 코드 변경, 외부 연동 구현은 계속 보류합니다.
