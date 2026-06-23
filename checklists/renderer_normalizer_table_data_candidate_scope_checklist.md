# renderer와 normalizer 표 데이터 후보 범위 점검 체크리스트

## 확인 대상

| 완료 | 항목 |
|---|---|
| [x] | `renderers/hwpx_renderer/README.md`를 확인했는가 |
| [x] | `normalizers/README.md`를 확인했는가 |
| [x] | `docs/21_template_renderer_requirements.md`를 확인했는가 |
| [x] | `docs/22_renderer_validation_samples.md`를 확인했는가 |
| [x] | `docs/70_hwpx_renderer_dry_run_scope.md`를 확인했는가 |
| [x] | `docs/136_table_data_candidate_user_input_display_criteria.md`와 비교했는가 |
| [x] | `docs/137_report_sample_json_table_data_candidate_review.md`와 비교했는가 |

## 범위 구분 확인

| 완료 | 항목 |
|---|---|
| [x] | 표 데이터 후보가 실제 HWPX 표 내부 데이터 자동 입력이 아님을 명시했는가 |
| [x] | 표 데이터 후보가 Excel/한셀 자동 연동 구현이 아님을 명시했는가 |
| [x] | `renderer_hints.table_template`이 서식 또는 표시 후보 힌트임을 명시했는가 |
| [x] | `table_data_candidate` 새 필드 추가 보류 기준을 유지했는가 |
| [x] | `missing_fields`, routing, HWPX payload 변경 금지를 유지했는가 |

## 변경 제한 확인

| 완료 | 항목 |
|---|---|
| [x] | renderer 코드를 변경하지 않았는가 |
| [x] | normalizer 코드를 변경하지 않았는가 |
| [x] | fixture JSON을 추가하거나 변경하지 않았는가 |
| [x] | routing 결과를 변경하지 않았는가 |
| [x] | HWPX payload 구조를 변경하지 않았는가 |
| [x] | HWPX output을 재생성하지 않았는가 |
| [x] | 실제 Excel/한셀 파일을 만들지 않았는가 |

## 보안 검수

| 완료 | 항목 |
|---|---|
| [x] | 실제 개인정보를 추가하지 않았는가 |
| [x] | 실제 기관명, 업체명, 담당자명을 추가하지 않았는가 |
| [x] | 실제 문서번호, 민원번호, 사건번호를 추가하지 않았는가 |
| [x] | 실제 날짜, 예산, 실적 수치를 추가하지 않았는가 |
| [x] | 실제 표 데이터, 물품명, 수량, 금액, 대상 목록을 추가하지 않았는가 |
| [x] | 실제 공문 원문 또는 보고서 원문을 추가하지 않았는가 |
| [x] | 실제 HWPX/HWP 원본 파일을 추가하지 않았는가 |
| [x] | 실제 Excel/한셀 파일을 추가하지 않았는가 |
| [x] | API 키, 토큰, 인증정보 예시값을 추가하지 않았는가 |

## 다음 단계 확인

| 완료 | 항목 |
|---|---|
| [x] | 다음 단계가 실제 연동 구현이 아니라 진입점 문서 최신화 점검인지 확인했는가 |
| [x] | 실제 HWPX 작업 복사본이 준비되기 전까지 실제 양식 preview 보류를 유지했는가 |

