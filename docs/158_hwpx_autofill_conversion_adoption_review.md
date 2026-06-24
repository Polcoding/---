# HWPX 자동 채우기 외부 자료 채택 검토

## 목적

사용자가 제공한 HWPX 자동 채우기 관련 자료를 현재 저장소의 HWPX 보고서 우선 자동화 방향에 맞게 검토합니다.

이번 검토는 외부 도구를 바로 운영 코드로 편입하기 위한 것이 아니라, 현재 Python 기반 placeholder 렌더러와 안전 절차를 유지하면서 참고할 수 있는 구조 분석 방식을 정리하기 위한 것입니다.

## 검토 자료

| 자료 | 확인 범위 | 판단 |
|---|---|---|
| `https://github.com/reallygood83/hwpx-cli` | README 기준 기능 범위, CLIㆍcoreㆍMCP 구성, 라이선스와 릴리스 상태 | 참고 후보 |
| `https://www.youtube.com/watch?v=S7p8_jcwPo0` | 제목과 사용자가 제공한 첨부 파일 기준 | 참고 후보 |
| `hwpx-autofill-conversion.skill` | 설치 전후 `SKILL.md` 내용 확인 | 로컬 참고용 skill |
| 다운로드된 HWPX 샘플 2건 | 패키지 구조, section XML, paragraph/table/text node 개수, placeholder 존재 여부 | 구조 분석 참고 |

YouTube 영상의 세부 설명과 자막 원문은 현재 도구에서 직접 확인하지 못했습니다. 따라서 이 문서는 영상 원문을 근거로 삼지 않고, 제목과 사용자가 제공한 첨부 파일 및 저장소에서 직접 확인한 구조만 기준으로 작성합니다.

## 외부 skill 설치 결과

로컬 Codex skill 경로에 다음 파일을 설치했습니다.

- `$CODEX_HOME\skills\hwpx-autofill-conversion\SKILL.md`

설치된 skill은 HWPX 파일을 압축 패키지로 보고, `mimetype`, `META-INF`, `BinData`, `Preview`, `Contents/header.xml`, `Contents/section*.xml`, `settings.xml` 구조를 분류한 뒤 HWPX 결과물을 만드는 방향을 설명합니다.

단, 이 저장소에서는 해당 skill 지시를 그대로 실행하지 않습니다. 실제 원문과 실제 HWPX 양식 원본을 외부 AI 입력으로 넣지 않고, 저장소의 `AGENTS.md`, 보안 원칙, Git 제외 정책을 우선합니다.

## 샘플 HWPX 구조 확인 결과

다운로드 폴더에 있는 샘플 HWPX 2건은 저장소로 복사하지 않았습니다. 본문 텍스트도 저장소에 기록하지 않았고, 구조 정보만 확인했습니다.

| 구분 | section 수 | 문단 수 | 텍스트 노드 수 | 표 수 | placeholder 유사 토큰 |
|---|---:|---:|---:|---:|---:|
| 샘플 1 | 1 | 179 | 172 | 13 | 0 |
| 샘플 2 | 1 | 44 | 30 | 2 | 0 |

확인 결과 두 샘플은 이미 `{{placeholder}}`가 들어간 템플릿이 아니라, 기존 양식 구조를 분석해 placeholder 후보 위치를 찾아야 하는 자료에 가깝습니다.

## 현재 프로젝트에 바로 적용 가능한 점

1. HWPX를 ZIP 패키지로 열어 `Contents/section*.xml` 중심으로 구조를 확인하는 절차
2. 문단, 표, 텍스트 노드 개수를 template intake 메타정보로 기록하는 방식
3. `Preview/PrvText.txt`는 비식별 샘플에서만 보조 확인용으로 제한하는 기준
4. 기존 양식을 바로 AI에 넣는 것이 아니라, 사람이 비식별 복사본을 만든 뒤 placeholder 후보를 표시하는 절차
5. 최종 치환은 현재 저장소의 placeholder 기반 HWPX renderer 흐름을 유지하는 방식

이 중 구조 분석은 `normalizers/hwpx_template_structure_analyzer_poc.py`로 저장소 내부 Python PoC에 흡수했습니다.

## 바로 적용하지 않는 점

- 실제 기관 HWPX/HWP 원본을 저장소에 추가하지 않음
- 실제 원문을 외부 AI나 skill 입력으로 넣지 않음
- `hwpx-cli` 또는 MCP를 즉시 운영 의존성으로 추가하지 않음
- Claude skill식 직접 자동 채우기를 현재 저장소의 기본 흐름으로 바꾸지 않음
- HWPX 표 내부 실제 수량, 금액, 대상 목록 자동 입력을 시작하지 않음
- Email/API/Make.com/Gmail/Outlook 연동과 결합하지 않음

## 권장 반영 구조

```text
저장소 밖 비식별 HWPX 작업 복사본
-> HWPX 패키지 구조 분석
-> 문단ㆍ표ㆍplaceholder 후보 위치 메타정보 기록
-> 사람이 placeholder 삽입 위치 검토
-> 로컬 placeholder HWPX 템플릿 유지
-> 기존 Python HWPX renderer로 치환
-> ignored output 생성
-> docs/150_manual_preview_resume_gate.md 기준으로 한컴 수동 preview
```

## `hwpx-cli` 참고 판단

`hwpx-cli`는 HWPX 읽기, 정보 확인, Markdown 변환, batch index, core library, MCP 서버 방향까지 포함한 도구 후보입니다. Apache-2.0 라이선스이고 공개 저장소이지만, 현재 확인 기준으로는 릴리스가 아직 없고 프로젝트 성숙도를 추가 검증해야 합니다.

따라서 지금은 현재 Python renderer를 대체하지 않고, 아래 용도로만 후속 후보로 둡니다.

- HWPX 구조 추출 결과 비교
- text/section/table count 검증 보조
- Markdown 변환 품질 비교
- 향후 별도 sandbox에서 의존성 설치 없이 가능한 문서 검토

## 로컬 설치ㆍ빌드 spike 결과

사용자 요청에 따라 `reallygood83/hwpx-cli`를 저장소 밖 외부 도구 폴더에 설치해 확인했습니다.

저장소 안에는 외부 repo 파일, `node_modules`, HWPX 샘플, 변환 output을 추가하지 않았습니다.

| 항목 | 결과 | 비고 |
|---|---|---|
| npm 임시 실행 | 실패 | `@masteroflearning/hwpx-cli` 패키지가 npm registry에 없어 404 반환 |
| Git clone checkout | 실패 | 외부 repo에 Windows에서 checkout할 수 없는 `:Zone.Identifier` 경로가 있어 working tree checkout 실패 |
| GitHub zip archive | 성공 | `DevDoc`와 `:Zone.Identifier` 항목을 제외하고 저장소 밖 폴더에 압축 해제 |
| pnpm install | 부분 성공 | 의존성은 설치됐으나 pnpm 11 ignored build scripts 정책으로 exit code 1 반환 |
| 직접 build | 성공 | `hwpx-core`, `hwpx-tools`, `hwpx-cli`를 로컬 `.bin/tsup`으로 순차 빌드 |
| CLI 도움말 | 성공 | `hwpxcli` 명령 목록 확인 |
| 외부 repo 샘플 `info` | 성공 | `sections`, `paragraphs` 구조 정보 출력 |
| 사용자 제공 샘플 2건 `info` | 성공 | 본문 추출 없이 구조 정보만 확인 |

실행 가능한 로컬 CLI 위치는 다음과 같습니다.

```text
..\_external_tools\reallygood83-hwpx-cli-archive\packages\hwpx-cli\dist\cli.js
```

사용 예시는 다음과 같습니다.

```powershell
$env:PATH = "[Codex bundled Node]\node\bin;" + $env:PATH
node ..\_external_tools\reallygood83-hwpx-cli-archive\packages\hwpx-cli\dist\cli.js info [비식별 HWPX 파일]
```

현재 확인한 명령은 `--help`, `info`, `read`, `hwpx-to-md`입니다. `read`와 `hwpx-to-md`는 외부 repo 샘플에서만 확인했고, 사용자 제공 샘플에는 내용 추출 없이 `info`만 실행했습니다.

주의할 점은 `hwpx-cli info`의 paragraph count가 기존 XML 직접 카운트와 다를 수 있다는 것입니다. 이는 도구가 HWPX XML을 해석하는 방식과 단순 태그 카운트 방식의 차이로 보이며, 당장은 어느 한쪽을 실제 문서 품질 판단 기준으로 단정하지 않습니다.

## 보안 판단

이번 검토에서 실제 개인정보, 실제 기관명, 실제 문서번호, 실제 공문 원문은 저장소에 추가하지 않았습니다.

다운로드된 HWPX 샘플은 저장소 밖에 두었고, Git 추적 대상에 포함하지 않았습니다.

실제 업무용 HWPX output도 생성하지 않았습니다.

`reallygood83/hwpx-cli` 설치 파일, `node_modules`, 빌드 결과, 변환 테스트 산출물은 저장소 밖 외부 도구 폴더에만 있습니다.

외부 도구 격리와 충돌 방지 기준은 `docs/159_external_tool_isolation_and_conflict_policy.md`를 따릅니다.

## 다음 추천 작업

다음 단계는 내부 Python 구조 분석 절차를 기존 수동 preview 재개 게이트와 연결하는 것입니다.

1. `docs/150_manual_preview_resume_gate.md` 조건을 유지합니다.
2. 비식별 HWPX 작업 복사본이 준비된 경우에만 HWPX 구조 분석을 수행합니다.
3. 구조 분석 결과는 본문 텍스트가 아니라 문단ㆍ표ㆍplaceholder 후보 메타정보 중심으로 기록합니다.
4. `hwpx-cli`는 현재 Python renderer와 내부 Python 구조 분석기를 대체하지 않고, 저장소 밖 비교 보조 도구로만 둡니다.
