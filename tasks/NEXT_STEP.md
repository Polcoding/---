# 다음 작업

## 목표

HWPX 보고서 4종 template manifest와 공통 placeholder 정합성을 문서로 점검합니다.

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
- Phase 4는 실제 구현이 아니라 HWPX 보고서 4종 문서 템플릿 안정화 검토로만 제한

## 확인 대상

- `docs/123_phase4_template_stabilization_entry_judgment.md`
- `checklists/phase4_template_stabilization_entry_judgment_checklist.md`
- `docs/54_hwpx_common_placeholder_design.md`
- `docs/60_hwpx_report_input_requirements.md`
- `docs/84_hwpx_report_user_input_templates.md`
- `docs/40_hwpx_institution_style_values_review.md`
- `templates/hwpx/template_manifest.md`
- `templates/hwpx/local_template_policy.md`
- `templates/hwpx/style_profile_manifest.md`
- `checklists/before_automation_checklist.md`
- `README.md`
- `AGENTS.md`

## 검토 항목

1. template manifest의 HWPX 보고서 4종 문서유형이 공통 placeholder 설계와 충돌하지 않는지 확인
2. `one_page_report`, `project_plan`, `result_report`, `review_report`별 핵심 placeholder가 입력 요구사항과 대응되는지 확인
3. `docs/84` 사용자 입력 템플릿이 실제 원문, 개인정보, 기관명, 문서번호 입력을 유도하지 않는지 확인
4. `missing_fields`, `[확인 필요]`, 안전한 빈 문자열 처리 기준이 문서 간 흔들리지 않는지 확인
5. `style_profile_manifest`가 확인되지 않은 서식값을 임의 확정하지 않는지 확인
6. `local_template_policy`가 실제 HWPX/HWP 파일 Git 제외 원칙을 충분히 유지하는지 확인
7. 실제 기관 HWPX 원본이나 output 재생성 없이 문서 기준으로만 점검 가능한지 판단
8. 코드, fixture, routing, HWPX payload, output 변경이 필요 없는지 판단
9. 필요한 경우 최소 범위 문서 또는 체크리스트만 보강
10. 필요한 경우 README, AGENTS, NEXT_STEP을 최소 범위로 갱신

## 작업 제한

- 실제 기관 양식 사용 금지
- 실제 문서 원문 사용 금지
- 실제 개인정보 또는 내부 운영정보 사용 금지
- 실제 HWPX 템플릿 Git 추가 금지
- HWPX output 재생성 금지
- Email/API/Make.com 연동 금지
- 확인되지 않은 서식값 임의 생성 금지
- `missing_fields` 자동 제외 금지
- routing 결과 변경 금지
- HWPX payload 반영 금지
- `placeholder_confirmed_values` normalizer 연결 금지
- fixture JSON 추가 금지
- renderer 또는 normalizer 코드 변경 금지
- 실제 계정, 실제 수신자, 실제 첨부, 실제 API 요청 생성 금지

## 완료 조건

- HWPX 보고서 4종 template manifest와 공통 placeholder 정합성 점검 결과 문서화
- 문서 유형별 placeholder와 입력 요구사항 대응 여부 정리
- 누락값, `[확인 필요]`, `missing_fields` 표시 기준 유지 여부 확인
- style profile 미확정 값 유지 여부 확인
- local template policy와 Git 제외 원칙 유지 여부 확인
- 현재 단계에서 코드 변경이 필요한지 판단
- 필요한 경우 관련 문서 또는 체크리스트 최소 범위 갱신
- README 최신화 필요 여부 판단
- AGENTS 최신화 필요 여부 판단
- 보안 검수 결과 재확인
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

현재 추천은 코드 변경 없이 HWPX 보고서 4종 template manifest와 공통 placeholder 정합성을 문서로 점검하는 것입니다. 실제 API, Make.com, Email 연동 구현과 실제 기관 HWPX 원본 투입은 계속 보류합니다.
