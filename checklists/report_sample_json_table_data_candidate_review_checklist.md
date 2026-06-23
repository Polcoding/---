# 보고서 샘플 JSON 표 데이터 후보 반영 검토 체크리스트

## 확인 대상

| 완료 | 항목 |
|---|---|
| [x] | `sample_one_page_report.json`을 확인했는가 |
| [x] | `sample_project_plan.json`을 확인했는가 |
| [x] | `sample_result_report.json`을 확인했는가 |
| [x] | `sample_review_report.json`을 확인했는가 |
| [x] | `docs/136_table_data_candidate_user_input_display_criteria.md`와 비교했는가 |

## 반영 판단

| 완료 | 항목 |
|---|---|
| [x] | 샘플 JSON 4종에 새 `table_data_candidate` 필드를 직접 추가하지 않기로 했는가 |
| [x] | 기존 `renderer_hints.table_template`을 서식 또는 표시 후보 힌트로만 해석했는가 |
| [x] | 표 데이터 후보 표시 기준을 사용자 입력 템플릿과 문서 기준으로 유지했는가 |
| [x] | HWPX payload 확장처럼 보일 수 있는 변경을 피했는가 |

## 변경 제한 확인

| 완료 | 항목 |
|---|---|
| [x] | 샘플 JSON 4종을 직접 수정하지 않았는가 |
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
| [x] | 다음 단계가 실제 연동 구현이 아니라 renderer와 normalizer 안내 문서 점검인지 확인했는가 |
| [x] | 실제 HWPX 작업 복사본이 준비되기 전까지 실제 양식 preview 보류를 유지했는가 |
