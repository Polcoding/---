# 다음 작업

## 목표

Phase 2 최소 PoC의 반복 운영 기준과 다음 최소 개선 후보를 정리합니다.

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

## 확인 대상

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

1. Phase 2 최소 PoC를 반복 실행할 때 매번 확인할 기준
2. 사용자가 직접 확인해야 하는 항목과 Codex가 자동 확인할 항목 구분
3. HWPX output 4종을 언제 다시 생성할지 기준
4. GitHub Desktop push 전 확인 기준
5. 다음 최소 개선 후보 우선순위
6. 계속 보류할 범위
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

- 반복 운영 기준 문서화
- 사용자 확인 항목과 Codex 확인 항목 구분
- 다음 최소 개선 후보 제안
- 계속 보류할 범위 재확인
- Git 제외 상태 재확인
- 보안 검수 결과 재확인
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

현재 추천은 Phase 2 최소 PoC 리허설 완료 상태를 기준으로 반복 운영 기준을 먼저 정리하고, 그 다음에 `placeholder_confirmed_values` 연결 여부나 fixture 확장 여부를 다시 판단하는 것입니다.
