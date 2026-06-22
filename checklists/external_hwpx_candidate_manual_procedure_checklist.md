# 저장소 밖 실제 양식 후보 수동 절차 체크리스트

## 기준 문서 확인

| 완료 | 항목 |
|---|---|
| [x] | `docs/53_real_hwpx_template_intake_safety_procedure.md`를 확인했는가 |
| [x] | `docs/58_external_hwpx_placeholder_conversion_runbook.md`를 확인했는가 |
| [x] | `docs/112_phase3_external_hwpx_and_manual_preview_criteria.md`를 확인했는가 |
| [x] | `docs/127_hwpx_manual_preview_gap_log_criteria.md`를 확인했는가 |
| [x] | `templates/hwpx/local_template_policy.md`를 확인했는가 |
| [x] | 기존 실제 양식 투입ㆍplaceholder 변환ㆍ수동 preview 체크리스트를 확인했는가 |

## 역할 구분 확인

| 완료 | 항목 |
|---|---|
| [x] | 실제 원본은 저장소 밖 로컬 위치에서만 다루도록 정리했는가 |
| [x] | 비식별 작업 복사본도 Git에 추가하지 않도록 정리했는가 |
| [x] | placeholder 후보는 Git 제외 상태의 로컬 HWPX로만 다루도록 정리했는가 |
| [x] | gap log는 실제 원문 없이 문서유형, 항목, 증상, 심각도만 기록하도록 정리했는가 |

## 수동 절차 확인

| 완료 | 항목 |
|---|---|
| [x] | 작업 필요성 판단 단계를 포함했는가 |
| [x] | A/B/C/D 보안등급 분류 단계를 포함했는가 |
| [x] | 저장소 밖 작업 위치 확인 단계를 포함했는가 |
| [x] | 실제 원본을 직접 수정하지 않는 복사본 원칙을 포함했는가 |
| [x] | 실제 내용과 식별 요소 제거 단계를 포함했는가 |
| [x] | 중립 placeholder 전환 기준을 포함했는가 |
| [x] | 표 내부 데이터는 전부 placeholder화하지 않고 표 틀 검수 범위로 제한할 수 있음을 포함했는가 |
| [x] | GitHub Desktop Changes 확인 단계를 포함했는가 |
| [x] | 수동 preview와 gap log 연결 기준을 포함했는가 |
| [x] | 보류 또는 다음 단계 판단 기준을 포함했는가 |

## 보류 조건 확인

| 완료 | 항목 |
|---|---|
| [x] | 실제 원본 또는 작업 복사본이 저장소 안에 있으면 중단하도록 했는가 |
| [x] | HWP/HWPX/output 파일이 GitHub Desktop Changes에 보이면 중단하도록 했는가 |
| [x] | C/D등급 또는 판단 애매 자료가 있으면 보류하도록 했는가 |
| [x] | 실제 개인정보, 문서번호, 기관정보, 내부 운영정보 의심 시 중단하도록 했는가 |
| [x] | 직인, 로고, 결재선 등 식별 요소가 남으면 placeholder 후보 전환을 막았는가 |
| [x] | `remaining_placeholders` 또는 gap log `차단` 상태를 중단 기준으로 두었는가 |
| [x] | style profile 미확정값은 `[확인 필요]`로 유지하도록 했는가 |

## 문서 유형별 확인

| 완료 | 항목 |
|---|---|
| [x] | `one_page_report` 수동 확인 중점을 정리했는가 |
| [x] | `project_plan` 수동 확인 중점을 정리했는가 |
| [x] | `result_report` 수동 확인 중점을 정리했는가 |
| [x] | `review_report` 수동 확인 중점을 정리했는가 |

## 변경 제한 확인

| 완료 | 항목 |
|---|---|
| [x] | renderer 코드를 변경하지 않았는가 |
| [x] | normalizer 코드를 변경하지 않았는가 |
| [x] | fixture JSON을 추가하거나 변경하지 않았는가 |
| [x] | routing 결과를 변경하지 않았는가 |
| [x] | HWPX payload 구조를 변경하지 않았는가 |
| [x] | HWPX output을 재생성하지 않았는가 |
| [x] | 실제 HWPX/HWP 파일을 Git에 추가하지 않았는가 |

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
| [x] | API 키, 토큰, 인증정보 예시값을 추가하지 않았는가 |

## 다음 단계 확인

| 완료 | 항목 |
|---|---|
| [x] | local template policy와 Git 제외 상태 반복 검증 기준이 `docs/129`에 반영되었는가 |
| [x] | Phase 4 문서 템플릿 안정화 통합 점검이 `docs/130`에 반영되었는가 |
| [x] | 실제 양식 수동 리허설 사용자 확인 패킷이 `docs/131`에 반영되었는가 |
| [x] | HWPX 일원화와 표 틀 우선 결정이 `docs/133`에 반영되었는가 |
| [x] | 다음 단계가 저장소 밖 한컴 preview 결과의 `table_scope: frame_only` 포함 실제값 없는 gap log 기록인가 |
| [x] | 실제 양식 투입, output 재생성, 외부 연동 구현을 다음 단계로 두지 않았는가 |
