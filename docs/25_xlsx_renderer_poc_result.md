# XLSX 렌더러 PoC 결과

## 목적

`examples/json/sample_survey_table.json`을 입력으로 사용하여 placeholder 기반 XLSX 조사표 초안을 생성하는 PoC 결과를 기록합니다.

## 생성 또는 수정한 파일

| 파일 | 역할 |
|---|---|
| renderers/xlsx_renderer/README.md | XLSX 렌더러 PoC 안내 |
| renderers/xlsx_renderer/render_xlsx_poc.py | 샘플 JSON을 읽고 검증 후 XLSX를 생성하는 실행 스크립트 |
| renderers/xlsx_renderer/validation.py | 보안 검증 및 입력 구조 검증 |
| renderers/xlsx_renderer/templates.py | XLSX 시트 구성과 서식 적용 |
| renderers/xlsx_renderer/output/.gitkeep | 로컬 테스트 산출물 폴더 유지 |

## 입력 파일

- examples/json/sample_survey_table.json

## 실행 방법

```text
python renderers/xlsx_renderer/render_xlsx_poc.py
```

## 보안 검증 방식

- security_review.risk_level이 high 또는 blocked이면 렌더링을 중단합니다.
- contains_personal_info가 true이면 렌더링을 중단합니다.
- contains_sensitive_info가 true이면 렌더링을 중단합니다.
- contains_internal_info가 true이면 렌더링을 중단합니다.
- 이메일, 전화번호, 차량번호, 주민등록번호, 금액처럼 보이는 실제값 패턴이 있으면 렌더링을 중단합니다.
- document_type이 survey_table인지 확인합니다.
- output_targets에 xlsx가 포함되어 있는지 확인합니다.

## 생성되는 XLSX 파일

- renderers/xlsx_renderer/output/sample_survey_table_poc.xlsx

## 생성 시트

- 조사표
- 작성요령
- 검수체크리스트
- 메타정보

## PoC 검수 테스트 결과

| 테스트 | 입력 방식 | 기대 결과 | 실제 결과 | 판정 |
|---|---|---|---|---|
| 정상 생성 테스트 | examples/json/sample_survey_table.json | XLSX 생성 성공 | renderers/xlsx_renderer/output/sample_survey_table_poc.xlsx 생성 | 통과 |
| risk_level blocked 차단 테스트 | 메모리에서 risk_level을 blocked로 변경 | 렌더링 차단 | 차단 사유: 차단 risk_level: blocked | 통과 |
| contains_personal_info true 차단 테스트 | 메모리에서 contains_personal_info를 true로 변경 | 렌더링 차단 | 차단 사유: contains_personal_info가 true입니다. | 통과 |

차단 테스트는 임시 파일을 만들지 않고 메모리상 데이터 변경 방식으로 수행했습니다.

생성된 XLSX 파일은 로컬 테스트 산출물이며 Git 커밋 대상이 아닙니다.

## 제한 사항

- 실제 업무자료를 사용하지 않습니다.
- 실제 개인정보, 기관명, 업체명, 담당자명, 차량번호, 장비명, 수량, 금액을 사용하지 않습니다.
- API 호출, Make.com 연동, 이메일 자동화, HWPX 구현은 포함하지 않습니다.

## Step 16 완료 체크리스트

- [x] 샘플 JSON을 읽는가
- [x] 보안 검증을 수행하는가
- [x] high 또는 blocked이면 XLSX 생성을 중단하는가
- [x] 개인정보 또는 민감정보 플래그가 true이면 XLSX 생성을 중단하는가
- [x] 안전한 경우 placeholder 기반 XLSX 초안을 생성하는가
- [x] 생성 파일을 로컬 테스트 산출물로만 사용하는가
- [x] 실제 원문이나 개인정보를 사용하지 않았는가
- [x] HWPX 구현, API 호출, 이메일 자동화를 하지 않았는가
