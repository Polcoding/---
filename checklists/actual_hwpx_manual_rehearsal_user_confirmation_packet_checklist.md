# 실제 양식 수동 리허설 사용자 확인 패킷 체크리스트

## 기준 문서 확인

| 완료 | 항목 |
|---|---|
| [x] | `docs/127_hwpx_manual_preview_gap_log_criteria.md`를 확인했는가 |
| [x] | `docs/128_external_hwpx_candidate_manual_procedure_and_hold_criteria.md`를 확인했는가 |
| [x] | `docs/129_local_template_gitignore_repeat_verification_criteria.md`를 확인했는가 |
| [x] | `docs/130_phase4_template_stabilization_integrated_review.md`를 확인했는가 |
| [x] | `templates/hwpx/local_template_policy.md`를 확인했는가 |
| [x] | `templates/hwpx/README.md`를 확인했는가 |

## 사용자 확인 표시

| 완료 | 항목 |
|---|---|
| [x] | `[사용자 확인 필요]` 구역을 눈에 띄게 분리했는가 |
| [x] | Codex가 대신 확인할 수 없는 항목을 사용자 확인으로 분리했는가 |
| [x] | 저장소 밖 작업 위치 확인 항목을 포함했는가 |
| [x] | GitHub Desktop Changes 확인 항목을 포함했는가 |
| [x] | HWPX 보고서 4종별 preview 확인 항목을 포함했는가 |

## 보류ㆍ중단 조건 확인

| 완료 | 항목 |
|---|---|
| [x] | 실제 원본 또는 작업 복사본이 저장소 안에 있으면 중단하도록 했는가 |
| [x] | HWP/HWPX/output 파일이 GitHub Desktop Changes에 보이면 중단하도록 했는가 |
| [x] | 실제 개인정보, 기관정보, 문서번호 의심 시 중단하도록 했는가 |
| [x] | C/D등급 또는 판단 애매 자료를 보류하도록 했는가 |
| [x] | 직인, 로고, 결재선, 문서 속성 실제값 잔존 시 placeholder 후보 전환을 막았는가 |
| [x] | renderer, normalizer, fixture, payload 변경은 별도 승인 전 보류하도록 했는가 |

## gap log 빈 양식 확인

| 완료 | 항목 |
|---|---|
| [x] | gap log 빈 양식을 포함했는가 |
| [x] | `document_type`, `section`, `gap_type`, `severity`, `next_action`, `status` 필드를 포함했는가 |
| [x] | gap log 값 선택 기준을 포함했는가 |
| [x] | 실제 원문, 실제 파일명, 실제 기관명, 실제 문서번호 기록 금지를 명시했는가 |
| [x] | severity `차단`이 있으면 다음 단계로 진행하지 않도록 했는가 |

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
| [x] | `.gitignore` 파일을 변경하지 않았는가 |

## 보안 검수

| 완료 | 항목 |
|---|---|
| [x] | 실제 개인정보를 추가하지 않았는가 |
| [x] | 실제 기관명, 업체명, 담당자명을 추가하지 않았는가 |
| [x] | 실제 문서번호, 민원번호, 사건번호를 추가하지 않았는가 |
| [x] | 실제 날짜, 예산, 실적 수치를 추가하지 않았는가 |
| [x] | 실제 공문 원문 또는 보고서 원문을 추가하지 않았는가 |
| [x] | 실제 HWPX 원본 파일을 추가하지 않았는가 |
| [x] | 실제 내부 경로나 파일명을 추가하지 않았는가 |
| [x] | 폰트 파일을 추가하지 않았는가 |
| [x] | API 키, 토큰, 인증정보 예시값을 추가하지 않았는가 |

## 다음 단계 확인

| 완료 | 항목 |
|---|---|
| [x] | 다음 단계가 저장소 밖 한컴 preview 결과의 실제값 없는 gap log 기록인가 |
| [x] | 실제 양식 투입, output 재생성, 외부 연동 구현을 다음 단계로 두지 않았는가 |
