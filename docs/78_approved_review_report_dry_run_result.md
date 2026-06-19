# approved review_report dry-run 결과

## 목적

`review_report`는 기본적으로 `needs_security_review`로 라우팅되므로 HWPX 렌더링하지 않습니다.

이 문서는 placeholder 수준의 보안 검토 완료 신호가 있는 경우에만 `review_report`가 validation과 dry-run을 통과하는지 확인합니다.

## 추가 fixture

- `normalizers/fixtures/approved_review_report_request.json`

fixture에는 실제 승인자명, 실제 부서명, 실제 결재번호, 실제 검토의견 원문을 넣지 않았습니다.

승인 신호는 다음 placeholder 구조만 사용합니다.

```json
{
  "security_gate": {
    "human_security_review_completed": true,
    "review_basis": "[비식별 보안 검토 완료]",
    "approved_for_placeholder_rendering": true
  }
}
```

## 구현 보정

### input normalizer

`security_gate`가 placeholder 승인 구조와 일치하면 정규화 결과에 포함합니다.

### security filter

`review_report`라도 placeholder 렌더링 승인 신호가 있으면 `ready_for_draft`로 라우팅합니다.

승인 신호가 없으면 기존처럼 `needs_security_review`를 유지합니다.

### payload mapper

승인된 placeholder 렌더링에서는 `contains_sensitive_info`와 `contains_internal_info`를 `false`로 변환합니다.

다만 `required_review`와 `notes`에는 보안 검토 이력을 남깁니다.

## 실행 결과

Codex 번들 Python으로 validation과 dry-run을 실행했습니다.

| fixture | routing | validation | dry-run | 판정 |
|---|---|---|---|---|
| `approved_review_report_request.json` | `ready_for_draft` | 통과 | `dry_run_ready` | 통과 |
| `review_report_needs_security_review.json` | `needs_security_review` | payload 미생성 | `skipped_security_review` | 통과 |
| `blocked_real_value_like_request.json` | `blocked` | payload 미생성 | `skipped_blocked` | 통과 |

기존 `one_page_report`, `project_plan`, `result_report` fixture도 validation과 dry-run 기준을 유지했습니다.

## 보안 검수

- 실제 개인정보 사용 여부: 사용하지 않음
- 실제 기관명, 업체명, 담당자명 사용 여부: 사용하지 않음
- 실제 승인자명, 실제 결재번호 사용 여부: 사용하지 않음
- 실제 문서번호, 민원번호, 사건번호 사용 여부: 사용하지 않음
- 실제 검토의견 원문 사용 여부: 사용하지 않음
- 실제 HWPX 생성 여부: 생성하지 않음
- Email/API/Make.com 연동 여부: 수행하지 않음

## 결론

`review_report`는 기본적으로 보안 검토 라우팅을 유지하며, placeholder 보안 승인 신호가 있을 때만 HWPX payload 생성과 dry-run을 허용할 수 있습니다.

다음 단계는 사용자가 허용하면 approved review_report 1건을 실제 HWPX로 렌더링하고 한컴 수동 검수를 진행하는 것입니다.
