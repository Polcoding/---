# HWPX 보고서 4종 수동 preview 서식 gap log 기준

## 목적

이 문서는 HWPX 보고서 4종을 한컴에서 수동 preview할 때 발견되는 서식 차이를 실제 원문 없이 기록하기 위한 gap log 기준을 정리합니다.

이번 단계는 실제 HWPX output을 재생성하거나 실제 기관 HWPX 원본을 투입하는 단계가 아닙니다. renderer, normalizer, fixture, routing, HWPX payload, output도 변경하지 않습니다.

## 확인 대상

- `docs/126_style_profile_confirmation_value_collection_criteria.md`
- `checklists/style_profile_confirmation_value_collection_checklist.md`
- `checklists/hwpx_institution_style_value_collection_checklist.md`
- `checklists/hwpx_rendered_output_manual_review_checklist.md`
- `docs/112_phase3_external_hwpx_and_manual_preview_criteria.md`
- `docs/119_phase3_user_preview_and_human_approval_integration.md`
- `docs/57_hwpx_report_4types_completion_and_safety_rehearsal.md`
- `templates/hwpx/local_template_policy.md`
- `templates/hwpx/README.md`

## 점검 결론

현재 저장소 기준으로 HWPX 보고서 4종은 로컬 placeholder output의 수동 검수를 완료했습니다.

다만 이후 사용자가 한컴에서 다시 확인해야 하는 서식 차이를 일관되게 기록하려면 다음 기준이 필요합니다.

| 항목 | 확인 내용 | 조치 |
|---|---|---|
| 기록 단위 | 문서유형, 항목 번호, 증상, 심각도, 후속 조치가 분리되어야 함 | gap log 필드 정의 |
| 사용자 확인 표시 | 사용자가 직접 확인해야 할 항목이 눈에 띄어야 함 | `[사용자 확인 필요]` 구역 명시 |
| 보안 제한 | 실제 원문, 실제 파일명, 실제 기관명 기록을 막아야 함 | 금지 정보 표 추가 |
| style profile 구분 | style profile 미확정값과 preview에서 보이는 gap을 혼동하지 않아야 함 | gap 유형 구분 |
| 후속 조치 | 코드 수정, 템플릿 수정, 수동 재확인, 보류를 구분해야 함 | 심각도와 조치 기준 추가 |

## gap log 기본 원칙

- 실제 원문이나 실제 기관 양식 원본을 기록하지 않습니다.
- 실제 HWPX/HWP 원본 파일명, 실제 기관명, 실제 문서번호를 기록하지 않습니다.
- output 재생성 없이 문서 기준으로 기록 양식만 정리합니다.
- 사용자가 한컴에서 확인한 결과는 placeholder 기반 파일명 또는 문서유형으로만 기록합니다.
- gap은 실제 서식값 확정이 아니라 preview에서 관찰된 차이입니다.
- style profile 값이 미확정이면 `[확인 필요]`로 유지합니다.

## gap log 필드

| 필드 | 기록 기준 | 예시 |
|---|---|---|
| `log_id` | 중립적 일련번호 | `GAP-001` |
| `document_type` | 문서유형 | `one_page_report` |
| `preview_target` | placeholder 기반 output 또는 문서유형 | `sample_one_page_report_poc.hwpx` |
| `section` | 항목 번호 또는 영역 | `2. 추진 배경` |
| `gap_type` | 서식 차이 유형 | `글자 겹침` |
| `severity` | 심각도 | `수정 필요` |
| `observed_symptom` | 실제 원문 없는 증상 설명 | `본문 두 줄이 가까워 보임` |
| `expected_state` | 기대 상태 | `문단 간격 검토 가능한 수준` |
| `suspected_scope` | 추정 범위 | `템플릿 문단 배치` |
| `next_action` | 후속 조치 | `사용자 재확인` |
| `status` | 처리 상태 | `보류` |

## gap 유형

| gap_type | 의미 | 기록 가능 예시 |
|---|---|---|
| `글자 겹침` | 제목, 번호, 본문, 표 안 글자가 겹쳐 보임 | `3번 본문 줄간격 좁음` |
| `줄바꿈` | 여러 줄 본문이 한 문단에 몰림 | `주요 내용 줄바꿈 분리 필요` |
| `번호 들여쓰기` | 1., 가., 1) 체계의 위치가 어색함 | `하위 항목 들여쓰기 확인 필요` |
| `기호 표기` | 내용 앞 `-` 또는 기호가 문서 내에서 불일치 | `7번 내용 앞 기호만 남음` |
| `표 폭` | 표 또는 표 역할 영역의 폭이 좁거나 넓음 | `일정 영역 폭 확인 필요` |
| `여백` | 상하좌우 여백 또는 문단 간격이 어색함 | `본문 아래 여백 부족` |
| `placeholder 잔여` | `{{placeholder}}`가 남아 있음 | `{{missing_fields}} 잔여` |
| `확인 필요 표시` | `[확인 필요]`가 실제값처럼 보임 | `예산 확인 문구 위치 조정 필요` |
| `보안 표시` | 실제값처럼 보이는 값 또는 민감정보 의심 | `즉시 보류` |

## 심각도 기준

| severity | 기준 | 처리 |
|---|---|---|
| `차단` | 실제값 의심, placeholder 잔여, 문서 열림 실패, 심각한 겹침 | 작업 중단, 보안 또는 템플릿 재검토 |
| `수정 필요` | 사람이 읽을 수 있으나 반복 사용 전 보정 필요 | 다음 문서 보강 후보로 기록 |
| `관찰` | 즉시 수정은 아니지만 반복 확인 필요 | gap log에 유지 |
| `문제 없음` | 확인 결과 정상 | 통과 기록 |

`차단`이 하나라도 있으면 실제 업무 적용 후보로 보지 않습니다.

## 문서유형별 확인 항목

### one_page_report

[사용자 확인 필요]

| 확인 | 항목 |
|---|---|
| [ ] | 제목 위치와 본문 첫 항목 간격 |
| [ ] | `1. 보고 개요` 아래 내용 겹침 여부 |
| [ ] | `3. 주요 내용` 다중 행 표시 |
| [ ] | 검토 의견, 고려사항, 향후 계획의 줄바꿈 |
| [ ] | 내용 앞 기호 표기 일관성 |

### project_plan

[사용자 확인 필요]

| 확인 | 항목 |
|---|---|
| [ ] | 1~10번 항목 순서 |
| [ ] | 추진개요, 일정, 예산 영역의 축약 문구 배치 |
| [ ] | 세부 추진계획 다중 행 표시 |
| [ ] | 표 역할 영역의 폭과 줄바꿈 |
| [ ] | `[확인 필요]` 값이 실제 일정이나 예산처럼 보이지 않는지 |

### result_report

[사용자 확인 필요]

| 확인 | 항목 |
|---|---|
| [ ] | 추진개요와 결과 영역의 문단 간격 |
| [ ] | 계획 항목과 실제 결과의 대응 표시 |
| [ ] | 실적, 예산, 참여 인원 placeholder 유지 |
| [ ] | 문제점과 개선사항의 번호ㆍ기호 표기 |
| [ ] | 향후계획 줄바꿈 |

### review_report

[사용자 확인 필요]

| 확인 | 항목 |
|---|---|
| [ ] | 보안 검토 조건 표시 |
| [ ] | 검토 배경, 범위, 항목 순서 |
| [ ] | 위험요소와 필요 검토 항목 줄바꿈 |
| [ ] | 후속조치 항목의 기호 표기 |
| [ ] | 실제 판단 확정처럼 보이는 표현 없음 |

## 기록 예시

허용 예시:

| log_id | document_type | section | gap_type | severity | observed_symptom | next_action | status |
|---|---|---|---|---|---|---|---|
| `GAP-001` | `one_page_report` | `1. 보고 개요` | `글자 겹침` | `수정 필요` | `본문 두 줄이 가까워 보임` | `사용자 재확인` | `보류` |
| `GAP-002` | `project_plan` | `7. 소요 예산` | `확인 필요 표시` | `관찰` | `[확인 필요]` 문구 위치 확인 필요 | `반복 preview 확인` | `관찰` |

금지 예시:

- 실제 기관명이 들어간 파일명
- 실제 문서번호
- 실제 보고서 본문 일부
- 실제 담당자명
- 실제 내부 경로
- 실제 예산액, 실적 수치, 일정

## style profile과 gap log 구분

| 구분 | 의미 | 처리 |
|---|---|---|
| style profile `[확인 필요]` | 실제 표준 서식값이 아직 확정되지 않음 | `docs/126` 기준 유지 |
| preview gap | 한컴에서 보이는 배치ㆍ표기 차이 | gap log에 기록 |
| renderer bug 후보 | 동일 입력에서 반복되는 치환 문제 | 별도 승인 전 코드 변경 금지 |
| template 조정 후보 | 로컬 placeholder 템플릿 배치 문제 | 실제 HWPX 파일은 Git 제외 유지 |

preview gap이 있다고 해서 즉시 style profile 값을 확정하지 않습니다.

## 후속 조치 기준

| next_action | 기준 |
|---|---|
| `사용자 재확인` | 한컴 화면에서 직접 다시 확인 필요 |
| `템플릿 후보 점검` | 로컬 placeholder HWPX 배치 확인 필요 |
| `문서 기준 보강` | checklist나 문서 기준만 보강 가능 |
| `보안 검토` | 실제값 의심 또는 민감정보 의심 |
| `보류` | 원인 불명 또는 실제값 확인 전 |

## 코드 변경 판단

이번 점검에서는 코드 변경이 필요하지 않습니다.

변경하지 않는 항목:

- `normalizers/`
- `renderers/`
- `examples/json/`
- routing fixture
- HWPX payload mapper
- HWPX renderer output
- local HWPX template
- API, Make.com, Email 연동 코드

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

HWPX 보고서 4종 수동 preview gap은 실제값 없이 문서유형, 항목, 증상, 심각도, 후속 조치로만 기록합니다.

저장소 밖 실제 양식 후보 수동 절차와 보류 조건은 `docs/128_external_hwpx_candidate_manual_procedure_and_hold_criteria.md`에 반영했습니다.

local template policy와 Git 제외 상태 반복 검증 기준은 `docs/129_local_template_gitignore_repeat_verification_criteria.md`에 반영했습니다.

Phase 4 문서 템플릿 안정화 통합 점검은 `docs/130_phase4_template_stabilization_integrated_review.md`에 반영했습니다.

실제 양식 수동 리허설 사용자 확인 패킷과 gap log 빈 양식은 `docs/131_actual_hwpx_manual_rehearsal_user_confirmation_packet.md`에 반영했습니다.

다음 단계는 저장소 밖 한컴 preview 결과를 실제값 없는 gap log로 기록하는 것입니다.
