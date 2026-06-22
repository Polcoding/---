# Phase 2 수동 리허설 실행 결과

## 목적

`docs/98_phase2_manual_rehearsal_runbook.md` 기준으로 Phase 2 최소 PoC를 1회 실행한 결과를 기록합니다.

이 결과는 실제 업무 원문이나 실제 기관 양식 검증이 아니라, placeholder 기반 로컬 PoC 흐름이 현재 저장소 상태에서 재현되는지 확인한 기록입니다.

## 실행 범위

실행한 범위:

- helper fixture 검증
- 입력 정규화 fixture 6종 검증
- HWPX payload mapper 검증
- HWPX payload validation 검증
- HWPX renderer dry-run 검증
- mapped HWPX 4종 렌더링
- output 및 로컬 HWPX 템플릿 Git 제외 확인

실행하지 않은 범위:

- 실제 기관 양식 원본 사용
- 실제 공문 또는 보고서 원문 사용
- 실제 개인정보 또는 내부 운영정보 사용
- OpenAI API 실제 호출
- Make.com 실제 시나리오 실행
- Email 자동 발송
- 한컴 자동 제어
- `placeholder_confirmed_values`의 routing, `missing_fields`, HWPX payload 연결

## 실행 명령과 결과

### 1. placeholder_confirmed_values helper 검증

명령:

```powershell
python .\normalizers\validate_placeholder_confirmed_values_poc.py
```

결과:

- safe fixture 통과
- invalid fixture 기대 invalid 건수와 일치
- plain text 실제값 후보는 안전하지 않은 값으로 판정
- sandbox 안에서는 summary output 쓰기가 제한되어 `summary_output_skipped_permission_error` 발생

판단:

- helper 로직 검증 통과
- helper 결과는 아직 normalizer routing, `missing_fields`, HWPX payload에 연결하지 않음

### 2. 입력 정규화 검증

명령:

```powershell
python .\normalizers\input_normalizer_poc.py
```

결과:

| fixture | document_type | routing | 결과 |
|---|---|---|---|
| `approved_review_report_request.json` | `review_report` | `ready_for_draft` | passed |
| `blocked_real_value_like_request.json` | `unknown` | `blocked` | passed |
| `missing_project_plan_request.json` | `project_plan` | `needs_more_input` | passed |
| `missing_result_report_request.json` | `result_report` | `needs_more_input` | passed |
| `review_report_needs_security_review.json` | `review_report` | `needs_security_review` | passed |
| `safe_one_page_report_request.json` | `one_page_report` | `ready_for_draft` | passed |

판단:

- 기존 routing fixture 6종 통과
- blocked와 security review 경로 유지

### 3. HWPX payload mapper 검증

명령:

```powershell
python .\normalizers\hwpx_payload_mapper_poc.py
```

결과:

| fixture | routing | mapper 결과 | 판단 |
|---|---|---|---|
| `approved_review_report_request.json` | `ready_for_draft` | created | passed |
| `blocked_real_value_like_request.json` | `blocked` | skipped | passed |
| `missing_project_plan_request.json` | `needs_more_input` | created | passed |
| `missing_result_report_request.json` | `needs_more_input` | created | passed |
| `review_report_needs_security_review.json` | `needs_security_review` | skipped | passed |
| `safe_one_page_report_request.json` | `ready_for_draft` | created | passed |

판단:

- blocked fixture payload 미생성 유지
- `needs_security_review` fixture payload 미생성 유지
- 허용 routing만 payload 생성

### 4. HWPX payload validation 검증

명령:

```powershell
python .\normalizers\validate_hwpx_payload_poc.py
```

결과:

- `ready_for_draft` payload validation 통과
- 허용된 `needs_more_input` payload validation 통과
- blocked fixture validation skip 유지
- `needs_security_review` fixture validation skip 유지

판단:

- 렌더링 전 payload 안전 검증 흐름 유지

### 5. HWPX renderer dry-run 검증

명령:

```powershell
python .\normalizers\hwpx_renderer_dry_run_poc.py
```

결과:

| fixture | routing | dry-run 결과 |
|---|---|---|
| `approved_review_report_request.json` | `ready_for_draft` | `dry_run_ready` |
| `blocked_real_value_like_request.json` | `blocked` | `skipped_blocked` |
| `missing_project_plan_request.json` | `needs_more_input` | `dry_run_ready_with_missing_fields` |
| `missing_result_report_request.json` | `needs_more_input` | `dry_run_ready_with_missing_fields` |
| `review_report_needs_security_review.json` | `needs_security_review` | `skipped_security_review` |
| `safe_one_page_report_request.json` | `ready_for_draft` | `dry_run_ready` |

판단:

- blocked와 security review 경로가 렌더링으로 넘어가지 않음
- 허용 fixture만 실제 HWPX 렌더링 후보로 남음

### 6. mapped HWPX 렌더링 검증

명령:

```powershell
python .\normalizers\render_mapped_hwpx_poc.py
```

sandbox 안 결과:

- HWPX output 파일 쓰기 제한으로 4종 모두 `output_error`
- summary output 쓰기 제한 발생

sandbox 밖 재실행 결과:

| fixture | output | status | replaced_count | remaining_placeholders |
|---|---|---|---:|---|
| `safe_one_page_report_request.json` | `mapped_safe_one_page_report_poc.hwpx` | rendered | 16 | 0 |
| `missing_project_plan_request.json` | `mapped_missing_project_plan_poc.hwpx` | rendered | 22 | 0 |
| `missing_result_report_request.json` | `mapped_missing_result_report_poc.hwpx` | rendered | 20 | 0 |
| `approved_review_report_request.json` | `mapped_approved_review_report_poc.hwpx` | rendered | 16 | 0 |

판단:

- mapped HWPX 4종 렌더링 성공
- 남은 `{{placeholder}}` 없음
- sandbox 쓰기 제한은 코드 회귀가 아니라 실행 환경 권한 문제로 분리

## 생성된 HWPX output

다음 파일이 로컬 output 폴더에 생성되었습니다.

```text
renderers/hwpx_renderer/output/mapped_safe_one_page_report_poc.hwpx
renderers/hwpx_renderer/output/mapped_missing_project_plan_poc.hwpx
renderers/hwpx_renderer/output/mapped_missing_result_report_poc.hwpx
renderers/hwpx_renderer/output/mapped_approved_review_report_poc.hwpx
```

이 파일은 Git에서 제외됩니다.

## Git 제외 확인

확인 결과:

- `normalizers/output/*.json` ignored
- `renderers/hwpx_renderer/output/*.hwpx` ignored
- `renderers/hwpx_renderer/output/*.json` ignored
- `renderers/hwpx_renderer/output/*.md` ignored
- `templates/hwpx/*.hwpx` ignored

tracked 변경으로 남기지 않는 대상:

- HWPX output
- output summary JSON
- 로컬 placeholder HWPX 템플릿
- Python cache

## 한컴 수동 검수

Codex는 HWPX 파일 내부의 placeholder 치환과 summary 결과는 확인했지만, 한컴 화면에서의 글자 겹침과 서식 배치는 사용자가 직접 확인해야 합니다.

사용자가 확인한 파일:

```text
renderers/hwpx_renderer/output/mapped_safe_one_page_report_poc.hwpx
renderers/hwpx_renderer/output/mapped_missing_project_plan_poc.hwpx
renderers/hwpx_renderer/output/mapped_missing_result_report_poc.hwpx
renderers/hwpx_renderer/output/mapped_approved_review_report_poc.hwpx
```

사용자 확인 결과:

- 결과: 올클리어
- 특이사항: 없음
- 추가 수정 필요 항목: 없음

확인 항목:

| 확인 | 항목 | 기준 |
|---|---|---|
| [x] | 파일 열림 | 한컴에서 정상 열림 |
| [x] | 글자 겹침 | 제목과 본문에 겹침 없음 |
| [x] | 항목 순서 | 보고서 항목 순서 정상 |
| [x] | 줄바꿈 | 여러 줄 본문이 문단 단위로 보임 |
| [x] | bullet 표기 | 내용 앞 `-` 표기 일관성 |
| [x] | placeholder 잔여 | 남은 `{{placeholder}}` 없음 |
| [x] | 확인 필요값 | `[확인 필요]`가 실제값처럼 보이지 않음 |
| [x] | 민감정보 | 실제 개인정보, 기관정보, 문서번호 없음 |

이상 발견 시 다음 형식으로 보고합니다.

```text
파일명:
항목 번호:
증상:
```

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX 원본 파일 추가 없음
- API, Make.com, Email 자동화 코드 추가 없음

## 결론

Phase 2 수동 리허설 1회는 Codex 검증과 사용자 한컴 수동 검수를 모두 통과했습니다.

다음 단계는 이 완료 상태를 기준으로 Phase 2 최소 PoC의 반복 운영 기준과 다음 최소 개선 후보를 정리하는 것입니다.
