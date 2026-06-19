# Phase 2 수동 리허설 runbook

## 목적

이 문서는 Phase 2 최소 PoC를 사용자가 반복 실행할 수 있도록 정리한 수동 리허설 절차입니다.

대상 흐름은 비식별 입력에서 시작해 normalizers 검증, mapped HWPX output 생성, 한컴 수동 검수, GitHub Desktop 확인까지입니다.

이 문서는 운영 자동화 절차가 아닙니다. 실제 업무 원문, 실제 개인정보, 실제 기관 양식 원본, 실제 이메일 발송, API, Make.com 연동은 다루지 않습니다.

## 리허설 범위

포함:

- placeholder 기반 사용자 입력 준비
- normalizers 명령 순서 확인
- HWPX output 생성 전 안전 확인
- mapped HWPX output 생성
- 사용자의 한컴 수동 검수
- GitHub Desktop Changes 확인

제외:

- 실제 기관 양식 원본 사용
- 실제 공문 또는 보고서 원문 사용
- 실제 개인정보, 민원정보, 내부 운영정보 사용
- 실제 이메일 발송
- OpenAI API 실제 호출
- Make.com 실제 시나리오 실행
- `placeholder_confirmed_values`의 routing, `missing_fields`, HWPX payload 연결

## 역할 구분

| 역할 | 담당 |
|---|---|
| 입력 비식별 확인 | 사용자 |
| normalizers 명령 실행 | Codex |
| HWPX output 생성 | Codex |
| 한컴 열람ㆍ겹침ㆍ문체ㆍ서식 검수 | 사용자 |
| GitHub Desktop Changes 확인 | 사용자와 Codex |
| 실제 업무 적용 판단 | 사용자 |

## 0. 시작 전 상태 확인

Codex는 리허설 시작 전에 다음을 확인합니다.

```powershell
git status --short
git status --short --ignored normalizers\output renderers\hwpx_renderer\output templates\hwpx
```

기대 상태:

- 추적 중인 변경 파일이 있으면 리허설 전 먼저 보고
- `normalizers/output/*`는 ignored 상태
- `renderers/hwpx_renderer/output/*`는 ignored 상태
- `templates/hwpx/*.hwpx`는 ignored 상태

중단 기준:

- GitHub Desktop Changes에 `.hwpx`, `.hwp`, output JSON, output Markdown이 추적 대상으로 보이면 중단
- 실제 기관 양식 원본으로 보이는 파일이 Git에 나타나면 중단

## 1. 사용자 입력 전 확인

[사용자 확인 필요]

사용자는 리허설 입력 전에 다음을 확인합니다.

| 확인 | 항목 |
|---|---|
| [ ] | 실제 공문 원문을 붙여넣지 않음 |
| [ ] | 실제 개인정보, 연락처, 이메일, 주소를 제거함 |
| [ ] | 실제 기관명, 부서명, 담당자명을 placeholder로 바꿈 |
| [ ] | 실제 문서번호, 접수번호, 민원번호, 사건번호를 제거함 |
| [ ] | 실제 예산액, 계약 금액, 업체 평가, 실적 수치를 제거함 |
| [ ] | 일정, 예산, 실적, 담당자, 수량은 모르면 `[확인 필요]`로 둠 |
| [ ] | 문서 유형을 `one_page_report`, `project_plan`, `result_report`, `review_report` 중 하나로 구분함 |
| [ ] | 발송, 결재, 계약, 예산 집행, 법률 판단 자동화를 요청하지 않음 |

입력은 `docs/84_hwpx_report_user_input_templates.md`의 형식을 따릅니다.

## 2. 리허설 명령 순서

Codex는 다음 순서로 실행합니다.

```powershell
python .\normalizers\validate_placeholder_confirmed_values_poc.py
python .\normalizers\input_normalizer_poc.py
python .\normalizers\hwpx_payload_mapper_poc.py
python .\normalizers\validate_hwpx_payload_poc.py
python .\normalizers\hwpx_renderer_dry_run_poc.py
python .\normalizers\render_mapped_hwpx_poc.py
```

기대 상태:

- helper safe/invalid fixture 통과
- routing fixture 6종 통과
- blocked fixture payload 미생성
- `needs_security_review` fixture HWPX 렌더링 제외
- 허용된 mapped HWPX 4종 렌더링
- summary output은 `normalizers/output/`에 생성
- HWPX output은 `renderers/hwpx_renderer/output/`에 생성

## 3. HWPX output 생성 전 확인

Codex는 HWPX output 생성 전에 다음을 확인합니다.

| 확인 | 항목 | 기준 |
|---|---|---|
| [ ] | routing | `ready_for_draft` 또는 허용된 `needs_more_input`만 렌더링 |
| [ ] | review_report | placeholder 보안 승인 신호 없는 검토보고서는 렌더링 제외 |
| [ ] | validation | HWPX payload validation 실패 없음 |
| [ ] | dry-run | renderer dry-run에서 보안 보류 또는 blocked 제외 |
| [ ] | 템플릿 | 로컬 `templates/hwpx/*.hwpx` 존재 |
| [ ] | output 폴더 | `normalizers/output/`, `renderers/hwpx_renderer/output/` 쓰기 가능 |
| [ ] | 파일 잠금 | 한컴에서 기존 output HWPX가 열려 있으면 닫은 뒤 진행 |

`output_error`가 발생하면 코드 보강 전에 다음을 먼저 확인합니다.

- 한컴에서 같은 output HWPX 파일을 열어 둔 상태인지
- output 폴더 쓰기 권한이 막힌 상태인지
- output 파일이 읽기 전용 또는 잠금 상태인지

## 4. HWPX output 생성 후 사용자 검수

[사용자 확인 필요]

사용자는 한컴에서 다음 파일을 직접 엽니다.

```text
renderers/hwpx_renderer/output/mapped_safe_one_page_report_poc.hwpx
renderers/hwpx_renderer/output/mapped_missing_project_plan_poc.hwpx
renderers/hwpx_renderer/output/mapped_missing_result_report_poc.hwpx
renderers/hwpx_renderer/output/mapped_approved_review_report_poc.hwpx
```

사용자 확인 항목:

| 확인 | 항목 | 기준 |
|---|---|---|
| [ ] | 파일 열림 | 한컴에서 정상 열림 |
| [ ] | 글자 겹침 | 제목과 본문에 겹침 없음 |
| [ ] | 항목 순서 | 보고서 항목 순서 정상 |
| [ ] | 줄바꿈 | 여러 줄 본문이 문단 단위로 보임 |
| [ ] | bullet 표기 | 내용 앞 `-` 표기 일관성 |
| [ ] | placeholder 잔여 | 남은 `{{placeholder}}` 없음 |
| [ ] | 확인 필요값 | `[확인 필요]`가 실제값처럼 보이지 않음 |
| [ ] | 민감정보 | 실제 개인정보, 기관정보, 문서번호 없음 |

사용자가 이상을 발견하면 파일명과 항목 번호를 함께 알려줍니다.

예:

```text
mapped_missing_result_report_poc.hwpx 5번 내용 앞에만 -가 있음
```

## 5. GitHub Desktop Changes 확인

[사용자 확인 필요]

HWPX output 생성 후 GitHub Desktop Changes에서 다음을 확인합니다.

보이면 안 되는 파일:

- `templates/hwpx/*.hwpx`
- `renderers/hwpx_renderer/output/*.hwpx`
- `renderers/hwpx_renderer/output/*.json`
- `renderers/hwpx_renderer/output/*.md`
- `normalizers/output/*.json`
- 실제 기관 양식 원본
- 실제 공문 또는 보고서 원문

보여도 되는 파일:

- 새 문서
- 새 체크리스트
- README 갱신
- 명시적으로 수정한 PoC 코드

## 6. 중단 기준

다음 중 하나라도 발생하면 리허설을 중단합니다.

- 실제 개인정보 또는 실제 기관정보가 입력이나 output에 보임
- 실제 문서번호, 민원번호, 접수번호, 사건번호처럼 보이는 값이 보임
- `review_report`가 승인 신호 없이 렌더링됨
- blocked fixture에서 HWPX payload 또는 HWPX output이 생성됨
- `{{placeholder}}`가 output에 남음
- 한컴에서 글자 겹침, 항목 누락, 제목 깨짐이 확인됨
- GitHub Desktop Changes에 `.hwpx`, `.hwp`, output 파일이 추적 대상으로 보임
- output 폴더 쓰기 권한 오류가 반복됨

## 7. 완료 기준

다음 조건을 모두 만족하면 Phase 2 최소 PoC 수동 리허설 1회를 완료한 것으로 봅니다.

- 입력 전 사용자 체크 통과
- normalizers 명령 순서 실행
- helper fixture 검증 통과
- routing fixture 6종 검증 통과
- mapped HWPX 4종 렌더링 완료
- 사용자의 한컴 수동 검수 통과
- output 및 로컬 HWPX 템플릿 Git 제외 확인
- 실제 원문, 개인정보, 기관정보, 실제 문서번호 추가 없음

## 다음 단계

이 runbook을 기준으로 실제 수동 리허설을 1회 실행하고, 결과를 별도 문서로 기록합니다.
