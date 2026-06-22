# Phase 2 반복 운영 로그 템플릿

## 목적

Phase 2 최소 PoC를 반복 실행할 때 실행 목적, 명령 결과, HWPX output 확인, 사용자 한컴 검수, Git 제외, 보안 검수 결과를 같은 형식으로 남기기 위한 템플릿입니다.

이 문서는 실제 업무 원문을 기록하기 위한 양식이 아닙니다. 모든 입력과 결과는 placeholder 기반으로만 작성합니다.

## 사용 원칙

- 실제 개인정보, 실제 기관명, 실제 문서번호, 실제 공문 원문을 기록하지 않습니다.
- 실제 HWPX 양식 원본 파일명이나 실제 내부 경로를 기록하지 않습니다.
- HWPX output 파일은 Git에 추가하지 않습니다.
- 확인되지 않은 값은 `[확인 필요]`로 둡니다.
- 이상이 있으면 파일명, 항목 번호, 증상만 기록합니다.
- 실제 업무 적용 여부는 이 로그에서 확정하지 않습니다.

## 로그 템플릿

아래 양식을 복사해 반복 운영 결과 문서에 사용합니다.

````markdown
# Phase 2 반복 운영 로그

## 기본 정보

| 항목 | 값 |
|---|---|
| 실행일 | [YYYY.MM.DD. 확인 필요] |
| 실행 목적 | [반복 운영 목적 확인 필요] |
| 실행 범위 | [예: HWPX 4종 회귀 확인] |
| 입력 유형 | [placeholder fixture / 비식별 사용자 입력 / 확인 필요] |
| 실제 원문 사용 여부 | 사용하지 않음 |
| 실제 개인정보 사용 여부 | 사용하지 않음 |
| 실제 기관 양식 원본 사용 여부 | 사용하지 않음 |

## 실행 전 확인

| 확인 | 항목 | 결과 |
|---|---|---|
| [ ] | Git 작업 트리 확인 | [확인 필요] |
| [ ] | `normalizers/output/` ignored 확인 | [확인 필요] |
| [ ] | `renderers/hwpx_renderer/output/` ignored 확인 | [확인 필요] |
| [ ] | `templates/hwpx/*.hwpx` ignored 확인 | [확인 필요] |
| [ ] | 실제 원문ㆍ개인정보ㆍ기관정보 미사용 확인 | [확인 필요] |

## 실행 명령 결과

| 확인 | 명령 | 기대 결과 | 실제 결과 |
|---|---|---|---|
| [ ] | `python .\normalizers\validate_placeholder_confirmed_values_poc.py` | helper fixture 통과 | [확인 필요] |
| [ ] | `python .\normalizers\input_normalizer_poc.py` | routing fixture 6종 통과 | [확인 필요] |
| [ ] | `python .\normalizers\hwpx_payload_mapper_poc.py` | 허용 routing만 payload 생성 | [확인 필요] |
| [ ] | `python .\normalizers\validate_hwpx_payload_poc.py` | payload validation 통과 | [확인 필요] |
| [ ] | `python .\normalizers\hwpx_renderer_dry_run_poc.py` | blocked/security review 렌더 제외 | [확인 필요] |
| [ ] | `python .\normalizers\render_mapped_hwpx_poc.py` | mapped HWPX 4종 rendered | [확인 필요] |

## 상태별 중단 확인

| 확인 | 상태 또는 증상 | 기준 | 결과 |
|---|---|---|---|
| [ ] | `needs_security_review` | 사람 보안 검토 전 HWPX 렌더링 중단 | [확인 필요] |
| [ ] | `blocked` | 처리 중단, 실제값 제거 요청 | [확인 필요] |
| [ ] | `template_required` | 로컬 템플릿 준비 전 안전 중단, output 생성 시도 없음 | [확인 필요] |
| [ ] | validation 실패 | 렌더링 중단, payload 또는 placeholder map 확인 | [확인 필요] |
| [ ] | `remaining_placeholders` 있음 | preview 중단, placeholder map 또는 템플릿 오탈자 확인 | [확인 필요] |
| [ ] | output 잠금 | 한컴에서 output 파일을 닫은 뒤 재시도 | [확인 필요] |
| [ ] | GitHub Desktop Changes에 HWPX 표시 | 작업 중단, `.gitignore`와 파일 위치 확인 | [확인 필요] |

## HWPX output 확인

| 확인 | output | 기대 결과 | 실제 결과 |
|---|---|---|---|
| [ ] | `mapped_safe_one_page_report_poc.hwpx` | rendered / remaining 0 | [확인 필요] |
| [ ] | `mapped_missing_project_plan_poc.hwpx` | rendered / remaining 0 | [확인 필요] |
| [ ] | `mapped_missing_result_report_poc.hwpx` | rendered / remaining 0 | [확인 필요] |
| [ ] | `mapped_approved_review_report_poc.hwpx` | rendered / remaining 0 | [확인 필요] |

## missing_fields 확인

| 확인 | 항목 | 결과 |
|---|---|---|
| [ ] | 확인 필요 항목 개수 확인 | [확인 필요] |
| [ ] | HWPX 본문과 검토용 확인 목록 분리 확인 | [확인 필요] |
| [ ] | `[확인 필요]`가 실제값처럼 보이지 않음 | [확인 필요] |
| [ ] | placeholder 유지 확인 대상 구분 | [확인 필요] |
| [ ] | 실제값 입력 금지 안내 포함 | [확인 필요] |

`missing_fields`는 검토용 목록이며, 본문 실제값으로 확정하지 않습니다.

## 사용자 한컴 검수

| 확인 | 항목 | 결과 |
|---|---|---|
| [ ] | 파일 열림 | [확인 필요] |
| [ ] | 글자 겹침 없음 | [확인 필요] |
| [ ] | 항목 순서 정상 | [확인 필요] |
| [ ] | 줄바꿈과 문단 배치 정상 | [확인 필요] |
| [ ] | 내용 앞 `-` 표기 일관성 | [확인 필요] |
| [ ] | 남은 `{{placeholder}}` 없음 | [확인 필요] |
| [ ] | `[확인 필요]`가 실제값처럼 오인되지 않음 | [확인 필요] |
| [ ] | 실제 개인정보, 기관정보, 문서번호 없음 | [확인 필요] |

## 이상 발생 기록

| 파일명 | 항목 번호 | 증상 | 처리 상태 |
|---|---|---|---|
| [파일명 확인 필요] | [항목 번호 확인 필요] | [증상 확인 필요] | [처리 상태 확인 필요] |

이상이 없으면 다음과 같이 기록합니다.

```text
이상 없음
```

## GitHub Desktop Changes 확인

| 확인 | 항목 | 결과 |
|---|---|---|
| [ ] | HWPX output이 Changes에 보이지 않음 | [확인 필요] |
| [ ] | `normalizers/output/*.json`이 Changes에 보이지 않음 | [확인 필요] |
| [ ] | 로컬 HWPX 템플릿이 Changes에 보이지 않음 | [확인 필요] |
| [ ] | 실제 원본 파일이 Changes에 보이지 않음 | [확인 필요] |

## 보안 검수

| 확인 | 항목 | 결과 |
|---|---|---|
| [ ] | 실제 개인정보 추가 없음 | [확인 필요] |
| [ ] | 실제 기관명, 업체명, 담당자명 추가 없음 | [확인 필요] |
| [ ] | 실제 문서번호, 민원번호, 사건번호 추가 없음 | [확인 필요] |
| [ ] | 실제 날짜, 예산, 실적 수치 추가 없음 | [확인 필요] |
| [ ] | 실제 공문 원문 또는 보고서 원문 추가 없음 | [확인 필요] |
| [ ] | 실제 HWPX 원본 파일 추가 없음 | [확인 필요] |

## 종합 판단

| 항목 | 판단 |
|---|---|
| Codex 검증 | [통과 / 보류 / 실패 / 확인 필요] |
| 사용자 한컴 검수 | [통과 / 보류 / 실패 / 확인 필요] |
| Git 제외 | [통과 / 보류 / 실패 / 확인 필요] |
| 보안 검수 | [통과 / 보류 / 실패 / 확인 필요] |
| 다음 조치 | [다음 조치 확인 필요] |
````

## 중단 기준

다음 중 하나라도 발생하면 반복 운영을 중단하고 원인을 기록합니다.

- 실제 개인정보 또는 실제 기관정보 발견
- 실제 문서번호, 민원번호, 접수번호, 사건번호 의심값 발견
- blocked fixture에서 payload 또는 HWPX output 생성
- `needs_security_review` fixture에서 HWPX output 생성
- `template_required` 상태에서 output 생성 시도
- payload validation 실패를 무시하고 HWPX 렌더링 진행
- HWPX output에 `{{placeholder}}` 잔여
- HWPX output에 `remaining_placeholders` 잔여
- `missing_fields`를 실제값처럼 확정하거나 자동 제외
- 한컴에서 글자 겹침 또는 항목 누락 발생
- 한컴에서 output 잠금 또는 쓰기 권한 오류가 반복됨
- GitHub Desktop Changes에 HWPX output 또는 로컬 템플릿 표시
- output 폴더 쓰기 권한 오류 반복

## 다음 단계

반복 운영 로그 템플릿에 `missing_fields` 확인 섹션과 상태별 중단 확인 섹션을 반영했습니다.

다음 단계에서는 Phase 3 운영 문서 묶음에서 안전 게이트, 저장소 밖 HWPX 취급, 상태별 중단 기준이 서로 모순 없이 연결되는지 통합 점검합니다. `placeholder_confirmed_values`의 routing 연결은 계속 보류합니다.
