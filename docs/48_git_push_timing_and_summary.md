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

- 새로운 문서 단계가 끝났을 때
- 렌더러 코드 보강과 테스트 결과 문서가 함께 정리됐을 때
- output과 로컬 템플릿이 Git 제외 상태임을 확인했을 때
- 다음 작업으로 넘어가기 전에 되돌아갈 기준점이 필요할 때

다음 경우에는 아직 push하지 않습니다.

- 한컴 수동 열람 피드백을 반영하는 중일 때
- 렌더러 테스트 결과가 `output_error` 등 환경 오류 상태로 남아 있을 때
- 실제 HWP/HWPX 파일이 Changes에 보일 때
- 문서에는 성공이라고 되어 있지만 실제 summary JSON이 다르게 나올 때

## 현재 작업 묶음 권장 summary

이번 작업 묶음은 다음 summary를 권장합니다.

```text
Add HWPX report renderer support checks
```

설명 예시:

```text
- Add ChatGPT handoff and next-step task documents
- Confirm one_page_report HWPX placeholder rendering
- Add result_report and review_report HWPX placeholder map support
- Document Git-excluded local HWPX/output handling
- Refresh AGENTS and README to match current PoC state
```

## 다음 작업 후보

이번 묶음을 push한 뒤 다음 중 하나를 선택합니다.

1. `placeholder_result_report.hwpx` 최소 템플릿을 로컬로 준비하고 치환 테스트
2. `placeholder_review_report.hwpx` 최소 템플릿을 로컬로 준비하고 치환 테스트
3. 실제 기관 양식 투입 전 안전 절차와 체크리스트 보강
4. HWPX 보고서 공통 placeholder 설계 정리

추천 순서:

1. 결과보고서 최소 placeholder 템플릿
2. 검토보고서 최소 placeholder 템플릿
3. 실제 양식 투입 전 안전 절차

