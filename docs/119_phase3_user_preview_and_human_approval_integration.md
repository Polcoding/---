# Phase 3 사용자 preview와 사람 승인 지점 통합 기준

## 목적

Phase 3에서 HWPX preview, 외부 전송 전 preview, Email 초안 preview의 사람 확인 지점을 구분하고, 승인 상태가 실제 결재ㆍ발송ㆍ계약ㆍ예산 집행 승인이 아님을 명확히 정리합니다.

이 문서는 구현 지시서가 아닙니다. 실제 OpenAI API 호출, Make.com 시나리오, GmailㆍOutlookㆍSMTP 연동, 실제 이메일 자동 발송, 실제 계정 연결은 계속 금지합니다.

## 기준 문서

- `docs/83_phase2_user_input_and_manual_operation_checkpoints.md`
- `docs/101_phase2_repeat_operation_log_template.md`
- `docs/111_phase3_entry_safety_gate.md`
- `docs/112_phase3_external_hwpx_and_manual_preview_criteria.md`
- `docs/115_phase3_external_integration_hold_criteria.md`
- `docs/116_phase3_log_and_audit_trace_criteria.md`
- `docs/117_phase3_test_account_and_test_data_criteria.md`
- `docs/118_phase3_source_blocking_and_deidentified_input_check_procedure.md`
- `docs/120_phase3_no_send_dry_run_criteria.md`
- `docs/121_phase3_external_integration_scope_approval_judgment.md`
- `docs/122_phase3_closeout_and_phase4_entry_decision.md`
- `checklists/before_automation_checklist.md`

## 검토 결론

사용자 preview와 사람 승인 지점은 문서 기준으로 통합할 필요가 있습니다.

현재 결론:

- HWPX preview는 로컬 HWPX output의 서식과 placeholder 치환 상태를 사람이 확인하는 단계입니다.
- 외부 전송 전 preview는 실제 외부 서비스로 보내도 되는 입력인지 최종 보류 조건을 확인하는 단계입니다.
- Email 초안 preview는 메일 본문, 수신자 placeholder, 첨부 여부, 발송 경계를 사람이 확인하는 단계입니다.
- 현재 기본값은 `외부 전송하지 않음`입니다.
- 사람 승인 상태는 초안 생성 흐름의 검수 상태일 뿐 실제 결재, 발송, 계약, 업체 선정, 예산 집행, 법률 판단 승인이 아닙니다.
- 이번 단계에서는 문서와 체크리스트만 보강하며 코드 변경은 필요하지 않습니다.

## preview 종류 구분

| preview 종류 | 확인 시점 | 확인 주체 | 통과 의미 | 통과해도 금지되는 것 |
|---|---|---|---|---|
| HWPX preview | 로컬 HWPX output 생성 후 | 사용자 또는 지정 검토자 | 한컴에서 열림, 겹침 없음, placeholder 잔여 없음 | 실제 결재, 실제 제출, 실제 기관 양식 Git 추가 |
| 외부 전송 전 preview | API, Make.com, Email 같은 외부 전송 후보 검토 전 | 사용자와 보안 검토자 | 실제 원문 없음, A/B 후보, 전송 보류 조건 없음 | 실제 전송 자동 실행, 실제 계정 연결 |
| Email 초안 preview | Email 초안 본문을 사람이 보기 전 | 사용자 또는 지정 검토자 | 초안 문체, 수신자 placeholder, 첨부 금지 확인 | 자동 발송, 실제 수신자 지정, 실제 첨부 전송 |

세 preview는 서로 대체하지 않습니다. HWPX preview를 통과해도 외부 전송 전 preview를 생략할 수 없고, Email 초안 preview를 통과해도 실제 발송 승인이 된 것이 아닙니다.

## HWPX preview 확인 지점

[사용자 확인 필요]

HWPX preview는 다음 조건을 확인합니다.

HWPX 보고서 4종의 세부 gap log 기준은 `docs/127_hwpx_manual_preview_gap_log_criteria.md`를 따릅니다.

실제 HWPX 수동 preview 재개 여부는 후속 기준인 `docs/150_manual_preview_resume_gate.md`를 먼저 확인합니다.

| 확인 | 기준 |
|---|---|
| 파일 열림 | 한컴에서 정상 열림 |
| 글자 겹침 | 제목, 번호, 본문, 표 영역에서 겹침 없음 |
| 항목 순서 | 문서 유형별 항목 순서 정상 |
| 줄바꿈 | 여러 줄 본문이 문단 단위로 분리됨 |
| bullet 표기 | 내용 앞 기호 표기 일관성 |
| placeholder 잔여 | 남은 `{{placeholder}}` 없음 |
| missing_fields | 본문 실제값이 아니라 검토용 목록으로 보임 |
| 보안 | 실제 개인정보, 기관정보, 문서번호 없음 |

HWPX preview 통과는 로컬 산출물 검수 통과입니다. 실제 업무 제출이나 내부 결재 완료가 아닙니다.

## 외부 전송 전 preview 확인 지점

[사용자 확인 필요]

현재 단계에서는 실제 외부 전송을 하지 않습니다. 향후 별도 승인 후에도 외부 전송 후보를 검토하려면 다음 조건을 모두 확인해야 합니다.

| 확인 | 기준 |
|---|---|
| 실제 원문 없음 | 원문 전체, 발췌, 원문 요약 없음 |
| 개인정보 없음 | 이름, 연락처, 이메일, 주소, 고유식별정보 없음 |
| 기관정보 없음 | 실제 기관명, 관서명, 부서명, 담당자명 없음 |
| 문서번호 없음 | 문서번호, 민원번호, 사건번호, 접수번호 없음 |
| 내부정보 없음 | 내부망, 계정, 권한, 장비, 차량, 운영정보 없음 |
| 보안등급 | A/B 후보만 검토 |
| 상태 | `ready_for_draft` 또는 허용된 `needs_more_input` |
| preview | HWPX 또는 초안 preview 결과가 `통과`로 확인됨 |
| 로그 | 실제값 없이 상태와 범주만 기록 |
| 계정 | 실제 업무 계정 연결 없음 |
| 비용ㆍ권한 | 비용 한도, 권한 범위, 로그 기준이 `[확인 필요]`이면 보류 |

하나라도 확인되지 않으면 외부 전송을 보류합니다.

## Email 초안 preview 확인 지점

[사용자 확인 필요]

Email 초안은 실제 발송이 아니라 사람이 읽고 수정할 초안입니다.

| 확인 | 기준 |
|---|---|
| 수신자 | 실제 수신자 자동 지정 없음, placeholder 유지 |
| 참조자 | 실제 참조자 자동 지정 없음 |
| 첨부 | 실제 HWPX, 실제 원문, 실제 내부자료 자동 첨부 없음 |
| 본문 | 공문체가 아니라 정중한 실무 메일체 |
| 표현 | 계약, 발송, 예산 집행이 확정된 표현 없음 |
| 민감정보 | 개인정보, 기관정보, 문서번호 없음 |
| 발송 경계 | 사람이 별도 확인하기 전 자동 발송 금지 |

Email 초안 preview 통과는 메일 초안의 문장과 위험 표현을 검수한 상태일 뿐, 실제 발송 승인이 아닙니다.

## 승인 상태와 실제 업무 승인의 경계

현재 문서에서 말하는 승인은 초안 생성 흐름의 검수 상태입니다.

| 표현 | 의미 | 실제 업무 승인 여부 |
|---|---|---|
| `preview 통과` | 사람이 초안 또는 output을 확인함 | 아님 |
| `초안 검수 통과` | 초안의 문체, 누락값, 보안 표시를 확인함 | 아님 |
| `외부 전송 후보 검토` | 전송 가능성을 문서 기준으로 검토함 | 아님 |
| `사람 승인 필요` | 자동 처리하지 말고 사람이 판단해야 함 | 아님 |
| 실제 결재 승인 | 조직 내부 결재 절차 완료 | 이 저장소 범위 밖 |
| 실제 발송 승인 | 수신자, 본문, 첨부, 계정 확인 후 사람이 별도 발송 결정 | 이 저장소 범위 밖 |
| 계약ㆍ예산 집행 승인 | 계약, 업체 선정, 예산 집행 권한자가 별도 결정 | 이 저장소 범위 밖 |

승인 상태를 자동 발송, 자동 결재, 자동 계약, 자동 예산 집행 조건으로 사용하지 않습니다.

## 외부 전송 전 최종 보류 조건

다음 중 하나라도 해당하면 외부 전송은 보류합니다.

| 보류 조건 | 처리 |
|---|---|
| 실제 원문 또는 실제값 의심 | `blocked` 또는 `needs_security_review` |
| C/D등급 후보 | 외부 처리 후보 제외 |
| `needs_security_review` | 사람 보안 검토 전 외부 전송 금지 |
| `blocked` | 처리 중단, 비식별 재작성 요청 |
| `template_required` | 로컬 템플릿 준비 전 HWPX output 생성 시도 금지 |
| `remaining_placeholders` 있음 | preview 중단 |
| HWPX 또는 output Git 제외 실패 | 작업 중단, `.gitignore`와 파일 위치 확인 |
| 테스트 계정ㆍ권한ㆍ비용 기준 미확정 | 외부 연동 보류 |
| 사용자 preview 미완료 | 외부 전송 보류 |
| 사람 승인 상태 불명확 | 외부 전송 보류 |

최종 보류 조건은 `docs/101_phase2_repeat_operation_log_template.md`의 외부 전송 전 확인 섹션과 `docs/116_phase3_log_and_audit_trace_criteria.md`의 로그 기준에 실제값 없이 기록합니다.

## 기록 기준

기록 가능한 항목:

- preview 종류
- preview 상태: `통과` / `보류` / `실패` / `[사용자 확인 필요]`
- 승인 상태: `초안 검수 통과` / `보류` / `반려` / `[사용자 확인 필요]`
- 외부 전송 여부: 기본값 `전송하지 않음`
- 보류 사유 범주
- 다음 조치: `재검토` / `비식별 재작성` / `사람 보안 검토` / `[확인 필요]`

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

## 코드 변경 판단

이번 통합 기준은 문서 기준으로 충분합니다.

변경하지 않는 항목:

- `normalizers/`
- `renderers/`
- `examples/json/`
- routing fixture
- HWPX payload mapper
- HWPX renderer output
- local HWPX template
- API, Make.com, Email 연동 코드

## 다음 작업 후보

후속 Phase 4 문서 템플릿 안정화 기준은 `docs/123`~`docs/127`에 반영했고, 저장소 밖 실제 양식 후보 수동 절차와 보류 조건은 `docs/128`에 반영했습니다. 현재 최신 기준은 비식별 작업 복사본 준비가 명시되기 전까지 문서 기반 검증 상태를 유지하고, 수동 preview는 `docs/150_manual_preview_resume_gate.md` 조건을 만족할 때만 재개하는 것입니다.

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
- API 키, 토큰, 인증정보 예시값 추가 없음
- Email, API, Make.com 연동 구현 없음

## 결론

사용자 preview와 사람 승인 지점은 문서 기준으로 통합했습니다.

HWPX preview, 외부 전송 전 preview, Email 초안 preview는 각각 별도 사람 확인 지점으로 유지하며, 어떤 preview 통과도 실제 결재ㆍ발송ㆍ계약ㆍ예산 집행 승인으로 해석하지 않습니다.
