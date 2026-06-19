# placeholder_confirmed_values read-only metadata schema

## 목적

`placeholder_confirmed_values` helper 결과를 normalizer 흐름에 연결하기 전에, read-only metadata schema 후보를 문서화합니다.

현재 단계에서는 이 schema를 코드에 연결하지 않습니다.

## schema 위치 후보

metadata는 `security_flags` 내부가 아니라 top-level 필드 후보로 둡니다.

후보 필드명:

```text
placeholder_confirmed_values_review
```

이유:

- `security_flags`는 보안 판단과 routing 보정에 영향을 주는 값입니다.
- helper 결과를 `security_flags`에 넣으면 blocked 또는 needs_security_review 판단과 섞일 수 있습니다.
- `placeholder_confirmed_values_review`는 보안 판단이 아니라 placeholder 형식 검토 결과입니다.
- top-level metadata로 두면 read-only 성격이 더 명확합니다.

## schema 후보

```json
{
  "placeholder_confirmed_values_review": {
    "checked": true,
    "source": "placeholder_confirmed_values",
    "valid": true,
    "invalid_count": 0,
    "findings": [],
    "affects_missing_fields": false,
    "affects_routing": false,
    "affects_payload": false
  }
}
```

## 필드 정의

| 필드 | 의미 | 필수 여부 |
|---|---|---|
| `checked` | helper 검증을 수행했는지 여부 | 필수 |
| `source` | 검증 대상 필드명 | 필수 |
| `valid` | invalid finding이 없는지 여부 | 필수 |
| `invalid_count` | invalid finding 개수 | 필수 |
| `findings` | field별 invalid reason 목록 | 필수 |
| `affects_missing_fields` | `missing_fields`에 영향을 주는지 여부 | 필수, 항상 `false` |
| `affects_routing` | routing에 영향을 주는지 여부 | 필수, 항상 `false` |
| `affects_payload` | HWPX payload에 영향을 주는지 여부 | 필수, 항상 `false` |

## findings 구조 후보

```json
{
  "field_name": "budget",
  "reason": "actual_value_marker"
}
```

`reason`은 helper가 반환하는 reason을 그대로 사용합니다.

예:

- `not_string`
- `not_bracket_placeholder`
- `empty_placeholder`
- `placeholder_too_long`
- `meaning_not_allowed`
- `actual_value_marker`
- `suspected_real_value:phone_like`
- `suspected_real_value:email_like`
- `suspected_real_value:resident_id_like`
- `suspected_real_value:vehicle_number_like`
- `suspected_real_value:date_like`
- `suspected_real_value:money_like`
- `suspected_real_value:document_number_like`

## safe 예시

```json
{
  "placeholder_confirmed_values": {
    "schedule": "[추진 일정 확인 필요]",
    "budget": "[예산 확인 필요]"
  },
  "placeholder_confirmed_values_review": {
    "checked": true,
    "source": "placeholder_confirmed_values",
    "valid": true,
    "invalid_count": 0,
    "findings": [],
    "affects_missing_fields": false,
    "affects_routing": false,
    "affects_payload": false
  }
}
```

## invalid 예시

```json
{
  "placeholder_confirmed_values": {
    "budget": "[실제 금액 입력됨]"
  },
  "placeholder_confirmed_values_review": {
    "checked": true,
    "source": "placeholder_confirmed_values",
    "valid": false,
    "invalid_count": 2,
    "findings": [
      {
        "field_name": "budget",
        "reason": "meaning_not_allowed"
      },
      {
        "field_name": "budget",
        "reason": "actual_value_marker"
      }
    ],
    "affects_missing_fields": false,
    "affects_routing": false,
    "affects_payload": false
  }
}
```

위 예시는 실제 금액을 쓰지 않고 설명형 placeholder만 사용합니다.

## 변경 금지 원칙

이 metadata가 추가되더라도 다음 값은 바꾸지 않습니다.

- `missing_fields`
- `routing_decision.status`
- `routing_decision.reason`
- `routing_decision.next_action`
- `security_flags`
- HWPX payload mapper 결과
- HWPX renderer dry-run 결과
- HWPX output

## 보안 필터 우선 원칙

`placeholder_confirmed_values_review.valid`가 `true`여도 보안 필터가 위험하다고 판단하면 보안 필터 판단이 우선합니다.

`placeholder_confirmed_values_review.valid`가 `false`여도 현재 단계에서는 즉시 `blocked`로 전환하지 않습니다.

invalid finding은 검토용 metadata로만 남깁니다.

## 현재 단계의 결정

현재 단계에서는 schema 후보만 문서화합니다.

아직 하지 않습니다.

- normalizer output에 metadata 추가
- 기존 fixture 6종 schema 변경
- `missing_fields` 자동 제외
- routing 결과 변경
- HWPX payload 반영

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX 원본 추가 없음
- API, Make.com, Email 자동화 코드 추가 없음

## 결론

`placeholder_confirmed_values_review`는 read-only top-level metadata 후보로 둡니다.

후속 작업에서 이 metadata는 코드에 연결하지 않고 문서 기준 schema 후보로 유지하기로 결정했습니다.

dry-run preview 전용 출력도 현재는 만들지 않습니다.

다음 단계는 Phase 2 최소 PoC의 전체 상태를 다시 묶어 구현 계속 진행 범위와 보류 범위를 구분하는 것입니다.
