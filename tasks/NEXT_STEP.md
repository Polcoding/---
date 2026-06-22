# 다음 작업

## 목표

Phase 2 운영 문서 묶음에서 `missing_fields` 표시 기준이 중복 없이 정리되었는지 통합 점검합니다.

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

## 확인 대상

- `docs/106_missing_fields_manual_operation_checkpoints_reflection.md`
- `checklists/missing_fields_manual_operation_checkpoints_reflection_checklist.md`
- `docs/105_missing_fields_repeat_log_reflection_result.md`
- `checklists/missing_fields_repeat_log_reflection_result_checklist.md`
- `docs/104_missing_fields_user_display_guidance.md`
- `checklists/missing_fields_user_display_guidance_checklist.md`
- `docs/83_phase2_user_input_and_manual_operation_checkpoints.md`
- `checklists/phase2_user_input_and_manual_operation_checklist.md`
- `docs/101_phase2_repeat_operation_log_template.md`
- `checklists/phase2_repeat_operation_log_template_checklist.md`
- `docs/100_phase2_repeat_operation_criteria.md`
- `checklists/phase2_repeat_operation_criteria_checklist.md`

## 검토 항목

1. `docs/83`, `docs/101`, `docs/104`, `docs/105`, `docs/106`의 역할이 분리되어 있는지 확인
2. `missing_fields`가 본문 실제값이 아니라 검토용 목록이라는 기준이 일관적인지 확인
3. `[확인 필요]`와 `missing_fields` 표현이 서로 모순되지 않는지 확인
4. `missing_fields` 자동 제외 금지 원칙이 모든 관련 문서에서 유지되는지 확인
5. 반복 운영 로그와 수동 운영 점검표의 확인 항목이 과하게 중복되지 않는지 확인
6. 코드 변경 없이 문서 기준만으로 충분한지 확인
7. 필요하면 통합 점검 결과 문서와 체크리스트를 추가

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

- Phase 2 운영 문서 묶음 통합 점검 결과 정리
- 문서별 역할 분리 여부 확인
- `missing_fields` 표시 기준 모순 여부 확인
- 중복이 과한 항목 보류 또는 유지 판단
- 코드 변경 여부 판단
- 보안 검수 결과 재확인
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

현재 추천은 코드 변경 없이 Phase 2 운영 문서 묶음의 `missing_fields` 표시 기준을 통합 점검하는 것입니다. `placeholder_confirmed_values`의 routing 연결은 계속 보류합니다.
