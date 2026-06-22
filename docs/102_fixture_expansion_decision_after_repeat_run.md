# fixture 확장 후보 재검토 결과

## 목적

Phase 2 수동 리허설과 반복 운영 기준 정리 이후, `normalizers/fixtures/`를 지금 확장할 필요가 있는지 재검토합니다.

이 문서는 실제 fixture JSON을 추가하는 작업이 아니라, 현재 fixture 범위와 확장 후보를 비교해 다음 작업 방향을 정하는 문서입니다.

## 현재 fixture 상태

현재 일반 routing fixture는 6종입니다.

| fixture | document_type | 기대 routing | 역할 |
|---|---|---|---|
| `safe_one_page_report_request.json` | `one_page_report` | `ready_for_draft` | 안전 입력 정상 경로 |
| `missing_project_plan_request.json` | `project_plan` | `needs_more_input` | 추진계획서 누락값 경로 |
| `missing_result_report_request.json` | `result_report` | `needs_more_input` | 결과보고서 누락값 경로 |
| `review_report_needs_security_review.json` | `review_report` | `needs_security_review` | 검토보고서 기본 보안 경로 |
| `approved_review_report_request.json` | `review_report` | `ready_for_draft` | 승인된 검토보고서 제한 경로 |
| `blocked_real_value_like_request.json` | `unknown` | `blocked` | 금지 요청 차단 경로 |

`placeholder_confirmed_values` helper fixture는 별도 폴더에 2종으로 분리되어 있습니다.

| fixture | 역할 |
|---|---|
| `placeholder_confirmed_values_safe.json` | placeholder-confirmed 값 안전 검증 |
| `placeholder_confirmed_values_invalid.json` | 실제값 또는 잘못된 placeholder 후보 차단 검증 |

## 현재 커버 범위 판단

현재 fixture는 다음 상태 전이를 모두 커버합니다.

- `ready_for_draft`
- `needs_more_input`
- `needs_security_review`
- `blocked`
- payload 생성 경로
- payload 미생성 경로
- HWPX 렌더링 허용 경로
- HWPX 렌더링 제외 경로
- `review_report` 승인/미승인 분기
- blocked fixture 차단 분기

따라서 단순 회귀 테스트 관점에서는 즉시 fixture를 늘릴 필요가 없습니다.

## 확장 후보 재검토

| 후보 | 재검토 판단 | 이유 |
|---|---|---|
| one_page_report 템플릿 기반 fixture | 보류 | 기존 safe one_page_report fixture와 역할 중복 |
| project_plan ready fixture | 보류 | 현재 missing_fields 규칙상 ready 경로를 새 fixture만으로 검증하기 어려움 |
| result_report ready fixture | 보류 | 실적ㆍ예산ㆍ수량을 실제값 없이 ready 처리할 규칙이 아직 없음 |
| review_report 템플릿 승인 fixture | 보류 | 기존 approved review_report fixture와 역할 중복 |
| unknown needs_more_input fixture | 보류 | unknown을 blocked 대신 needs_more_input으로 보낼 정책 결정이 선행되어야 함 |
| blocked 입력 변형 fixture | 보류 | 기존 blocked fixture가 금지 요청 차단 경로를 커버 |
| placeholder_confirmed_values routing fixture | 보류 | helper는 read-only이며 routing 연결 전 단계 |

## 지금 fixture를 추가하지 않는 이유

현재 상태에서 fixture를 늘리면 다음 문제가 생깁니다.

- 기존 routing과 중복되는 fixture 증가
- 테스트 출력은 길어지지만 새 보장 범위가 작음
- project_plan/result_report ready 경로 기대값을 코드보다 앞서 확정하는 문제
- `placeholder_confirmed_values` helper 결과가 routing에 연결된 것처럼 오해될 위험
- missing_fields 자동 제외 금지 원칙과 충돌 가능

## 유지 결정

현재 결정:

- 일반 routing fixture 6종 유지
- helper fixture 2종은 별도 폴더 유지
- fixture JSON 추가 없음
- normalizer 코드 변경 없음
- routing 결과 변경 없음
- HWPX payload 반영 없음
- `placeholder_confirmed_values` 연결 없음

## 다음에 fixture를 추가할 수 있는 조건

fixture를 추가하려면 다음 중 하나가 먼저 정리되어야 합니다.

1. `missing_fields` 생성 규칙 개선 여부 결정
2. placeholder-confirmed 값을 `[확인 필요]`와 어떻게 구분할지 결정
3. project_plan/result_report의 ready 경로를 열지 여부 결정
4. unknown 문서 유형을 blocked가 아닌 `needs_more_input`으로 보낼지 결정
5. review_report 승인 신호 fixture가 기존 approved fixture보다 더 큰 검증 가치를 갖는지 확인

## 다음 최소 작업 후보

현재 추천은 fixture 추가가 아니라 `missing_fields` 생성 규칙 개선 여부를 다시 보는 것입니다.

검토할 질문:

- project_plan/result_report의 필수값 누락을 항상 `needs_more_input`으로 둘지
- placeholder-confirmed 값이 있으면 `[확인 필요]` 유지 초안으로 볼 수 있는지
- `missing_fields`를 자동 제외하지 않는 원칙을 유지하면서 사용자에게 더 보기 좋게 표시할 방법이 있는지
- 코드 변경 없이 문서 기준으로만 운영할 수 있는지

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX 원본 파일 추가 없음
- Email, API, Make.com 연동 없음

## 결론

현재는 fixture 확장을 진행하지 않습니다.

기존 6종 fixture와 helper 전용 2종 fixture를 유지하고, 다음 단계에서 `missing_fields` 생성 규칙 개선 여부를 문서 기준으로 재검토합니다.
