# Superpowers 재적용 후 프로젝트 재정비 요약

## 목적

Superpowers 계열 작업 skill을 재적용한 뒤, 현재 저장소의 실제 파일 상태를 기준으로 프로젝트 진입점 문서와 다음 작업 방향을 다시 정리합니다.

이 문서는 새 기능 구현 문서가 아니라, 지금까지 쌓인 문서와 PoC 결과가 서로 같은 방향을 가리키는지 확인하기 위한 재정비 기록입니다.

## 현재 저장소 기준 핵심 상태

- Phase 1 문서화와 안전 기준 정리는 완료된 상태로 봅니다.
- HWPX 보고서 4종은 placeholder 기반 로컬 템플릿 치환과 한컴 수동 검수를 완료했습니다.
- `normalizers/`에는 비식별 입력 정규화, 보안 필터, HWPX payload mapper, payload validation, renderer dry-run 최소 PoC가 있습니다.
- mapped HWPX 보고서 4종 output은 로컬 검증 산출물이며 실제 업무용 문서가 아닙니다.
- 로컬 HWPX 템플릿과 output 산출물은 Git 제외 상태를 유지해야 합니다.
- 실제 기관 양식 원본, 실제 공문 원문, 실제 개인정보, 실제 내부 운영정보는 저장소에 추가하지 않습니다.

## 현재 단계 판단

현재도 API, Make.com, Email 자동화로 넘어가는 단계가 아닙니다.

이 문서는 Superpowers 재적용 직후의 Phase 2 재정비 기록입니다. 최신 기준에서는 Phase 2 최소 PoC와 Phase 3 안전 게이트 문서화를 마무리했고, Phase 4 문서 템플릿 안정화 진입 판단까지 완료했습니다.

최신 프로젝트 방향 재확인과 구형 문서 업데이트 기준은 `docs/124_project_direction_and_legacy_update_review.md`를 따르며, HWPX template manifest와 공통 placeholder 정합성 점검 결과는 `docs/125_hwpx_template_manifest_placeholder_consistency_review.md`를, style profile 확인 필요 값 유지 기준은 `docs/126_style_profile_confirmation_value_collection_criteria.md`를, HWPX 수동 preview gap log 기준은 `docs/127_hwpx_manual_preview_gap_log_criteria.md`를, 저장소 밖 실제 양식 후보 수동 절차와 보류 조건은 `docs/128_external_hwpx_candidate_manual_procedure_and_hold_criteria.md`를, local template Git 제외 반복 검증 기준은 `docs/129_local_template_gitignore_repeat_verification_criteria.md`를, Phase 4 문서 템플릿 안정화 통합 점검은 `docs/130_phase4_template_stabilization_integrated_review.md`를 따릅니다.

Phase 2 최소 PoC의 목적은 다음과 같습니다.

- 비식별 업무 지시를 안전한 구조로 정규화
- 보안 필터로 위험 입력 차단 또는 검토 라우팅
- HWPX 보고서 4종 payload로 안전하게 매핑
- template/output Git 제외 상태 유지
- 사람이 한컴에서 열람하고 최종 판단하는 흐름 유지

## 재정비한 진입점

이번 재정비에서 기준 문서로 맞춘 파일은 다음과 같습니다.

- `AGENTS.md`
- `README.md`
- `docs/00_project_overview.md`
- `docs/00_chatgpt_handoff.md`
- `renderers/README.md`
- `tasks/NEXT_STEP.md`

## Superpowers 적용 방식

Superpowers 계열 skill은 작업 흐름을 보조하는 절차 도구로 봅니다.

이 저장소에서는 다음 우선순위를 유지합니다.

1. 사용자 명시 지시
2. 저장소의 실제 파일 상태
3. `AGENTS.md`와 최신 `docs/`, `tasks/NEXT_STEP.md`
4. Superpowers 계열 작업 절차

따라서 skill이 작업 속도와 검증 습관을 보강하더라도, 실제 원문 금지, 개인정보 금지, 로컬 HWPX Git 제외, 운영 자동화 보류 원칙은 바뀌지 않습니다.

## 현재 발견한 정비 필요 지점

| 구분 | 상태 | 조치 |
|---|---|---|
| README 현재 단계 | Phase 1 중심 표현이 남아 있었음 | Phase 1 완료 및 Phase 2 최소 PoC 준비 상태로 갱신 |
| AGENTS 현재 범위 | 최신 normalizers와 mapped HWPX 검증이 부족하게 표현됨 | 현재 진행 기준과 Codex 작업 방식 보강 |
| `docs/00_project_overview.md` | 다음 단계가 입력 정규화와 보안 필터 설계로 남아 있었음 | 이미 완료된 범위와 다음 helper 작업으로 갱신 |
| `docs/00_chatgpt_handoff.md` | Phase 2 보안 필터 문서 확정 전 상태가 남아 있었음 | 최신 완료 상태와 다음 작업으로 갱신 |
| `renderers/README.md` | 실제 렌더러 코드를 작성하지 않는다고 되어 있었음 | placeholder 기반 PoC 렌더러 보관 위치로 갱신 |
| `tasks/NEXT_STEP.md` | helper 범위 정리 단계에 머물러 있었음 | 다음 작업을 read-only helper 최소 구현으로 정리했고, 후속 작업에서 fixture schema 검토로 갱신 |

## 다음 권장 작업

이 문서 작성 시점의 다음 작업은 `placeholder_confirmed_values` read-only 판정 helper 최소 구현이었습니다.

후속 작업에서 해당 helper는 `docs/91_placeholder_confirmed_values_helper_result.md` 기준으로 최소 구현되었습니다.

현재 최신 다음 작업은 `tasks/NEXT_STEP.md` 기준으로 저장소 밖 한컴 preview 결과를 실제값 없는 gap log로 기록하는 것입니다.

최소 구현 원칙은 다음과 같습니다.

- `missing_fields` 생성 결과 변경 없음
- routing 결과 변경 없음
- HWPX 렌더링 결과 변경 없음
- helper 판정 결과는 검토용 정보로만 사용
- 실제값 의심 패턴과 충돌하면 보안 필터 판단 우선
- 기존 fixture 회귀 테스트 통과

## 보안 재확인

이번 재정비는 문서 정리입니다.

- 실제 개인정보 추가 없음
- 실제 기관명 또는 업체명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 HWPX 원본 추가 없음
- 실제 공문 원문 추가 없음
- API, Make.com, Email 자동화 구현 없음

## 결론

현재 저장소는 보고서 중심 HWPX 자동화 방향을 유지하면서 Phase 4 문서 템플릿 안정화 검토로 넘어간 상태입니다.

현재 후속 작업은 운영 자동화가 아니라 저장소 밖 한컴 preview 결과를 실제값 없는 gap log로 기록하는 것입니다.
