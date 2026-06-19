# mapped review_report 렌더링 정책

## 목적

이 문서는 입력 정규화 PoC에서 `review_report`가 `needs_security_review`로 라우팅되는 경우, HWPX 렌더링을 어떤 조건에서 허용할지 정합니다.

검토보고서는 법무, 계약, 개인정보, 내부 판단이 섞일 가능성이 높으므로 다른 보고서 유형보다 보수적으로 처리합니다.

## 결론

`review_report`는 기본적으로 HWPX 렌더링하지 않습니다.

렌더링 허용은 사람이 보안 검토를 완료했다는 명시적 승인 신호가 있을 때만 가능합니다.

## 기본 라우팅

| 상황 | routing | HWPX payload | HWPX 렌더링 |
|---|---|---|---|
| 일반 review_report | `needs_security_review` | 생성하지 않음 | 금지 |
| 민감정보 의심 | `needs_security_review` 또는 `blocked` | 생성하지 않음 | 금지 |
| 실제 식별정보 포함 의심 | `blocked` | 생성하지 않음 | 금지 |
| 사람 보안 검토 완료 | `ready_for_draft` 또는 승인된 `needs_more_input` | 조건부 생성 | 조건부 허용 |

## 렌더링 허용 조건

다음 조건을 모두 만족해야 합니다.

- 실제 개인정보 없음
- 실제 원문 없음
- 실제 기관명, 업체명, 담당자명 없음
- 실제 문서번호, 민원번호, 접수번호, 사건번호 없음
- 법률 적합성, 계약 가능성, 예산 집행 가능성 등을 확정하지 않음
- 검토 의견은 초안이며 사람 검토 필요 표시 유지
- `human_review_required`는 `true`
- 보안 검토 완료 신호가 placeholder 수준으로만 존재

## 승인 신호

승인 신호는 실제 승인자명이나 실제 결재 정보를 담지 않습니다.

허용 가능한 placeholder 신호:

```json
{
  "security_gate": {
    "human_security_review_completed": true,
    "review_basis": "[비식별 보안 검토 완료]",
    "approved_for_placeholder_rendering": true
  }
}
```

금지되는 승인 신호:

- 실제 승인자 이름
- 실제 부서명
- 실제 결재번호
- 실제 검토의견 원문
- 실제 내부 승인 경로

## PoC 처리 방향

현재 `review_report_needs_security_review.json` fixture는 그대로 유지합니다.

이 fixture는 렌더링 금지 케이스를 검증하는 기준입니다.

별도 렌더링 허용 케이스가 필요하면 새 fixture를 추가합니다.

권장 fixture:

```text
normalizers/fixtures/approved_review_report_request.json
```

이 fixture도 실제값 없이 placeholder만 사용해야 합니다.

## mapper 정책

`normalizers/hwpx_payload_mapper_poc.py`는 기본적으로 `needs_security_review` payload를 생성하지 않습니다.

향후 승인 fixture를 추가하는 경우에도 다음 방식 중 하나로 구현합니다.

1. 보안 필터가 승인 신호를 확인해 `ready_for_draft`로 라우팅
2. mapper가 `security_gate.approved_for_placeholder_rendering`을 확인해 제한적으로 payload 생성

현재 추천은 1번입니다.

보안 필터가 최종 라우팅을 결정하고, mapper는 라우팅 결과만 따르는 구조가 더 안전합니다.

## 중단 조건

다음 중 하나라도 있으면 렌더링하지 않습니다.

- `routing_decision.status`가 `needs_security_review`
- `routing_decision.status`가 `blocked`
- `security_flags.requires_security_review`가 `true`인데 승인 신호 없음
- 실제값 의심 패턴 감지
- 승인 신호에 실제 이름, 실제 결재정보, 실제 문서번호 포함

## 다음 단계

다음 작업은 approved placeholder review_report fixture를 만들지 여부를 결정하는 것입니다.

현재 추천은 fixture를 추가하되, 실제 렌더링 전에는 먼저 보안 필터와 mapper가 승인 신호를 올바르게 처리하는지 dry-run으로 검증하는 것입니다.
