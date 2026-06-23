# 다음 작업

## 현재 상태

사용자 입력 역할 구분을 반복 운영 로그, missing_fields 표시 기준, 주요 진입점 문서에 연결했습니다.

`docs/00_project_overview.md`, `docs/00_chatgpt_handoff.md`, `CURRENT_STATUS.md`, `README.md`, `AGENTS.md`는 현재 기준으로 HWPX 보고서 우선 방향, 실제값 임의 생성 금지, 보류 항목 분리를 같은 방향으로 설명합니다.

`docs/101_phase2_repeat_operation_log_template.md`, `docs/104_missing_fields_user_display_guidance.md`, 관련 체크리스트의 과거형 다음 단계 문구도 현재 사용자 안내 기준으로 정리했습니다.

`docs/84_hwpx_report_user_input_templates.md`에는 사용자가 직접 확인할 부분 빠른 보기 블록을 추가했습니다.

현재 공통 표시는 다음과 같습니다.

- `[사용자 확인 필요]`: 사람이 직접 판단하거나 확인해야 하는 값
- `[Codex 처리 가능]`: 비식별 placeholder 입력을 바탕으로 구조화 가능한 항목
- `[보류]`: 현재 단계에서 자동화하지 않는 항목

## 목표

사용자가 직접 해야 하는 일과 Codex가 처리할 일을 한 번에 볼 수 있는 A-to-Z 운영 안내 문서 후보를 정리합니다.

## 확인 대상

- `docs/84_hwpx_report_user_input_templates.md`
- `docs/101_phase2_repeat_operation_log_template.md`
- `docs/104_missing_fields_user_display_guidance.md`
- `CURRENT_STATUS.md`
- `README.md`
- `AGENTS.md`

## 생성 후보

- `docs/140_user_operation_atoz_guide.md`

## 확인 항목

1. 사용자가 직접 해야 하는 일을 `[사용자 확인 필요]`로 분리하는지
2. Codex가 처리할 수 있는 일을 `[Codex 처리 가능]`으로 분리하는지
3. 현재 단계에서 하지 않는 일을 `[보류]`로 분리하는지
4. 실제 HWPX 파일, 실제 표 데이터, 실제 개인정보를 요구하지 않는지
5. 한컴에서 사용자가 확인해야 하는 지점이 A-to-Z 순서로 보이는지

## 작업 제한

- 실제 기관 양식 사용 금지
- 실제 기관 HWPX/HWP 원본 Git 추가 금지
- 실제 HWPX output 재생성 금지
- 실제 Excel/한셀 파일 생성 금지
- 실제 표 데이터, 물품명, 수량, 금액, 대상 목록 기록 금지
- 실제 문서 원문 사용 금지
- 실제 개인정보 또는 내부 운영정보 사용 금지
- 실제 문서번호, 기관명, 담당자명, 수신자명 기록 금지
- Email/API/Make.com 연동 금지
- normalizer, renderer, fixture, routing 코드 변경 금지

## 완료 조건

- 사용자용 A-to-Z 운영 안내 문서 후보 생성
- 기존 사용자 입력 안내 문서와 모순 없음
- 실제 구현물과 보류 항목 분리 유지
- output과 local HWPX 파일의 Git 제외 상태 유지 여부 확인
- 다음 추천 작업을 `tasks/NEXT_STEP.md`에 갱신

## 다음 단계 후보

추천 방향은 `docs/140_user_operation_atoz_guide.md`를 만들고 README 또는 CURRENT_STATUS에서 찾을 수 있도록 연결하는 것입니다.

이 작업은 문서 산출물 중심이며, 실제 HWPX 파일 생성이나 외부 연동은 포함하지 않습니다.
