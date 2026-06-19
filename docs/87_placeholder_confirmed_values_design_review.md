# placeholder_confirmed_values 도입 검토

## 목적

`missing_fields` 생성 규칙을 바로 바꾸기 전에 `placeholder_confirmed_values` 구조를 도입할 필요가 있는지 검토합니다.

이 문서는 코드 구현 문서가 아니라 입력 구조 설계 검토 문서입니다.

## 문제 배경

현재 `normalizers/input_normalizer_poc.py`는 문서 유형별로 고정 `missing_fields`를 생성합니다.

이 방식은 안전하지만, 사용자가 다음처럼 실제값이 아니라 placeholder 유지 의도를 명시해도 누락값이 줄어들지 않습니다.

```text
추진 일정은 아직 확정하지 않고 [추진 일정 확인 필요]로 유지합니다.
예산은 아직 확정하지 않고 [예산 확인 필요]로 유지합니다.
```

이 값은 실제 일정이나 예산이 아닙니다. 그러나 현재 구조에서는 "확인 필요 placeholder를 의도적으로 유지한다"는 사실을 별도로 표현할 방법이 없습니다.

## 정의

`placeholder_confirmed_values`는 사용자가 실제값을 제공한 것이 아니라, 해당 필드를 placeholder 상태로 유지하겠다고 명시한 값입니다.

예:

```json
{
  "placeholder_confirmed_values": {
    "schedule": "[추진 일정 확인 필요]",
    "budget": "[예산 확인 필요]",
    "results_or_metrics": "[실적 수치 확인 필요]"
  }
}
```

## known_values와의 구분

| 구분 | 의미 | 예시 | 현재 처리 |
|---|---|---|---|
| `known_values` | 사용자가 제공했고 보안상 허용되는 확인값 | `[비식별 사업명]` | 제한적으로 허용 |
| `placeholder_confirmed_values` | 실제값 없이 placeholder 유지가 확인된 값 | `[예산 확인 필요]` | 도입 검토 |
| `missing_fields` | 아직 사용자 확인이 필요한 값 | `budget`, `schedule` | 현재 고정 생성 |

`placeholder_confirmed_values`는 실제값이 아니므로 `known_values`에 넣지 않습니다.

## 허용 조건

다음 조건을 모두 만족할 때만 `placeholder_confirmed_values`로 인정합니다.

- 값이 문자열 placeholder 형식임
- 값이 `[`로 시작하고 `]`로 끝남
- 실제 숫자, 금액, 날짜, 사람 이름, 연락처, 문서번호가 없음
- 의미가 "확인 필요", "검토 필요", "미확정" 계열임
- 사용자가 실제값 대신 placeholder로 유지하겠다고 명시함

허용 예:

- `[추진 일정 확인 필요]`
- `[예산 확인 필요]`
- `[실적 수치 확인 필요]`
- `[담당부서 확인 필요]`
- `[검토 범위 확인 필요]`

## 금지 조건

다음은 `placeholder_confirmed_values`로 인정하지 않습니다.

- 실제 날짜처럼 보이는 값
- 실제 금액처럼 보이는 값
- 실제 담당자명 또는 연락처
- 실제 기관명 또는 부서명
- 실제 문서번호, 민원번호, 사건번호
- 실제 검토의견 원문
- 실제 계약 조건 또는 업체 평가

## missing_fields와의 관계

향후 코드 개선 시 후보 규칙은 다음과 같습니다.

```text
문서 유형별 required field 목록
→ placeholder_confirmed_values에 포함된 field 제외
→ 남은 field만 missing_fields 생성
```

예:

```json
{
  "document_type": "project_plan",
  "placeholder_confirmed_values": {
    "schedule": "[추진 일정 확인 필요]",
    "budget": "[예산 확인 필요]"
  }
}
```

위 입력은 실제 일정과 예산이 확정된 것이 아니라, 해당 항목을 placeholder 상태로 유지하겠다는 의미입니다.

## 도입 효과

- `docs/84_hwpx_report_user_input_templates.md`의 입력 템플릿을 fixture 구조로 옮기기 쉬워집니다.
- `project_plan`과 `result_report`에서 placeholder-confirmed ready 경로를 검토할 수 있습니다.
- 실제값을 생성하지 않으면서 누락값과 의도적 placeholder 유지값을 구분할 수 있습니다.

## 도입 위험

- 실제값이 placeholder-confirmed로 잘못 분류될 수 있습니다.
- `missing_fields`가 줄어들면서 사람이 확인해야 할 항목이 덜 보일 수 있습니다.
- 현재 안정적인 fixture 6종 회귀 기준이 복잡해질 수 있습니다.

## 현재 판단

현재 단계에서는 구조 도입을 문서상 후보로 채택하되, 코드 구현은 보류합니다.

이유:

- 기존 fixture 6종이 회귀 기준으로 충분히 안정적입니다.
- 실제값 필터링과 placeholder 판정 함수를 먼저 설계해야 합니다.
- `known_values`와의 역할 분리가 더 명확해진 뒤 코드에 반영하는 것이 안전합니다.

## 코드 도입 전 최소 조건

코드로 도입하려면 다음 조건을 먼저 만족해야 합니다.

1. placeholder 형식 판정 함수 정의
2. 실제값 의심 패턴과 충돌할 때는 보안 필터 우선
3. `known_values`와 `placeholder_confirmed_values`를 분리한 fixture schema 확정
4. 기존 fixture 6종 기대 결과 유지
5. 신규 fixture는 실제값 없이 placeholder만 사용
6. `project_plan`과 `result_report` ready 경로를 열지 여부 별도 결정

## 보안 조건

- 실제 원문 사용 금지
- 실제 개인정보 사용 금지
- 실제 기관명, 부서명, 담당자명 사용 금지
- 실제 문서번호, 민원번호, 사건번호 사용 금지
- 실제 예산액, 일정, 실적 수치 사용 금지
- 실제 승인자명, 결재번호, 검토의견 원문 사용 금지
- Email/API/Make.com 연동 금지

## 결론

`placeholder_confirmed_values`는 도입 가치가 있지만, 현재는 문서상 설계 후보로 유지합니다.

다음 단계는 placeholder 형식 판정 기준과 실제값 의심 패턴 충돌 처리 규칙을 정리하는 것입니다.
