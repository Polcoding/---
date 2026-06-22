# Phase 4 문서 템플릿 안정화 통합 점검

## 목적

이 문서는 Phase 4 문서 템플릿 안정화 작업 묶음을 통합 점검하고, 실제 양식 수동 리허설로 넘어갈 수 있는지 문서 기준으로 판단합니다.

이번 단계는 실제 기관 HWPX 원본을 저장소에 넣거나 실제 HWPX output을 재생성하는 단계가 아닙니다. renderer, normalizer, fixture, routing, HWPX payload, output, `.gitignore`도 변경하지 않습니다.

## 확인 대상

- `docs/123_phase4_template_stabilization_entry_judgment.md`
- `docs/124_project_direction_and_legacy_update_review.md`
- `docs/125_hwpx_template_manifest_placeholder_consistency_review.md`
- `docs/126_style_profile_confirmation_value_collection_criteria.md`
- `docs/127_hwpx_manual_preview_gap_log_criteria.md`
- `docs/128_external_hwpx_candidate_manual_procedure_and_hold_criteria.md`
- `docs/129_local_template_gitignore_repeat_verification_criteria.md`
- `docs/133_hwpx_only_table_frame_decision.md`
- `checklists/phase4_template_stabilization_entry_judgment_checklist.md`
- `checklists/project_direction_and_legacy_update_review_checklist.md`
- `checklists/hwpx_template_manifest_placeholder_consistency_checklist.md`
- `checklists/style_profile_confirmation_value_collection_checklist.md`
- `checklists/hwpx_manual_preview_gap_log_checklist.md`
- `checklists/external_hwpx_candidate_manual_procedure_checklist.md`
- `checklists/local_template_gitignore_repeat_verification_checklist.md`
- `templates/hwpx/README.md`
- `templates/hwpx/local_template_policy.md`
- `templates/hwpx/template_manifest.md`
- `templates/hwpx/style_profile_manifest.md`
- `README.md`
- `AGENTS.md`
- `tasks/NEXT_STEP.md`

## 통합 판단 결론

현재 저장소 기준으로 Phase 4 문서 템플릿 안정화 작업 묶음은 서로 충돌하지 않습니다.

실제 양식 수동 리허설은 문서 기준으로 조건부 진입 가능합니다. 다만 이는 실제 원본을 저장소에 넣거나 실제 output을 재생성해도 된다는 의미가 아닙니다.

진입 가능 범위:

- 사용자가 저장소 밖 로컬 환경에서 실제 양식 후보를 직접 확인
- 실제 원본을 직접 수정하지 않고 저장소 밖 작업 복사본으로만 확인
- 실제 내용과 식별 요소를 제거한 뒤 placeholder 후보로만 검토
- 로컬 HWP/HWPX 템플릿과 output 산출물은 Git 제외 상태 유지
- gap log는 실제 원문 없이 문서유형, 항목, 증상, 심각도, 후속 조치만 기록
- 표가 포함된 문서는 `table_scope: frame_only` 기준으로 표 틀만 확인

계속 보류하는 범위:

- 실제 기관 HWPX/HWP 원본 Git 추가
- 실제 HWPX output 재생성
- 실제 원문, 실제 개인정보, 실제 기관정보 기반 검증
- renderer, normalizer, fixture, routing, HWPX payload 변경
- style profile 미확정값의 임의 확정
- Email, API, Make.com 실제 연동 구현
- HWPX 표 내부 실제 데이터 자동 입력 또는 Excel/한셀 자동 연동

## Phase 4 작업 묶음 정합성

| 작업 묶음 | 기준 문서 | 통합 판단 |
|---|---|---|
| Phase 4 범위 제한 | `docs/123` | 실제 구현이 아닌 문서 템플릿 안정화로 제한되어 정합 |
| 프로젝트 방향과 구형 문서 처리 | `docs/124` | HWPX 보고서 우선, Email/XLSX 보조, 구형 문서 보존 기준 정합 |
| template manifest와 placeholder | `docs/125` | HWPX 보고서 4종 template_id, placeholder, 공통 메타 기준 정합 |
| style profile 미확정값 | `docs/126` | `[확인 필요]` 유지와 상태 전환 gate 정합 |
| 수동 preview gap log | `docs/127` | 실제값 없이 증상과 후속 조치만 기록하는 기준 정합 |
| 저장소 밖 실제 양식 후보 절차 | `docs/128` | 실제 원본, 작업 복사본, placeholder 후보, gap log 분리 정합 |
| local template Git 제외 반복 검증 | `docs/129` | 폴더별 `.gitignore` 기준으로 HWPX/output 제외 상태 유지 |
| HWPX 일원화와 표 틀 결정 | `docs/133` | HWPX 최종 형식 유지, 표 데이터는 Excel/한셀 연동 후보로 분리 |

## 실제 양식 수동 리허설 진입 조건

다음 조건을 모두 만족할 때만 실제 양식 수동 리허설을 진행할 수 있습니다.

1. 리허설 대상 문서유형이 `one_page_report`, `project_plan`, `result_report`, `review_report` 중 하나임
2. 실제 원본과 작업 복사본을 저장소 밖 로컬 위치에서만 취급함
3. A/B/C/D 보안등급 분류를 먼저 수행함
4. C등급은 내부 참고만 가능하고, D등급은 외부 처리와 샘플화 모두 금지함
5. 실제 본문, 기관명, 문서번호, 결재선, 직인, 로고, 담당자 정보, 문서 속성의 식별 요소를 제거함
6. placeholder 후보에도 실제 대상을 추정할 수 있는 이름이나 값이 남지 않음
7. `templates/hwpx/*.hwpx`, `renderers/hwpx_renderer/output/*`, `normalizers/output/*`가 GitHub Desktop Changes에 보이지 않음
8. style profile 값은 확인 전까지 `[확인 필요]` 상태로 유지함
9. gap log에는 실제 원문, 실제 파일명, 실제 기관명, 실제 문서번호를 기록하지 않음
10. 사용자 수동 확인이 필요한 항목을 명확히 표시함
11. 표가 포함된 문서는 표 내부 값이 아니라 표 위치, 폭, 줄바꿈, 겹침, 여백만 확인함

## 즉시 보류 조건

다음 중 하나라도 있으면 실제 양식 수동 리허설로 진행하지 않습니다.

| 보류 조건 | 처리 |
|---|---|
| 실제 원본 또는 작업 복사본이 저장소 안에 있음 | 즉시 중단 |
| GitHub Desktop Changes에 HWP/HWPX/output 파일이 보임 | Git 제외 상태 확인 전 중단 |
| 실제 개인정보, 기관정보, 문서번호, 내부 운영정보 의심 | 보안 검토 전 중단 |
| C/D등급 또는 판단 애매 자료 포함 | 더 보수적 등급 적용 후 보류 |
| 직인, 로고, 결재선, 문서 속성의 식별 요소 잔존 | placeholder 후보 전환 불가 |
| style profile 값을 근거 없이 확정하려 함 | `[확인 필요]` 유지 |
| gap log에 실제 원문 또는 실제 파일명이 들어가려 함 | 기록 전 중단 |
| code, fixture, routing, payload 변경이 필요해 보임 | 별도 승인 전 보류 |
| 외부 API, Email, Make.com 연결이 필요해 보임 | 별도 보안 검토 전 보류 |

## 코드와 `.gitignore` 변경 판단

현재 단계에서는 코드 변경이 필요하지 않습니다.

변경하지 않는 항목:

- `normalizers/`
- `renderers/`
- `examples/json/`
- routing fixture
- HWPX payload mapper
- HWPX renderer output
- local HWPX template
- `.gitignore`
- API, Make.com, Email 연동 코드

root `.gitignore`는 현재 없지만, `templates/hwpx/.gitignore`, `renderers/hwpx_renderer/output/.gitignore`, `normalizers/output/.gitignore` 기준으로 local HWPX template과 output 산출물 제외가 관리되고 있습니다. 따라서 이번 단계에서 `.gitignore`를 새로 만들 필요는 없습니다.

## 사용자 확인 필요 지점

[사용자 확인 필요]

실제 양식 수동 리허설을 시작하려면 사용자가 저장소 밖에서 다음을 확인해야 합니다.

| 확인 | 항목 |
|---|---|
| [ ] | 실제 원본을 저장소 밖 로컬 위치에만 두었는가 |
| [ ] | 원본을 직접 수정하지 않고 작업 복사본을 만들었는가 |
| [ ] | 작업 복사본에서 실제 내용과 식별 요소를 제거했는가 |
| [ ] | placeholder 후보가 GitHub Desktop Changes에 보이지 않는가 |
| [ ] | 한컴 preview 결과를 실제 원문 없이 gap log 형식으로만 기록할 수 있는가 |
| [ ] | style profile 값을 아직 확정하지 않고 `[확인 필요]`로 둘 수 있는가 |

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX 원본 파일 추가 없음
- 실제 파일명, 내부 경로, 원본 양식명 추가 없음
- 폰트 파일 추가 없음
- API 키, 토큰, 인증정보 예시값 추가 없음
- Email, API, Make.com 연동 구현 없음

## 결론

Phase 4 문서 템플릿 안정화 작업 묶음은 통합 점검 기준으로 정합합니다.

실제 양식 수동 리허설은 조건부로 진입 가능합니다. 사용자가 저장소 밖에서 확인해야 할 항목과 gap log 빈 양식은 `docs/131_actual_hwpx_manual_rehearsal_user_confirmation_packet.md`에 정리했습니다.

사용자의 저장소 밖 준비 확인 완료 결과는 `docs/132_actual_hwpx_manual_rehearsal_readiness_confirmation.md`에 정리했습니다.

HWPX 일원화 유지와 표 데이터 Excel/한셀 연동 후보 분리 결정은 `docs/133_hwpx_only_table_frame_decision.md`에 정리했습니다.

다음 단계는 실제 원본 투입이나 output 재생성이 아니라, 사용자가 저장소 밖에서 확인한 한컴 preview 결과를 `table_scope: frame_only` 포함 실제값 없는 gap log로 기록하는 것입니다.
