# Phase 3 진입 조건 및 안전 게이트

## 목적

Phase 3에 들어가기 전에 반드시 고정해야 할 안전 게이트를 정리합니다.

이 문서는 구현 지시서가 아닙니다. Phase 3는 실제 API 호출, Make.com 연동, Email 자동화, 실제 기관 HWPX 원본 자동화를 바로 시작하는 단계가 아닙니다.

## Phase 3의 정의

Phase 3는 Phase 2 최소 PoC 이후의 다음 준비 단계입니다.

현재 기준에서 Phase 3의 목적은 다음과 같습니다.

- 실제 운영 자동화 전 안전 게이트 정리
- 저장소 밖 실제 HWPX 양식 복사본 취급 절차 재확인
- 사용자 수동 preview와 중단 기준 문서화
- `template_required`, `needs_security_review`, `blocked` 상태별 처리 기준 고정
- 이후 API, Make.com, Email 연동 필요성 재검토

Phase 3는 다음을 의미하지 않습니다.

- 실제 API 호출 구현
- Make.com 실제 시나리오 구현
- Gmail, Outlook, SMTP 연동
- 실제 이메일 자동 발송
- 실제 기관 HWPX 원본 Git 추가
- 실제 공문 원문 또는 개인정보 처리
- 실제 결재, 계약, 업체 선정, 예산 집행 자동화

## 진입 전 필수 조건

Phase 3 진입 전 다음 조건을 모두 만족해야 합니다.

| 조건 | 기준 |
|---|---|
| Phase 2 closeout | `docs/110_phase2_closeout_and_phase3_entry_decision.md` 완료 |
| 회귀 테스트 | `docs/109_normalizers_regression_recheck_result.md` 기준 통과 |
| 로컬 HWPX 템플릿 | Git 제외 상태 유지 |
| output 산출물 | Git 제외 상태 유지 |
| 실제 원문 | 저장소 추가 금지 |
| 실제 개인정보 | 입력 및 저장 금지 |
| 실제 기관 양식 원본 | 저장소 밖에서만 취급 |
| 자동화 연동 | API, Make.com, Email 보류 |

## 안전 게이트

### Gate 1. 입력 안전성

사용자 입력은 비식별 업무 지시만 허용합니다.

허용:

- placeholder 기반 업무 지시
- 실제값이 제거된 문서 구조 설명
- 문체, 목차, 검토 기준 설명
- `[확인 필요]`, null, placeholder로 남겨 둔 값

금지:

- 실제 공문 원문
- 실제 보고서 원문
- 실제 개인정보
- 실제 민원정보
- 실제 문서번호, 사건번호, 접수번호
- 실제 기관명, 관서명, 업체명, 담당자명
- 실제 내부 운영정보

중단 기준:

- 실제값처럼 보이는 정보가 포함되면 `blocked` 또는 `needs_security_review`로 분류
- 판단이 애매하면 더 보수적으로 분류
- 실제 원문을 요약하거나 재구성하지 않음

### Gate 2. 저장소 밖 HWPX 양식 취급

실제 HWPX 양식 원본은 저장소에 넣지 않습니다.

기준:

- 원본은 저장소 밖 로컬 폴더에서만 보관
- 작업 복사본도 저장소 밖에서 먼저 비식별 처리
- 파일명에 실제 기관명, 실제 문서명, 실제 문서번호 사용 금지
- C/D등급 자료는 placeholder 후보에서 제외
- 저장소 안으로 이동하더라도 `.hwpx`는 Git 제외 상태여야 함

중단 기준:

- GitHub Desktop Changes에 `.hwp`, `.hwpx`, output 파일이 보이면 작업 중단
- 실제 기관명, 문서번호, 결재선, 직인, 로고가 남아 있으면 작업 중단
- 파일 속성 또는 미리보기에 실제 정보가 남아 있으면 작업 중단

### Gate 3. 렌더링 전 검증

HWPX 렌더링 전에는 dry-run으로 안전 상태를 확인합니다.

확인 기준:

- routing 상태가 `ready_for_draft` 또는 `needs_more_input`
- `needs_security_review`는 HWPX 렌더링 제외
- `blocked`는 HWPX 렌더링 제외
- missing fields는 본문 실제값이 아니라 검토용 목록
- `placeholder_confirmed_values`는 read-only 검증용이며 routing에 연결하지 않음

중단 기준:

- routing이 `blocked`이면 즉시 중단
- routing이 `needs_security_review`이면 사람 검토 전 렌더링 중단
- 필수 로컬 템플릿이 없으면 `template_required`로 안전 중단
- payload validation 실패 시 렌더링 중단

### Gate 4. 사용자 수동 preview

HWPX output은 사람이 열람하여 확인합니다.

사용자 확인 항목:

- 파일 열림
- 글자 겹침 없음
- 항목 순서 정상
- 줄바꿈과 문단 배치 정상
- 내용 앞 기호 표기 일관성
- 남은 `{{placeholder}}` 없음
- `[확인 필요]`가 실제값처럼 오인되지 않음
- 실제 개인정보, 기관정보, 문서번호 없음

이 확인은 자동화하지 않습니다.

### Gate 5. 산출물 보관

검증용 산출물은 Git에 포함하지 않습니다.

Git 제외 대상:

- `normalizers/output/*`
- `renderers/hwpx_renderer/output/*`
- `templates/hwpx/*.hwpx`
- `templates/hwpx/*.hwp`
- `__pycache__/`

Git 포함 가능 대상:

- 문서
- 체크리스트
- placeholder 기반 fixture
- PoC 코드
- 실제값 없는 결과 요약 문서

### Gate 6. 외부 연동 보류

Phase 3에서도 외부 연동은 바로 시작하지 않습니다.

계속 보류:

- OpenAI API 실제 호출
- Make.com 실제 시나리오
- Gmail, Outlook, SMTP 연동
- 실제 이메일 자동 발송
- 실제 업무 계정 연결

외부 연동은 다음이 문서화된 뒤에만 재검토합니다.

- 입력 안전성 검증
- 실제 원문 차단 기준
- 사용자 preview 흐름
- 로그와 감사 추적 기준
- 실패 시 중단 및 사람 검토 흐름

## 상태별 처리 기준

| 상태 | 처리 |
|---|---|
| `ready_for_draft` | placeholder 기반 초안 생성 가능 |
| `needs_more_input` | `[확인 필요]` 유지, 초안 생성 가능 |
| `needs_security_review` | 사람 보안 검토 전 HWPX 렌더링 중단 |
| `blocked` | 처리 중단, 실제값 제거 요청 |
| `template_required` | 로컬 템플릿 준비 전 안전 중단 |
| validation 실패 | 렌더링 중단 |

## Phase 3 문서화 진행 상태

Phase 3 첫 문서화 흐름은 다음 순서로 진행했습니다.

| 순서 | 항목 | 상태 |
|---|---|---|
| 1 | 안전 게이트 문서와 체크리스트 고정 | 완료 |
| 2 | 저장소 밖 HWPX 양식 취급 절차 재확인 | `docs/112`에 반영 완료 |
| 3 | 사용자 수동 preview 체크리스트 정리 | `docs/112`에 반영 완료 |
| 4 | 상태별 중단 기준 반복 운영 문서 반영 | `docs/113`에 반영 완료 |
| 5 | Phase 3 운영 문서 묶음 통합 점검 | `docs/114`에 반영 완료 |
| 6 | 외부 연동 필요성 및 보류 기준 검토 | `docs/115`에 반영 완료 |
| 7 | 로그와 감사 추적 기준 구체화 | `docs/116`에 반영 완료 |
| 8 | 테스트 계정과 테스트 데이터 기준 구체화 | `docs/117`에 반영 완료 |
| 9 | 실제 원문 차단과 비식별 입력 확인 절차 | `docs/118`에 반영 완료 |
| 10 | 사용자 preview와 사람 승인 지점 통합 기준 | `docs/119`에 반영 완료 |
| 11 | 외부 전송 없는 no-send dry-run 기준 | `docs/120`에 반영 완료 |
| 12 | 외부 연동 구현 범위 승인 판단 | `docs/121`에 반영 완료 |

## 계속 보류할 범위

- 실제 기관 HWPX 양식 원본 Git 추가
- 실제 공문 또는 보고서 원문 처리
- 실제 개인정보, 민원정보, 내부 운영정보 처리
- `missing_fields` 자동 제외
- `placeholder_confirmed_values` routing 연결
- HWPX payload metadata 자동 반영
- 실제 기관 표준 글꼴, 자간, 줄간격 값 임의 확정
- Email, API, Make.com 실제 연동

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX 원본 파일 추가 없음
- Email, API, Make.com 연동 없음

## 결론

Phase 3는 운영 자동화 구현 단계가 아니라 안전 게이트를 고정하는 준비 단계입니다.

다음 단계는 실제 연동 구현이 아니라, 외부 연동 구현 보류 결정과 Phase 3 closeout 기준을 문서로 정리하는 것입니다.
