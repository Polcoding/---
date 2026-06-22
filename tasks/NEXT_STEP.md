# 다음 작업

## 목표

Phase 2 마무리 전 normalizers 회귀 테스트 묶음을 재검증합니다.

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
- Phase 2 운영 문서 묶음 최종 정리 완료
- README와 AGENTS 최신화 필요 여부 확인 및 반영 완료

## 확인 대상

- `docs/108_phase2_operating_docs_final_review.md`
- `checklists/phase2_operating_docs_final_review_checklist.md`
- `docs/81_normalizers_regression_test_suite.md`
- `checklists/normalizers_regression_test_suite_checklist.md`
- `normalizers/validate_placeholder_confirmed_values_poc.py`
- `normalizers/input_normalizer_poc.py`
- `normalizers/hwpx_payload_mapper_poc.py`
- `normalizers/validate_hwpx_payload_poc.py`
- `normalizers/hwpx_renderer_dry_run_poc.py`
- `normalizers/render_mapped_hwpx_poc.py`
- `docs/107_missing_fields_phase2_docs_integrated_review.md`
- `checklists/missing_fields_phase2_docs_integrated_review_checklist.md`
- `README.md`
- `AGENTS.md`

## 검토 항목

1. `docs/81`의 회귀 테스트 묶음이 현재 Phase 2 마무리 검증 기준으로 충분한지 확인
2. helper fixture와 routing fixture를 모두 검증하는지 확인
3. blocked fixture와 `needs_security_review` fixture가 HWPX payload 및 렌더링으로 넘어가지 않는지 확인
4. mapped HWPX 4종 결과가 `rendered`와 `remaining_placeholders: 0`을 유지하는지 확인
5. output과 로컬 HWPX 템플릿이 Git 제외 상태인지 확인
6. 회귀 검증 중 코드 변경이 필요한 실패인지, 로컬 output 잠금ㆍ권한 문제인지 구분
7. 필요한 경우 최소 범위로 결과 문서와 NEXT_STEP을 갱신

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
- HWPX output은 회귀 테스트 명령이 생성하는 로컬 ignored 산출물만 허용

## 완료 조건

- normalizers 회귀 테스트 묶음 실행 가능 여부 판단
- 실행한 경우 각 명령 결과 확인
- mapped HWPX 4종 렌더링 상태 확인
- output 및 로컬 HWPX Git 제외 상태 확인
- 코드 변경 여부 판단
- 보안 검수 결과 재확인
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

현재 추천은 Phase 2 마무리 전 normalizers 회귀 테스트 묶음을 재검증하는 것입니다. `placeholder_confirmed_values`의 routing 연결은 계속 보류합니다.
