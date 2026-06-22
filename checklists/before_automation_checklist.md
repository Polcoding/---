# 자동화 전 체크리스트

## 목적

Make.com 또는 OpenAI API 자동화 전 반드시 확인할 사항을 정리합니다.

## 체크 항목

| 완료 | 항목 |
|---|---|
| [ ] | 테스트 5개 이상 통과 |
| [ ] | 위험 요청 처리 확인 |
| [ ] | 비식별화 규칙 검증 |
| [ ] | 실제 원문 업로드 금지 원칙 확인 |
| [ ] | 초안 회신까지만 허용 |
| [ ] | 자동 외부 발송 금지 |
| [ ] | 로그에 원문 저장 금지 |
| [ ] | API 키 관리 정책 필요 |
| [ ] | 비용 관리 필요 |
| [ ] | 조직 보안정책 검토 필요 |
| [ ] | 개인정보 담당자 또는 보안 담당자 검토 필요 |
| [ ] | 공식 문서 확인 필요 |
| [ ] | high 위험도 요청 차단 방식 필요 |
| [ ] | 이메일 자동화 전 테스트 계정 사용 |
| [ ] | 실제 업무 계정 연결 전 승인 필요 |
| [ ] | Make.com 또는 API 연동 전 별도 설계 문서 필요 |
| [ ] | Custom GPT 테스트 5개 이상 통과 |
| [ ] | 업체 선정ㆍ계약 확정 표현 차단 확인 |
| [ ] | Knowledge 업로드 전 비식별 샘플 기준 확정 |
| [ ] | Phase 3 안전 게이트 확인 |
| [ ] | 저장소 밖 HWPX 취급 기준 확인 |
| [ ] | 사용자 수동 preview 기준 확인 |
| [ ] | 반복 운영 로그 기준 확인 |
| [ ] | 감사 추적 기준 확인 |
| [ ] | 테스트 계정과 테스트 데이터 기준 확인 |
| [ ] | 실제 원문 차단과 비식별 입력 확인 절차 확인 |
| [ ] | 사용자 preview와 사람 승인 지점 통합 기준 확인 |
| [ ] | 외부 전송 없는 no-send dry-run 기준 확인 |
| [ ] | 외부 연동 구현 범위 승인 판단 확인 |
| [ ] | Phase 3 마무리 판단 및 Phase 4 진입 여부 확인 |
| [ ] | Phase 4 문서 템플릿 안정화 진입 판단 확인 |
| [ ] | 프로젝트 방향 재확인 및 구형 문서 업데이트 기준 확인 |
| [ ] | HWPX template manifest와 공통 placeholder 정합성 확인 |
| [ ] | style profile 확인 필요 값 유지 기준 확인 |
| [ ] | HWPX 수동 preview gap log 기준 확인 |
| [ ] | 저장소 밖 실제 양식 후보 수동 절차와 보류 조건 확인 |
| [ ] | local template과 output Git 제외 반복 검증 기준 확인 |
| [ ] | `needs_security_review` 외부 전송 금지 확인 |
| [ ] | `blocked` 외부 전송 금지 확인 |
| [ ] | 실제 업무 계정 연결 별도 승인 확인 |

## 자동화 허용 범위

초기 자동화는 초안 생성과 초안 회신까지만 검토합니다. 실제 외부 발송, 결재, 계약, 업체 선정, 예산 집행은 자동화 대상이 아닙니다.

## 다음 단계 진입 조건

- 테스트 결과가 안정적으로 통과해야 합니다.
- 위험 요청이 제한되는지 확인해야 합니다.
- 사용자가 발송 전 내용을 확인하는 절차가 있어야 합니다.
- 민감정보가 포함된 입력은 API 호출 전에 차단되어야 합니다.
- 실제 업무 계정을 연결하기 전 별도 승인과 테스트 계정 검증이 필요합니다.
- Make.com 또는 API 연동은 별도 설계 문서와 보안 검토 후 진행해야 합니다.
- Phase 3와 Phase 4 진입 판단의 최신 기준은 `docs/115_phase3_external_integration_hold_criteria.md`, `docs/116_phase3_log_and_audit_trace_criteria.md`, `docs/117_phase3_test_account_and_test_data_criteria.md`, `docs/118_phase3_source_blocking_and_deidentified_input_check_procedure.md`, `docs/119_phase3_user_preview_and_human_approval_integration.md`, `docs/120_phase3_no_send_dry_run_criteria.md`, `docs/121_phase3_external_integration_scope_approval_judgment.md`, `docs/122_phase3_closeout_and_phase4_entry_decision.md`, `docs/123_phase4_template_stabilization_entry_judgment.md`, `docs/124_project_direction_and_legacy_update_review.md`, `docs/125_hwpx_template_manifest_placeholder_consistency_review.md`, `docs/126_style_profile_confirmation_value_collection_criteria.md`, `docs/127_hwpx_manual_preview_gap_log_criteria.md`, `docs/128_external_hwpx_candidate_manual_procedure_and_hold_criteria.md`, `docs/129_local_template_gitignore_repeat_verification_criteria.md`, `docs/130_phase4_template_stabilization_integrated_review.md`, `docs/131_actual_hwpx_manual_rehearsal_user_confirmation_packet.md`를 따릅니다.
- 현재 다음 단계는 실제 연동 구현이 아니라 사용자가 저장소 밖 준비 여부를 확인하는 것입니다.
