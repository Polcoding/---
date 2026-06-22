# Phase 3 외부 연동 필요성과 보류 기준

## 목적

Phase 3에서 API, Make.com, Email 연동을 바로 구현하지 않고 보류해야 하는 기준을 정리합니다.

이 문서는 구현 지시서가 아닙니다. 실제 OpenAI API 호출, Make.com 시나리오 작성, GmailㆍOutlookㆍSMTP 연동, 실제 이메일 자동 발송은 계속 금지합니다.

## 기준 문서

- `docs/06_future_architecture.md`
- `docs/07_make_api_next_steps.md`
- `docs/62_security_filter_requirements.md`
- `docs/82_phase2_minimal_operation_flow.md`
- `docs/83_phase2_user_input_and_manual_operation_checkpoints.md`
- `docs/100_phase2_repeat_operation_criteria.md`
- `docs/101_phase2_repeat_operation_log_template.md`
- `docs/111_phase3_entry_safety_gate.md`
- `docs/112_phase3_external_hwpx_and_manual_preview_criteria.md`
- `docs/114_phase3_operating_docs_integrated_review.md`
- `docs/116_phase3_log_and_audit_trace_criteria.md`
- `docs/117_phase3_test_account_and_test_data_criteria.md`
- `docs/118_phase3_source_blocking_and_deidentified_input_check_procedure.md`
- `docs/119_phase3_user_preview_and_human_approval_integration.md`
- `checklists/before_automation_checklist.md`

## 검토 결론

현재 저장소 기준으로 외부 연동 구현은 아직 진행하지 않습니다.

판단:

- HWPX 보고서 4종 로컬 PoC와 문서 기준은 안정화되었지만, 운영 계정ㆍ외부 서비스ㆍ실제 입력이 연결되는 단계는 별도 위험을 만듭니다.
- 감사 추적, 테스트 계정, 테스트 데이터 기준은 문서화되었습니다.
- 실제 원문 차단과 비식별 입력 확인 절차는 `docs/118_phase3_source_blocking_and_deidentified_input_check_procedure.md`에 문서 기준으로 반영했습니다.
- 사용자 preview와 사람 승인 지점은 `docs/119_phase3_user_preview_and_human_approval_integration.md`에 문서 기준으로 반영했습니다.
- Email은 보조 초안 작성 대상이며, HWPX 보고서 자동화보다 우선하지 않습니다.
- API, Make.com, Email 연동은 필요성을 문서 기준으로 검토할 수 있지만, 구현ㆍ테스트 계정 연결ㆍ실제 발송은 아직 범위 밖입니다.

## 연동별 현재 판단

| 연동 후보 | 현재 판단 | 이유 |
|---|---|---|
| OpenAI API | 구현 보류 | 실제 입력 차단ㆍ키 관리ㆍ비용 관리ㆍ보안 승인 기준이 더 필요 |
| Make.com | 구현 보류 | 외부 서비스로 입력과 output이 이동하므로 실제 원문 차단과 비식별 입력 확인 절차가 먼저 필요 |
| Email 자동화 | 구현 보류 | 실제 발송, 수신자 지정, 첨부 자동 포함 위험이 있어 초안 작성까지만 유지 |
| Email 초안 렌더러 | 유지 가능 | 로컬 placeholder 기반 초안 렌더링 PoC이며 실제 발송이 아님 |
| HWPX 로컬 렌더러 | 유지 가능 | ignored output과 로컬 템플릿 기준으로 사람 수동 검수 전제 |

## 구현 전 필수 보류 조건

다음 중 하나라도 미충족이면 외부 연동 구현을 시작하지 않습니다.

| 조건 | 기준 |
|---|---|
| 실제 원문 차단 | 실제 공문ㆍ보고서 원문을 API, Make.com, Email 입력으로 보내지 않음 |
| 비식별 입력 | A/B등급 placeholder 기반 입력만 검토 |
| C/D등급 제외 | C등급은 내부 참고만, D등급은 외부 처리 금지 |
| 보안 검토 | 사람 보안 검토 전 `needs_security_review` 입력은 외부 전송 금지 |
| 차단 상태 | `blocked` 입력은 외부 전송 금지 |
| 사용자 preview | HWPX output은 사람이 열람하고 확인 |
| 로그 기준 | 로그에 실제 원문, 개인정보, 실제 기관명, 실제 문서번호를 저장하지 않음 |
| 발송 경계 | 초안 생성과 실제 발송을 분리 |
| 계정 연결 | 실제 업무 계정 연결 전 별도 승인 필요 |
| 키 관리 | API 키, 토큰, 인증정보 예시값을 저장소에 쓰지 않음 |
| 비용 관리 | 비용 기준과 사용량 모니터링 방식 별도 검토 |
| 공식 문서 확인 | 실제 도입 전 최신 공식 문서와 조직 정책 확인 |

## 절대 구현 금지 범위

현재 단계에서 금지합니다.

- 실제 OpenAI API 호출 코드
- Make.com 실제 시나리오 구성
- Gmail, Outlook, SMTP 연동
- 실제 이메일 자동 발송
- 실제 업무 계정 연결
- 실제 원문 또는 개인정보를 외부 서비스로 전송
- 실제 HWPX 원본을 외부 서비스에 업로드
- API 키, 토큰, 인증정보 예시값 작성
- 내부망 자료를 외부 서비스로 보내는 절차 작성
- 자동 결재, 계약, 업체 선정, 예산 집행, 법률 판단

## 문서 기준으로만 가능한 검토

현재 허용되는 작업은 다음에 한정합니다.

- 외부 연동 전 안전 게이트 문서화
- 입력ㆍ출력 데이터 흐름을 placeholder로 설명
- 초안 생성과 실제 발송의 경계 정리
- 로그와 감사 추적에서 저장 가능한 항목과 금지 항목 정리
- 테스트 계정 사용 여부를 문서 기준으로 검토
- 실제 구현 전 사용자 승인 지점을 정의

## 외부 연동 검토 순서

외부 연동이 필요하다고 판단되더라도 다음 순서를 먼저 거칩니다.

1. 외부 연동 보류 기준 확인
2. 로그와 감사 추적 기준 문서화
3. 테스트 계정ㆍ테스트 데이터 기준 문서화
4. 실제 원문 차단과 비식별 입력 확인 절차 문서화
5. 사용자 preview와 사람 승인 지점 문서화
6. 외부 전송 없는 no-send dry-run 기준 문서화
7. 구현 범위 승인 여부 별도 판단

현재 2번 기준은 `docs/116_phase3_log_and_audit_trace_criteria.md`에 문서 기준으로 반영했습니다.

현재 3번 기준은 `docs/117_phase3_test_account_and_test_data_criteria.md`에 문서 기준으로 반영했습니다.

현재 4번 기준은 `docs/118_phase3_source_blocking_and_deidentified_input_check_procedure.md`에 문서 기준으로 반영했습니다.

현재 5번 기준은 `docs/119_phase3_user_preview_and_human_approval_integration.md`에 문서 기준으로 반영했습니다.

## 현재 부족한 기준

외부 연동 구현 전에 다음 기준은 더 구체화해야 합니다.

| 기준 | 현재 판단 |
|---|---|
| 감사 로그 필드 | `docs/116`에 저장 허용 항목과 금지 항목 기준 반영 |
| 로그 보관 기간 | `docs/116`에 임의 확정 금지, 조직 정책 확인 필요로 정리 |
| 테스트 계정 범위 | `docs/117`에 실제 계정 연결 금지와 테스트 계정 최소 조건 반영 |
| 실제 업무 계정 연결 승인 | `docs/117`에 별도 승인 전 연결 금지 기준 반영 |
| 외부 서비스 장애 시 중단 기준 | `docs/117`에 장애ㆍrate limitㆍquota 보류 기준 반영 |
| 비용 한도와 모니터링 | `docs/117`에 비용 기준 미확정 시 보류 기준 반영 |
| 실제 원문 차단 절차 | `docs/118`에 원문 의심 기준과 중단 기준 반영 |
| 비식별 입력 확인 절차 | `docs/118`에 A/B/C/D 등급 확인 절차 반영 |
| 사용자 preview와 사람 승인 지점 | `docs/119`에 preview 종류와 승인 상태 경계 반영 |
| no-send dry-run 기준 | 다음 단계에서 실제 전송 없는 검토 기준 문서화 필요 |

## 다음 작업 후보

다음 단계는 외부 연동 구현이 아니라 외부 전송 없는 no-send dry-run 기준을 문서로 점검하는 것입니다.

검토 질문:

- 외부 전송 없이 어떤 상태값과 로그만 확인할지
- no-send dry-run에서 실제 계정, 실제 수신자, 실제 API 호출을 어떻게 계속 제외할지
- `전송하지 않음` 상태를 반복 운영 로그에 어떻게 표시할지
- 다음 단계에서도 코드 변경 없이 문서 기준만 보강할 수 있는지

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX 원본 파일 추가 없음
- Email, API, Make.com 연동 구현 없음

## 결론

현재 단계에서는 외부 연동 필요성은 검토할 수 있지만 실제 구현은 보류합니다.

다음 단계는 외부 전송 없는 no-send dry-run 기준을 문서로 점검하는 것입니다.
