# renderer와 normalizer 안내 문서의 표 데이터 후보 오해 가능성 점검

## 목적

이 문서는 renderer와 normalizer 안내 문서가 표 데이터 후보를 실제 HWPX 표 내부 데이터 자동 입력, Excel/한셀 연동, HWPX payload 확장으로 오해하게 만들지 않는지 점검한 결과입니다.

이번 점검은 renderer 코드, normalizer 코드, fixture, routing, HWPX payload, output을 변경하기 위한 작업이 아닙니다.

## 확인 대상

| 파일 | 확인 결과 |
|---|---|
| `renderers/hwpx_renderer/README.md` | HWPX output 제외 정책은 유지되어 있으나, 보고서 4종 샘플과 표 데이터 후보 보류 기준 보강 필요 |
| `normalizers/README.md` | `missing_fields`, routing, HWPX payload 미반영 원칙은 있으나, 최신 작업 축과 표 데이터 후보 보류 기준 보강 필요 |
| `docs/21_template_renderer_requirements.md` | `표 데이터` 표현이 실제 표 내부 데이터 생성처럼 읽힐 수 있어 `표 데이터 후보 또는 구조`로 축소 필요 |
| `docs/22_renderer_validation_samples.md` | 샘플 검증 문서에 표 데이터 후보 직접 반영 보류 기준 연결 필요 |
| `docs/70_hwpx_renderer_dry_run_scope.md` | dry-run이 실제 HWPX 생성이 아니라는 기준은 명확하며, table data candidate payload 확장이 아니라는 문구 보강 필요 |
| `docs/136_table_data_candidate_user_input_display_criteria.md` | 표 데이터 후보는 사용자 입력 표시 기준이며 구현 지시가 아님 |
| `docs/137_report_sample_json_table_data_candidate_review.md` | 샘플 JSON 4종에 표 데이터 후보 필드를 직접 추가하지 않기로 결정 |

## 판단

renderer와 normalizer 안내 문서는 큰 방향에서는 안전합니다.

다만 일부 오래된 표현은 표 데이터 후보를 실제 구현 대상으로 오해하게 만들 수 있어, 다음처럼 최소 보강합니다.

| 항목 | 판단 | 조치 |
|---|---|---|
| HWPX renderer README | 샘플 입력 범위가 오래됨 | 보고서 4종 샘플과 표 데이터 후보 보류 기준 추가 |
| normalizers README | 최신 작업 축이 과거 문구에 머묾 | 표 데이터 후보가 routing, `missing_fields`, HWPX payload 변경 대상이 아님을 추가 |
| renderer requirements | `표 데이터` 생성 표현이 넓음 | `표 데이터 후보 또는 구조`로 축소 |
| validation samples | 표 데이터 후보 직접 반영 보류 연결 없음 | `docs/137` 기준 연결 |
| dry-run scope | output 미생성 기준은 명확함 | table data candidate payload 확장 아님을 추가 |

## 유지하는 범위

- HWPX 보고서 4종이 최우선 자동화 대상
- 표는 현재 단계에서 틀과 배치 검수 대상
- 표 내부 데이터, 수량, 금액, 대상 목록은 향후 Excel/한셀 연동 후보
- `renderer_hints.table_template`은 실제 표 데이터가 아니라 서식 또는 표시 후보 힌트
- `table_data_candidate` 새 필드 추가 보류
- `missing_fields` 생성 규칙 변경 없음
- routing, HWPX payload, renderer, normalizer 변경 없음

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 표 데이터, 물품명, 수량, 금액, 대상 목록 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX/HWP 원본 파일 추가 없음
- 실제 Excel/한셀 파일 추가 없음
- HWPX output 재생성 없음
- renderer, normalizer, fixture, routing, HWPX payload 변경 없음
- Email, API, Make.com 연동 구현 없음

## 결론

renderer와 normalizer 안내 문서는 표 데이터 후보를 구현 지시로 오해하지 않도록 보강합니다.

현재 단계에서는 표 데이터 후보를 사용자 입력 표시와 문서 검토 기준으로만 유지합니다. 실제 표 내부 데이터 자동 입력, Excel/한셀 연동, HWPX payload 확장은 별도 승인 전까지 보류합니다.

