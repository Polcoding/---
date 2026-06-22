# 다음 작업

## 목표

Phase 2 반복 운영 로그 템플릿을 정리합니다.

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

## 확인 대상

- `docs/100_phase2_repeat_operation_criteria.md`
- `checklists/phase2_repeat_operation_criteria_checklist.md`
- `docs/98_phase2_manual_rehearsal_runbook.md`
- `checklists/phase2_manual_rehearsal_runbook_checklist.md`
- `docs/99_phase2_manual_rehearsal_result.md`
- `checklists/phase2_manual_rehearsal_result_checklist.md`
- `docs/97_phase2_minimal_poc_checkpoint.md`
- `docs/82_phase2_minimal_operation_flow.md`
- `normalizers/README.md`
- `normalizers/`
- `templates/hwpx/local_template_policy.md`
- `renderers/hwpx_renderer/output/.gitignore`
- `normalizers/output/.gitignore`

## 검토 항목

1. 반복 실행 날짜와 목적 기록 형식
2. 실행한 normalizers 명령 기록 형식
3. HWPX output 4종 생성 여부 기록 형식
4. 사용자 한컴 확인 결과 기록 형식
5. 이상 발생 시 파일명, 항목 번호, 증상 기록 형식
6. Git 제외 확인 결과 기록 형식
7. 보안 검수 결과 기록 형식

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

- 반복 운영 로그 템플릿 문서화
- 실행 명령 기록 항목 정리
- HWPX output 확인 항목 정리
- 사용자 한컴 검수 결과 기록 항목 정리
- 이상 발생 시 기록 형식 정리
- Git 제외 및 보안 검수 항목 포함
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

현재 추천은 반복 운영 기준에 맞춰 실행 로그 템플릿을 만들고, 이후 fixture 확장 후보를 검토하는 것입니다. `placeholder_confirmed_values`의 routing 연결은 계속 보류합니다.
