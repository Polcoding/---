# 다음 작업

## [사용자 확인 필요]

실제 양식 수동 리허설을 진행하려면 사용자가 먼저 저장소 밖 준비 여부를 확인해야 합니다.

Codex는 사용자가 준비 완료라고 명시하기 전까지 실제 기관 HWPX/HWP 원본, 실제 output 재생성, renderer 코드 변경, 외부 연동 구현으로 넘어가지 않습니다.

## 목표

`docs/131_actual_hwpx_manual_rehearsal_user_confirmation_packet.md` 기준으로 실제 양식 수동 리허설 전 사용자 확인 항목을 점검합니다.

이번 단계는 실제 기관 HWPX 원본을 저장소에 넣거나 실제 HWPX output을 재생성하는 단계가 아닙니다. 사용자가 저장소 밖 로컬 환경에서 원본 위치, 작업 복사본, 식별 요소 제거, GitHub Desktop Changes 상태를 확인해야 합니다.

## 현재 완료 상태

- HWPX 보고서 4종 placeholder 기반 렌더링 및 수동 검수 완료
- 입력 정규화, 보안 필터, payload mapper, validation, dry-run PoC 작성 완료
- mapped HWPX 보고서 4종 렌더링 완료
- Phase 2 최소 PoC 문서 기준 마무리 가능 판단 완료
- Phase 3 진입 조건 및 안전 게이트 문서화 완료
- Phase 3 외부 연동 구현 범위 승인 판단 완료
- Phase 3 마무리 판단 및 Phase 4 진입 여부 결정 완료
- Phase 4 문서 템플릿 안정화 진입 판단 완료
- HWPX 보고서 4종 template manifest와 공통 placeholder 정합성 점검 완료
- style profile `[확인 필요]` 값 유지 기준과 수집 체크리스트 점검 완료
- HWPX 보고서 4종 수동 preview 서식 gap log 기준 정리 완료
- 저장소 밖 실제 양식 후보 수동 절차와 보류 조건 재정렬 완료
- local template policy와 Git 제외 상태 반복 검증 기준 정리 완료
- Phase 4 문서 템플릿 안정화 통합 점검 완료
- 실제 양식 수동 리허설 사용자 확인 패킷과 gap log 빈 양식 정리 완료
- renderer, normalizer, fixture, routing, HWPX payload, output 변경 없이 문서 기준으로만 점검 완료

## 확인 대상

- `docs/131_actual_hwpx_manual_rehearsal_user_confirmation_packet.md`
- `checklists/actual_hwpx_manual_rehearsal_user_confirmation_packet_checklist.md`
- `docs/127_hwpx_manual_preview_gap_log_criteria.md`
- `docs/128_external_hwpx_candidate_manual_procedure_and_hold_criteria.md`
- `docs/129_local_template_gitignore_repeat_verification_criteria.md`
- `docs/130_phase4_template_stabilization_integrated_review.md`
- `templates/hwpx/local_template_policy.md`
- `README.md`
- `AGENTS.md`

## 사용자가 확인할 항목

1. 실제 원본이 저장소 밖 로컬 위치에만 있는지 확인
2. 작업 복사본도 저장소 밖 로컬 위치에만 있는지 확인
3. 실제 본문, 기관명, 문서번호, 결재선, 직인, 로고, 담당자 정보가 제거되었는지 확인
4. 문서 속성, 미리보기, 마지막 저장자 정보에 실제값이 남지 않았는지 확인
5. GitHub Desktop Changes에 HWP/HWPX/output 파일이 보이지 않는지 확인
6. gap log에 실제 원문, 실제 파일명, 실제 기관명, 실제 문서번호 없이 기록 가능한지 확인
7. style profile 값은 아직 `[확인 필요]`로 유지할 수 있는지 확인

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
- routing 결과 변경 금지
- HWPX payload 반영 금지
- fixture JSON 추가 금지
- renderer 또는 normalizer 코드 변경 금지
- `.gitignore` 변경은 실제 필요성이 확인된 경우에만 검토

## 완료 조건

- 사용자가 `docs/131`의 `[사용자 확인 필요]` 항목을 확인
- GitHub Desktop Changes에 HWP/HWPX/output 파일이 없음을 사용자가 확인
- 실제 원본, 개인정보, 기관정보, 문서번호가 저장소 문서에 포함되지 않음을 확인
- local template과 output Git 제외 상태 유지 여부 확인
- 실제 양식 수동 리허설을 진행할지, 보류할지 판단
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

사용자가 저장소 밖 준비 완료와 GitHub Desktop Changes 이상 없음을 확인하면, 다음 단계는 저장소 밖 실제 양식 수동 리허설 결과를 gap log 형식으로 기록하는 것입니다.

준비가 안 되었거나 HWP/HWPX/output 파일이 Changes에 보이면 즉시 보류합니다. 실제 기관 HWPX 원본 투입, HWPX output 재생성, renderer 코드 변경, APIㆍMake.comㆍEmail 연동 구현은 계속 보류합니다.
