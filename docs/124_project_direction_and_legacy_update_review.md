# 프로젝트 방향 재확인 및 구형 문서 업데이트 검토

## 목적

현재 저장소의 실제 파일 상태를 기준으로 프로젝트 목표, 지금까지 만든 문서와 PoC의 방향성, 구형 문서 처리 기준, 남은 작업량을 다시 정리합니다.

이 문서는 새 구현 지시서가 아닙니다. 실제 기관 HWPX 원본 투입, 실제 HWPX output 재생성, renderer 코드 변경, normalizer 연결, APIㆍMake.comㆍEmail 연동 구현은 계속 보류합니다.

## 프로젝트 목표 재확인

이 프로젝트의 목표는 공공기관 행정업무를 지원하는 AI 초안 생성 시스템을 단계적으로 구축하는 것입니다.

핵심 목표:

- 비식별 업무 지시를 받아 행정문서 초안을 생성
- 실제 원문, 개인정보, 기관정보, 내부 운영정보는 저장소에 포함하지 않음
- AI는 내용 구조와 초안을 담당
- HWPX/XLSX/Markdown/Email 렌더러는 placeholder와 서식을 담당
- 모든 결과물은 사람이 검토ㆍ수정ㆍ승인
- 실제 발송, 결재, 계약, 업체 선정, 예산 집행, 법률 판단은 자동화하지 않음

자동화 우선순위:

| 우선순위 | 대상 | 상태 |
|---:|---|---|
| 1 | HWPX 원페이지 보고서 | placeholder 기반 로컬 검증 완료, 문서 템플릿 안정화 필요 |
| 2 | HWPX 추진계획서 | placeholder 기반 로컬 검증 완료, 문서 템플릿 안정화 필요 |
| 3 | HWPX 결과보고서 | placeholder 기반 로컬 검증 완료, 문서 템플릿 안정화 필요 |
| 4 | HWPX 검토보고서 | placeholder 기반 로컬 검증 완료, 보안 검토 조건 유지 필요 |
| 5 | XLSX 조사표 | 보조 PoC 유지 |
| 6 | Email 초안 | 보조 초안 렌더러 유지, 자동 발송 금지 |

## 방향성 판단

현재까지 구성한 파일들은 프로젝트의 큰 방향과 대체로 일치합니다.

일치하는 점:

- HWPX 보고서 4종을 최우선 대상으로 재정렬함
- 실제 원문과 개인정보를 저장소에 넣지 않는 원칙을 유지함
- local HWPX template과 output 산출물을 Git 제외로 유지함
- `missing_fields`, `[확인 필요]`, 사람 검토 필요 기준을 계속 유지함
- Email, API, Make.com 실제 연동을 보류함
- `placeholder_confirmed_values`는 read-only 검토용으로 유지하고 normalizer 흐름에 연결하지 않음
- Phase 4를 실제 구현이 아니라 문서 템플릿 안정화 검토로 제한함

주의할 점:

- 일부 초기 문서는 작성 당시의 다음 단계가 그대로 남아 있어 현재 진행 상태처럼 읽힐 수 있음
- 초기 문서의 "1단계" 또는 "Phase 2 진행 중" 표현은 최신 진입점 문서에서 보정해야 함
- 구형 문서를 전부 수정하면 당시 판단 기록이 흐려질 수 있으므로, 진입점 문서와 안내 문서만 최신화하고 과거 결과 문서는 기록으로 유지하는 방식이 적절함

## 구형 문서 처리 기준

구형 문서는 다음 세 가지로 나누어 관리합니다.

| 분류 | 기준 | 조치 |
|---|---|---|
| 최신 진입점 문서 | README, AGENTS, `docs/00_project_overview.md`, `tasks/NEXT_STEP.md` | 현재 상태로 갱신 |
| 안내 문서 | `docs/00_chatgpt_handoff.md`, `docs/90...`, `templates/hwpx/README.md`, `normalizers/README.md` | 오래된 현재상태 문구만 갱신 |
| 역사적 결과 문서 | Phase 1~3 단계별 결과 문서와 체크리스트 | 당시 기록으로 유지, 최신 판단 문서로 연결 |

이번 검토에서 우선 갱신할 문서:

- `README.md`
- `AGENTS.md`
- `docs/00_project_overview.md`
- `docs/00_chatgpt_handoff.md`
- `docs/59_phase1_completion_and_phase2_entry_criteria.md`
- `docs/90_project_reorganization_after_superpowers.md`
- `templates/hwpx/README.md`
- `normalizers/README.md`
- `tasks/NEXT_STEP.md`

## 현재 진행률 판단

진행률은 기준을 무엇으로 보느냐에 따라 다릅니다.

| 기준 | 진행률 판단 | 설명 |
|---|---:|---|
| 문서ㆍ정책ㆍ안전 기준 | 85~90% | 보안, 비식별, 금지 범위, 단계별 판단 문서가 충분히 쌓임 |
| HWPX 보고서 로컬 PoC | 75~80% | 4종 placeholder 렌더링과 수동 검수 완료, 실제 양식 안정화 전 |
| 입력 정규화ㆍ보안 필터 최소 PoC | 65~70% | fixture 기반 PoC와 회귀 기준 있음, 운영 연결은 보류 |
| 문서 템플릿 안정화 | 74~80% | Phase 4 진입 판단, manifestㆍplaceholder 정합성, style profile 확인 기준, 수동 preview gap log 기준, 실제 양식 후보 수동 절차, Git 제외 반복 검증 기준, 통합 점검, 사용자 확인 패킷과 준비 확인 기록 완료 |
| 실제 기관 양식 전환 | 40~50% | 저장소 밖 절차, 보류 조건, Git 제외 반복 검증 기준, 조건부 수동 리허설 진입 판단, 사용자 준비 확인은 완료했으나 실제 preview 결과 기록 전 |
| 외부 연동/API/Email 자동화 | 0~10% | 의도적으로 구현 보류 |

전체 시스템 구축 관점에서는 약 61~65% 진행으로 봅니다.

다만 "안전한 로컬 HWPX 보고서 초안 생성 MVP" 기준으로는 약 75~81%까지 진행된 상태입니다. 반대로 실제 운영 자동화와 외부 연동까지 포함한 최종 시스템 기준으로는 아직 절반을 조금 넘은 수준입니다.

## 최근 완료와 앞으로 남은 큰 묶음

남은 작업은 다음 순서가 적절합니다.

1. HWPX 보고서 4종 template manifest와 공통 placeholder 정합성 점검 완료
2. 입력 요구사항, 사용자 입력 템플릿, placeholder 설계 간 누락ㆍ중복 정리 완료
3. style profile의 `[확인 필요]` 값 유지 여부와 수집 체크리스트 정비 완료
4. HWPX 보고서 4종 수동 preview 서식 gap log와 점검 기준 정리 완료
5. 저장소 밖 실제 양식 후보를 다룰 때의 수동 절차 재정렬 완료
6. local template policy와 Git 제외 상태 반복 검증 기준 정리 완료
7. Phase 4 문서 템플릿 안정화 통합 점검과 실제 양식 수동 리허설 조건부 진입 판단 완료
8. 실제 양식 수동 리허설 사용자 확인 패킷과 gap log 빈 양식 정리 완료
9. 사용자 저장소 밖 준비 여부 확인 완료
10. 저장소 밖 한컴 preview 결과의 실제값 없는 gap log 기록
11. 실제 기관 양식 투입은 사용자와 별도 승인 후 저장소 밖에서만 수행
12. API, Make.com, Email 자동화는 조직 보안 검토와 별도 승인 전까지 계속 보류

예상 남은 반복 횟수:

- 문서 템플릿 안정화까지만 보면 약 0~1회
- 저장소 밖 실제 양식 후보 수동 리허설까지 보면 약 3~6회
- 외부 연동 검토까지 포함하면 별도 보안 검토 후 추가 단계 필요

## 업데이트 판단 결론

현재 방향은 올바릅니다. 지금까지의 파일들은 HWPX 보고서 우선, placeholder 기반, 안전 중단, 사람 검토 흐름이라는 핵심 방향을 유지하고 있습니다.

다만 진입점 문서 일부에는 Phase 2 기준의 구형 현재상태 표현이 남아 있어 갱신이 필요합니다. 과거 결과 문서는 삭제하거나 되돌리지 않고, 최신 문서에서 현재 기준을 명확히 연결하는 방식으로 정리합니다.

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX 원본 파일 추가 없음
- 실제 계정명, 이메일 주소, 결제정보 추가 없음
- 실제 수신자, 참조자, 첨부 파일명 추가 없음
- API 키, 토큰, 인증정보 예시값 추가 없음
- Email, API, Make.com 연동 구현 없음

## 다음 작업 후보

HWPX 보고서 4종 template manifest와 공통 placeholder 정합성 점검은 `docs/125_hwpx_template_manifest_placeholder_consistency_review.md`에 반영했습니다.

style profile의 `[확인 필요]` 값 유지 기준과 수집 체크리스트는 `docs/126_style_profile_confirmation_value_collection_criteria.md`에 반영했습니다.

HWPX 보고서 4종 수동 preview 서식 gap log 기준은 `docs/127_hwpx_manual_preview_gap_log_criteria.md`에 반영했습니다.

저장소 밖 실제 양식 후보 수동 절차와 보류 조건은 `docs/128_external_hwpx_candidate_manual_procedure_and_hold_criteria.md`에 반영했습니다.

local template policy와 Git 제외 상태 반복 검증 기준은 `docs/129_local_template_gitignore_repeat_verification_criteria.md`에 반영했습니다.

Phase 4 문서 템플릿 안정화 통합 점검은 `docs/130_phase4_template_stabilization_integrated_review.md`에 반영했습니다.

실제 양식 수동 리허설 사용자 확인 패킷과 gap log 빈 양식은 `docs/131_actual_hwpx_manual_rehearsal_user_confirmation_packet.md`에 반영했습니다.

실제 양식 수동 리허설 전 사용자 준비 확인 완료 결과는 `docs/132_actual_hwpx_manual_rehearsal_readiness_confirmation.md`에 반영했습니다.

다음 작업은 `tasks/NEXT_STEP.md` 기준으로 저장소 밖 한컴 preview 결과를 실제값 없는 gap log로 기록하는 것입니다.
