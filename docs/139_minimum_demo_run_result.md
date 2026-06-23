# 최소 demo 실행 결과 요약

작성일: 2026-06-23

## 목적

이 문서는 `CURRENT_STATUS.md`에 정리한 최소 PoC 경로를 사람이 바로 확인할 수 있게 요약한 demo 결과입니다.

대상 경로는 다음입니다.

```text
비식별 요청 fixture
-> 입력 정규화
-> 보안 필터
-> HWPX payload mapper
-> payload validation
-> HWPX renderer dry-run
```

이 문서는 실제 업무용 HWPX 파일 생성 결과가 아닙니다. 실제 기관 양식, 실제 원문, 실제 개인정보, 실제 표 데이터, 실제 이메일/API/Make.com 연동은 포함하지 않습니다.

## 전체 진행 도식

```mermaid
flowchart LR
    A["1. 기획ㆍ보안 원칙<br/>완료"] --> B["2. 문서 유형ㆍ샘플 JSON<br/>완료"]
    B --> C["3. HWPX 보고서 4종 placeholder PoC<br/>작동 확인"]
    C --> D["4. 입력 정규화ㆍ보안 필터<br/>작동 확인"]
    D --> E["5. HWPX payload mapperㆍvalidation<br/>작동 확인"]
    E --> F["6. renderer dry-run<br/>작동 확인"]
    F --> G["7. 최소 demo 결과 요약<br/>현재 단계"]
    G --> H["8. 실제 양식 안정화<br/>수동 확인 필요"]
    H --> I["9. 운영 연동<br/>보류"]
```

## 현재 체감 진행률

| 기준 | 현재 수준 | 설명 |
|---|---:|---|
| 로컬 PoC 기준 | 약 65% | 비식별 fixture에서 dry-run까지 연결 확인 |
| 실제 운영 시스템 기준 | 약 30~35% | 실제 양식 안정화, 운영 화면, 외부 연동, 운영 로그는 미진입 |

## 확인한 증거 파일

| 구분 | 파일 | 확인 내용 |
|---|---|---|
| placeholder 값 검증 helper | `normalizers/output/placeholder_confirmed_values_summary.json` | safe/invalid fixture 7건 기대 결과 통과 |
| 입력 정규화 | `normalizers/output/normalization_summary.json` | routing fixture 6건 기대 문서 유형과 상태 통과 |
| HWPX payload mapper | `normalizers/output/hwpx_payload_mapping_summary.json` | payload 생성 4건, 안전 스킵 2건 기대 결과 통과 |
| HWPX payload validation | `normalizers/output/hwpx_payload_validation_summary.json` | validation 4건 통과, 안전 스킵 2건 통과 |
| HWPX renderer dry-run | `normalizers/output/hwpx_renderer_dry_run_summary.json` | dry-run ready 2건, missing_fields 포함 ready 2건, 안전 스킵 2건 확인 |

## demo fixture별 결과

| fixture | 문서 유형 | routing 상태 | payload | dry-run 상태 | 판단 |
|---|---|---|---|---|---|
| `safe_one_page_report_request.json` | `one_page_report` | `ready_for_draft` | 생성 | `dry_run_ready` | 원페이지 보고서 dry-run 가능 |
| `missing_project_plan_request.json` | `project_plan` | `needs_more_input` | 생성 | `dry_run_ready_with_missing_fields` | 추진계획서 missing_fields 유지 후 dry-run 가능 |
| `missing_result_report_request.json` | `result_report` | `needs_more_input` | 생성 | `dry_run_ready_with_missing_fields` | 결과보고서 missing_fields 유지 후 dry-run 가능 |
| `approved_review_report_request.json` | `review_report` | `ready_for_draft` | 생성 | `dry_run_ready` | 검토보고서 보안 검토 승인 조건에서 dry-run 가능 |
| `review_report_needs_security_review.json` | `review_report` | `needs_security_review` | 미생성 | `skipped_security_review` | 보안 검토 전 안전 스킵 |
| `blocked_real_value_like_request.json` | `unknown` | `blocked` | 미생성 | `skipped_blocked` | 실제값 또는 금지 자동화 의심 입력 차단 |

## HWPX 템플릿 인식 상태

| 문서 유형 | dry-run template | 상태 |
|---|---|---|
| `one_page_report` | `templates\hwpx\placeholder_one_page_report.hwpx` | `template_available: true` |
| `project_plan` | `templates\hwpx\placeholder_project_plan.hwpx` | `template_available: true` |
| `result_report` | `templates\hwpx\placeholder_result_report.hwpx` | `template_available: true` |
| `review_report` | `templates\hwpx\placeholder_review_report.hwpx` | `template_available: true` |

위 파일들은 local placeholder HWPX 템플릿입니다. Git 커밋 대상이 아니며, 실제 기관 양식 원본도 아닙니다.

## 안전 동작 확인

| 상황 | 확인 결과 |
|---|---|
| 실제값 또는 금지 자동화 의심 | `blocked`, payload 미생성 |
| 보안 검토 필요 | `needs_security_review`, payload 미생성 |
| 필수값 미확정 | `needs_more_input`, missing_fields 유지 |
| HWPX 렌더링 전 상태 확인 | `dry_run_ready` 또는 `dry_run_ready_with_missing_fields` |
| 실제 업무용 HWPX output 생성 | 이번 demo 요약에서는 수행하지 않음 |

## 사용자 확인 필요

아래 항목은 아직 사람이 직접 확인해야 합니다.

1. 실제 기관 양식 후보를 사용할지 여부
2. 실제 양식 후보가 필요한 경우 저장소 밖 비식별 작업 복사본 준비 여부
3. 한컴에서 열었을 때 글자 겹침, 줄바꿈, 표 폭, 여백이 실제 업무용으로 맞는지 여부
4. 기관 표준 글꼴, 자간, 줄간격, 문단 간격 값
5. 표 내부 데이터 자동화를 Excel/한셀 연동 후보로 별도 진행할지 여부

## 결론

최소 demo 경로는 저장소 내부 기준으로 확인 가능합니다.

현재 단계에서 사용자에게 보여줄 수 있는 결과물은 실제 업무용 HWPX 파일이 아니라, 비식별 fixture가 안전하게 정규화되고 HWPX payload 및 renderer dry-run까지 도달한다는 검증 요약입니다.

다음 단계는 실제 업무용 HWPX 파일 생성보다, 이 demo 결과를 기준으로 어떤 사용자 입력 양식을 먼저 다듬을지 결정하는 것입니다.
