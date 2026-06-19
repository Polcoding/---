# placeholder_confirmed_values normalizer 연결 정책

## 목적

`placeholder_confirmed_values` helper 결과를 normalizer 흐름에 연결할지 판단하기 전에, 연결 허용 조건과 금지 조건을 정리합니다.

현재 결론은 helper 결과를 아직 normalizer 흐름에 연결하지 않는 것입니다.

## 현재 코드 기준

현재 normalizer 흐름은 다음 구조입니다.

```text
fixture
→ input_normalizer_poc.py
→ make_content_inputs()
→ make_missing_fields()
→ make_initial_security_flags()
→ security_filter_poc.py
→ routing_decision
→ hwpx_payload_mapper_poc.py
```

`placeholder_confirmed_values` helper는 별도 검증 스크립트에서만 사용합니다.

```text
normalizers/fixtures/placeholder_confirmed_values/*.json
→ validate_placeholder_confirmed_values_poc.py
→ placeholder_confirmed_values.py
```

## 연결하지 않는 이유

현재 단계에서는 helper 결과를 normalizer output에 붙이지 않습니다.

이유:

- `missing_fields` 감소는 routing 결과에 직접 영향을 줄 수 있습니다.
- invalid helper finding을 `blocked`로 바꾸면 기존 회귀 기준이 달라질 수 있습니다.
- helper 결과를 metadata로만 붙이더라도 normalizer output schema가 확장됩니다.
- 기존 fixture 6종은 routing 회귀 테스트 기준으로 안정화되어 있습니다.
- `project_plan`과 `result_report`의 `ready_for_draft` 경로를 아직 열지 않았습니다.
- HWPX payload mapper와 renderer dry-run의 입력 구조를 당장 바꿀 필요가 없습니다.

## 연결 허용 조건

향후 연결을 검토하려면 다음 조건을 모두 만족해야 합니다.

1. 연결 방식은 read-only metadata여야 합니다.
2. `missing_fields` 목록을 변경하지 않아야 합니다.
3. `routing_decision.status`를 변경하지 않아야 합니다.
4. `routing_decision.reason`과 `next_action`을 변경하지 않아야 합니다.
5. HWPX payload mapper 결과를 변경하지 않아야 합니다.
6. HWPX renderer dry-run 결과를 변경하지 않아야 합니다.
7. invalid helper finding은 blocked 전환이 아니라 검토용 metadata로만 남겨야 합니다.
8. 보안 필터 판단이 helper 판단보다 우선해야 합니다.
9. 기존 fixture 6종 회귀 테스트가 그대로 통과해야 합니다.
10. helper 전용 fixture 검증이 기존 routing fixture와 분리되어야 합니다.

## 연결 금지 조건

다음 중 하나라도 해당하면 normalizer 연결을 하지 않습니다.

- helper 결과로 `missing_fields`를 자동 제외하려는 경우
- helper 결과로 `ready_for_draft` 경로를 열려는 경우
- invalid finding을 즉시 `blocked`로 바꾸려는 경우
- HWPX payload에 `placeholder_confirmed_values`를 넣으려는 경우
- 실제값 의심 패턴을 helper가 보안 필터보다 우선 판단하게 되는 경우
- 기존 fixture 6종의 expected routing을 바꿔야 하는 경우
- 실제 원문, 실제 개인정보, 실제 기관정보를 사용해야 하는 경우
- API, Make.com, Email 자동화와 결합하려는 경우

## 보안 필터 우선 원칙

helper는 placeholder 형식 판정 보조 도구입니다.

보안 판단 우선순위는 다음과 같습니다.

1. 명시적 차단 marker
2. 실제값 의심 패턴
3. security flags
4. security gate
5. `placeholder_confirmed_values` helper finding

따라서 helper가 safe로 판정해도 보안 필터가 위험하다고 판단하면 차단 또는 보안 검토가 우선입니다.

## 허용 가능한 read-only metadata 후보

향후 연결한다면 다음처럼 별도 metadata로만 둘 수 있습니다.

```json
{
  "placeholder_confirmed_values_review": {
    "checked": true,
    "valid": true,
    "invalid_count": 0,
    "findings": []
  }
}
```

이 metadata는 다음에 영향을 주지 않아야 합니다.

- `missing_fields`
- `routing_decision`
- `security_flags`
- HWPX payload
- HWPX output

## 현재 단계의 결정

현재 단계에서는 normalizer 연결을 보류합니다.

먼저 read-only metadata 설계 후보만 별도 문서로 검토합니다.

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX 원본 추가 없음
- API, Make.com, Email 자동화 코드 추가 없음

## 결론

`placeholder_confirmed_values` helper 결과는 아직 normalizer 흐름에 연결하지 않습니다.

다음 단계는 연결 전 검토용으로 read-only metadata schema 후보를 문서화하는 것입니다.
