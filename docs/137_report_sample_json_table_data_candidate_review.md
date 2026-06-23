# 보고서 샘플 JSON 표 데이터 후보 표시 반영 검토

## 목적

이 문서는 `examples/json` 보고서 샘플 4종에 `docs/136_table_data_candidate_user_input_display_criteria.md`의 표 데이터 후보 표시 기준을 직접 반영할 필요가 있는지 검토한 결과입니다.

이번 검토는 실제 JSON fixture 추가, renderer 변경, normalizer 변경, HWPX payload 변경, HWPX output 재생성을 위한 작업이 아닙니다.

## 확인 대상

| 파일 | document_type | 확인 결과 |
|---|---|---|
| `examples/json/sample_one_page_report.json` | `one_page_report` | `renderer_hints.table_template`이 placeholder로 존재하나, 별도 표 데이터 필드는 없음 |
| `examples/json/sample_project_plan.json` | `project_plan` | `schedule`, `budget`, `table_template`은 placeholder 기반이며 실제 일정ㆍ예산 없음 |
| `examples/json/sample_result_report.json` | `result_report` | 실적, 참여 인원, 예산 집행액은 placeholder와 `missing_fields`로 분리됨 |
| `examples/json/sample_review_report.json` | `review_report` | 검토항목과 위험요소는 placeholder 기반이며 확정 판단 없음 |

샘플 JSON 4종은 모두 실제 원문, 실제 개인정보, 실제 기관정보, 실제 표 데이터를 포함하지 않습니다.

## 판단

현재 단계에서는 샘플 JSON 4종에 `table_data_candidate` 같은 새 필드를 직접 추가하지 않습니다.

이유:

- 샘플 JSON은 HWPX renderer 검증에도 사용되는 기준 데이터입니다.
- 새 필드가 HWPX payload 확장이나 renderer placeholder 추가처럼 오해될 수 있습니다.
- 현재 `tasks/NEXT_STEP.md`는 routing, HWPX payload, fixture JSON, renderer, normalizer 변경을 금지합니다.
- `docs/136`은 사용자 입력 표시 기준이며, 실행 payload 구조 변경 지시가 아닙니다.
- 기존 샘플의 `renderer_hints.table_template`은 표 서식 또는 표시 후보 힌트로만 해석하면 충분합니다.

따라서 이번 단계의 결정은 다음과 같습니다.

| 항목 | 결정 |
|---|---|
| 샘플 JSON 직접 수정 | 보류 |
| `table_data_candidate` 새 필드 추가 | 보류 |
| `missing_fields` 생성 규칙 변경 | 없음 |
| `renderer_hints.table_template` 해석 | 표 데이터 후보가 아니라 서식 또는 표시 후보 힌트 |
| 향후 반영 조건 | 별도 승인 후 schema, renderer, normalizer 영향 검토 필요 |

## 문서유형별 판단

### one_page_report

원페이지 보고서는 본문 공간이 좁으므로 표 데이터 후보를 JSON 본문에 추가하면 초안 구조가 복잡해질 수 있습니다.

현재는 `renderer_hints.table_template`의 placeholder만 유지하고, 실제 표 데이터 후보 표시는 사용자 입력 템플릿과 검토용 문서에서만 다룹니다.

### project_plan

추진계획서는 일정표와 예산표 후보가 있으나, 현재 샘플의 `schedule`, `budget`은 이미 placeholder 기반입니다.

새 표 데이터 필드를 추가하지 않고, 일정과 예산은 `[확인 필요]` 또는 기존 placeholder로 유지합니다.

### result_report

결과보고서는 실적 집계, 참여 인원, 예산 집행액 후보가 있으나, 현재 샘플은 실제 수치 없이 `missing_fields`와 placeholder로 분리되어 있습니다.

따라서 새 표 데이터 후보 필드를 추가하지 않습니다.

### review_report

검토보고서는 검토항목 목록과 위험요소 매트릭스 후보가 있으나, 현재 샘플은 확정 판단을 하지 않는 구조입니다.

표 데이터 후보는 실제 검토 매트릭스가 아니라 필요 시 내부 검토용 후보로만 유지합니다.

## 향후 반영 조건

샘플 JSON에 표 데이터 후보 필드를 실제로 추가하려면 아래 조건을 먼저 충족해야 합니다.

| 조건 | 기준 |
|---|---|
| schema 영향 검토 | `docs/18_ai_output_json_schema.md`에서 필드 목적과 범위 재검토 |
| renderer 영향 검토 | HWPX placeholder map과 무관한 표시 후보인지 확인 |
| normalizer 영향 검토 | routing, `missing_fields`, HWPX payload가 바뀌지 않는지 확인 |
| 보안 검토 | 실제 표 데이터, 수량, 금액, 대상 목록이 포함되지 않는지 확인 |
| 사용자 승인 | 샘플 JSON 구조 변경을 별도 승인 |

현재 단계에서는 위 조건을 충족시키는 구현 또는 구조 변경을 진행하지 않습니다.

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 표 데이터, 물품명, 수량, 금액, 대상 목록 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX/HWP 원본 파일 추가 없음
- 실제 Excel/한셀 파일 추가 없음
- 샘플 JSON 4종 직접 수정 없음
- renderer, normalizer, fixture, routing, HWPX payload 변경 없음
- Email, API, Make.com 연동 구현 없음

## 결론

`examples/json` 보고서 샘플 4종에는 현재 단계에서 표 데이터 후보 필드를 직접 추가하지 않습니다.

표 데이터 후보 표시 기준은 `docs/136`과 사용자 입력 템플릿에서 관리하고, 샘플 JSON은 기존 placeholder 기반 renderer 검증 샘플로 유지합니다. 향후 실제 샘플 구조 변경이 필요하면 별도 승인 후 schema, renderer, normalizer 영향을 함께 검토합니다.

