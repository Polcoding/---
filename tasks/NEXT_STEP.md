# 다음 작업

## 목표

local template policy와 Git 제외 상태 반복 검증 기준을 HWPX 보고서 4종 기준으로 정리합니다.

실제 기관 HWPX 원본을 저장소에 넣거나 실제 HWPX output을 재생성하는 단계가 아닙니다. `templates/hwpx/`의 로컬 HWPX 템플릿, renderer output, normalizer output이 반복 작업 중 GitHub Desktop Changes에 나타나지 않도록 확인 절차를 문서 기준으로 고정합니다.

## 현재 완료 상태

- HWPX 보고서 4종 placeholder 기반 렌더링 및 수동 검수 완료
- 입력 정규화, 보안 필터, payload mapper, validation, dry-run PoC 작성 완료
- mapped HWPX 보고서 4종 렌더링 완료
- `placeholder_confirmed_values` helper와 fixture 검증 완료
- metadata는 코드에 연결하지 않고 문서 기준으로 유지하기로 결정
- `missing_fields` 생성 규칙 고정 및 사용자 표시 기준 문서화 완료
- Phase 2 운영 문서 묶음 최종 정리 완료
- Phase 2 최소 PoC 문서 기준 마무리 가능 판단 완료
- Phase 3 진입 조건 및 안전 게이트 문서화 완료
- Phase 3 저장소 밖 HWPX 양식 취급 기준 구체화 완료
- Phase 3 사용자 수동 preview 기준 구체화 완료
- Phase 3 외부 연동 필요성과 보류 기준 검토 완료
- Phase 3 로그와 감사 추적 기준 구체화 완료
- Phase 3 테스트 계정과 테스트 데이터 기준 구체화 완료
- Phase 3 실제 원문 차단과 비식별 입력 확인 절차 구체화 완료
- Phase 3 사용자 preview와 사람 승인 지점 통합 기준 구체화 완료
- Phase 3 외부 전송 없는 no-send dry-run 기준 구체화 완료
- Phase 3 외부 연동 구현 범위 승인 판단 완료
- Phase 3 마무리 판단 및 Phase 4 진입 여부 결정 완료
- Phase 4 문서 템플릿 안정화 진입 판단 완료
- 프로젝트 방향 재확인 및 구형 진입점 문서 업데이트 검토 완료
- HWPX 보고서 4종 template manifest와 공통 placeholder 정합성 점검 완료
- style profile `[확인 필요]` 값 유지 기준과 수집 체크리스트 점검 완료
- HWPX 보고서 4종 수동 preview 서식 gap log 기준 정리 완료
- 저장소 밖 실제 양식 후보 수동 절차와 보류 조건 재정렬 완료
- `docs/128_external_hwpx_candidate_manual_procedure_and_hold_criteria.md`와 관련 체크리스트 작성 완료
- renderer, normalizer, fixture, routing, HWPX payload, output 변경 없이 문서 기준으로만 점검 완료

## 확인 대상

- `docs/128_external_hwpx_candidate_manual_procedure_and_hold_criteria.md`
- `checklists/external_hwpx_candidate_manual_procedure_checklist.md`
- `templates/hwpx/local_template_policy.md`
- `templates/hwpx/README.md`
- `docs/53_real_hwpx_template_intake_safety_procedure.md`
- `docs/58_external_hwpx_placeholder_conversion_runbook.md`
- `docs/112_phase3_external_hwpx_and_manual_preview_criteria.md`
- `docs/127_hwpx_manual_preview_gap_log_criteria.md`
- `docs/72_dry_run_artifact_retention_policy.md`
- `checklists/real_hwpx_template_intake_checklist.md`
- `checklists/external_hwpx_placeholder_conversion_checklist.md`
- `checklists/hwpx_rendered_output_manual_review_checklist.md`
- `checklists/before_automation_checklist.md`
- `.gitignore`
- `templates/hwpx/.gitignore`
- `renderers/hwpx_renderer/output/.gitignore`
- `normalizers/output/.gitignore`
- `README.md`
- `AGENTS.md`

## 검토 항목

1. `templates/hwpx/*.hwpx`와 `templates/hwpx/*.hwp`가 Git 제외 상태인지 반복 확인 기준이 명확한지 확인
2. `renderers/hwpx_renderer/output/*`와 `normalizers/output/*` 산출물 제외 기준이 서로 충돌하지 않는지 확인
3. GitHub Desktop Changes에 HWP/HWPX/output/임시 파일이 보이면 즉시 중단하는 기준이 충분한지 확인
4. local placeholder 템플릿, output 산출물, dry-run summary, gap log 기록 대상이 구분되는지 확인
5. 실제 원본, 비식별 작업 복사본, placeholder 후보를 Git 제외 기준에서 혼동하지 않는지 확인
6. `.gitignore` 자체를 변경해야 하는지 먼저 판단하고, 변경이 필요 없으면 문서 기준으로만 정리
7. HWPX 보고서 4종 반복 preview 또는 수동 리허설 때 확인할 Git 제외 체크 순서를 정리
8. 코드, fixture, routing, HWPX payload, output 변경이 필요 없는지 판단
9. 필요한 경우 최소 범위 문서 또는 체크리스트만 보강
10. 필요한 경우 README, AGENTS, NEXT_STEP을 최소 범위로 갱신

## 작업 제한

- 실제 기관 양식 사용 금지
- 실제 기관 HWPX/HWP 원본 Git 추가 금지
- 실제 문서 원문 사용 금지
- 실제 개인정보 또는 내부 운영정보 사용 금지
- 실제 문서번호, 기관명, 담당자명, 수신자명 기록 금지
- 실제 서식값 임의 생성 금지
- 폰트 파일 저장소 추가 금지
- HWPX output 재생성 금지
- Email/API/Make.com 연동 금지
- `missing_fields` 자동 제외 금지
- routing 결과 변경 금지
- HWPX payload 반영 금지
- `placeholder_confirmed_values` normalizer 연결 금지
- fixture JSON 추가 금지
- renderer 또는 normalizer 코드 변경 금지
- 실제 계정, 실제 수신자, 실제 첨부, 실제 API 요청 생성 금지

## 완료 조건

- local template policy와 Git 제외 상태 반복 검증 기준 정리
- 로컬 HWPX 템플릿, renderer output, normalizer output, dry-run summary의 Git 제외 기준 구분
- GitHub Desktop Changes 확인 순서와 즉시 중단 조건 정리
- 실제 원본, 개인정보, 기관정보, 문서번호 미포함 여부 확인
- `.gitignore` 변경 필요 여부 판단
- 현재 단계에서 코드 변경이 필요한지 판단
- 필요한 경우 관련 문서 또는 체크리스트 최소 범위 갱신
- README 최신화 필요 여부 판단
- AGENTS 최신화 필요 여부 판단
- 보안 검수 결과 재확인
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

현재 추천은 코드 변경 없이 local template policy와 Git 제외 상태 반복 검증 기준을 문서로 정리하는 것입니다. 실제 기관 HWPX 원본 투입, HWPX output 재생성, renderer 코드 변경, APIㆍMake.comㆍEmail 연동 구현은 계속 보류합니다.
