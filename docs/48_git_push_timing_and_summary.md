# GitHub Desktop push 타이밍과 summary 기준

## 목적

작업이 길어질 때 GitHub Desktop에서 어떤 단위로 commit/push할지 정하기 위한 기준입니다.

이 저장소는 실제 업무자료가 아니라 placeholder 기반 PoC와 문서 검증 저장소이므로, push 전에는 보안 검수와 Git 제외 상태를 먼저 확인합니다.

## 현재 시스템 이해

이 프로젝트는 공공기관 행정업무를 AI가 직접 처리하게 만드는 시스템이 아닙니다.

목표는 비식별 업무 지시를 받아 행정문서 초안을 만들고, 사람이 최종 검토ㆍ수정ㆍ승인하는 보조 시스템입니다.

핵심 구조:

1. 사용자는 실제 원문과 개인정보를 제거한 업무 지시를 입력합니다.
2. AI는 문서 유형에 맞는 JSON 구조와 초안 문장을 생성합니다.
3. 렌더러는 JSON을 HWPX/XLSX/Markdown/Email 초안으로 변환합니다.
4. HWPX/XLSX 템플릿은 폰트, 자간, 줄간격, 표, 문단 배치를 담당합니다.
5. output 산출물은 로컬 검증용이며 Git에 포함하지 않습니다.
6. 실제 발송, 결재, 계약, 업체 선정, 예산 집행, 법률 판단은 사람이 수행합니다.

현재 최우선 흐름:

- HWPX 원페이지 보고서
- HWPX 추진계획서
- HWPX 결과보고서
- HWPX 검토보고서
- XLSX 조사표
- Email 초안

## push 전 확인 기준

GitHub Desktop에서 commit/push하기 전에 다음을 확인합니다.

- 실제 개인정보, 실제 기관명, 실제 문서번호, 실제 공문 원문이 추가되지 않았는가
- 실제 HWP/HWPX 기관 양식 원본이 Changes에 보이지 않는가
- `renderers/*/output/` 산출물이 Changes에 보이지 않는가
- 로컬 HWPX 템플릿이 `.gitignore`로 제외되는가
- `__pycache__` 바이너리 변경이 작업에 포함되지 않는가
- README 링크가 새 문서를 가리키는가
- 테스트 결과 문서가 실제 파일 상태와 일치하는가

## commit/push 타이밍

다음 경우에는 한 번 commit/push하는 것이 좋습니다.

- 여러 개의 관련 문서ㆍ체크리스트ㆍ진입점 갱신이 하나의 의미 있는 묶음으로 끝났을 때
- 렌더러 코드 보강과 테스트 결과 문서가 함께 정리됐을 때
- output과 로컬 템플릿이 Git 제외 상태임을 확인했을 때
- 다음 작업으로 넘어가기 전에 되돌아갈 기준점이 필요할 때
- 사용자가 직접 HWPX를 확인해야 하거나 주요 방향 전환이 필요한 지점에 도달했을 때

다음 경우에는 아직 push하지 않습니다.

- 단일 문서 closeout 또는 작은 문구 정리만 끝났을 때
- 다음 추천 작업이 같은 문서 묶음 안에서 계속 이어질 때
- 사용자가 명시적으로 push를 줄이라고 한 흐름에서 아직 여러 작업을 묶을 수 있을 때
- 한컴 수동 열람 피드백을 반영하는 중일 때
- 렌더러 테스트 결과가 `output_error` 등 환경 오류 상태로 남아 있을 때
- 실제 HWP/HWPX 파일이 Changes에 보일 때
- 문서에는 성공이라고 되어 있지만 실제 summary JSON이 다르게 나올 때

## 현재 push 빈도 원칙

사용자가 push가 너무 잦다고 피드백한 뒤에는 closeout 하나마다 멈추지 않습니다.

기본 원칙:

- `p` 또는 `P`는 push 완료 후 다음 추천 작업 진행 요청으로 해석합니다.
- `p` 이후에도 다음 작업이 작은 문서 보강이면 계속 이어서 진행합니다.
- commit/push 후보는 여러 관련 작업을 묶은 뒤, 검증 결과와 함께 한 번만 정리합니다.
- 작은 문서 1개, 체크리스트 1개, 진입점 문구 일부 수정만으로는 멈추지 않습니다.
- 5분 단위의 작은 확인이나 단일 문구 정리 때문에 사용자에게 매번 확인하지 않습니다.
- 같은 단계 안에서 이어지는 작업은 대략 여러 개의 소작업을 하나의 변경 묶음으로 모은 뒤 commit/push 여부를 판단합니다.
- 파일 또는 폴더 삭제처럼 되돌리기 어려운 작업은 먼저 사용자에게 알리고, 그 외 추가 수정은 저장소 범위 안에서 계속 진행합니다.
- commit/push는 한 번에 묶는 것을 우선하며, 작은 수정마다 별도 commit을 만들지 않습니다.
- 실제 HWPX 열람, 주요 방향 전환, 코드 변경, 테스트 실행 결과 묶음, 보안상 기준점이 필요할 때 push를 권장합니다.

## summary 작성 기준

summary는 현재 실제 변경 묶음을 기준으로 짧게 작성합니다.

```text
docs: summarize changed scope briefly
```

설명 예시:

```text
- Add or update related user guidance docs
- Refresh README, CURRENT_STATUS, AGENTS, and NEXT_STEP only when they are true entry points
- Keep local HWPX templates and output artifacts Git-excluded
```

## 다음 작업 후보

현재 다음 작업은 `tasks/NEXT_STEP.md`를 우선합니다.

구형 후보가 이 문서에 남아 있더라도, 최신 작업 순서는 `CURRENT_STATUS.md`와 `tasks/NEXT_STEP.md` 기준으로 판단합니다.
