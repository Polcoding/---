# placeholder_confirmed_values fixture schema 검토

## 목적

`placeholder_confirmed_values` read-only helper 구현 결과를 기준으로, 해당 구조를 `normalizers/fixtures/` schema에 확장할지 검토합니다.

이번 문서는 코드 연결 문서가 아니라 fixture schema 후보와 검증 방식을 정리하는 문서입니다.

## 현재 기준

현재 저장소에는 다음 helper가 있습니다.

- `normalizers/placeholder_confirmed_values.py`
- `normalizers/validate_placeholder_confirmed_values_poc.py`

이 helper는 read-only입니다.

현재 helper는 다음 결과를 바꾸지 않습니다.

- `missing_fields`
- `routing_decision`
- HWPX payload mapper 결과
- HWPX renderer dry-run 결과
- mapped HWPX 렌더링 결과

## 검토 결론

`placeholder_confirmed_values`는 fixture schema 후보로 문서화합니다.

다만 현재 단계에서는 기존 fixture 6종에 바로 추가하지 않습니다.

이유:

- 기존 fixture 6종은 정규화, 보안 필터, mapper, validation, dry-run 회귀 기준으로 안정화되어 있습니다.
- `placeholder_confirmed_values`를 기존 fixture에 넣으면 read-only helper라도 fixture 의미가 복잡해질 수 있습니다.
- `missing_fields` 자동 제외를 아직 허용하지 않았습니다.
- `project_plan`과 `result_report`의 `ready_for_draft` 경로도 아직 열지 않았습니다.
- helper 검증은 기존 routing 회귀 테스트와 분리하는 편이 더 안전합니다.

## schema 후보

향후 fixture에 도입한다면 다음 형태를 사용합니다.

```json
{
  "fixture_id": "[fixture ID placeholder]",
  "request_text": "[비식별 업무 지시 placeholder]",
  "expected_document_type": "project_plan",
  "expected_routing_status": "needs_more_input",
  "placeholder_confirmed_values": {
    "schedule": "[추진 일정 확인 필요]",
    "budget": "[예산 확인 필요]"
  },
  "expected_placeholder_confirmed_validation": {
    "valid": true,
    "invalid_count": 0
  }
}
```

## 필드 의미

| 필드 | 의미 | 현재 처리 |
|---|---|---|
| `placeholder_confirmed_values` | 사용자가 실제값 대신 placeholder 유지 의사를 밝힌 값 | schema 후보 |
| `expected_placeholder_confirmed_validation.valid` | helper 판정 기대값 | helper 전용 검증 |
| `expected_placeholder_confirmed_validation.invalid_count` | invalid finding 기대 수 | helper 전용 검증 |

## 허용 예

다음 값은 helper 검증용 후보로 허용할 수 있습니다.

- `[추진 일정 확인 필요]`
- `[예산 확인 필요]`
- `[실적 수치 확인 필요]`
- `[담당부서 확인 필요]`
- `[검토 범위 확인 필요]`
- `[비식별 배경 요약]`

## 금지 예

다음 값은 대괄호 안에 있어도 placeholder-confirmed 값으로 인정하지 않습니다.

- 실제 날짜처럼 보이는 값
- 실제 금액처럼 보이는 값
- 실제 담당자명 또는 연락처
- 실제 기관명 또는 부서명
- 실제 문서번호, 민원번호, 사건번호
- 실제 검토의견 원문
- 실제 계약 조건 또는 업체 평가

## 회귀 테스트 분리 원칙

현재는 두 검증 축을 분리합니다.

### 기존 fixture 회귀 테스트

대상:

- `normalizers/input_normalizer_poc.py`
- `normalizers/hwpx_payload_mapper_poc.py`
- `normalizers/validate_hwpx_payload_poc.py`
- `normalizers/hwpx_renderer_dry_run_poc.py`
- `normalizers/render_mapped_hwpx_poc.py`

역할:

- 문서 유형 판정 확인
- routing 확인
- `missing_fields` 유지 확인
- HWPX payload 생성 확인
- dry-run 및 mapped render 확인

### helper 전용 검증

대상:

- `normalizers/validate_placeholder_confirmed_values_poc.py`

역할:

- placeholder-confirmed 값의 형식 판정
- 실제값 의심 marker 또는 패턴 충돌 확인
- invalid finding 수 확인

## 현재 단계에서 하지 않는 것

- 기존 fixture 6종에 `placeholder_confirmed_values` 추가
- `missing_fields` 자동 제외
- routing 결과 변경
- `project_plan` ready 경로 개방
- `result_report` ready 경로 개방
- HWPX payload에 `placeholder_confirmed_values` 반영
- API, Make.com, Email 자동화 연동

## 후속 처리 결과

후속 작업에서 helper 전용 검증 케이스를 fixture 파일 기반으로 분리했습니다.

분리 위치:

- `normalizers/fixtures/placeholder_confirmed_values/placeholder_confirmed_values_safe.json`
- `normalizers/fixtures/placeholder_confirmed_values/placeholder_confirmed_values_invalid.json`

이 fixture는 기존 routing 회귀 테스트에 섞지 않습니다.

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX 원본 추가 없음
- API, Make.com, Email 자동화 코드 추가 없음

## 결론

`placeholder_confirmed_values` fixture schema는 후보로 채택합니다.

하지만 현재 단계에서는 기존 fixture 6종에 적용하지 않고, helper 전용 검증으로 분리해 유지합니다.

다음 작업은 helper 결과를 normalizer 흐름에 연결할지 여부를 판단하기 전에, 연결 허용 조건과 금지 조건을 별도 문서로 정리하는 것입니다.
