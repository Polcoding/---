# 다음 작업

## [사용자 확인 필요]

실제 양식 수동 리허설 전 준비 확인은 사용자가 `1~3 모두 올클리어`라고 명시하여 통과한 것으로 기록했습니다.

다음 단계는 실제 원본을 저장소에 넣는 것이 아니라, 사용자가 저장소 밖에서 한컴 preview를 확인한 결과를 실제값 없는 gap log 형식으로 전달하는 것입니다.

## 목표

`docs/132_actual_hwpx_manual_rehearsal_readiness_confirmation.md`와 `docs/131_actual_hwpx_manual_rehearsal_user_confirmation_packet.md` 기준으로 실제 양식 수동 리허설 결과를 기록할 준비를 합니다.

이번 단계는 실제 기관 HWPX/HWP 원본을 저장소에 넣거나 실제 HWPX output을 재생성하는 단계가 아닙니다. 사용자가 저장소 밖 로컬 환경에서 preview를 확인하고, 결과만 비식별 gap log 형식으로 제공합니다.

## 현재 완료 상태

- HWPX 보고서 4종 placeholder 기반 렌더링 및 수동 검수 완료
- 입력 정규화, 보안 필터, payload mapper, validation, dry-run PoC 작성 완료
- mapped HWPX 보고서 4종 렌더링 완료
- Phase 2 최소 PoC 문서 기준 마무리 가능 판단 완료
- Phase 3 진입 조건 및 안전 게이트 문서화 완료
- Phase 3 외부 연동 구현 범위 승인 판단 완료
- Phase 3 마무리 판단 및 Phase 4 진입 여부 결정 완료
- Phase 4 문서 템플릿 안정화 진입 판단 완료
- HWPX 보고서 4종 template manifest와 공통 placeholder 정합성 점검 완료
- style profile `[확인 필요]` 값 유지 기준과 수집 체크리스트 점검 완료
- HWPX 보고서 4종 수동 preview 서식 gap log 기준 정리 완료
- 저장소 밖 실제 양식 후보 수동 절차와 보류 조건 재정렬 완료
- local template policy와 Git 제외 상태 반복 검증 기준 정리 완료
- Phase 4 문서 템플릿 안정화 통합 점검 완료
- 실제 양식 수동 리허설 사용자 확인 패킷과 gap log 빈 양식 정리 완료
- 사용자가 실제 원본ㆍ작업 복사본 저장소 밖 보관, 식별 요소 제거, GitHub Desktop Changes 이상 없음을 확인 완료
- renderer, normalizer, fixture, routing, HWPX payload, output 변경 없이 문서 기준으로만 점검 완료

## 확인 대상

- `docs/132_actual_hwpx_manual_rehearsal_readiness_confirmation.md`
- `docs/131_actual_hwpx_manual_rehearsal_user_confirmation_packet.md`
- `checklists/actual_hwpx_manual_rehearsal_readiness_confirmation_checklist.md`
- `checklists/actual_hwpx_manual_rehearsal_user_confirmation_packet_checklist.md`
- `docs/127_hwpx_manual_preview_gap_log_criteria.md`
- `docs/128_external_hwpx_candidate_manual_procedure_and_hold_criteria.md`
- `docs/129_local_template_gitignore_repeat_verification_criteria.md`
- `docs/130_phase4_template_stabilization_integrated_review.md`
- `templates/hwpx/local_template_policy.md`
- `README.md`
- `AGENTS.md`

## 사용자가 제공할 항목

문제가 없으면 아래처럼 문서유형별로 알려줍니다.

```text
document_type: one_page_report
status: 문제 없음
```

문제가 있으면 아래 항목만 제공합니다.

```text
document_type:
section:
gap_type:
severity:
observed_symptom:
expected_state:
suspected_scope:
next_action:
```

허용되는 `document_type`:

- `one_page_report`
- `project_plan`
- `result_report`
- `review_report`

허용되는 `gap_type`:

- `글자 겹침`
- `줄바꿈`
- `번호 들여쓰기`
- `기호 표기`
- `표 폭`
- `여백`
- `placeholder 잔여`
- `확인 필요 표시`
- `보안 표시`

허용되는 `severity`:

- `차단`
- `수정 필요`
- `관찰`
- `문제 없음`

## 작업 제한

- 실제 기관 양식 사용 금지
- 실제 기관 HWPX/HWP 원본 Git 추가 금지
- 실제 문서 원문 사용 금지
- 실제 개인정보 또는 내부 운영정보 사용 금지
- 실제 문서번호, 기관명, 담당자명, 수신자명 기록 금지
- 실제 파일명 또는 내부 경로 기록 금지
- 실제 서식값 임의 생성 금지
- 폰트 파일 저장소 추가 금지
- HWPX output 재생성 금지
- Email/API/Make.com 연동 금지
- routing 결과 변경 금지
- HWPX payload 반영 금지
- fixture JSON 추가 금지
- renderer 또는 normalizer 코드 변경 금지
- `.gitignore` 변경은 실제 필요성이 확인된 경우에만 검토

## 완료 조건

- 사용자가 저장소 밖 한컴 preview 결과를 실제값 없는 gap log 형식으로 제공
- gap log에 실제 원문, 실제 파일명, 실제 기관명, 실제 문서번호가 없음을 확인
- `차단` severity가 있으면 즉시 보류
- `수정 필요` 또는 `관찰` severity가 있으면 문서 기준 보강 또는 템플릿 후보 점검으로 분리
- 모든 문서유형이 `문제 없음`이면 실제 양식 수동 리허설 1차 통과로 기록
- local template과 output Git 제외 상태 유지 여부 확인
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

사용자가 실제값 없는 preview 결과를 제공하면, 다음 단계는 `docs/133` 형태로 실제 양식 수동 리허설 gap log 결과를 기록하는 것입니다.

결과가 `문제 없음`이면 Phase 4 실제 양식 수동 리허설 1차 통과로 정리합니다.

결과에 `차단`이 있거나 실제값이 포함되면 즉시 보류합니다. 실제 기관 HWPX 원본 투입, HWPX output 재생성, renderer 코드 변경, APIㆍMake.comㆍEmail 연동 구현은 계속 보류합니다.
