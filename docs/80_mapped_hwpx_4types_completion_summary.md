# HWPX 4종 mapped 렌더링 완료 요약

## 목적

입력 정규화 PoC에서 생성한 HWPX payload가 보고서 4종 placeholder 템플릿으로 안전하게 연결되는지 통합 확인합니다.

대상 보고서 4종:

1. `one_page_report`
2. `project_plan`
3. `result_report`
4. `review_report`

## 완료 상태

| 문서 유형 | fixture | routing | output | replaced_count | remaining_placeholders | 한컴 수동 검수 |
|---|---|---|---|---:|---:|---|
| `one_page_report` | `safe_one_page_report_request.json` | `ready_for_draft` | `mapped_safe_one_page_report_poc.hwpx` | 16 | 0 | 완료 |
| `project_plan` | `missing_project_plan_request.json` | `needs_more_input` | `mapped_missing_project_plan_poc.hwpx` | 22 | 0 | 완료 |
| `result_report` | `missing_result_report_request.json` | `needs_more_input` | `mapped_missing_result_report_poc.hwpx` | 20 | 0 | 완료 |
| `review_report` | `approved_review_report_request.json` | `ready_for_draft` | `mapped_approved_review_report_poc.hwpx` | 16 | 0 | 완료 |

## 사용자 수동 검수 요약

사용자가 한컴에서 생성 HWPX를 직접 열람해 다음을 확인했습니다.

- 파일 열림 정상
- 글자 겹침 없음
- 항목 제목 표시 정상
- 줄바꿈과 본문 배치 정상
- 내용 앞 `-` 표기 보정 완료
- 남은 `{{placeholder}}` 없음

## review_report 조건

`review_report`는 기본적으로 `needs_security_review`로 라우팅하고 HWPX payload를 생성하지 않습니다.

렌더링은 다음 placeholder 보안 승인 신호가 있을 때만 허용합니다.

```json
{
  "security_gate": {
    "human_security_review_completed": true,
    "review_basis": "[비식별 보안 검토 완료]",
    "approved_for_placeholder_rendering": true
  }
}
```

승인 신호가 없는 `review_report` fixture는 계속 `needs_security_review`로 멈춥니다.

## Git 제외 확인

다음 산출물은 Git 제외 상태로 유지합니다.

- `renderers/hwpx_renderer/output/*.hwpx`
- `normalizers/output/*`
- `templates/hwpx/*.hwpx`

로컬 HWPX 템플릿과 output HWPX는 저장소에 커밋하지 않습니다.

## 보안 검수

- 실제 기관 양식 원본 사용 여부: 사용하지 않음
- 실제 문서 원문 사용 여부: 사용하지 않음
- 실제 개인정보 사용 여부: 사용하지 않음
- 실제 기관명, 업체명, 담당자명 사용 여부: 사용하지 않음
- 실제 문서번호, 민원번호, 접수번호, 사건번호 사용 여부: 사용하지 않음
- 실제 승인자명, 결재번호 사용 여부: 사용하지 않음
- 실제 예산액, 일정, 실적 수치 생성 여부: 생성하지 않음
- Email/API/Make.com 연동 여부: 수행하지 않음

## 결론

HWPX 보고서 4종은 입력 정규화 결과에서 HWPX payload로 매핑되고, 로컬 placeholder HWPX 템플릿으로 렌더링되는 최소 end-to-end 흐름을 통과했습니다.

현재 단계의 완료 범위는 placeholder 기반 PoC입니다.

다음 단계는 실제 원본을 저장소에 넣지 않는 조건을 유지하면서, 입력 정규화와 보안 필터의 회귀 테스트 묶음을 정리하는 것입니다.
