# Markdown 미리보기 렌더러 안내

## 목적
이 폴더는 AI 출력 JSON을 사람이 검토하기 쉬운 Markdown 미리보기 문서로 변환하는 PoC 코드를 보관합니다.

## 현재 범위
- JSON 샘플 읽기
- 보안 검증
- Markdown 미리보기 생성
- blocked 샘플은 차단 보고 Markdown 생성

## 현재 단계에서 하지 않는 것
- 실제 외부 발송
- API 호출
- 이메일 자동화
- HWPX 생성
- XLSX 생성
- 실제 업무자료 처리

## 입력
examples/json/*.json

## 출력
renderers/markdown_renderer/output/*.md
