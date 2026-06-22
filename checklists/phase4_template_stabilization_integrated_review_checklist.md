# Phase 4 문서 템플릿 안정화 통합 점검 체크리스트

## 기준 문서 확인

| 완료 | 항목 |
|---|---|
| [x] | `docs/123_phase4_template_stabilization_entry_judgment.md`를 확인했는가 |
| [x] | `docs/124_project_direction_and_legacy_update_review.md`를 확인했는가 |
| [x] | `docs/125_hwpx_template_manifest_placeholder_consistency_review.md`를 확인했는가 |
| [x] | `docs/126_style_profile_confirmation_value_collection_criteria.md`를 확인했는가 |
| [x] | `docs/127_hwpx_manual_preview_gap_log_criteria.md`를 확인했는가 |
| [x] | `docs/128_external_hwpx_candidate_manual_procedure_and_hold_criteria.md`를 확인했는가 |
| [x] | `docs/129_local_template_gitignore_repeat_verification_criteria.md`를 확인했는가 |
| [x] | `docs/133_hwpx_only_table_frame_decision.md`를 확인했는가 |
| [x] | HWPX template manifest, local template policy, style profile manifest를 확인했는가 |

## 통합 정합성 확인

| 완료 | 항목 |
|---|---|
| [x] | Phase 4가 실제 구현이 아니라 문서 템플릿 안정화 범위로 제한되어 있는가 |
| [x] | HWPX 보고서 4종 template_id, placeholder 그룹, style_profile_id가 서로 대응되는가 |
| [x] | `[확인 필요]`, `missing_fields`, 사람 검토 필요 기준이 유지되는가 |
| [x] | style profile 미확정값을 실제 확정값처럼 기록하지 않았는가 |
| [x] | 수동 preview gap log가 실제 원문 없이 기록되도록 되어 있는가 |
| [x] | 실제 원본, 작업 복사본, placeholder 후보, output, gap log의 역할이 분리되어 있는가 |
| [x] | local template과 output Git 제외 반복 검증 기준이 연결되어 있는가 |
| [x] | 표 데이터 자동화는 Excel/한셀 연동 후보로 분리하고 현재는 표 틀만 확인하도록 되어 있는가 |

## 실제 양식 수동 리허설 진입 판단

| 완료 | 항목 |
|---|---|
| [x] | 실제 양식 수동 리허설을 조건부 진입 가능으로 판단했는가 |
| [x] | 실제 원본과 작업 복사본은 저장소 밖에서만 다루도록 했는가 |
| [x] | A/B/C/D 보안등급 분류를 리허설 전 조건으로 두었는가 |
| [x] | C/D등급 또는 판단 애매 자료는 보류하도록 했는가 |
| [x] | GitHub Desktop Changes에 HWP/HWPX/output 파일이 보이면 중단하도록 했는가 |
| [x] | gap log에 실제 원문, 실제 파일명, 실제 기관명을 기록하지 않도록 했는가 |
| [x] | 표 포함 문서는 `table_scope: frame_only` 기준으로 확인하도록 했는가 |
| [x] | 사용자가 직접 확인해야 할 항목을 `[사용자 확인 필요]`로 분리했는가 |

## 계속 보류할 범위 확인

| 완료 | 항목 |
|---|---|
| [x] | 실제 기관 HWPX/HWP 원본을 Git에 추가하지 않았는가 |
| [x] | 실제 HWPX output을 재생성하지 않았는가 |
| [x] | renderer 코드를 변경하지 않았는가 |
| [x] | normalizer 코드를 변경하지 않았는가 |
| [x] | fixture JSON을 추가하거나 변경하지 않았는가 |
| [x] | routing 결과를 변경하지 않았는가 |
| [x] | HWPX payload 구조를 변경하지 않았는가 |
| [x] | `.gitignore` 파일을 변경하지 않았는가 |
| [x] | HWPX 표 내부 실제 데이터 자동 입력 또는 Excel/한셀 자동 연동을 구현하지 않았는가 |
| [x] | Email, API, Make.com 연동 구현을 하지 않았는가 |

## 보안 검수

| 완료 | 항목 |
|---|---|
| [x] | 실제 개인정보를 추가하지 않았는가 |
| [x] | 실제 기관명, 업체명, 담당자명을 추가하지 않았는가 |
| [x] | 실제 문서번호, 민원번호, 사건번호를 추가하지 않았는가 |
| [x] | 실제 날짜, 예산, 실적 수치를 추가하지 않았는가 |
| [x] | 실제 표 데이터, 물품명, 수량, 금액, 대상 목록을 추가하지 않았는가 |
| [x] | 실제 공문 원문 또는 보고서 원문을 추가하지 않았는가 |
| [x] | 실제 HWPX 원본 파일을 추가하지 않았는가 |
| [x] | 실제 내부 경로나 파일명을 추가하지 않았는가 |
| [x] | 폰트 파일을 추가하지 않았는가 |
| [x] | API 키, 토큰, 인증정보 예시값을 추가하지 않았는가 |

## 다음 단계 확인

| 완료 | 항목 |
|---|---|
| [x] | 실제 양식 수동 리허설 사용자 확인 패킷이 `docs/131`에 반영되었는가 |
| [x] | HWPX 일원화와 표 틀 우선 결정이 `docs/133`에 반영되었는가 |
| [x] | 다음 단계가 저장소 밖 한컴 preview 결과의 `table_scope: frame_only` 포함 실제값 없는 gap log 기록인가 |
| [x] | 실제 양식 수동 리허설은 사용자 저장소 밖 준비와 별도 확인 후 진행하도록 했는가 |
| [x] | 실제 양식 투입, output 재생성, 외부 연동 구현을 다음 단계로 두지 않았는가 |
