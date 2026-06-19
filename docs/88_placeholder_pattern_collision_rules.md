# placeholder 형식 판정 및 실제값 충돌 규칙

## 목적

`placeholder_confirmed_values`를 코드에 넣기 전에 placeholder로 인정할 수 있는 문자열 기준과 실제값 의심 패턴이 섞였을 때의 처리 규칙을 정리합니다.

이 문서는 보안 필터 우선 원칙을 확정하기 위한 설계 문서입니다.

## 기본 원칙

placeholder는 실제값이 아닙니다.

placeholder처럼 보여도 실제값 의심 패턴이 포함되면 placeholder로 인정하지 않습니다.

충돌 시 항상 보안 필터가 우선합니다.

```text
placeholder 형식처럼 보임
→ 실제값 의심 패턴 검사
→ 의심 패턴 있으면 needs_security_review 또는 blocked
→ 의심 패턴 없고 허용 의미이면 placeholder 인정
```

## 허용 placeholder 형식

다음 조건을 모두 만족해야 합니다.

| 조건 | 기준 |
|---|---|
| 괄호 | `[`로 시작하고 `]`로 끝남 |
| 길이 | 지나치게 길지 않은 짧은 문구 |
| 의미 | 확인 필요, 검토 필요, 미확정, 비식별 요약 계열 |
| 실제값 | 실제 사람, 기관, 번호, 금액, 날짜, 연락처 없음 |
| 용도 | missing value 유지 또는 비식별 설명 |

허용 예:

- `[확인 필요]`
- `[추진 일정 확인 필요]`
- `[예산 확인 필요]`
- `[실적 수치 확인 필요]`
- `[담당부서 확인 필요]`
- `[검토 범위 확인 필요]`
- `[비식별 배경 요약]`

## 조건부 허용

다음은 문맥에 따라 허용하지만, 실제값으로 오인될 수 있으면 보류합니다.

| 예시 | 조건 |
|---|---|
| `[비식별 사업명]` | 실제 사업명 아님이 명확할 때 |
| `[비식별 사안]` | 실제 사건명, 민원명, 대상자명 아님이 명확할 때 |
| `[비식별 부서]` | 실제 부서명 아님이 명확할 때 |
| `[검토 의견 확인 필요]` | 실제 검토의견 원문이 아님이 명확할 때 |

## 금지 placeholder 형식

다음은 대괄호 안에 있어도 placeholder로 인정하지 않습니다.

| 유형 | 이유 |
|---|---|
| 실제 연락처 형식 | 개인정보 의심 |
| 실제 이메일 형식 | 개인정보 또는 계정정보 의심 |
| 실제 주민등록번호 형식 | 고유식별정보 의심 |
| 실제 차량번호 형식 | 내부 운영정보 또는 개인정보 의심 |
| 실제 문서번호ㆍ민원번호ㆍ사건번호 형식 | 식별정보 의심 |
| 실제 금액 또는 견적 형태 | 예산ㆍ계약 실제값 의심 |
| 실제 날짜 또는 세부 일정 형태 | 일정 실제값 의심 |
| 실제 기관명ㆍ부서명ㆍ담당자명 | 식별정보 의심 |
| 실제 검토의견 원문 | 내부 판단 또는 민감정보 의심 |

## 충돌 처리 규칙

| 상황 | 처리 |
|---|---|
| placeholder 형식이고 실제값 패턴 없음 | placeholder 인정 |
| placeholder 형식이지만 연락처ㆍ이메일 패턴 포함 | `blocked` |
| placeholder 형식이지만 문서번호ㆍ민원번호ㆍ사건번호 의심 | `blocked` 또는 `needs_security_review` |
| placeholder 형식이지만 금액ㆍ견적ㆍ계약 조건 포함 | `needs_security_review` |
| placeholder 형식이지만 실제 날짜ㆍ상세 일정 포함 | `needs_security_review` |
| placeholder 형식이지만 실제 기관명ㆍ담당자명 의심 | `needs_security_review` |
| 판단이 애매함 | 더 보수적으로 `needs_security_review` |

## 보안 필터 우선 원칙

`placeholder_confirmed_values`에 들어온 값도 보안 필터 대상입니다.

보안 필터는 다음을 확인해야 합니다.

- 전화번호, 이메일, 고유식별번호 패턴
- 문서번호, 민원번호, 사건번호 의심 패턴
- 차량번호, 내부 운영정보 의심 패턴
- 예산ㆍ계약ㆍ업체 평가 실제값 의심
- 실제 원문 또는 자동화 금지 요청 문맥

보안 필터가 위험하다고 판단하면 placeholder 인정 여부와 관계없이 중단합니다.

## missing_fields 반영 후보 규칙

향후 코드 도입 시 후보 규칙은 다음과 같습니다.

```text
field가 placeholder_confirmed_values에 있음
→ 값이 허용 placeholder 형식인지 확인
→ 실제값 의심 패턴과 충돌하는지 확인
→ 충돌 없으면 missing_fields에서 제외 가능
→ 충돌 있으면 security_flags에 반영하고 제외 금지
```

## fixture 작성 기준

`placeholder_confirmed_values` fixture를 추가한다면 다음 조건을 지킵니다.

- 실제값 없이 placeholder만 사용
- 실제 일정, 실제 예산, 실제 실적 수치 사용 금지
- 기존 fixture 6종 기대 결과 유지
- 신규 fixture는 `project_plan` 또는 `result_report`의 placeholder-confirmed 경로 검토용으로 제한
- `review_report`는 별도 보안 승인 신호와 혼동하지 않음

## 예시

허용 가능:

```json
{
  "placeholder_confirmed_values": {
    "schedule": "[추진 일정 확인 필요]",
    "budget": "[예산 확인 필요]"
  }
}
```

보류 또는 차단:

```json
{
  "placeholder_confirmed_values": {
    "budget": "[실제 금액 입력됨]",
    "manager": "[실제 담당자 연락처 입력됨]"
  }
}
```

위 예시는 실제값을 재현하지 않기 위해 설명형 문구만 사용합니다.

## 결론

placeholder 형식 판정은 단독으로 사용하지 않습니다.

항상 실제값 의심 패턴 검사와 함께 적용하며, 충돌 시 보안 필터가 우선합니다.

이 기준은 이후 read-only helper 구현에 반영되었습니다.

다음 단계는 helper 판정 결과를 기준으로 fixture schema 확장 여부를 검토하는 것입니다.
