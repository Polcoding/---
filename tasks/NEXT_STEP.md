# 다음 작업

## 목표

Phase 2 최소 PoC 수동 리허설 절차를 정리합니다.

## 현재 완료 상태

- HWPX 보고서 4종 placeholder 기반 렌더링 및 수동 검수 완료
- 입력 정규화, 보안 필터, payload mapper, validation, dry-run PoC 작성 완료
- mapped HWPX 보고서 4종 렌더링 완료
- `placeholder_confirmed_values` helper와 fixture 검증 완료
- metadata는 코드에 연결하지 않고 문서 기준으로 유지하기로 결정
- Phase 2 최소 PoC checkpoint 문서화 완료

## 확인 대상

- `docs/82_phase2_minimal_operation_flow.md`
- `docs/83_phase2_user_input_and_manual_operation_checkpoints.md`
- `docs/84_hwpx_report_user_input_templates.md`
- `docs/97_phase2_minimal_poc_checkpoint.md`
- `checklists/phase2_minimal_poc_checkpoint_checklist.md`
- `normalizers/README.md`
- `normalizers/`
- `templates/hwpx/local_template_policy.md`
- `renderers/hwpx_renderer/output/.gitignore`
- `normalizers/output/.gitignore`

## 검토 항목

1. 사용자가 입력 전 확인해야 할 사항
2. Codex가 실행할 normalizers 명령 순서
3. HWPX output 생성 전 확인할 사항
4. HWPX output 생성 후 사용자가 한컴에서 확인할 사항
5. GitHub Desktop Changes에서 확인할 사항
6. `normalizers/output/` 및 `renderers/hwpx_renderer/output/` 쓰기 권한 또는 파일 잠금 확인 절차
7. 문제가 생겼을 때 중단하고 되돌아갈 기준

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

- Phase 2 수동 리허설 절차 문서화
- 사용자 확인 필요 지점 표시
- Codex 실행 명령 순서 정리
- Git 제외 확인 절차 정리
- output 폴더 쓰기 권한과 산출물 잠금 확인 절차 정리
- 문제 발생 시 중단 기준 정리
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

현재 추천은 수동 리허설 절차를 문서화한 뒤, 사용자가 실제로 한 번 따라 할 수 있는 runbook 형태로 정리하는 것입니다.
