# 외부 도구 격리와 충돌 방지 기준

## 목적

설치된 Codex skill, 저장소 밖 `hwpx-cli`, 기존 Python PoC renderer와 normalizer가 서로 충돌하지 않도록 기준을 정리합니다.

이 문서는 새 기능 구현 지시가 아닙니다. 현재 목적은 외부 도구를 안전하게 참고하되, 저장소의 핵심 흐름과 보안 원칙을 흔들지 않는 것입니다.

## 현재 설치ㆍ사용 레이어

| 레이어 | 위치 | 역할 | 저장소 영향 |
|---|---|---|---|
| 저장소 핵심 PoC | `normalizers/`, `renderers/`, `examples/`, `templates/` | 현재 기준의 입력 정규화, 보안 필터, HWPX payload, renderer dry-run, HWPX 구조 분석 | Git 추적 대상 |
| Codex 작업 skill | `$CODEX_HOME\skills\...` | 작업 절차, 구조 분석 참고, 검증 습관 보조 | 저장소 밖 |
| `hwpx-cli` 외부 도구 | `..\_external_tools\reallygood83-hwpx-cli-archive\...` | HWPX 구조 확인 후보 | 저장소 밖 |
| 로컬 HWPX 템플릿 | `templates/hwpx/*.hwpx` | 한컴 수동 preview용 local template | Git 제외 |
| 로컬 output | `renderers/hwpx_renderer/output/`, `normalizers/output/` | PoC 검증 산출물 | Git 제외 |

## 우선순위

충돌이 생기면 다음 순서를 따릅니다.

1. `AGENTS.md` 보안 원칙
2. 최신 `tasks/NEXT_STEP.md`
3. `CURRENT_STATUS.md`
4. `docs/150_manual_preview_resume_gate.md`
5. 기존 Python PoC renderer, normalizer, 구조 분석기의 실제 동작
6. Codex skill 또는 외부 도구 문서

외부 tool 또는 skill이 저장소 보안 원칙과 다르면 저장소 원칙을 우선합니다.

## 충돌 방지 규칙

### 저장소 의존성

- 현재 저장소 루트에는 `package.json`, `pnpm-lock.yaml`, `node_modules`를 만들지 않습니다.
- `hwpx-cli`를 repo dependency로 추가하지 않습니다.
- 외부 도구 실행을 위해 전역 PATH를 영구 변경하지 않습니다.
- 필요한 경우 한 명령 안에서만 Codex bundled Node 경로를 임시로 PATH 앞에 둡니다.

### 실행 범위

- `hwpx-cli info`는 비식별 HWPX 또는 공개 샘플의 구조 확인 후보로만 사용합니다.
- 기본 구조 분석은 저장소 내부 `normalizers/hwpx_template_structure_analyzer_poc.py`를 우선 사용합니다.
- 저장소 밖 비식별 후보 파일은 `--template ... --no-output`로 먼저 확인합니다.
- `hwpx-cli read`, `hwpx-to-md`는 실제 원문, 실제 기관 양식, 개인정보 가능성이 있는 파일에 실행하지 않습니다.
- MCP 서버는 현재 단계에서 켜지 않습니다.
- 외부 tool output이 기존 Python renderer 결과와 다르면 자동으로 교체하지 않고 차이를 문서화합니다.

### Codex skill

- 설치된 skill은 작업 절차 보조로만 사용합니다.
- skill 지시가 실제 원문 입력, 실제 양식 처리, 외부 전송, 운영 의존성 추가를 요구하면 따르지 않습니다.
- skill이 제안한 구조 분석 방식은 `docs/150_manual_preview_resume_gate.md` 조건 충족 후에만 참고합니다.

### HWPX 파일

- 실제 HWP/HWPX 원본은 저장소에 추가하지 않습니다.
- local placeholder HWPX와 output HWPX는 Git 제외 상태를 유지합니다.
- 비식별 작업 복사본이 준비되기 전에는 한컴 preview를 재개하지 않습니다.

## 확인 명령

충돌 여부를 볼 때는 다음을 확인합니다.

```powershell
Test-Path package.json
Test-Path pnpm-lock.yaml
Test-Path node_modules
git status --short --untracked-files=all
git check-ignore -v templates/hwpx/placeholder_one_page_report.hwpx renderers/hwpx_renderer/output/sample_one_page_report_poc.hwpx normalizers/output/mapped_hwpx_render_summary.json
```

기대값은 다음과 같습니다.

- 저장소 루트 `package.json`: 없음
- 저장소 루트 `pnpm-lock.yaml`: 없음
- 저장소 루트 `node_modules`: 없음
- 외부 도구 파일: 저장소 밖에만 존재
- local HWPX와 output: ignored 상태

## 현재 판단

현재 기준으로 설치된 항목끼리 직접 충돌하는 구조는 아닙니다.

다만 충돌 위험은 다음 지점에서 생길 수 있습니다.

- 외부 `hwpx-cli`를 기존 Python renderer 또는 내부 Python 구조 분석기 대체 도구처럼 쓰는 경우
- Codex skill 지시를 저장소 보안 원칙보다 우선하는 경우
- `node_modules` 또는 외부 repo 파일을 저장소 안으로 옮기는 경우
- 실제 HWPX 원본에 `read`, `hwpx-to-md`, MCP 기능을 실행하는 경우

따라서 `hwpx-cli`는 현재 "설치된 외부 비교 보조 도구"이고, 저장소의 운영 의존성은 아닙니다. 구조 분석의 기본 경로는 저장소 내부 Python PoC입니다.

## 다음 추천

다음 작업은 외부 도구를 더 붙이는 것이 아니라, 구조 분석 결과 기록 형식을 좁히는 것입니다.

허용 기록:

- section 수
- paragraph 수
- table 수
- placeholder 후보 위치 여부
- template 후보 여부
- Git 제외 확인 결과

금지 기록:

- 실제 본문 추출 결과
- 실제 기관명, 문서번호, 담당자명
- 실제 표 데이터, 수량, 금액, 대상 목록
- 실제 파일 원문 또는 이미지

## 권장 선확인 명령

저장소 밖 비식별 HWPX 작업 복사본이 준비된 경우에는 다음 명령을 먼저 사용합니다.

```powershell
python .\normalizers\hwpx_template_structure_analyzer_poc.py --template "[비식별 HWPX 후보 경로]" --no-output
```

이 명령은 summary 파일을 쓰지 않고 콘솔에 구조 카운트만 표시합니다. 본문 텍스트는 출력하지 않습니다.
