# 다음 작업

## 목표

Phase 2 수동 리허설 runbook을 기준으로 1회 실행 결과를 기록합니다.

## 현재 완료 상태

- HWPX 보고서 4종 placeholder 기반 렌더링 및 수동 검수 완료
- 입력 정규화, 보안 필터, payload mapper, validation, dry-run PoC 작성 완료
- mapped HWPX 보고서 4종 렌더링 완료
- `placeholder_confirmed_values` helper와 fixture 검증 완료
- metadata는 코드에 연결하지 않고 문서 기준으로 유지하기로 결정
- Phase 2 최소 PoC checkpoint 문서화 완료
- Phase 2 수동 리허설 runbook 문서화 완료

## 확인 대상

- `docs/98_phase2_manual_rehearsal_runbook.md`
- `checklists/phase2_manual_rehearsal_runbook_checklist.md`
- `normalizers/README.md`
- `normalizers/`
- `templates/hwpx/local_template_policy.md`
- `renderers/hwpx_renderer/output/.gitignore`
- `normalizers/output/.gitignore`

## 검토 항목

1. runbook 명령 순서대로 normalizers 검증 실행
2. HWPX output 4종 생성 여부 확인
3. `normalizers/output/` 및 `renderers/hwpx_renderer/output/` Git 제외 확인
4. GitHub Desktop Changes에 output 또는 로컬 HWPX 템플릿이 보이지 않는지 확인
5. 사용자가 한컴에서 HWPX 4종을 열어 글자 겹침, placeholder 잔여, bullet 표기, 민감정보 여부 확인
6. 이상 발생 시 파일명, 항목 번호, 증상을 기록
7. 결과를 별도 문서와 체크리스트로 남길지 판단

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

- runbook 기준 normalizers 검증 실행
- HWPX output 생성 또는 안전 중단 상태 보고
- `[사용자 확인 필요]` HWPX 4종 열람 항목 제시
- Git 제외 확인 결과 보고
- output 폴더 쓰기 권한 또는 산출물 잠금 문제 여부 보고
- 보안 검수 통과 여부 보고
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

현재 추천은 runbook을 기준으로 실제 수동 리허설을 1회 실행하고, 사용자의 한컴 확인 결과를 받아 결과 문서로 정리하는 것입니다.
