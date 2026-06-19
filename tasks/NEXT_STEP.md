# 다음 작업

## 목표

`placeholder_confirmed_values` read-only helper 구현 결과를 바탕으로 fixture schema 확장 여부를 검토합니다.

## 현재 완료 상태

- HWPX 보고서 4종 placeholder 기반 로컬 렌더링 및 한컴 수동 검수 완료
- Phase 1 완료 기준 및 Phase 2 진입 조건 문서화 완료
- 입력 정규화, 보안 필터, HWPX payload mapper, payload validation, renderer dry-run 최소 PoC 작성 완료
- mapped HWPX 보고서 4종 렌더링과 수동 검수 완료
- Phase 2 최소 운영 흐름과 사용자 입력 템플릿 문서화 완료
- `placeholder_confirmed_values` 설계, 충돌 규칙, 코드 도입 여부 재검토 완료
- `placeholder_confirmed_values` read-only 판정 helper 최소 구현 완료
- 기존 fixture 6종 회귀 테스트 통과

## 확인 대상

- `docs/87_placeholder_confirmed_values_design_review.md`
- `docs/88_placeholder_pattern_collision_rules.md`
- `docs/89_placeholder_confirmed_values_code_adoption_decision.md`
- `docs/91_placeholder_confirmed_values_helper_result.md`
- `checklists/placeholder_confirmed_values_helper_result_checklist.md`
- `normalizers/placeholder_confirmed_values.py`
- `normalizers/validate_placeholder_confirmed_values_poc.py`
- `normalizers/fixtures/`
- `normalizers/input_normalizer_poc.py`
- `normalizers/security_filter_poc.py`

## 검토 항목

1. `placeholder_confirmed_values`를 fixture schema 후보로 문서화할지
2. 신규 fixture를 추가한다면 routing 결과를 바꾸지 않는 검증용 fixture로 둘지
3. 신규 fixture를 기존 6종 회귀 테스트에 포함할지 또는 helper 전용 검증으로 분리할지
4. `missing_fields` 자동 제외는 계속 보류할지
5. `project_plan`과 `result_report` ready 경로는 계속 열지 않을지
6. 실제값 의심 패턴과 충돌하는 경우 security filter 우선 원칙을 어떻게 기록할지

## 작업 제한

- 실제 기관 양식 사용 금지
- 실제 문서 원문 사용 금지
- 실제 개인정보 또는 내부 운영정보 사용 금지
- 실제 HWPX 템플릿 Git 추가 금지
- Email/API/Make.com 연동 금지
- 확인되지 않은 서식값 임의 생성 금지
- `missing_fields` 자동 제외 금지
- routing 결과 변경 금지

## 완료 조건

- fixture schema 확장 여부 판단
- 신규 fixture 추가 여부 판단
- 기존 6종 회귀 기준 유지 여부 확인
- `missing_fields` 반영 보류 여부 확인
- 보안 필터 우선 원칙 유지
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

현재 추천은 신규 fixture를 바로 routing에 넣지 않고, `placeholder_confirmed_values` schema 후보를 문서화한 뒤 helper 전용 검증 케이스를 유지하는 것입니다.
