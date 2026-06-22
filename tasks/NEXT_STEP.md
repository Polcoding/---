# 다음 작업

## 목표

외부 연동 구현 범위 승인 여부를 문서로 판단합니다.

## 현재 완료 상태

- HWPX 보고서 4종 placeholder 기반 렌더링 및 수동 검수 완료
- 입력 정규화, 보안 필터, payload mapper, validation, dry-run PoC 작성 완료
- mapped HWPX 보고서 4종 렌더링 완료
- `placeholder_confirmed_values` helper와 fixture 검증 완료
- metadata는 코드에 연결하지 않고 문서 기준으로 유지하기로 결정
- Phase 2 최소 PoC checkpoint 문서화 완료
- Phase 2 수동 리허설 runbook 문서화 완료
- Phase 2 수동 리허설 Codex 실행 결과 기록 완료
- HWPX 4종 사용자 한컴 수동 검수 올클리어
- Phase 2 반복 운영 기준 문서화 완료
- Phase 2 반복 운영 로그 템플릿 문서화 완료
- fixture 확장 후보 재검토 완료
- fixture JSON 추가 없이 기존 6종과 helper 전용 2종 분리 유지 결정
- `missing_fields` 생성 규칙 재검토 완료
- 고정 missing_fields 정책 유지 결정
- `placeholder_confirmed_values`를 `missing_fields`, routing, HWPX payload에 연결하지 않기로 재확인
- `missing_fields` 사용자 확인 표시 기준 문서화 완료
- HWPX 본문과 검토용 확인 목록 분리 기준 정리 완료
- `missing_fields` 표시 기준을 Phase 2 반복 운영 로그 템플릿에 반영 완료
- 반복 운영 로그에 `missing_fields 확인` 섹션 추가 완료
- `missing_fields` 표시 기준을 Phase 2 사용자 입력 및 수동 운영 점검표에 반영 완료
- 입력 전, HWPX 생성 전, HWPX 생성 후 수동 점검 기준 보강 완료
- Phase 2 운영 문서 묶음의 `missing_fields` 표시 기준 통합 점검 완료
- 반복되는 `missing_fields` 확인 항목은 문서별 사용 시점 차이로 유지 결정
- Phase 2 운영 문서 묶음 최종 정리 완료
- README와 AGENTS 최신화 필요 여부 확인 및 반영 완료
- Phase 2 마무리 전 normalizers 회귀 테스트 묶음 재검증 완료
- mapped HWPX 4종 `rendered`, `remaining_placeholders` 0, `errors` 0 확인
- Phase 2 최소 PoC 문서 기준 마무리 가능 판단 완료
- Phase 3 진입 조건 별도 문서화 필요 결정 완료
- Phase 3 진입 조건 및 안전 게이트 문서화 완료
- Phase 3 저장소 밖 HWPX 양식 취급 기준 구체화 완료
- Phase 3 사용자 수동 preview 기준 구체화 완료
- Phase 3 상태별 중단 기준 반복 운영 문서 반영 완료
- Phase 3 운영 문서 묶음 통합 점검 완료
- Phase 3 외부 연동 필요성과 보류 기준 검토 완료
- Phase 3 로그와 감사 추적 기준 구체화 완료
- Phase 3 테스트 계정과 테스트 데이터 기준 구체화 완료
- Phase 3 실제 원문 차단과 비식별 입력 확인 절차 구체화 완료
- Phase 3 사용자 preview와 사람 승인 지점 통합 기준 구체화 완료
- Phase 3 외부 전송 없는 no-send dry-run 기준 구체화 완료

## 확인 대상

- `docs/120_phase3_no_send_dry_run_criteria.md`
- `checklists/phase3_no_send_dry_run_criteria_checklist.md`
- `docs/119_phase3_user_preview_and_human_approval_integration.md`
- `checklists/phase3_user_preview_and_human_approval_integration_checklist.md`
- `docs/118_phase3_source_blocking_and_deidentified_input_check_procedure.md`
- `docs/117_phase3_test_account_and_test_data_criteria.md`
- `docs/116_phase3_log_and_audit_trace_criteria.md`
- `docs/115_phase3_external_integration_hold_criteria.md`
- `docs/114_phase3_operating_docs_integrated_review.md`
- `docs/111_phase3_entry_safety_gate.md`
- `docs/101_phase2_repeat_operation_log_template.md`
- `checklists/before_automation_checklist.md`
- `README.md`
- `AGENTS.md`

## 검토 항목

1. 실제 구현 검토 단계로 넘어가기 위한 필수 조건이 문서상 충분한지 판단
2. 현재 기준으로 승인 가능한 범위와 계속 보류해야 할 범위를 분리
3. OpenAI API, Make.com, Email 중 어떤 것도 실제 구현 대상으로 자동 승격되지 않도록 확인
4. 실제 계정, 실제 수신자, 실제 첨부, 실제 API 요청, 실제 HWPX 원본이 계속 제외되는지 확인
5. no-send dry-run 통과가 실제 구현 승인으로 오인되지 않도록 표시
6. 구현 범위 승인을 하더라도 별도 사용자 명시 승인 없이는 코드 변경하지 않는다고 정리
7. 코드, fixture, routing, HWPX payload, output 변경이 필요 없는지 판단
8. 필요한 경우 최소 범위 문서 또는 체크리스트만 보강
9. 필요한 경우 README, AGENTS, NEXT_STEP을 최소 범위로 갱신

## 작업 제한

- 실제 기관 양식 사용 금지
- 실제 문서 원문 사용 금지
- 실제 개인정보 또는 내부 운영정보 사용 금지
- 실제 HWPX 템플릿 Git 추가 금지
- Email/API/Make.com 연동 금지
- 확인되지 않은 서식값 임의 생성 금지
- `missing_fields` 자동 제외 금지
- routing 결과 변경 금지
- HWPX payload 반영 금지
- `placeholder_confirmed_values` normalizer 연결 금지
- HWPX output 재생성 금지
- 실제 계정, 실제 수신자, 실제 첨부, 실제 API 요청 생성 금지
- 실제 구현 코드를 작성하지 않음

## 완료 조건

- 외부 연동 구현 범위 승인 여부 문서화 필요 판단
- 승인 가능한 범위와 계속 보류할 범위 구분
- 실제 구현이 필요한 경우에도 별도 명시 승인 전까지 보류한다는 경계 정리
- 현재 단계에서 코드 변경이 필요한지 판단
- 필요한 경우 관련 문서 또는 체크리스트 최소 범위 갱신
- README 최신화 필요 여부 판단
- AGENTS 최신화 필요 여부 판단
- 보안 검수 결과 재확인
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

현재 추천은 코드 변경 없이 외부 연동 구현 범위 승인 여부를 문서로 판단하는 것입니다. 실제 API, Make.com, Email 연동 구현은 계속 보류합니다.
