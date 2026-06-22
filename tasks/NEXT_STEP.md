# 다음 작업

## 목표

실제 양식 수동 리허설을 바로 실행하지 않고, 사용자가 저장소 밖에서 확인해야 할 항목과 gap log 빈 양식을 눈에 잘 보이도록 문서로 정리합니다.

이번 단계는 실제 기관 HWPX 원본을 저장소에 넣거나 실제 HWPX output을 재생성하는 단계가 아닙니다. Phase 4 통합 점검 결과를 바탕으로 사용자 확인 패킷을 만들고, 실제 양식 수동 리허설이 필요할 때 빠뜨리지 말아야 할 확인 지점을 분리합니다.

## 현재 완료 상태

- HWPX 보고서 4종 placeholder 기반 렌더링 및 수동 검수 완료
- 입력 정규화, 보안 필터, payload mapper, validation, dry-run PoC 작성 완료
- mapped HWPX 보고서 4종 렌더링 완료
- `placeholder_confirmed_values` helper와 fixture 검증 완료
- metadata는 코드에 연결하지 않고 문서 기준으로 유지하기로 결정
- `missing_fields` 생성 규칙 고정 및 사용자 표시 기준 문서화 완료
- Phase 2 최소 PoC 문서 기준 마무리 가능 판단 완료
- Phase 3 진입 조건 및 안전 게이트 문서화 완료
- Phase 3 외부 연동 구현 범위 승인 판단 완료
- Phase 3 마무리 판단 및 Phase 4 진입 여부 결정 완료
- Phase 4 문서 템플릿 안정화 진입 판단 완료
- 프로젝트 방향 재확인 및 구형 진입점 문서 업데이트 검토 완료
- HWPX 보고서 4종 template manifest와 공통 placeholder 정합성 점검 완료
- style profile `[확인 필요]` 값 유지 기준과 수집 체크리스트 점검 완료
- HWPX 보고서 4종 수동 preview 서식 gap log 기준 정리 완료
- 저장소 밖 실제 양식 후보 수동 절차와 보류 조건 재정렬 완료
- local template policy와 Git 제외 상태 반복 검증 기준 정리 완료
- Phase 4 문서 템플릿 안정화 통합 점검 완료
- 실제 양식 수동 리허설은 조건부 진입 가능하되, 실제 원본 투입과 output 재생성은 계속 보류
- renderer, normalizer, fixture, routing, HWPX payload, output 변경 없이 문서 기준으로만 점검 완료

## 확인 대상

- `docs/127_hwpx_manual_preview_gap_log_criteria.md`
- `docs/128_external_hwpx_candidate_manual_procedure_and_hold_criteria.md`
- `docs/129_local_template_gitignore_repeat_verification_criteria.md`
- `docs/130_phase4_template_stabilization_integrated_review.md`
- `checklists/hwpx_manual_preview_gap_log_checklist.md`
- `checklists/external_hwpx_candidate_manual_procedure_checklist.md`
- `checklists/local_template_gitignore_repeat_verification_checklist.md`
- `checklists/phase4_template_stabilization_integrated_review_checklist.md`
- `templates/hwpx/README.md`
- `templates/hwpx/local_template_policy.md`
- `README.md`
- `AGENTS.md`

## 검토 항목

1. 사용자가 실제 양식 수동 리허설 전에 확인해야 할 항목이 눈에 잘 보이는지 확인
2. 저장소 밖 실제 원본, 작업 복사본, placeholder 후보의 위치와 역할을 다시 구분
3. GitHub Desktop Changes에 보이면 안 되는 항목을 사용자 확인용으로 정리
4. gap log 빈 양식에 실제 원문, 실제 파일명, 실제 기관정보를 쓰지 않도록 제한
5. HWPX 보고서 4종별 수동 preview 확인 항목을 사용자 체크 형태로 정리
6. 실제 양식 수동 리허설 보류 조건과 중단 조건을 다시 분리
7. 코드 변경이 필요 없으면 문서 기준으로만 정리
8. 필요한 경우 관련 문서 또는 체크리스트 최소 범위만 보강
9. 필요한 경우 README, AGENTS, NEXT_STEP을 최소 범위로 갱신

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
- `.gitignore` 변경은 실제 필요성이 확인된 경우에만 검토
- 실제 계정, 실제 수신자, 실제 첨부, 실제 API 요청 생성 금지

## 완료 조건

- 실제 양식 수동 리허설 사용자 확인 패킷 작성
- HWPX 보고서 4종 gap log 빈 양식 또는 기록 기준 정리
- 실제 원본, 개인정보, 기관정보, 문서번호 미포함 여부 확인
- local template과 output Git 제외 상태 유지 여부 확인
- 현재 단계에서 코드 또는 `.gitignore` 변경이 필요한지 판단
- 필요한 경우 관련 문서 또는 체크리스트 최소 범위 갱신
- README 최신화 필요 여부 판단
- AGENTS 최신화 필요 여부 판단
- 보안 검수 결과 재확인
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

현재 추천은 실제 양식 수동 리허설 사용자 확인 패킷과 gap log 빈 양식을 먼저 정리하는 것입니다. 실제 기관 HWPX 원본 투입, HWPX output 재생성, renderer 코드 변경, APIㆍMake.comㆍEmail 연동 구현은 계속 보류합니다.
