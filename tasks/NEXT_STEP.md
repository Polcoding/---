# 다음 작업

## 목표

Phase 2 운영 문서 묶음을 최종 정리하고 READMEㆍAGENTS 최신화 필요 여부를 확인합니다.

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

## 확인 대상

- `docs/107_missing_fields_phase2_docs_integrated_review.md`
- `checklists/missing_fields_phase2_docs_integrated_review_checklist.md`
- `docs/106_missing_fields_manual_operation_checkpoints_reflection.md`
- `checklists/missing_fields_manual_operation_checkpoints_reflection_checklist.md`
- `docs/105_missing_fields_repeat_log_reflection_result.md`
- `checklists/missing_fields_repeat_log_reflection_result_checklist.md`
- `docs/104_missing_fields_user_display_guidance.md`
- `checklists/missing_fields_user_display_guidance_checklist.md`
- `README.md`
- `AGENTS.md`
- `docs/83_phase2_user_input_and_manual_operation_checkpoints.md`
- `checklists/phase2_user_input_and_manual_operation_checklist.md`
- `docs/101_phase2_repeat_operation_log_template.md`
- `checklists/phase2_repeat_operation_log_template_checklist.md`
- `docs/100_phase2_repeat_operation_criteria.md`
- `checklists/phase2_repeat_operation_criteria_checklist.md`

## 검토 항목

1. Phase 2 운영 문서 묶음의 현재 완료 상태를 요약할지 확인
2. README의 현재 진행 위치와 다음 단계가 최신 상태인지 확인
3. AGENTS.md의 현재까지 작업 범위가 최신 상태인지 확인
4. `docs/100`의 다음 후보가 오래된 기준인지 확인
5. Phase 2 마무리 전 normalizers 회귀 검증이 필요한지 확인
6. Phase 3 진입 조건 문서화가 다음 단계인지 확인
7. 필요한 경우 최소 범위로 README, AGENTS, NEXT_STEP을 갱신

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

## 완료 조건

- Phase 2 운영 문서 묶음 최종 정리 필요성 판단
- README 최신화 필요 여부 판단
- AGENTS 최신화 필요 여부 판단
- Phase 2 마무리 전 검증 후보 정리
- 코드 변경 여부 판단
- 보안 검수 결과 재확인
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

현재 추천은 코드 변경 없이 Phase 2 운영 문서 묶음 최종 정리와 READMEㆍAGENTS 최신화 필요 여부를 확인하는 것입니다. `placeholder_confirmed_values`의 routing 연결은 계속 보류합니다.
