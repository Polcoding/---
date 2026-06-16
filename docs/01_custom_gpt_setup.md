# Custom GPT 설정 절차

## 목적

데스크탑 또는 노트북 브라우저에서 안전한 Custom GPT 테스트판을 만드는 절차를 정리합니다.

## 준비

- 데스크탑 또는 노트북 브라우저 사용을 권장합니다.
- 테스트용으로만 사용합니다.
- 실제 공문 원문, 개인정보, 내부자료, 대외비 자료는 준비하지 않습니다.

## GPT 설정값 요약

| 항목 | 설정값 |
|---|---|
| Name | `공공기관 행정 비서 테스트판` |
| Description | `비식별 업무 지시를 바탕으로 공문, 기획서, 조사표, 업체 연락 메일 초안을 작성하는 1단계 테스트용 GPT입니다. 실제 발송과 결재는 수행하지 않습니다.` |
| Instructions | `prompts/custom_gpt_instructions_v0.1.md` 전체 내용 |
| Conversation Starters | `prompts/conversation_starters.md`의 문구 |
| Knowledge | 1단계에서는 비워 둠 |
| Capabilities | 초기 테스트에서는 비활성 권장 |
| Actions/Apps | 사용하지 않음 |
| 공개 범위 | 비공개 저장 권장 |

## 설정 절차

1. ChatGPT의 GPT 만들기 화면으로 이동합니다.
2. 새 GPT 생성 화면을 엽니다. 화면 이름은 바뀔 수 있으므로 예를 들면 `Create`, `Configure`, `Instructions`와 유사한 영역을 찾습니다.
3. Name에는 다음과 같이 입력합니다.

   `공공기관 행정 비서 테스트판`

4. Description에는 다음과 같이 입력합니다.

   `비식별 업무 지시를 바탕으로 공문, 기획서, 조사표, 업체 연락 메일 초안을 작성하는 1단계 테스트용 GPT입니다. 실제 발송과 결재는 수행하지 않습니다.`

5. Instructions 영역에 `prompts/custom_gpt_instructions_v0.1.md` 내용을 그대로 붙여넣습니다.
6. Conversation Starters에는 `prompts/conversation_starters.md`의 문구를 등록합니다.
7. Knowledge는 1단계에서 비워 둡니다.
8. Capabilities는 초기 테스트에서 끄는 것을 권장합니다.
9. Actions 또는 Apps 연동은 사용하지 않습니다.
10. Preview에서 `docs/04_test_cases.md`의 테스트 케이스를 실행합니다.
11. 결과를 `docs/05_evaluation_sheet.md` 기준으로 기록합니다.
12. 저장 범위는 비공개로 설정합니다.

## 테스트 기록 방법

각 테스트마다 다음을 기록합니다.

- 테스트 번호
- 입력 문구
- GPT 응답 요약
- 보안 대응 여부
- 허위 정보 생성 여부
- 평가 총점
- 수정 필요 사항

## 주의사항

- 실제 화면의 버튼명은 변경될 수 있습니다.
- Knowledge에 기존 공문 원문을 올리지 않습니다.
- Preview에서 실제 개인정보를 입력하지 않습니다.
- 외부 발송용 결과는 반드시 초안으로만 취급합니다.
