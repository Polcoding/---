# 다음 작업

## 목표

`placeholder_confirmed_values` helper 전용 검증 케이스를 파일 기반 fixture로 분리할지 검토합니다.

## 현재 완료 상태

- `placeholder_confirmed_values` read-only helper 최소 구현 완료
- helper 검증 스크립트 작성 완료
- 기존 fixture 6종 회귀 테스트 통과
- `placeholder_confirmed_values` fixture schema 후보 문서화 완료
- 기존 fixture 6종에는 아직 `placeholder_confirmed_values`를 추가하지 않기로 결정
- `missing_fields`, routing, HWPX payload 반영은 계속 보류

## 확인 대상

- `docs/91_placeholder_confirmed_values_helper_result.md`
- `docs/92_placeholder_confirmed_values_fixture_schema_review.md`
- `checklists/placeholder_confirmed_values_fixture_schema_review_checklist.md`
- `normalizers/placeholder_confirmed_values.py`
- `normalizers/validate_placeholder_confirmed_values_poc.py`
- `normalizers/fixtures/`
- `normalizers/README.md`

## 검토 항목

1. helper 검증 케이스를 코드 내부 상수로 유지할지
2. helper 검증 케이스를 `normalizers/fixtures/` 파일로 분리할지
3. 파일로 분리한다면 기존 routing fixture와 이름 규칙을 어떻게 구분할지
4. 파일로 분리하더라도 기존 6종 회귀 테스트에 섞지 않을지
5. safe 케이스와 invalid 케이스를 각각 만들지
6. output summary 생성 권한 문제를 건드리지 않고 콘솔 검증만 유지할지

## 작업 제한

- 실제 기관 양식 사용 금지
- 실제 문서 원문 사용 금지
- 실제 개인정보 또는 내부 운영정보 사용 금지
- 실제 HWPX 템플릿 Git 추가 금지
- Email/API/Make.com 연동 금지
- 확인되지 않은 서식값 임의 생성 금지
- `missing_fields` 자동 제외 금지
- routing 결과 변경 금지
- 기존 fixture 6종 회귀 경로 변경 금지

## 완료 조건

- helper 전용 fixture 파일 분리 여부 판단
- 분리한다면 safe/invalid fixture 후보 구조 정리
- 기존 6종 회귀 기준 유지 확인
- 보안 필터 우선 원칙 유지
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

현재 추천은 helper 검증 케이스를 코드 내부 상수에서 별도 fixture 파일로 분리하되, 기존 routing fixture 6종과는 다른 이름 규칙으로 관리하는 것입니다.
