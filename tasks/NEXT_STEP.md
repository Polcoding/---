# 다음 작업

## 목표

`placeholder_confirmed_values_review` metadata를 코드에 연결하지 않고 문서 기준으로 유지할지, 또는 dry-run preview 전용 출력으로만 둘지 검토합니다.

## 현재 완료 상태

- `placeholder_confirmed_values` read-only helper 최소 구현 완료
- helper 전용 safe/invalid fixture 파일 분리 완료
- helper fixture 검증 통과
- existing routing fixture 6종 회귀 테스트 통과
- normalizer 연결 허용 조건과 금지 조건 문서화 완료
- read-only metadata schema 후보 문서화 완료
- 현재 단계에서는 helper 결과를 normalizer 흐름에 연결하지 않기로 결정

## 확인 대상

- `docs/94_placeholder_confirmed_values_normalizer_connection_policy.md`
- `docs/95_placeholder_confirmed_values_readonly_metadata_schema.md`
- `checklists/placeholder_confirmed_values_readonly_metadata_schema_checklist.md`
- `normalizers/placeholder_confirmed_values.py`
- `normalizers/validate_placeholder_confirmed_values_poc.py`
- `normalizers/input_normalizer_poc.py`
- `normalizers/hwpx_renderer_dry_run_poc.py`

## 검토 항목

1. metadata를 문서 기준으로만 유지할지
2. dry-run preview 전용 summary에만 metadata 후보를 출력할지
3. dry-run preview 출력이 기존 `normalization_summary.json`과 섞이지 않아야 하는지
4. preview를 추가하더라도 `missing_fields`, routing, payload를 바꾸지 않는지
5. preview용 output도 Git 제외 상태를 유지하는지
6. 코드 구현보다 문서 기준 유지가 더 안전한지

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

- metadata 문서 기준 유지 여부 판단
- dry-run preview 전용 출력 여부 판단
- 기존 6종 회귀 기준 유지
- 보안 필터 우선 원칙 유지
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

현재 추천은 metadata를 아직 코드에 연결하지 않고 문서 기준으로 유지하는 것입니다. dry-run preview 전용 출력은 필요성이 더 명확해진 뒤 검토합니다.
