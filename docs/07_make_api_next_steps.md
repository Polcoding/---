# Make.com 및 API 연동 전 준비사항

## 지금 API 연동하지 않는 이유

현재 단계는 안전한 테스트 기준을 만드는 단계입니다. API 연동을 먼저 구현하면 민감정보 입력, 자동 발송, 로그 저장, 권한 관리 문제가 충분히 정리되지 않은 상태에서 운영 위험이 커질 수 있습니다.

Phase 3와 Phase 4 진입 판단의 최신 기준은 `docs/115_phase3_external_integration_hold_criteria.md`, `docs/116_phase3_log_and_audit_trace_criteria.md`, `docs/117_phase3_test_account_and_test_data_criteria.md`, `docs/118_phase3_source_blocking_and_deidentified_input_check_procedure.md`, `docs/119_phase3_user_preview_and_human_approval_integration.md`, `docs/120_phase3_no_send_dry_run_criteria.md`, `docs/121_phase3_external_integration_scope_approval_judgment.md`, `docs/122_phase3_closeout_and_phase4_entry_decision.md`, `docs/123_phase4_template_stabilization_entry_judgment.md`를 따릅니다. 현재도 실제 OpenAI API 호출, Make.com 실제 시나리오, GmailㆍOutlookㆍSMTP 연동, 실제 이메일 자동 발송은 구현하지 않습니다.

## 자동화 전 필요한 조건

- 테스트 케이스 5개 이상 통과
- 위험 요청 처리 기준 검증
- 비식별화 규칙 검증
- 실제 원문 업로드 금지 원칙 확인
- 초안 회신까지만 허용하는 정책 정리
- 자동 외부 발송 금지 원칙 정리
- 조직 보안정책 검토
- 개인정보 담당자 또는 보안 담당자 검토
- Phase 3 안전 게이트 확인
- 저장소 밖 HWPX 취급 기준 확인
- 사용자 수동 preview 기준 확인
- 반복 운영 로그와 감사 추적 기준 확인
- 테스트 계정과 테스트 데이터 기준 확인
- 실제 원문 차단과 비식별 입력 확인 절차 확인
- 사용자 preview와 사람 승인 지점 확인
- 외부 전송 없는 no-send dry-run 기준 확인
- 외부 연동 구현 범위 승인 판단 확인
- Phase 3 마무리 판단 및 Phase 4 진입 여부 확인
- Phase 4 문서 템플릿 안정화 진입 판단 확인

## 이메일 자동화 전 체크리스트

- 수신자 자동 지정 금지 여부 확인
- 첨부파일 자동 포함 금지 여부 확인
- 초안과 실제 발송의 경계 명확화
- 사용자가 발송 전 본문을 확인하는 화면 필요
- 민감정보 포함 시 자동 중단하는 규칙 필요
- 발송 로그에 원문 민감정보가 남지 않도록 설계

## OpenAI API 호출 전 보안 점검

- API에 전달되는 입력이 비식별화되어 있는지 확인
- high 위험도 요청은 API 호출 전에 차단
- API 키 관리 정책 수립
- 접근 권한과 호출 로그 관리 방식 수립
- 비용 사용량 모니터링 방식 수립
- 공식 문서와 조직 정책 확인

## Make.com 시나리오 예상 흐름

```text
입력 수신
→ 입력 정규화
→ 보안 위험도 분류
→ 비식별화
→ 초안 생성 요청
→ 사용자에게 초안 회신
→ 사용자 검토
→ 사람 승인 후 별도 실무 처리
```

## 금지 원칙

- 실제 발송 자동화는 이번 단계에서 금지합니다.
- 초안 회신까지만 허용합니다.
- API 키나 인증 토큰 예시 값을 문서에 쓰지 않습니다.
- 내부망 자료를 외부 서비스로 보내는 방법을 안내하지 않습니다.
- 실제 업무 계정 연결은 별도 승인 전까지 금지합니다.
- 실제 원문 또는 개인정보를 외부 서비스로 전송하지 않습니다.

## 비용 관련 주의

API 사용 비용과 ChatGPT 구독은 별도일 수 있습니다. 실제 도입 전에는 공식 문서, 조직 예산 기준, 비용 관리 방식을 확인해야 합니다.

## 실제 도입 전 확인 문구

실제 운영 전에는 OpenAI와 Make.com의 최신 공식 문서, 조직 내부 보안정책, 개인정보 처리 기준, 비용 관리 기준을 반드시 확인해야 합니다.

## 현재 다음 단계

현재 다음 단계는 실제 연동 구현이 아니라 HWPX 보고서 4종 template manifest와 공통 placeholder 정합성을 문서로 점검하는 것입니다.
