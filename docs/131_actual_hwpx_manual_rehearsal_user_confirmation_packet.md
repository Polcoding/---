# 실제 양식 수동 리허설 사용자 확인 패킷

## 목적

이 문서는 실제 양식 수동 리허설을 시작하기 전 사용자가 저장소 밖에서 직접 확인해야 할 항목과 HWPX 보고서 4종 gap log 빈 양식을 한곳에 모은 확인 패킷입니다.

이번 단계는 실제 기관 HWPX/HWP 원본을 저장소에 넣거나 실제 HWPX output을 재생성하는 단계가 아닙니다. renderer, normalizer, fixture, routing, HWPX payload, output, `.gitignore`도 변경하지 않습니다.

## 기준 문서

- `docs/127_hwpx_manual_preview_gap_log_criteria.md`
- `docs/128_external_hwpx_candidate_manual_procedure_and_hold_criteria.md`
- `docs/129_local_template_gitignore_repeat_verification_criteria.md`
- `docs/130_phase4_template_stabilization_integrated_review.md`
- `docs/133_hwpx_only_table_frame_decision.md`
- `templates/hwpx/local_template_policy.md`
- `templates/hwpx/README.md`

## 사용 방법

아래 `[사용자 확인 필요]` 항목은 Codex가 대신 확인할 수 없습니다. 사용자가 저장소 밖 로컬 환경과 GitHub Desktop 화면에서 직접 확인합니다.

확인 결과는 실제 원문, 실제 파일명, 실제 기관명, 실제 문서번호 없이 이 문서의 중립 문구와 gap log 형식으로만 기록합니다.

## [사용자 확인 필요] 1. 시작 전 중단 조건

다음 중 하나라도 해당하면 실제 양식 수동 리허설을 시작하지 않습니다.

| 확인 | 중단 조건 | 처리 |
|---|---|---|
| [ ] | 실제 원본 또는 작업 복사본이 저장소 안에 있음 | 즉시 중단 |
| [ ] | GitHub Desktop Changes에 HWP/HWPX/output 파일이 보임 | 즉시 중단 |
| [ ] | 실제 개인정보, 기관정보, 문서번호, 결재정보 의심 | 보안 검토 전 중단 |
| [ ] | C/D등급 또는 판단 애매 자료가 포함됨 | 보류 |
| [ ] | 직인, 로고, 결재선, 문서 속성에 실제값이 남음 | placeholder 후보 전환 금지 |
| [ ] | 실제 원문 일부를 gap log에 기록해야 하는 상황 | 기록 전 중단 |
| [ ] | renderer, normalizer, fixture, payload 변경이 필요해 보임 | 별도 승인 전 보류 |

## [사용자 확인 필요] 2. 저장소 밖 작업 위치 확인

| 확인 | 항목 | 통과 기준 |
|---|---|---|
| [ ] | 실제 원본 위치 | 저장소 밖 로컬 위치 |
| [ ] | 작업 복사본 위치 | 저장소 밖 로컬 위치 |
| [ ] | 작업 폴더명 | 실제 기관명, 실제 문서명, 실제 문서번호 없음 |
| [ ] | 파일명 | 실제 기관명, 실제 문서명, 실제 문서번호 없음 |
| [ ] | GitHub Desktop Changes | 실제 원본, 작업 복사본, HWP/HWPX, output 없음 |
| [ ] | 저장소 문서 기록 | 실제 경로, 실제 파일명, 실제 기관명 없음 |

## [사용자 확인 필요] 3. 비식별ㆍplaceholder 후보 전환 확인

| 확인 | 항목 | 통과 기준 |
|---|---|---|
| [ ] | 실제 본문 | 제거 또는 중립 placeholder 전환 |
| [ ] | 실제 기관명ㆍ부서명ㆍ업체명 | 제거 또는 `[기관 A]`, `[부서 A]`, `[업체 A]` 등으로 대체 |
| [ ] | 실제 개인명ㆍ담당자명ㆍ연락처ㆍ이메일 | 제거 또는 `[담당부서]`, `[공용 연락처]`, `[공용 이메일]`로 대체 |
| [ ] | 실제 문서번호ㆍ시행일자ㆍ접수번호ㆍ사건번호 | 제거 또는 `[문서번호 확인 필요]`, `[YYYY.MM.DD. 확인 필요]`로 대체 |
| [ ] | 결재선ㆍ직인ㆍ로고 | 제거 또는 저장소 반입 금지 |
| [ ] | 예산ㆍ일정ㆍ실적ㆍ수량 | 임의 생성 금지, `[확인 필요]` 유지 |
| [ ] | 문서 속성ㆍ미리보기ㆍ마지막 저장자 | 실제값 제거 확인 |
| [ ] | placeholder 이름 | 실제 대상을 추정할 수 없는 중립 이름 |

표 안 실제 물품명, 수량, 금액, 대상 목록은 현재 HWPX 자동화 대상이 아닙니다. 보안 노출을 막을 정도로 삭제, 공란, 짧은 중립 표기만 사용하고, 표 데이터 자동화는 향후 Excel/한셀 연동 후보로 분리합니다.

## [사용자 확인 필요] 4. GitHub Desktop Changes 확인

GitHub Desktop Changes에 다음 항목이 보이면 commit 또는 push하지 않습니다.

| 확인 | 보이면 안 되는 항목 |
|---|---|
| [ ] | `templates/hwpx/*.hwpx` |
| [ ] | `templates/hwpx/*.hwp` |
| [ ] | `renderers/hwpx_renderer/output/*` |
| [ ] | `normalizers/output/*` |
| [ ] | 실제 기관 HWPX/HWP 원본 |
| [ ] | 저장소 밖 작업 복사본 |
| [ ] | 실제 공문 또는 보고서 원문 |
| [ ] | 잠금 파일, 임시 파일, `__pycache__` |

보여도 되는 항목:

- `docs/*.md`
- `checklists/*.md`
- `README.md`
- `AGENTS.md`
- `tasks/NEXT_STEP.md`
- `templates/hwpx/*.md`

## [사용자 확인 필요] 5. HWPX 보고서 4종 preview 확인

### one_page_report

| 확인 | 항목 | 결과 |
|---|---|---|
| [ ] | 제목 위치와 본문 첫 항목 간격 |  |
| [ ] | `1. 보고 개요` 아래 내용 겹침 여부 |  |
| [ ] | `3. 주요 내용` 다중 행 표시 |  |
| [ ] | 검토 의견, 고려사항, 향후 계획 줄바꿈 |  |
| [ ] | 내용 앞 기호 표기 일관성 |  |
| [ ] | 실제값처럼 보이는 문구 없음 |  |

### project_plan

| 확인 | 항목 | 결과 |
|---|---|---|
| [ ] | 1~10번 항목 순서 |  |
| [ ] | 추진개요, 일정, 예산 영역 배치 |  |
| [ ] | 세부 추진계획 다중 행 표시 |  |
| [ ] | 표 역할 영역 폭과 줄바꿈 |  |
| [ ] | `[확인 필요]`가 실제 일정이나 예산처럼 보이지 않음 |  |
| [ ] | 실제값처럼 보이는 문구 없음 |  |

### result_report

| 확인 | 항목 | 결과 |
|---|---|---|
| [ ] | 추진개요와 결과 영역 문단 간격 |  |
| [ ] | 계획 항목과 실제 결과 대응 표시 |  |
| [ ] | 실적, 예산, 참여 인원 placeholder 유지 |  |
| [ ] | 문제점과 개선사항 번호ㆍ기호 표기 |  |
| [ ] | 향후계획 줄바꿈 |  |
| [ ] | 실제값처럼 보이는 문구 없음 |  |

### review_report

| 확인 | 항목 | 결과 |
|---|---|---|
| [ ] | 보안 검토 조건 표시 |  |
| [ ] | 검토 배경, 범위, 항목 순서 |  |
| [ ] | 위험요소와 필요 검토 항목 줄바꿈 |  |
| [ ] | 후속조치 항목 기호 표기 |  |
| [ ] | 실제 판단 확정처럼 보이는 표현 없음 |  |
| [ ] | 실제값처럼 보이는 문구 없음 |  |

## [사용자 확인 필요] 6. 표가 있는 문서 preview 확인

현재 단계에서 표는 내부 데이터가 아니라 틀과 배치만 확인합니다.

| 확인 | 항목 | 결과 |
|---|---|---|
| [ ] | 표 위치가 본문 흐름 안에서 자연스러움 |  |
| [ ] | 표 폭과 셀 폭이 크게 무너지지 않음 |  |
| [ ] | 짧은 중립 문구가 셀 안에서 겹치지 않음 |  |
| [ ] | 표가 제목, 번호, 본문 문단과 겹치지 않음 |  |
| [ ] | 실제 표 값이 gap log에 기록되지 않음 |  |

문제가 없으면 아래처럼만 전달합니다.

```text
document_type: one_page_report
table_scope: frame_only
status: 문제 없음
```

## gap log 빈 양식

gap log에는 실제 원문, 실제 파일명, 실제 기관명, 실제 문서번호를 기록하지 않습니다.

| log_id | document_type | table_scope | preview_target | section | gap_type | severity | observed_symptom | expected_state | suspected_scope | next_action | status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| GAP-001 |  |  |  |  |  |  |  |  |  |  |  |
| GAP-002 |  |  |  |  |  |  |  |  |  |  |  |
| GAP-003 |  |  |  |  |  |  |  |  |  |  |  |
| GAP-004 |  |  |  |  |  |  |  |  |  |  |  |

## gap log 값 선택 기준

| 필드 | 허용 값 또는 기록 기준 |
|---|---|
| `document_type` | `one_page_report`, `project_plan`, `result_report`, `review_report` |
| `table_scope` | 표 관련 확인이면 `frame_only`, 표와 무관하면 비움 |
| `preview_target` | placeholder 기반 파일명 또는 문서유형만 기록 |
| `section` | 항목 번호 또는 중립 영역명 |
| `gap_type` | `글자 겹침`, `줄바꿈`, `번호 들여쓰기`, `기호 표기`, `표 폭`, `여백`, `placeholder 잔여`, `확인 필요 표시`, `보안 표시` |
| `severity` | `차단`, `수정 필요`, `관찰`, `문제 없음` |
| `observed_symptom` | 실제 원문 없는 증상 설명 |
| `expected_state` | 기대 상태를 일반 표현으로 기록 |
| `suspected_scope` | `템플릿 문단 배치`, `placeholder 위치`, `수동 재확인`, `보안 검토` 등 |
| `next_action` | `사용자 재확인`, `템플릿 후보 점검`, `문서 기준 보강`, `보안 검토`, `보류` |
| `status` | `보류`, `관찰`, `수정 필요`, `문제 없음` |

## 기록 금지 예시

- 실제 기관명
- 실제 부서명
- 실제 업체명
- 실제 사람 이름
- 실제 문서번호
- 실제 접수번호, 사건번호, 민원번호
- 실제 파일명
- 실제 내부 경로
- 실제 원문 일부
- 실제 예산액, 일정, 실적 수치
- 실제 결재선, 직인, 로고 설명

## 다음 단계 판단

| 상황 | 다음 조치 |
|---|---|
| 모든 사용자 확인 항목 통과, gap severity `차단` 없음 | 저장소 밖 수동 리허설 결과 기록 가능 |
| GitHub Desktop Changes에 HWP/HWPX/output 표시 | commit 또는 push 중단 |
| 실제값 의심 또는 보안 의심 | 보안 검토 전 중단 |
| style profile 값 미확정 | `[확인 필요]` 유지 |
| 반복 gap이 있으나 실제값 없음 | 문서 기준 보강 또는 사용자 재확인 |
| 코드 변경이 필요해 보임 | 별도 승인 전 보류 |

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
- `.gitignore`
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

실제 양식 수동 리허설은 사용자가 저장소 밖에서 직접 확인해야 하는 작업입니다.

이 패킷을 통과하기 전에는 실제 원본 투입, HWPX output 재생성, renderer 코드 변경, 외부 연동 구현으로 넘어가지 않습니다.
