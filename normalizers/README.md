# 입력 정규화 PoC

## 목적

이 폴더는 HWPX 보고서 4종에 한정해 사용자의 비식별 업무 지시를 표준 입력 구조로 정리하는 최소 PoC입니다.

대상 문서 유형:

- `one_page_report`
- `project_plan`
- `result_report`
- `review_report`

## 범위

포함:

- 문서 유형 후보 판정
- `content_inputs` placeholder 구성
- `missing_fields` 분리
- `security_flags` 초기 구성
- 보안 필터 기반 `routing_decision` 보정
- 정규화 결과를 HWPX 렌더러 입력 JSON 형태로 매핑
- placeholder fixture 기반 테스트

제외:

- OpenAI API 호출
- Make.com 연동
- Email 자동 발송
- 실제 원문 파싱
- 실제 HWPX 양식 처리
- 운영용 렌더러 직접 연결
- 표 데이터 후보를 routing, `missing_fields`, HWPX payload 변경 대상으로 처리
- 실제 표 데이터, 수량, 금액, 대상 목록 자동 정규화
- Excel/한셀 자동 연동

## 실행

```powershell
python .\normalizers\validate_placeholder_confirmed_values_poc.py
python .\normalizers\input_normalizer_poc.py
python .\normalizers\hwpx_payload_mapper_poc.py
python .\normalizers\validate_hwpx_payload_poc.py
python .\normalizers\hwpx_renderer_dry_run_poc.py
python .\normalizers\render_mapped_hwpx_poc.py
```

실행 결과는 `normalizers/output/`에 생성됩니다.

`normalizers/output/` 산출물은 Git에 포함하지 않습니다.

회귀 테스트 기준은 `docs/81_normalizers_regression_test_suite.md`와 `checklists/normalizers_regression_test_suite_checklist.md`를 따릅니다.

`placeholder_confirmed_values` helper는 read-only 검증용입니다. 현재 단계에서는 `missing_fields`, routing, HWPX payload 결과에 반영하지 않습니다.

helper 전용 fixture는 `normalizers/fixtures/placeholder_confirmed_values/` 하위 폴더에 둡니다. 이 fixture는 기존 routing fixture 6종과 분리해서 검증합니다.

최근 점검에서는 normalizer 기능 확장이 아니라 표 데이터 후보가 renderer와 normalizer 구현 지시로 오해되지 않도록 문서 기준을 정리했습니다. normalizer, fixture, routing, `missing_fields`, HWPX payload 변경은 별도 명시 승인 전까지 보류합니다.

`renderer_hints.table_template`과 표 데이터 후보는 서식 또는 표시 후보 힌트입니다. 실제 표 내부 데이터 자동 입력이나 Excel/한셀 연동을 의미하지 않습니다.

## 보안 원칙

- fixture는 placeholder 기반만 사용합니다.
- 실제 개인정보, 실제 기관명, 실제 문서번호, 실제 공문 원문을 사용하지 않습니다.
- 실제 표 데이터, 물품명, 수량, 금액, 대상 목록을 사용하지 않습니다.
- 차단 테스트도 실제값이 아니라 설명형 placeholder만 사용합니다.
- 판단이 애매하면 `needs_security_review` 또는 `blocked`로 보수 라우팅합니다.
