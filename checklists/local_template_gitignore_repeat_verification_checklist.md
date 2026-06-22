# local template policy와 Git 제외 상태 반복 검증 체크리스트

## 기준 문서 확인

| 완료 | 항목 |
|---|---|
| [x] | `docs/128_external_hwpx_candidate_manual_procedure_and_hold_criteria.md`를 확인했는가 |
| [x] | `templates/hwpx/local_template_policy.md`를 확인했는가 |
| [x] | `templates/hwpx/README.md`를 확인했는가 |
| [x] | `docs/72_dry_run_artifact_retention_policy.md`를 확인했는가 |
| [x] | 실제 양식 후보, local template, renderer output, normalizer output의 역할을 구분했는가 |

## ignore 파일 확인

| 완료 | 항목 |
|---|---|
| [x] | root `.gitignore`가 현재 없음을 확인했는가 |
| [x] | `templates/hwpx/.gitignore`가 `.hwpx`, `.hwp`, 임시 파일을 제외하는가 |
| [x] | `renderers/hwpx_renderer/output/.gitignore`가 output HWPX, JSON, MD를 제외하는가 |
| [x] | `normalizers/output/.gitignore`가 output 전체를 제외하고 `.gitignore`, `.gitkeep`만 허용하는가 |
| [x] | 현재 단계에서 `.gitignore` 변경이 필요 없다고 판단했는가 |

## 반복 검증 시점 확인

| 완료 | 항목 |
|---|---|
| [x] | 로컬 placeholder HWPX 템플릿 생성 또는 교체 후 확인하도록 정리했는가 |
| [x] | renderer output 또는 normalizer output 생성 후 확인하도록 정리했는가 |
| [x] | 한컴 수동 preview 후 gap log 기록 전 확인하도록 정리했는가 |
| [x] | commit 또는 push 전 확인하도록 정리했는가 |
| [x] | 작업 재개 또는 탭 전환 후 다시 확인하도록 정리했는가 |

## Git 상태 확인

| 완료 | 항목 |
|---|---|
| [x] | `git status --short --untracked-files=all` 확인 기준을 정리했는가 |
| [x] | `git status --ignored --short normalizers/output renderers/hwpx_renderer/output templates/hwpx` 확인 기준을 정리했는가 |
| [x] | 로컬 HWPX 템플릿과 output 산출물이 `!!` ignored로 보이면 정상이라고 정리했는가 |
| [x] | 문서, 체크리스트, README, AGENTS, NEXT_STEP만 Changes에 보여야 한다고 정리했는가 |

## GitHub Desktop 확인

| 완료 | 항목 |
|---|---|
| [x] | `templates/hwpx/*.hwpx` 또는 `.hwp`가 Changes에 보이면 중단하도록 했는가 |
| [x] | `renderers/hwpx_renderer/output/*`가 Changes에 보이면 중단하도록 했는가 |
| [x] | `normalizers/output/*`가 Changes에 보이면 중단하도록 했는가 |
| [x] | 실제 원본, 작업 복사본, 잠금 파일, 임시 파일이 보이면 중단하도록 했는가 |
| [x] | `git add -f`는 사용자 명시 승인 전 금지한다고 정리했는가 |

## 변경 제한 확인

| 완료 | 항목 |
|---|---|
| [x] | renderer 코드를 변경하지 않았는가 |
| [x] | normalizer 코드를 변경하지 않았는가 |
| [x] | fixture JSON을 추가하거나 변경하지 않았는가 |
| [x] | routing 결과를 변경하지 않았는가 |
| [x] | HWPX payload 구조를 변경하지 않았는가 |
| [x] | HWPX output을 재생성하지 않았는가 |
| [x] | 실제 HWPX/HWP 파일을 Git에 추가하지 않았는가 |
| [x] | `.gitignore` 파일을 불필요하게 변경하지 않았는가 |

## 보안 검수

| 완료 | 항목 |
|---|---|
| [x] | 실제 개인정보를 추가하지 않았는가 |
| [x] | 실제 기관명, 업체명, 담당자명을 추가하지 않았는가 |
| [x] | 실제 문서번호, 민원번호, 사건번호를 추가하지 않았는가 |
| [x] | 실제 날짜, 예산, 실적 수치를 추가하지 않았는가 |
| [x] | 실제 공문 원문 또는 보고서 원문을 추가하지 않았는가 |
| [x] | 실제 HWPX 원본 파일을 추가하지 않았는가 |
| [x] | API 키, 토큰, 인증정보 예시값을 추가하지 않았는가 |

## 다음 단계 확인

| 완료 | 항목 |
|---|---|
| [x] | Phase 4 문서 템플릿 안정화 통합 점검이 `docs/130`에 반영되었는가 |
| [x] | 다음 단계가 실제 양식 수동 리허설 사용자 확인 패킷과 gap log 빈 양식 정리인가 |
| [x] | 실제 양식 투입, output 재생성, 외부 연동 구현을 다음 단계로 두지 않았는가 |
