# 다음 작업

## 현재 상태

`docs/139_minimum_demo_run_result.md` 기준으로 최소 demo 결과를 정리했고, `docs/84_hwpx_report_user_input_templates.md`에 사용자 입력 역할 구분을 보강했습니다.

현재 사용자 입력 템플릿은 다음 세 표시를 사용합니다.

- `[사용자 확인 필요]`: 사람이 직접 판단하거나 확인해야 하는 값
- `[Codex 처리 가능]`: 비식별 placeholder 입력을 바탕으로 구조화 가능한 항목
- `[보류]`: 현재 단계에서 자동화하지 않는 항목

## 목표

사용자 입력 템플릿 기준을 수동 운영 체크리스트와 반복 운영 로그에 더 쉽게 연결합니다.

## 확인 대상

- `docs/84_hwpx_report_user_input_templates.md`
- `checklists/phase2_user_input_and_manual_operation_checklist.md`
- `docs/101_phase2_repeat_operation_log_template.md`
- `docs/104_missing_fields_user_display_guidance.md`
- `docs/139_minimum_demo_run_result.md`
- `CURRENT_STATUS.md`

## 확인 항목

1. 사용자가 직접 확인해야 하는 항목이 수동 운영 체크리스트에서도 보이는지
2. `[사용자 확인 필요]`, `[Codex 처리 가능]`, `[보류]` 표시가 반복 운영 로그에도 반영될 필요가 있는지
3. `missing_fields`가 본문 값이 아니라 검토용 목록임이 계속 유지되는지
4. 실제 HWPX 파일 생성 없이도 사용자가 다음에 무엇을 확인해야 하는지 알 수 있는지
5. 실제 표 데이터, 수량, 금액, 대상 목록을 요구하지 않는지

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

- 사용자 입력 템플릿과 수동 운영 체크리스트가 같은 역할 구분을 사용함
- 반복 운영 로그에 반영할지 여부가 정리됨
- 실제 구현물과 보류 항목이 분리됨
- output과 local HWPX 파일의 Git 제외 상태 유지 여부 확인
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

추천 방향은 `docs/101_phase2_repeat_operation_log_template.md`에 사용자 입력 역할 구분을 반영할지 검토하는 것입니다.

반영하더라도 실제값을 넣는 로그가 아니라, `[사용자 확인 필요]`, `[Codex 처리 가능]`, `[보류]` 상태를 기록하는 placeholder 기반 운영 로그로 유지합니다.
