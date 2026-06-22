# 다음 작업

## 목표

`missing_fields` 생성 규칙 개선 여부를 재검토합니다.

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

## 확인 대상

- `docs/102_fixture_expansion_decision_after_repeat_run.md`
- `checklists/fixture_expansion_decision_after_repeat_run_checklist.md`
- `docs/86_missing_fields_rule_improvement_review.md`
- `checklists/missing_fields_rule_improvement_review_checklist.md`
- `docs/101_phase2_repeat_operation_log_template.md`
- `checklists/phase2_repeat_operation_log_template_checklist.md`
- `docs/100_phase2_repeat_operation_criteria.md`
- `checklists/phase2_repeat_operation_criteria_checklist.md`
- `docs/85_normalizers_fixture_expansion_review.md`
- `checklists/normalizers_fixture_expansion_review_checklist.md`
- `docs/63_input_normalization_test_cases.md`
- `normalizers/fixtures/`
- `normalizers/README.md`
- `normalizers/`

## 검토 항목

1. project_plan/result_report의 필수값 누락을 계속 `needs_more_input`으로 둘지 확인
2. placeholder-confirmed 값을 `[확인 필요]`와 구분할지 확인
3. `missing_fields` 자동 제외 금지 원칙을 유지할지 확인
4. 사용자에게 missing_fields를 더 보기 좋게 표시하는 문서 기준이 필요한지 확인
5. 지금 단계에서 코드 변경이 필요한지 확인
6. fixture 확장 없이 문서 기준으로 충분한지 확인
7. `placeholder_confirmed_values`를 아직 연결하지 않을지 재확인

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

## 완료 조건

- missing_fields 생성 규칙 개선 필요성 재검토
- 코드 변경 여부 판단
- 자동 제외 금지 원칙 유지 여부 정리
- placeholder-confirmed 값과 `[확인 필요]` 구분 여부 정리
- fixture 확장 없이 충분한지 판단
- 보안 검수 결과 재확인
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

현재 추천은 `missing_fields` 생성 규칙 개선 여부를 문서 기준으로 다시 검토하고, 실제 코드 변경은 필요성이 분명할 때만 최소 범위로 판단하는 것입니다. `placeholder_confirmed_values`의 routing 연결은 계속 보류합니다.
