# 다음 작업

## 목표

저장소 밖 실제 양식 후보를 다룰 때의 수동 절차와 보류 조건을 HWPX 보고서 4종 기준으로 재정렬합니다.

실제 기관 HWPX 원본을 저장소에 넣거나 실제 HWPX output을 재생성하는 단계가 아닙니다. 기존 안전 절차, local template policy, 수동 preview gap log 기준을 서로 연결해 실제 양식 후보를 다루기 전 중단 조건을 더 분명하게 정리합니다.

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
- `docs/127_hwpx_manual_preview_gap_log_criteria.md`와 관련 체크리스트 작성 완료
- renderer, normalizer, fixture, routing, HWPX payload, output 변경 없이 문서 기준으로만 점검 완료

## 확인 대상

- `docs/127_hwpx_manual_preview_gap_log_criteria.md`
- `checklists/hwpx_manual_preview_gap_log_checklist.md`
- `docs/53_real_hwpx_template_intake_safety_procedure.md`
- `docs/58_external_hwpx_placeholder_conversion_runbook.md`
- `docs/112_phase3_external_hwpx_and_manual_preview_criteria.md`
- `templates/hwpx/local_template_policy.md`
- `templates/hwpx/README.md`
- `checklists/real_hwpx_template_intake_checklist.md`
- `checklists/external_hwpx_placeholder_conversion_checklist.md`
- `checklists/hwpx_rendered_output_manual_review_checklist.md`
- `README.md`
- `AGENTS.md`

## 검토 항목

1. 실제 양식 후보를 저장소 밖에서만 다루는 절차가 충분히 명확한지 확인
2. 실제 원본, 비식별 복사본, placeholder 후보, gap log의 역할이 구분되는지 확인
3. GitHub Desktop Changes에 HWP/HWPX/output 파일이 보이면 즉시 중단하는 기준이 유지되는지 확인
4. C/D등급 또는 실제 원문ㆍ개인정보ㆍ문서번호가 섞였을 때 보류 조건이 명확한지 확인
5. placeholder 후보 전환 전 제거해야 할 식별 요소가 충분히 정리되어 있는지 확인
6. 수동 preview gap log와 실제 양식 후보 절차가 연결되는지 확인
7. 실제 HWPX output 재생성 없이 문서 기준으로만 정리 가능한지 판단
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

- 저장소 밖 실제 양식 후보 수동 절차 재정렬
- 실제 원본, 비식별 복사본, placeholder 후보, gap log 역할 구분
- 보류 조건과 즉시 중단 조건 정리
- 실제 원본, 개인정보, 기관정보, 문서번호 미포함 여부 확인
- local template policy와 Git 제외 원칙 유지 여부 확인
- 현재 단계에서 코드 변경이 필요한지 판단
- 필요한 경우 관련 문서 또는 체크리스트 최소 범위 갱신
- README 최신화 필요 여부 판단
- AGENTS 최신화 필요 여부 판단
- 보안 검수 결과 재확인
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

현재 추천은 코드 변경 없이 저장소 밖 실제 양식 후보를 다룰 때의 수동 절차와 보류 조건을 HWPX 보고서 4종 기준으로 재정렬하는 것입니다. 실제 기관 HWPX 원본 투입, HWPX output 재생성, renderer 코드 변경, APIㆍMake.comㆍEmail 연동 구현은 계속 보류합니다.
