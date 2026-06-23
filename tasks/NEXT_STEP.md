# 다음 작업

## 현재 상태

사용자 운영 A-to-Z 안내 문서, 리허설 체크리스트, 문서 유형별 비식별 요청 예시를 작성하고 주요 진입점 문서에 연결했습니다.

현재 사용자는 `docs/140_user_operation_atoz_guide.md`에서 직접 확인할 일, Codex가 처리할 일, 현재 보류할 일을 한 번에 볼 수 있습니다.

`checklists/user_operation_atoz_rehearsal_checklist.md`에서는 실제 HWPX 없이도 현재 단계 확인을 체크박스로 리허설할 수 있습니다.

`docs/141_user_rehearsal_prompt_examples.md`에서는 보고서 4종 요청 예시를 실제값 없이 확인할 수 있습니다.

`README.md`와 `CURRENT_STATUS.md`도 이 문서와 체크리스트를 현재 사용자 안내 진입점으로 연결합니다.

현재 공통 표시는 다음과 같습니다.

- `[사용자 확인 필요]`: 사람이 직접 판단하거나 확인해야 하는 값
- `[Codex 처리 가능]`: 비식별 placeholder 입력을 바탕으로 구조화 가능한 항목
- `[보류]`: 현재 단계에서 자동화하지 않는 항목

## 목표

사용자 안내 3종이 서로 모순되지 않는지 최종 점검하고, 다음 실제 확인 지점을 분리합니다.

## 확인 대상

- `docs/140_user_operation_atoz_guide.md`
- `docs/141_user_rehearsal_prompt_examples.md`
- `docs/84_hwpx_report_user_input_templates.md`
- `checklists/user_operation_atoz_rehearsal_checklist.md`
- `docs/101_phase2_repeat_operation_log_template.md`
- `docs/104_missing_fields_user_display_guidance.md`
- `CURRENT_STATUS.md`
- `README.md`
- `AGENTS.md`

## 생성 후보

- 필요 시 `docs/142_user_guidance_integrated_review.md`

## 확인 항목

1. A-to-Z 안내, 리허설 체크리스트, 요청 예시가 같은 역할 구분을 사용하는지
2. `one_page_report`, `project_plan`, `result_report`, `review_report` 예시가 실제값 없이 유지되는지
3. `[사용자 확인 필요]`, `[Codex 처리 가능]`, `[보류]` 구분이 유지되는지
4. 실제 개인정보, 실제 기관정보, 실제 문서번호, 실제 표 데이터를 요구하지 않는지
5. HWPX 파일 열람이 필요한 지점은 별도 사용자 확인 지점으로 남기는지

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

- 사용자 안내 3종 정합성 확인
- 기존 사용자 입력 안내 문서와 모순 없음
- 실제 구현물과 보류 항목 분리 유지
- output과 local HWPX 파일의 Git 제외 상태 유지 여부 확인
- 다음 추천 작업을 `tasks/NEXT_STEP.md`에 갱신

## 다음 단계 후보

추천 방향은 사용자 안내 3종을 최종 점검하고, 실제 HWPX 파일 열람이 필요한 지점과 지금 문서만으로 진행 가능한 지점을 분리하는 것입니다.

이 작업은 문서 산출물 중심이며, 실제 HWPX 파일 생성이나 외부 연동은 포함하지 않습니다.
