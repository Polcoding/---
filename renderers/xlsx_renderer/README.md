# XLSX 렌더러 PoC

## 목적

이 폴더는 `examples/json/sample_survey_table.json`을 입력으로 사용해 placeholder 기반 XLSX 조사표 초안을 생성하는 PoC 코드 위치입니다.

## 범위

- 입력 JSON 보안 검증
- 현황조사표 XLSX 초안 생성
- 로컬 테스트 산출물 생성

## 사용 제한

- 실제 업무자료를 사용하지 않습니다.
- 실제 개인정보, 기관명, 차량번호, 장비명, 수량, 금액을 사용하지 않습니다.
- API 호출, Make.com 연동, 이메일 자동화, HWPX 구현은 포함하지 않습니다.

## 실행 방법

```text
python renderers/xlsx_renderer/render_xlsx_poc.py
```

기본 입력:

```text
examples/json/sample_survey_table.json
```

기본 출력:

```text
renderers/xlsx_renderer/output/sample_survey_table_poc.xlsx
```
