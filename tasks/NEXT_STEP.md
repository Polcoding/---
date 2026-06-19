# 다음 작업

## 목표

`placeholder_confirmed_values` read-only 판정 helper를 최소 범위로 구현하고, 기존 정규화ㆍ보안 필터ㆍHWPX payload 흐름을 깨뜨리지 않는지 확인합니다.

## 현재 완료 상태

- HWPX 보고서 4종 placeholder 기반 로컬 렌더링 및 한컴 수동 검수 완료
- Phase 1 완료 기준 및 Phase 2 진입 조건 문서화 완료
- HWPX 보고서 4종 입력 요구사항 문서화 완료
- 입력 정규화 스키마 초안 문서화 완료
- Phase 2 보안 필터 요구사항 문서화 완료
- `normalizers/` 입력 정규화 최소 PoC 작성 완료
- HWPX payload mapper, validation, renderer dry-run PoC 작성 완료
- mapped HWPX 보고서 4종 렌더링과 수동 검수 완료
- Phase 2 최소 운영 흐름과 사용자 입력 템플릿 문서화 완료
- `placeholder_confirmed_values` 설계, 충돌 규칙, 코드 도입 여부 재검토 완료
- Superpowers 재적용 후 프로젝트 진입점 재정비 완료

## 확인 대상

- `docs/87_placeholder_confirmed_values_design_review.md`
- `docs/88_placeholder_pattern_collision_rules.md`
- `docs/89_placeholder_confirmed_values_code_adoption_decision.md`
- `docs/90_project_reorganization_after_superpowers.md`
- `checklists/placeholder_confirmed_values_design_review_checklist.md`
- `checklists/placeholder_pattern_collision_rules_checklist.md`
- `checklists/placeholder_confirmed_values_code_adoption_decision_checklist.md`
- `normalizers/input_normalizer_poc.py`
- `normalizers/security_filter_poc.py`
- `normalizers/hwpx_payload_mapper_poc.py`
- `normalizers/validate_hwpx_payload_poc.py`
- `normalizers/hwpx_renderer_dry_run_poc.py`
- `normalizers/fixtures/`
- `normalizers/README.md`

## 구현 원칙

1. helper는 read-only로만 동작해야 합니다.
2. `missing_fields` 생성 결과를 변경하지 않습니다.
3. routing 결과를 변경하지 않습니다.
4. HWPX payload mapper 결과를 변경하지 않습니다.
5. HWPX 렌더링 결과를 변경하지 않습니다.
6. 실제값 의심 패턴과 충돌하면 보안 필터 판단을 우선합니다.
7. 기존 fixture 회귀 테스트를 통과해야 합니다.

## helper 후보

후보 함수명은 다음 범위에서 검토합니다.

```text
is_placeholder_confirmed_value(value)
find_invalid_placeholder_confirmed_values(values)
```

역할:

- 값이 문자열인지 확인
- 값이 `[`와 `]`로 감싸진 placeholder 형식인지 확인
- 빈 placeholder 또는 의미 없는 placeholder 제외
- 실제 개인정보, 문서번호, 연락처, 계좌번호, 차량번호, 내부 운영정보로 보이는 패턴 제외
- invalid 항목은 routing 변경 없이 검토용 reasons로만 반환

## 작업 제한

- 실제 기관 양식 사용 금지
- 실제 문서 원문 사용 금지
- 실제 개인정보 또는 내부 운영정보 사용 금지
- 실제 HWPX 템플릿 Git 추가 금지
- Email/API/Make.com 연동 금지
- 확인되지 않은 서식값 임의 생성 금지
- `known_values`와 `placeholder_confirmed_values`를 혼합하지 않기

## 완료 조건

- read-only 판정 helper 최소 구현
- 기존 fixture 회귀 테스트 통과
- `missing_fields` 결과 미변경 확인
- routing 결과 미변경 확인
- HWPX payload 및 dry-run 결과 미변경 확인
- 보안 테스트 통과
- output 및 로컬 HWPX 파일 Git 제외 확인
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

helper가 안정적으로 추가되면, 다음 단계에서 helper 판정 결과를 문서화하고 fixture schema 확장 여부를 별도 검토합니다.
