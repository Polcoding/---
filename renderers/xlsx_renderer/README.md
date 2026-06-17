# XLSX 렌더러 PoC

## 목적

이 폴더는 `examples/json/sample_survey_table.json`을 입력으로 사용해 placeholder 기반 XLSX 조사표 초안을 생성하는 PoC 코드 위치입니다.

## 범위

- 입력 JSON 보안 검증
- 현황조사표 XLSX 초안 생성
- 로컬 테스트 산출물 생성
- 제목 행, 표 머리글, 테두리, 줄바꿈, 정렬, 열 너비, freeze pane 등 기본 서식 적용

## 사용 제한

- 실제 업무자료를 사용하지 않습니다.
- 실제 개인정보, 기관명, 차량번호, 장비명, 수량, 금액을 사용하지 않습니다.
- API 호출, Make.com 연동, 이메일 자동화, HWPX 구현은 포함하지 않습니다.
- 생성된 XLSX는 로컬 테스트 산출물이며 Git 커밋 대상에서 제외합니다.

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

## v0.2 보강 사항

- 조사표, 작성요령, 검수체크리스트, 메타정보 4개 시트 구조 유지
- 제목 행 강조와 표 머리글 강조 적용
- 열 너비와 행 높이 조정
- 줄바꿈, 셀 정렬, 테두리 적용
- 시트별 freeze pane 적용
- validation 차단 메시지를 사람이 읽기 쉬운 문장으로 보강
- 메타정보 시트에 missing_fields와 security_review 구역 표시
- 실제 기관 표준 서식값은 확정하지 않으며 PoC용 기본 스타일만 적용
