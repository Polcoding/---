# 사용자 Quick Start

## 목적

처음 보는 사용자가 현재 PoC에서 무엇을 보면 되는지 1페이지로 정리합니다.

이 문서는 실제 업무값 입력용이 아닙니다. 실제 원문, 개인정보, 기관명, 문서번호, 실제 표 데이터, 실제 HWPX/HWP 원본을 기록하지 않습니다.

## 먼저 열 파일

1. `CURRENT_STATUS.md`
2. `docs/140_user_operation_atoz_guide.md`
3. `checklists/user_operation_atoz_rehearsal_checklist.md`
4. `docs/141_user_rehearsal_prompt_examples.md`

## 지금 할 수 있는 일

`[사용자 확인 필요]`

- 만들 문서 유형 고르기
- 실제값이 제거되었는지 확인하기
- 확인되지 않은 값은 `[확인 필요]`로 남기기
- HWPX 파일을 열어야 하는 단계인지 구분하기

`[Codex 처리 가능]`

- 비식별 placeholder 입력 구조화
- 보고서 4종 초안 방향 정리
- `missing_fields` 검토 목록 분리
- 보안 주의문구 유지

`[보류]`

- 실제 HWPX/HWP 원본 사용
- 실제 표 데이터 자동 작성
- 실제 Email/API/Make.com 연동
- 실제 발송, 결재, 계약, 예산 집행 판단

## 가장 짧은 진행 순서

1. `CURRENT_STATUS.md`에서 현재 되는 것과 안 되는 것을 봅니다.
2. `docs/140_user_operation_atoz_guide.md`에서 사용자 확인 항목만 봅니다.
3. `checklists/user_operation_atoz_rehearsal_checklist.md`로 실제 HWPX 없이 리허설합니다.
4. `docs/141_user_rehearsal_prompt_examples.md`에서 문서 유형별 요청 예시를 고릅니다.
5. 실제값은 모두 `[확인 필요]` 또는 placeholder로 둡니다.
6. HWPX 열람이 필요한 단계가 나오면 한컴에서 사람이 확인합니다.

## 한컴에서 직접 확인할 때만 보는 것

- 파일 열림
- 글자 겹침
- 항목 순서
- 줄바꿈과 문단 배치
- 표 폭, 여백, 행 높이
- 남은 `{{placeholder}}`
- bullet 또는 번호 표기 일관성

## 바로 멈출 지점

- 실제 개인정보 또는 기관정보가 들어간 경우
- 실제 문서번호, 민원번호, 사건번호가 들어간 경우
- 실제 표 데이터, 수량, 금액, 대상 목록을 입력하려는 경우
- 실제 HWPX/HWP 원본이 GitHub Desktop Changes에 보이는 경우
- 로컬 output HWPX가 Git 추적 대상처럼 보이는 경우
- 보안 검토 없는 `review_report` 렌더링을 시도하는 경우

## 처음 요청 예시

```text
아래 입력은 비식별 placeholder 기반입니다.
실제 원문, 개인정보, 기관명, 문서번호, 실제 예산액, 실제 일정, 실제 실적, 실제 표 데이터는 포함하지 않았습니다.
확인되지 않은 값은 [확인 필요]로 유지해 주세요.

[비식별 업무] one_page_report 초안 구조를 정리해 주세요.

제목 힌트: [비식별 업무 원페이지 보고]
보고 목적: [확인 필요]
추진 배경: [비식별 배경 요약]
주요 내용:
1. [주요 내용 확인 필요]
2. [주요 내용 확인 필요]
향후 계획: [후속조치 확인 필요]
표 데이터 후보: [요약 표 필요 여부 확인 필요 또는 해당 없음]
```

## 완료 기준

- 실제값 없이 요청 예시를 선택할 수 있음
- 사용자가 직접 확인할 항목이 `[사용자 확인 필요]`로 보임
- Codex가 처리할 항목과 보류 항목이 분리됨
- 실제 HWPX 파일 열람이 필요한 지점이 분리됨
- output과 local HWPX 파일을 Git에 추가하지 않음
