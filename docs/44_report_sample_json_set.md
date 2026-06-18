# HWPX 보고서용 샘플 JSON 세트

## 목적

원페이지 보고서, 추진계획서, 결과보고서, 검토보고서 HWPX 자동화를 검증하기 위한 placeholder 기반 샘플 JSON 세트를 정의합니다.

이 문서는 실제 HWPX 파일 생성이나 렌더러 구현이 아니라, 향후 HWPX 보고서 템플릿 자동화 검증에 사용할 샘플 데이터 범위를 정리하는 문서입니다.

## 샘플 목록

| 파일 | document_type | 목적 | 출력 후보 |
|---|---|---|---|
| examples/json/sample_one_page_report.json | one_page_report | 원페이지 보고서 HWPX 렌더링 검증 | hwpx |
| examples/json/sample_project_plan.json | project_plan | 추진계획서 HWPX 렌더링 검증 | hwpx |
| examples/json/sample_result_report.json | result_report | 결과보고서 HWPX 렌더링 검증 | hwpx |
| examples/json/sample_review_report.json | review_report | 검토보고서 HWPX 렌더링 검증 | hwpx |

## 공통 원칙

- 모든 샘플은 placeholder 기반입니다.
- 실제 원문, 개인정보, 기관정보는 포함하지 않습니다.
- 예산, 일정, 실적 수치, 담당자는 임의 생성하지 않습니다.
- 모든 산출물은 초안이며 사람 검토가 필요합니다.
- HWPX 보고서 자동화가 우선이며, Email은 이번 샘플 세트의 대상이 아닙니다.
- 실제 HWP/HWPX 파일을 생성하지 않습니다.
- API 호출, 이메일 자동화, Make.com 연동을 수행하지 않습니다.

## 샘플별 검증 초점

| document_type | 검증 초점 |
|---|---|
| one_page_report | 제목, 보고 요약, 배경, 주요내용, 검토의견, 향후조치 구조 |
| project_plan | 추진배경, 목적, 개요, 일정, 예산, 기대효과 구조 |
| result_report | 기존 추진계획서와의 placeholder 연결, 계획 대비 결과, 성과, 문제점, 개선사항 구조 |
| review_report | 검토배경, 검토범위, 검토의견, 위험요소, 필요 검토 항목 구조 |

## 결과보고서와 추진계획서 연결 원칙

- 결과보고서는 기존 추진계획서의 주요 항목과 대응 구조를 가질 수 있습니다.
- 다만 실제 계획서 원문을 자동으로 가져오지 않습니다.
- 사용자가 제공하지 않은 결과값은 [확인 필요]로 표시합니다.
- 계획 대비 결과, 주요성과, 문제점, 개선사항, 향후계획을 구분합니다.
- 실적 수치, 예산 집행액, 참여 인원은 사용자가 제공한 경우에만 입력합니다.
- 계획 대비 결과가 불명확하면 [계획 대비 결과 확인 필요]로 표시합니다.

## Step 31 완료 체크리스트

- [x] one_page_report 샘플 JSON이 작성되었는가
- [x] project_plan 샘플 JSON이 검수되었는가
- [x] result_report 샘플 JSON이 작성되었는가
- [x] review_report 샘플 JSON이 작성되었는가
- [x] 모든 샘플이 placeholder 기반인가
- [x] 실제 원문, 개인정보, 내부 운영정보가 없는가
- [x] 실제 예산, 일정, 수량, 실적을 임의 생성하지 않았는가
- [x] 구현 코드를 작성하지 않았는가
