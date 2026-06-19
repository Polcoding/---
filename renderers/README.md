# 렌더러 폴더 안내

이 폴더는 HWPX, XLSX, 이메일, Markdown 렌더러 관련 설계와 placeholder 기반 로컬 PoC 코드를 관리하기 위한 위치입니다.

현재 저장소에는 다음 로컬 PoC 렌더러가 있습니다.

- `hwpx_renderer/`: placeholder 기반 HWPX 템플릿 치환 PoC
- `xlsx_renderer/`: placeholder 기반 XLSX 조사표 렌더러 PoC
- `markdown_renderer/`: Markdown 미리보기 렌더러 PoC
- `email_renderer/`: Email 초안 렌더러 PoC

## 현재 허용 범위

- placeholder 기반 샘플 JSON 처리
- 로컬 테스트용 output 생성
- 템플릿이 없을 때 안전 중단
- 보안 검증 실패 시 렌더링 중단
- 사람이 검토하는 초안 산출물 생성

## 금지 범위

- API 코드 작성 금지
- 이메일 자동화 코드 작성 금지
- 실제 이메일 자동 발송 금지
- Make.com 자동화 구현 금지
- 실제 기관 양식 또는 실제 업무자료 저장 금지
- 실제 공문 원문 또는 개인정보 처리 금지
- 실제 업무용 HWPX/XLSX 산출물 생성 금지

## Git 관리 원칙

- `output/` 산출물은 로컬 검증 결과이며 Git에 포함하지 않습니다.
- 로컬 HWPX 템플릿은 Git에 포함하지 않습니다.
- 실제 기관 HWPX 양식 원본은 저장소에 추가하지 않습니다.
