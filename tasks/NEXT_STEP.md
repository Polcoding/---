# 다음 작업

## 목표

fixture 확장 후보를 검토합니다.

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

## 확인 대상

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

1. 기존 fixture 6종을 유지할지 확인
2. fixture 확장이 실제로 필요한지 확인
3. 추가한다면 어떤 문서 유형에 필요한지 확인
4. 실제값 없이 placeholder만으로 작성 가능한지 확인
5. 기존 routing 결과를 흔들지 않는지 확인
6. `placeholder_confirmed_values` fixture와 일반 routing fixture를 계속 분리할지 확인
7. 지금은 코드 추가 없이 문서 기준 후보만 정리할지 판단

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

- fixture 확장 필요성 재검토
- 추가 후보가 있으면 placeholder 기반으로만 정리
- 기존 fixture 6종과 helper fixture 분리 유지 여부 보고
- 코드 변경 여부 판단
- 보안 검수 결과 재확인
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

현재 추천은 fixture 확장 후보를 문서 기준으로 재검토하고, 실제 코드/fixture 추가가 필요한지 판단하는 것입니다. `placeholder_confirmed_values`의 routing 연결은 계속 보류합니다.
