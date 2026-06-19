# 다음 작업

## 목표

`placeholder_confirmed_values` helper 결과를 normalizer 흐름에 연결할지 판단하기 전에, 연결 허용 조건과 금지 조건을 문서화합니다.

## 현재 완료 상태

- `placeholder_confirmed_values` read-only helper 최소 구현 완료
- helper 전용 safe/invalid fixture 파일 분리 완료
- helper fixture 검증 통과
- 기존 routing fixture 6종 회귀 테스트 통과
- 기존 fixture 6종에는 아직 `placeholder_confirmed_values`를 추가하지 않기로 결정
- `missing_fields`, routing, HWPX payload 반영은 계속 보류

## 확인 대상

- `docs/91_placeholder_confirmed_values_helper_result.md`
- `docs/92_placeholder_confirmed_values_fixture_schema_review.md`
- `docs/93_placeholder_confirmed_values_file_fixture_result.md`
- `checklists/placeholder_confirmed_values_file_fixture_result_checklist.md`
- `normalizers/placeholder_confirmed_values.py`
- `normalizers/validate_placeholder_confirmed_values_poc.py`
- `normalizers/fixtures/placeholder_confirmed_values/`
- `normalizers/input_normalizer_poc.py`
- `normalizers/security_filter_poc.py`

## 검토 항목

1. helper 결과를 normalizer output에 read-only metadata로 붙일지
2. 붙인다면 `missing_fields`와 routing을 전혀 바꾸지 않는 조건을 어떻게 보장할지
3. security filter와 helper 중 어떤 판단이 우선인지 다시 명시할지
4. invalid helper finding이 있을 때 blocked로 바꿀지 또는 metadata로만 남길지
5. 기존 fixture 6종 회귀 테스트에 영향을 주지 않는 연결 방식이 있는지
6. 연결을 하지 않고 문서 기준으로만 유지할지

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
- 기존 fixture 6종 회귀 경로 변경 금지

## 완료 조건

- normalizer 연결 허용 조건 정리
- normalizer 연결 금지 조건 정리
- read-only metadata 연결 여부 판단
- 보안 필터 우선 원칙 유지
- 기존 6종 회귀 기준 유지
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

현재 추천은 helper 결과를 아직 normalizer에 연결하지 않고, 연결 허용 조건과 금지 조건을 먼저 문서로 확정하는 것입니다.
