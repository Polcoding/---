# 다음 작업

## 목표

style profile의 `[확인 필요]` 값 유지 기준과 기관 표준 서식값 수집 체크리스트를 문서로 점검합니다.

실제 서식값을 확정하거나 실제 기관 HWPX 원본을 투입하는 단계가 아닙니다. 확인되지 않은 글꼴, 자간, 줄간격, 문단 간격, 표 서식, 번호 들여쓰기 값은 계속 `[확인 필요]`로 유지합니다.

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
- 프로젝트 방향 재확인 및 구형 진입점 문서 업데이트 검토 완료
- HWPX 보고서 4종 template manifest와 공통 placeholder 정합성 점검 완료
- `one_page_report` style profile 후보를 `[확인 필요]` 상태로 추가 완료
- 입력 필드와 HWPX placeholder 이름이 다른 항목의 명시 매핑 문서화 완료
- `docs/125_hwpx_template_manifest_placeholder_consistency_review.md`와 관련 체크리스트 작성 완료
- renderer, normalizer, fixture, routing, HWPX payload, output 변경 없이 문서 기준으로만 점검 완료

## 확인 대상

- `docs/125_hwpx_template_manifest_placeholder_consistency_review.md`
- `checklists/hwpx_template_manifest_placeholder_consistency_checklist.md`
- `docs/40_hwpx_institution_style_values_review.md`
- `templates/hwpx/style_profile_manifest.md`
- `checklists/hwpx_institution_style_value_collection_checklist.md`
- `templates/hwpx/local_template_policy.md`
- `templates/hwpx/template_manifest.md`
- `templates/hwpx/README.md`
- `checklists/before_automation_checklist.md`
- `README.md`
- `AGENTS.md`

## 검토 항목

1. style profile의 `[확인 필요]` 값이 실제 확정값처럼 취급되지 않는지 확인
2. `style_one_page_report_basic`, `style_project_plan_basic`, `style_result_report_basic`, `style_review_report_basic`의 미확정 상태가 일관적인지 확인
3. 수집 체크리스트가 실제 기관명, 실제 문서번호, 실제 HWPX 원본, 실제 공문 원문, 개인정보 입력을 유도하지 않는지 확인
4. 글꼴, 자간, 줄간격, 문단 간격, 번호 들여쓰기, 표 서식, 여백 값이 임의 생성되지 않는지 확인
5. 수집 결과를 Git에 바로 기록하지 않고 비식별 요약값 또는 placeholder 기준으로만 반영하도록 제한하는지 확인
6. 로컬 placeholder HWPX 템플릿과 output 산출물의 Git 제외 원칙이 유지되는지 확인
7. 실제 서식값 확인 전에도 다음 단계에서 수동 점검이 가능한 체크리스트 구조인지 확인
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

- style profile `[확인 필요]` 값 유지 기준 문서화
- 기관 표준 서식값 수집 체크리스트 보강 여부 판단
- 보고서 4종 style profile 후보의 미확정 상태 유지 여부 확인
- 실제 원본, 개인정보, 기관정보, 문서번호 미포함 여부 확인
- local template policy와 Git 제외 원칙 유지 여부 확인
- 현재 단계에서 코드 변경이 필요한지 판단
- 필요한 경우 관련 문서 또는 체크리스트 최소 범위 갱신
- README 최신화 필요 여부 판단
- AGENTS 최신화 필요 여부 판단
- 보안 검수 결과 재확인
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

현재 추천은 코드 변경 없이 style profile의 `[확인 필요]` 값 유지 기준과 기관 표준 서식값 수집 체크리스트를 정리하는 것입니다. 실제 기관 HWPX 원본 투입, HWPX output 재생성, renderer 코드 변경, APIㆍMake.comㆍEmail 연동 구현은 계속 보류합니다.
