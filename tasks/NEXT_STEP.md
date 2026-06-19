# 다음 작업

## 목표

`placeholder_confirmed_values` helper 결과를 normalizer에 연결하기 전, read-only metadata schema 후보를 문서화합니다.

## 현재 완료 상태

- `placeholder_confirmed_values` read-only helper 최소 구현 완료
- helper 전용 safe/invalid fixture 파일 분리 완료
- helper fixture 검증 통과
- 기존 routing fixture 6종 회귀 테스트 통과
- normalizer 연결 허용 조건과 금지 조건 문서화 완료
- 현재 단계에서는 helper 결과를 normalizer 흐름에 연결하지 않기로 결정

## 확인 대상

- `docs/91_placeholder_confirmed_values_helper_result.md`
- `docs/92_placeholder_confirmed_values_fixture_schema_review.md`
- `docs/93_placeholder_confirmed_values_file_fixture_result.md`
- `docs/94_placeholder_confirmed_values_normalizer_connection_policy.md`
- `checklists/placeholder_confirmed_values_normalizer_connection_policy_checklist.md`
- `normalizers/placeholder_confirmed_values.py`
- `normalizers/validate_placeholder_confirmed_values_poc.py`
- `normalizers/input_normalizer_poc.py`
- `normalizers/security_filter_poc.py`

## 검토 항목

1. metadata 필드명을 무엇으로 할지
2. metadata가 `security_flags` 안에 들어갈지 별도 top-level 필드로 들어갈지
3. metadata에 `checked`, `valid`, `invalid_count`, `findings`를 둘지
4. metadata가 `missing_fields`, routing, payload에 영향을 주지 않는다고 어떻게 명시할지
5. invalid finding이 있을 때도 metadata로만 남기는지
6. helper fixture 결과와 normalizer metadata 후보를 어떻게 연결해서 설명할지

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
- 아직 코드 연결 금지

## 완료 조건

- read-only metadata schema 후보 문서화
- metadata 필드 위치 후보 결정
- metadata가 기존 결과를 바꾸지 않는 원칙 정리
- 보안 필터 우선 원칙 유지
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

현재 추천은 metadata를 `placeholder_confirmed_values_review` top-level 후보로 문서화하되, 코드 연결은 계속 보류하는 것입니다.
