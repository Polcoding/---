# Email 초안 렌더러 안내

## 목적

이 폴더는 AI 출력 JSON 중 업체 연락 메일 초안을 사람이 검토하기 쉬운 Markdown 또는 TXT 형식으로 변환하는 PoC 코드를 보관합니다.

## 현재 범위

- sample_vendor_email.json 읽기
- 보안 검증
- 이메일 제목/본문/유의사항/서명 placeholder 렌더링
- blocked 샘플은 차단 보고 파일로 처리

## 현재 단계에서 하지 않는 것

- 실제 이메일 발송
- Gmail 연결
- Outlook 연결
- SMTP 연결
- Make.com 자동화
- API 호출
- 실제 업무자료 처리

## 입력

- examples/json/sample_vendor_email.json
- examples/json/sample_blocked_security_case.json

## 출력

- renderers/email_renderer/output/*.md
- renderers/email_renderer/output/*.txt
