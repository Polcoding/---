# Phase 3 외부 연동 구현 범위 승인 판단

## 목적

Phase 3에서 외부 연동 구현 범위를 실제 코드 작성 단계로 승인할 수 있는지 문서 기준으로 판단합니다.

이 문서는 구현 지시서가 아닙니다. 실제 OpenAI API 호출, Make.com 시나리오 작성, GmailㆍOutlookㆍSMTP 연동, 실제 이메일 자동 발송, 실제 계정 연결, 실제 수신자 지정, 실제 첨부 전송은 계속 금지합니다.

## 기준 문서

- `docs/101_phase2_repeat_operation_log_template.md`
- `docs/111_phase3_entry_safety_gate.md`
- `docs/115_phase3_external_integration_hold_criteria.md`
- `docs/116_phase3_log_and_audit_trace_criteria.md`
- `docs/117_phase3_test_account_and_test_data_criteria.md`
- `docs/118_phase3_source_blocking_and_deidentified_input_check_procedure.md`
- `docs/119_phase3_user_preview_and_human_approval_integration.md`
- `docs/120_phase3_no_send_dry_run_criteria.md`
- `docs/122_phase3_closeout_and_phase4_entry_decision.md`
- `checklists/phase3_external_integration_scope_approval_judgment_checklist.md`
- `checklists/before_automation_checklist.md`

## 판단 결론

현재 저장소 기준으로 외부 연동 실제 구현은 승인하지 않습니다.

판단:

- no-send dry-run 기준은 문서로 정리되었지만, 실제 구현 승인과 다릅니다.
- 실제 계정, 실제 수신자, 실제 첨부, 실제 API 요청, 실제 Make.com 실행은 모두 현재 범위 밖입니다.
- 조직 보안정책, 개인정보 처리 기준, 비용 기준, 계정 권한, 로그 보관 기준은 저장소만으로 확정할 수 없습니다.
- 실제 구현이 필요하더라도 사용자와 조직의 별도 명시 승인이 먼저 필요합니다.
- 이번 단계에서는 코드, fixture, routing, HWPX payload, output을 변경하지 않습니다.

따라서 현재 상태는 `implementation_scope_status = 보류`입니다.

## 상태 구분

| 구분 | 현재 판단 | 비고 |
|---|---|---|
| Phase 3 문서 기준 검토 | 완료 | 안전 게이트, preview, 로그, 테스트 데이터, no-send 기준 정리 |
| no-send dry-run 기준 | 완료 | 실제 전송 없는 상태 점검 기준 |
| 실제 외부 연동 구현 승인 | 보류 | 별도 명시 승인 전까지 코드 작성 금지 |
| 실제 계정 연결 승인 | 보류 | 테스트 계정도 조건 충족 전 연결 금지 |
| 실제 발송 승인 | 보류 | 사람이 별도 실무 절차에서 판단 |
| 실제 결재ㆍ계약ㆍ예산 집행 승인 | 범위 밖 | 자동화 대상 아님 |

## 현재 허용 범위

현재 허용되는 범위는 문서 기준 검토와 placeholder 기반 로컬 PoC 유지에 한정합니다.

| 범위 | 허용 여부 | 기준 |
|---|---|---|
| Phase 3 기준 문서 보강 | 허용 | 실제값 없이 문서와 체크리스트만 수정 |
| 외부 연동 후보의 위험 분류 | 허용 | 실제 요청, 실제 계정, 실제 데이터 없이 범주만 판단 |
| Email 초안 렌더러 유지 | 허용 | 로컬 placeholder 기반 초안, 실제 발송 없음 |
| HWPX 로컬 렌더러 유지 | 허용 | ignored output과 로컬 템플릿, 사람 preview 전제 |
| 반복 운영 로그 양식 보강 | 허용 | 실제 원문과 개인정보 없이 상태값만 기록 |

## 계속 보류할 범위

다음 범위는 계속 보류합니다.

| 범위 | 판단 | 이유 |
|---|---|---|
| OpenAI API 실제 호출 코드 | 보류 | 입력 비식별, 키 관리, 비용, 로그 기준의 외부 확인 필요 |
| Make.com 실제 시나리오 | 보류 | 외부 서비스로 데이터 이동 가능성 |
| GmailㆍOutlookㆍSMTP 연동 | 보류 | 실제 발송, 실제 수신자, 실제 첨부 위험 |
| 실제 업무 계정 연결 | 보류 | 조직 승인과 권한 범위 확인 필요 |
| 실제 수신자 지정 | 보류 | 발송 자동화로 오인될 수 있음 |
| 실제 첨부 포함 | 보류 | 실제 원문 또는 내부자료 유출 위험 |
| 실제 HWPX 원본 처리 | 보류 | 저장소 밖에서만 비식별 복사본 후보 검토 |
| API 키ㆍ토큰ㆍ환경변수 예시 작성 | 금지 | 인증정보 저장 위험 |

## 구현 검토 전 필수 조건

실제 구현 검토 단계로 넘어가려면 최소한 다음 조건이 모두 별도 확인되어야 합니다.

| 조건 | 기준 |
|---|---|
| 사용자 명시 승인 | 어떤 연동을 어떤 범위로 검토할지 별도 승인 |
| 조직 보안 검토 | 개인정보, 외부 서비스, 로그, 계정 정책 확인 |
| 개인정보 처리 기준 | 실제 원문 차단과 비식별 입력 기준 확인 |
| 최신 공식 문서 확인 | API, Make.com, Email 서비스의 최신 공식 문서 확인 |
| 테스트 계정 기준 | 실제 업무 계정과 분리된 테스트 범위 확인 |
| 테스트 데이터 기준 | placeholder 또는 A/B등급 비식별 데이터만 사용 |
| no-send dry-run 통과 | 실제 전송 없이 상태와 보류 조건 확인 |
| 로그 기준 | 실제 원문, 실제 개인정보, 실제 계정명 저장 금지 |
| 비밀정보 관리 | API 키, 토큰, 인증정보 저장 방식 별도 검토 |
| 비용ㆍquotaㆍrate limit 기준 | 비용 한도와 중단 기준 확인 |
| rollback 기준 | 오작동 시 중단ㆍ폐기ㆍ사람 검토 절차 확인 |

위 조건 중 하나라도 `[확인 필요]`이면 실제 구현은 보류합니다.

## 연동 후보별 판단

| 후보 | 현재 판단 | 다음에 가능한 일 |
|---|---|---|
| OpenAI API | 구현 보류 | 별도 승인 전까지 문서 기준 위험 검토만 가능 |
| Make.com | 구현 보류 | 실제 시나리오 작성 없이 흐름도와 보류 조건만 유지 |
| Email 자동 발송 | 구현 보류 | Email 초안 preview 기준만 유지 |
| Email 초안 렌더러 | 유지 가능 | 실제 수신자와 첨부 없이 placeholder 초안만 |
| HWPX 로컬 렌더러 | 유지 가능 | Git 제외 output과 사람 preview 기준만 |

## 기록 권장값

외부 연동 구현 범위 판단 결과는 실제값 없이 다음처럼 기록합니다.

| 항목 | 값 |
|---|---|
| implementation_scope_status | `보류` |
| external_transfer | `전송하지 않음` |
| external_request_created | `생성하지 않음` |
| account_connected | `연결하지 않음` |
| real_recipient_used | `사용하지 않음` |
| real_attachment_used | `사용하지 않음` |
| code_change_required | `아니오` |
| next_action | `Phase 4 문서 템플릿 안정화 진입 여부 판단` |

## 코드 변경 판단

이번 판단은 문서 기준으로 충분합니다.

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

다음 단계는 Phase 4 문서 템플릿 안정화 진입 여부를 문서로 판단하는 것입니다.

검토 질문:

- Phase 4를 HWPX 보고서 4종 문서 템플릿 안정화로 제한할 수 있는지
- 실제 양식 원본 없이 placeholder와 manifest 기준만으로 점검 가능한지
- 누락값, 공통 placeholder, style profile, local template policy가 서로 충돌하지 않는지
- README, AGENTS, `tasks/NEXT_STEP.md`가 실제 구현 보류 상태를 충분히 보여주는지

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

현재 저장소 기준으로 외부 연동 실제 구현은 승인하지 않고 보류합니다.

Phase 3 마무리 판단은 `docs/122_phase3_closeout_and_phase4_entry_decision.md`에 후속 반영했습니다. 다음 단계는 실제 구현이 아니라 Phase 4 문서 템플릿 안정화 진입 여부를 문서로 판단하는 것입니다.
