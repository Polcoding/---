# Phase 3 외부 전송 없는 no-send dry-run 기준

## 목적

Phase 3에서 실제 API 호출, Make.com 실행, Email 발송, 실제 계정 연결 없이 외부 전송 전 흐름을 어디까지 문서 기준으로 점검할 수 있는지 정리합니다.

이 문서는 구현 지시서가 아닙니다. 실제 OpenAI API 호출, Make.com 시나리오, GmailㆍOutlookㆍSMTP 연동, 실제 이메일 자동 발송, 실제 계정 연결, 실제 수신자 지정, 실제 첨부 생성은 계속 금지합니다.

## 기준 문서

- `docs/101_phase2_repeat_operation_log_template.md`
- `docs/111_phase3_entry_safety_gate.md`
- `docs/115_phase3_external_integration_hold_criteria.md`
- `docs/116_phase3_log_and_audit_trace_criteria.md`
- `docs/117_phase3_test_account_and_test_data_criteria.md`
- `docs/118_phase3_source_blocking_and_deidentified_input_check_procedure.md`
- `docs/119_phase3_user_preview_and_human_approval_integration.md`
- `docs/121_phase3_external_integration_scope_approval_judgment.md`
- `docs/122_phase3_closeout_and_phase4_entry_decision.md`
- `checklists/before_automation_checklist.md`

## 검토 결론

no-send dry-run 기준은 문서로 구체화할 필요가 있습니다.

현재 결론:

- no-send dry-run은 실제 외부 전송을 하지 않는 점검 절차입니다.
- 외부 전송 여부는 기본값 `전송하지 않음`으로 기록합니다.
- 실제 API 요청, Make.com 실행, Email 발송, 실제 계정 연결, 실제 수신자 지정, 실제 첨부 포함은 모두 제외합니다.
- no-send dry-run 통과는 실제 연동 준비 완료, 실제 발송 승인, 실제 결재 승인, 계약ㆍ예산 집행 승인으로 해석하지 않습니다.
- 이번 단계에서는 문서와 체크리스트만 보강하며 코드 변경은 필요하지 않습니다.

## no-send dry-run의 의미

| 구분 | 의미 |
|---|---|
| no-send | 외부 서비스로 실제 데이터를 전송하지 않음 |
| dry-run | 실행 후보 상태와 보류 조건만 문서 기준으로 점검 |
| 확인 대상 | 상태값, 보류 조건, preview 상태, 승인 상태, 로그 항목 |
| 제외 대상 | 실제 요청, 실제 응답, 실제 발송, 실제 계정, 실제 첨부 |

no-send dry-run은 실제 연동 테스트가 아니라 외부 전송 전 안전 절차가 빠짐없이 준비되었는지 확인하는 문서 기준 점검입니다.

## 확인 가능한 항목

no-send dry-run에서 확인 가능한 항목은 실제값 없이 기록 가능한 상태와 범주에 한정합니다.

| 항목 | 허용 기록 형식 | 기준 |
|---|---|---|
| 문서 유형 | `one_page_report` 등 document_type | 실제 문서 제목 기록 금지 |
| 입력 유형 | `placeholder fixture` / `비식별 사용자 입력` / `[확인 필요]` | 실제 원문 기록 금지 |
| 보안등급 후보 | `A` / `B` / `[확인 필요]` | C/D 후보는 외부 처리 제외 |
| routing 상태 | `ready_for_draft` / `needs_more_input` / `needs_security_review` / `blocked` | 실제 본문 없이 상태만 기록 |
| renderer 상태 | `rendered` / `template_required` / `skipped` / `[확인 필요]` | output 내용 기록 금지 |
| preview 상태 | `통과` / `보류` / `실패` / `[사용자 확인 필요]` | 사람이 확인한 범주만 기록 |
| 승인 상태 | `초안 검수 통과` / `보류` / `반려` / `[사용자 확인 필요]` | 실제 결재나 발송 승인 아님 |
| 외부 전송 여부 | `전송하지 않음` | 현재 기본값 |
| 계정 연결 | `연결하지 않음` | 실제 계정명 기록 금지 |
| 수신자 지정 | `지정하지 않음` / `placeholder only` | 실제 수신자 기록 금지 |
| 첨부 포함 | `포함하지 않음` | 실제 파일명 기록 금지 |
| 다음 조치 | `보류` / `사람 검토` / `비식별 재작성` / `[확인 필요]` | 자동 처리로 쓰지 않음 |

## 확인할 수 없는 항목

no-send dry-run으로는 다음을 확인할 수 없습니다.

| 항목 | 이유 |
|---|---|
| 실제 API 인증 성공 | API 호출을 하지 않음 |
| 실제 Make.com 시나리오 실행 | Make.com 실행을 하지 않음 |
| 실제 Email 발송 성공 | 발송하지 않음 |
| 실제 수신자 도달 여부 | 실제 수신자를 지정하지 않음 |
| 실제 첨부 업로드 성공 | 실제 첨부를 포함하지 않음 |
| 실제 외부 서비스 로그 | 외부 서비스에 요청하지 않음 |
| 실제 비용 발생 여부 | 유료 호출 또는 실행을 하지 않음 |
| 실제 업무 계정 권한 | 계정을 연결하지 않음 |

위 항목은 no-send dry-run 통과 여부와 무관하게 별도 승인 전까지 계속 확인 대상이 아니라 보류 대상입니다.

## no-send dry-run 진행 조건

다음 조건을 모두 만족할 때만 no-send dry-run 검토 후보로 둡니다.

| 조건 | 기준 |
|---|---|
| 실제 원문 없음 | 원문 전체, 발췌, 요약 없음 |
| 개인정보 없음 | 이름, 연락처, 이메일, 주소, 고유식별정보 없음 |
| 기관정보 없음 | 실제 기관명, 관서명, 부서명, 담당자명 없음 |
| 문서번호 없음 | 문서번호, 민원번호, 사건번호, 접수번호 없음 |
| 보안등급 | A/B 후보 또는 `[확인 필요]` |
| 상태 | `ready_for_draft` 또는 허용된 `needs_more_input` |
| preview | 필요한 preview가 완료되었거나 `[사용자 확인 필요]`로 보류됨 |
| 외부 전송 | `전송하지 않음` |
| 계정 | 실제 계정 연결 없음 |
| 수신자ㆍ첨부 | 실제 수신자, 참조자, 첨부 없음 |

`[사용자 확인 필요]`가 남아 있으면 no-send dry-run을 통과로 기록하지 않고 보류로 둡니다.

HWPX 수동 preview가 필요한 경우에는 `docs/150_manual_preview_resume_gate.md` 조건 충족 전까지 no-send dry-run도 통과로 기록하지 않습니다.

## no-send dry-run 중단 또는 보류 조건

다음 중 하나라도 해당하면 no-send dry-run은 중단 또는 보류합니다.

| 조건 | 처리 |
|---|---|
| `blocked` | no-send dry-run 중단, 비식별 재작성 요청 |
| `needs_security_review` | 사람 보안 검토 전 보류 |
| `template_required` | 로컬 템플릿 준비 전 HWPX output 생성 시도 금지 |
| preview 미완료 | `[사용자 확인 필요]`로 보류 |
| 승인 상태 불명확 | 외부 전송 후보 검토 보류 |
| 실제 원문 또는 실제값 의심 | `blocked` 또는 `needs_security_review` |
| 실제 계정 연결 필요 | 보류 |
| 실제 수신자 또는 첨부 필요 | 보류 |
| 비용ㆍ권한ㆍ로그 기준 미확정 | 보류 |
| Git Changes에 HWPX 또는 output 표시 | 작업 중단, Git 제외 확인 |

no-send dry-run 보류는 실패가 아니라 외부 전송을 계속 하지 않는 안전 상태입니다.

## 로그 기록 기준

no-send dry-run 결과는 `docs/101_phase2_repeat_operation_log_template.md`와 `docs/116_phase3_log_and_audit_trace_criteria.md` 기준에 맞춰 실제값 없이 기록합니다.

권장 기록 항목:

| 항목 | 값 |
|---|---|
| no-send dry-run 상태 | `통과` / `보류` / `중단` / `[확인 필요]` |
| 외부 전송 여부 | `전송하지 않음` |
| 외부 요청 생성 여부 | `생성하지 않음` |
| 실제 계정 연결 여부 | `연결하지 않음` |
| 실제 수신자 지정 여부 | `지정하지 않음` |
| 실제 첨부 포함 여부 | `포함하지 않음` |
| 보류 사유 | 범주만 기록 |
| 다음 조치 | `사람 검토` / `비식별 재작성` / `문서 기준 보강` / `[확인 필요]` |

기록 금지 항목:

- 실제 원문
- 실제 원문 요약
- 실제 개인정보
- 실제 기관명, 관서명, 업체명, 담당자명
- 실제 문서번호, 민원번호, 사건번호
- 실제 이메일 수신자, 참조자, 첨부 파일명
- 실제 HWPX 원본 파일명
- 실제 API 요청ㆍ응답 전문
- 실제 계정명, 인증정보, 결제정보

## 통과 의미 제한

no-send dry-run 통과는 다음만 의미합니다.

- 외부 전송 없이 상태값과 보류 조건을 문서 기준으로 확인함
- 실제 원문과 개인정보를 기록하지 않음
- 실제 계정, 수신자, 첨부, API 요청을 만들지 않음
- `전송하지 않음` 상태를 로그에 남김

no-send dry-run 통과가 의미하지 않는 것:

- 실제 API 연동 준비 완료
- 실제 Make.com 시나리오 승인
- 실제 Email 발송 승인
- 실제 업무 계정 연결 승인
- 실제 결재, 계약, 업체 선정, 예산 집행 승인
- 실제 외부 서비스 보안 검토 완료

## 코드 변경 판단

이번 기준 정리는 문서 기준으로 충분합니다.

변경하지 않는 항목:

- `normalizers/`
- `renderers/`
- `examples/json/`
- routing fixture
- HWPX payload mapper
- HWPX renderer output
- local HWPX template
- API, Make.com, Email 연동 코드
- 실제 계정 또는 수신자 설정

## 다음 작업 후보

다음 단계는 실제 연동 구현이 아니라, 이미 정리된 Phase 4 문서 템플릿 안정화 기준과 수동 preview 재개 게이트를 유지 점검하는 것입니다.

검토 질문:

- Phase 4를 HWPX 보고서 4종 문서 템플릿 안정화로 제한할 수 있는지
- 실제 양식 원본 없이 placeholder와 manifest 기준만으로 점검 가능한지
- 누락값, 공통 placeholder, style profile, local template policy가 서로 충돌하지 않는지
- 다음 단계에서도 코드 변경 없이 문서 기준만 보강할 수 있는지

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX 원본 파일 추가 없음
- 실제 계정명, 이메일 주소, 결제정보 추가 없음
- 실제 수신자, 참조자, 첨부 파일명 추가 없음
- API 키, 토큰, 인증정보 예시값 추가 없음
- Email, API, Make.com 연동 구현 없음

## 결론

no-send dry-run 기준은 문서 기준으로 구체화했습니다.

현재 단계에서는 실제 외부 전송 없이 상태값, preview 상태, 승인 상태, 보류 조건, `전송하지 않음` 로그만 확인합니다. 실제 API 호출, Make.com 실행, Email 발송, 실제 계정 연결은 계속 보류합니다.

외부 연동 구현 범위 승인 판단은 `docs/121_phase3_external_integration_scope_approval_judgment.md`에 후속 반영했습니다.

Phase 3 마무리 판단은 `docs/122_phase3_closeout_and_phase4_entry_decision.md`에 후속 반영했습니다.
