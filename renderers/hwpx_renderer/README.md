# HWPX 최소 PoC 렌더러 안내

## 목적

이 폴더는 placeholder 기반 HWPX 템플릿을 읽고, AI 출력 JSON의 값을 안전하게 치환하여 검토용 HWPX 초안을 생성하기 위한 최소 PoC 코드를 보관합니다.

## 현재 범위

- HWPX 템플릿 파일 존재 여부 확인
- HWPX 패키지 구조 검사
- XML 파일 내 placeholder 탐색
- 허용된 placeholder만 치환
- 보안 검증 통과 시에만 렌더링
- 템플릿이 없으면 렌더링 중단 및 보고
- 보고서 4종 샘플의 placeholder 기반 치환 검증

## 현재 단계에서 하지 않는 것

- 실제 기관 HWPX 양식 사용
- 실제 업무용 또는 발송용 HWPX 생성
- 실제 공문 원문 처리
- 실제 개인정보 처리
- HWPX 표 내부 실제 데이터 자동 입력
- Excel/한셀 자동 연동
- `table_data_candidate` 필드나 HWPX payload 구조 확장
- API 호출
- 이메일 자동화
- Make.com 자동화

## 입력

- examples/json/sample_official_letter.json
- examples/json/sample_one_page_report.json
- examples/json/sample_project_plan.json
- examples/json/sample_result_report.json
- examples/json/sample_review_report.json
- templates/hwpx/placeholder 템플릿 파일

`renderer_hints.table_template`은 서식 또는 표시 후보 힌트입니다. 실제 표 데이터, 물품명, 수량, 금액, 대상 목록을 자동 입력하라는 의미가 아닙니다.

## 출력

- renderers/hwpx_renderer/output/*.hwpx
- renderers/hwpx_renderer/output/*.json
- renderers/hwpx_renderer/output/*.md

## 주의

output 산출물은 로컬 테스트 결과이며 Git 추적 대상에서 제외합니다.

output/.gitignore 내용:

```text
*.hwpx
*.hwp
*.json
*.md
!.gitkeep
```
