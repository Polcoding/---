# placeholder_confirmed_values 코드 도입 여부 재검토

## 목적

`docs/87_placeholder_confirmed_values_design_review.md`와 `docs/88_placeholder_pattern_collision_rules.md`를 기준으로 `placeholder_confirmed_values`를 코드에 도입할지 재검토합니다.

## 현재 코드 상태

현재 `normalizers/input_normalizer_poc.py`는 다음 구조입니다.

- fixture의 `request_text`를 읽음
- 문서 유형을 판정함
- 문서 유형별 `content_inputs`를 생성함
- 문서 유형별 고정 `missing_fields`를 생성함
- `security_filter_poc.py`로 라우팅함

현재 `normalizers/security_filter_poc.py`는 다음을 수행합니다.

- 문자열 전체에서 차단 패턴 탐지
- 보안 flag와 차단 사유에 따라 routing 결정
- `review_report` 승인 gate를 별도 처리

## 도입 판단

`placeholder_confirmed_values`는 코드 도입 가치가 있습니다.

다만 현재 단계에서 바로 `missing_fields` 생성 결과를 바꾸는 것은 보류합니다.

이유:

- `missing_fields` 감소는 routing 결과에 직접 영향을 줄 수 있습니다.
- `project_plan`과 `result_report`의 `ready_for_draft` 경로를 열지 여부가 아직 별도 결정되지 않았습니다.
- placeholder 판정과 실제값 충돌 검사를 먼저 안정적으로 확인해야 합니다.
- 기존 fixture 6종 회귀 테스트를 흔들지 않는 것이 우선입니다.

## 권장 도입 순서

### 1단계: 판정 helper만 추가

`placeholder_confirmed_values` 값을 실제로 `missing_fields`에 반영하지 않고, 안전한 placeholder인지 판정하는 helper만 추가합니다.

후보 함수:

```text
is_placeholder_confirmed_value(value)
find_invalid_placeholder_confirmed_values(values)
```

역할:

- 문자열이 `[`와 `]`로 감싸져 있는지 확인
- 허용 의미인지 확인
- 실제값 의심 패턴과 충돌하지 않는지 확인
- 충돌 시 security filter가 우선되도록 reasons 생성

### 2단계: fixture schema 후보 추가

기존 fixture 6종은 유지합니다.

신규 fixture 후보는 바로 routing을 바꾸지 않고 helper 판정만 검증하는 형태로 둡니다.

### 3단계: missing_fields 반영 여부 재검토

helper와 fixture 검증이 안정화된 뒤 다음을 결정합니다.

- `placeholder_confirmed_values`에 있는 field를 `missing_fields`에서 제외할지
- 제외하더라도 `draft_status`와 `routing_decision`은 어떻게 유지할지
- `project_plan`과 `result_report`의 `ready_for_draft` 경로를 허용할지

## 현재 단계의 결정

이 문서 작성 시점에는 코드 변경을 하지 않았습니다.

이후 `docs/91_placeholder_confirmed_values_helper_result.md` 기준으로 read-only 판정 helper를 최소 구현했습니다.

현재 helper는 `missing_fields` 생성 결과와 routing 결과에 연결하지 않았습니다.

## 코드 도입 시 최소 범위

도입한다면 다음 범위를 넘지 않습니다.

- `normalizers/security_filter_poc.py` 또는 별도 normalizer helper에 placeholder 판정 함수 추가
- 기존 fixture 6종 기대 결과 유지
- `missing_fields` 생성 결과 변경 없음
- HWPX 렌더링 결과 변경 없음
- 실제값 의심 패턴과 충돌 시 blocked 또는 needs_security_review 유지

## 도입하지 않는 범위

다음은 아직 하지 않습니다.

- `missing_fields` 자동 제외
- `project_plan` ready fixture 추가
- `result_report` ready fixture 추가
- 실제값을 `known_values`로 받는 구조
- API/Make.com/Email 연동

## 보안 조건

- 실제 원문 사용 금지
- 실제 개인정보 사용 금지
- 실제 기관명, 부서명, 담당자명 사용 금지
- 실제 문서번호, 민원번호, 사건번호 사용 금지
- 실제 예산액, 일정, 실적 수치 사용 금지
- 실제 승인자명, 결재번호, 검토의견 원문 사용 금지

## 결론

`placeholder_confirmed_values`는 코드 도입 후보로 유지합니다.

현재는 `missing_fields`를 바꾸지 않는 read-only 판정 helper만 추가한 상태입니다.

다음 단계에서는 helper 판정 결과를 기준으로 fixture schema 확장 여부를 별도 검토합니다.
