# missing_fields 사용자 확인 표시 기준

## 목적

`missing_fields`를 사용자에게 보여줄 때 HWPX 본문, 검토용 확인 목록, 반복 운영 로그에서 혼동이 생기지 않도록 표시 기준을 정리합니다.

이 문서는 코드 변경 지시서가 아닙니다. 현재 단계에서는 `missing_fields` 생성 규칙, routing 결과, HWPX payload 구조를 바꾸지 않고 문서 기준만 정합니다.

## 적용 범위

적용 대상:

- Codex 완료 보고
- Phase 2 반복 운영 로그
- HWPX output 수동 검수 기준
- 향후 사용자 확인 화면 또는 preview 문서 후보

적용하지 않는 대상:

- `make_missing_fields()` 생성 규칙
- `routing_decision.status`
- HWPX payload 구조
- HWPX 본문 자동 치환 규칙
- `placeholder_confirmed_values` normalizer 연결

## 기본 원칙

- `missing_fields`는 본문 내용이 아니라 사람 검토용 확인 목록입니다.
- HWPX 본문에는 기존 placeholder 또는 `[확인 필요]`를 유지합니다.
- 검토용 영역에는 누락값의 의미, 위치, 사용자 조치만 분리해 표시합니다.
- `missing_fields`가 있어도 허용된 `needs_more_input` 경로는 placeholder 초안 렌더링이 가능합니다.
- `missing_fields`가 있다는 이유만으로 실제값을 임의 생성하지 않습니다.
- `placeholder_confirmed_values`가 있어도 `missing_fields`를 자동 제외하지 않습니다.

## 표시 순서

사용자에게는 다음 순서로 보여줍니다.

1. 문서 유형
2. routing 상태
3. 초안 생성 가능 여부
4. 확인 필요 항목 개수
5. 확인 필요 항목 목록
6. 사용자 조치
7. 보안 주의사항

확인 필요 항목 목록은 코드에서 생성된 순서를 유지합니다. 알파벳순 또는 임의 중요도순으로 재정렬하지 않습니다.

현재 문서 유형별 표시 순서는 다음과 같습니다.

| document_type | 표시 순서 |
|---|---|
| `one_page_report` | `purpose` |
| `project_plan` | `schedule` → `budget` |
| `result_report` | `results_or_metrics` → `budget` |
| `review_report` | `review_scope` → `required_reviews` |

## 필드 표시 방식

`missing_fields`의 내부 필드는 사용자에게 다음처럼 바꿔 보여줍니다.

| 내부 필드 | 사용자 표시명 | 표시 기준 |
|---|---|---|
| `field_name` | 확인 항목 | 내부 영문 키와 한글 설명을 함께 표시 |
| `reason` | 확인 사유 | 왜 확인이 필요한지 짧게 표시 |
| `required_for` | 관련 위치 | 어느 문서 영역에 필요한 값인지 표시 |
| `suggested_placeholder` | 임시 표시 | `[확인 필요]` 또는 안전 placeholder 표시 |

권장 표 형식:

| 순번 | 확인 항목 | 확인 사유 | 관련 위치 | 임시 표시 | 사용자 조치 | 처리 상태 |
|---|---|---|---|---|---|---|
| 1 | `schedule` / 추진 일정 | 추진 일정 미확정 | `project_plan.schedule` | `[확인 필요]` | 로컬 검토 후 확정 또는 placeholder 유지 | [확인 필요] |

위 표는 예시 구조입니다. 실제 일정, 예산, 실적, 담당자, 수량은 넣지 않습니다.

## 한글 표시명 후보

현재 고정 `missing_fields`는 다음 한글 표시명을 사용합니다.

| field_name | 한글 표시명 |
|---|---|
| `purpose` | 보고 목적 |
| `schedule` | 추진 일정 |
| `budget` | 예산 |
| `results_or_metrics` | 실적 또는 결과 수치 |
| `review_scope` | 검토 범위 |
| `required_reviews` | 필요 검토 주체 |

표시명은 사용자 가독성을 위한 설명입니다. 코드 키를 바꾸는 의미가 아닙니다.

## 표시 상태 구분

`[확인 필요]`, placeholder-confirmed 값, 실제값 금지 상태는 다음처럼 구분합니다.

| 상태 | 의미 | 권장 표시 |
|---|---|---|
| 값 미확인 | 아직 확인되지 않은 값 | 사용자 확인 필요 |
| placeholder 유지 확인 | 실제값 대신 placeholder 상태 유지 의사 확인 | placeholder 유지 확인 |
| 실제값 입력 금지 | 입력하면 안 되는 실제값 또는 민감값 | 실제값 입력 금지 |
| 보안 검토 필요 | 민감정보 또는 내부정보 가능성 있음 | 보안 검토 필요 |

현재 단계에서는 이 상태를 코드에 연결하지 않습니다. 운영 로그나 수동 검수 표에서 사람이 구분하기 위한 표시 기준입니다.

## HWPX 본문과 검토용 목록 분리

HWPX 본문에는 문서 초안 흐름을 유지합니다.

본문 예:

```text
추진 일정: [추진 일정 확인 필요]
예산: [예산 확인 필요]
```

검토용 확인 목록 예:

| 순번 | 확인 항목 | 확인 사유 | 사용자 조치 |
|---|---|---|---|
| 1 | 추진 일정 | 추진 일정 미확정 | 로컬 검토 후 확정 또는 placeholder 유지 |
| 2 | 예산 | 예산 미확정 | 실제 금액 입력 금지, 내부 검토 후 처리 |

본문과 검토용 목록을 같은 문단에 섞지 않습니다.

## 사용자에게 보여줄 요약 문구

Codex 완료 보고나 운영 로그에는 다음 문구를 사용할 수 있습니다.

```text
[사용자 확인 필요]
이 초안에는 확인 필요 항목이 있습니다.
본문의 [확인 필요] 값은 실제값이 아니며, 로컬 검토 후 유지ㆍ수정ㆍ제외 여부를 결정해야 합니다.
실제 개인정보, 실제 기관정보, 실제 문서번호, 실제 예산액, 실제 실적 수치는 입력하지 마세요.
```

더 짧게 표시해야 할 때:

```text
[사용자 확인 필요] missing_fields는 검토용 목록입니다. 본문 실제값으로 확정하지 마세요.
```

## 반복 운영 로그 반영 방식

Phase 2 반복 운영 로그에는 다음 섹션을 추가할 수 있습니다.

```markdown
## missing_fields 확인

| 확인 | 항목 | 결과 |
|---|---|---|
| [ ] | 확인 필요 항목 개수 확인 | [확인 필요] |
| [ ] | HWPX 본문과 검토용 목록 분리 확인 | [확인 필요] |
| [ ] | `[확인 필요]`가 실제값처럼 보이지 않음 | [확인 필요] |
| [ ] | placeholder 유지 확인 대상 구분 | [확인 필요] |
| [ ] | 실제값 입력 금지 안내 포함 | [확인 필요] |
```

이 섹션에는 실제 업무 값이나 실제 원문을 기록하지 않습니다.

## 중단 기준

다음 중 하나라도 발생하면 작업을 멈추고 입력을 다시 비식별화합니다.

- `missing_fields`를 이유로 실제 일정, 예산, 실적, 담당자를 임의 작성하려는 경우
- placeholder-confirmed 값을 실제값 확인 완료로 처리하려는 경우
- `missing_fields`를 자동 제외해 routing을 바꾸려는 경우
- 검토용 목록에 실제 개인정보, 기관명, 문서번호, 금액, 수치를 넣으려는 경우
- HWPX 본문과 검토용 확인 목록이 섞여 실제값처럼 보이는 경우

## 코드 변경 판단

현재 단계에서는 코드 변경이 필요하지 않습니다.

유지:

- 고정 `missing_fields` 생성 규칙
- 기존 routing fixture 6종
- helper fixture 2종 분리
- `placeholder_confirmed_values` read-only 유지
- HWPX payload 구조 유지

보류:

- `missing_fields` 자동 제외
- `placeholder_confirmed_values` normalizer 연결
- 사용자 표시용 preview output 생성
- HWPX payload에 display metadata 추가

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX 원본 파일 추가 없음
- Email, API, Make.com 연동 없음

## 결론

`missing_fields`는 사용자 확인용 검토 목록으로 표시합니다.

HWPX 본문에는 `[확인 필요]` placeholder를 유지하고, 검토용 목록에는 확인 항목ㆍ사유ㆍ관련 위치ㆍ사용자 조치를 분리해 표시합니다.

다음 단계는 이 기준을 Phase 2 반복 운영 로그 템플릿과 수동 점검표에 반영할지 검토하는 것입니다.

후속 작업에서 반복 운영 로그 템플릿 반영 결과는 `docs/105_missing_fields_repeat_log_reflection_result.md`에 정리했습니다.
