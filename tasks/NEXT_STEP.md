# 다음 작업

## 현재 상태

비식별 HWPX 작업 복사본이 없으므로 실제 양식 수동 리허설은 계속 보류합니다.

복사본 없음 보류 기록은 `docs/134_actual_hwpx_manual_rehearsal_no_copy_hold.md`에 정리되어 있습니다.

HWPX 보고서와 Excel/한셀 표 데이터 역할 분리 범위는 `docs/135_hwp_report_and_hancell_table_data_scope.md`에 정리되어 있습니다.

HWPX 보고서 4종 사용자 입력 템플릿의 표 데이터 후보 표시 기준은 `docs/136_table_data_candidate_user_input_display_criteria.md`에 정리되어 있습니다.

보고서 샘플 JSON 4종에는 표 데이터 후보 필드를 직접 추가하지 않기로 `docs/137_report_sample_json_table_data_candidate_review.md`에 정리되어 있습니다.

renderer와 normalizer 안내 문서가 표 데이터 후보를 실제 구현 지시처럼 오해하지 않도록 `docs/138_renderer_normalizer_table_data_candidate_scope_review.md`에 정리되어 있습니다.

## 목표

복사본 없이 가능한 다음 내부 작업으로, 최신 `docs/136`~`docs/138` 결정이 프로젝트 진입점 문서와 주요 안내 문서에 빠짐없이 연결되어 있는지 점검합니다.

이번 단계는 실제 HWPX/HWP 원본을 저장소에 넣거나 실제 Excel/한셀 파일을 만드는 단계가 아닙니다. renderer, normalizer, fixture, routing, HWPX payload, output도 변경하지 않습니다.

## 확인 대상

- `README.md`
- `AGENTS.md`
- `docs/00_chatgpt_handoff.md`
- `docs/00_project_overview.md`
- `docs/07_make_api_next_steps.md`
- `templates/hwpx/README.md`
- `renderers/hwpx_renderer/README.md`
- `normalizers/README.md`
- `examples/json/README.md`
- `docs/136_table_data_candidate_user_input_display_criteria.md`
- `docs/137_report_sample_json_table_data_candidate_review.md`
- `docs/138_renderer_normalizer_table_data_candidate_scope_review.md`
- 관련 checklists

## 확인 항목

1. README와 AGENTS가 `docs/136`~`docs/138` 최신 결정을 모두 가리키는지
2. ChatGPT handoff와 project overview가 다음 작업을 실제 구현이 아닌 문서 정합성 점검으로 안내하는지
3. renderer, normalizer, templates, examples 안내 문서가 표 데이터 후보를 실제 구현 지시처럼 오해하게 만들지 않는지
4. Make/API 안내 문서가 실제 연동 구현을 다음 단계로 오해하게 만들지 않는지
5. checklists가 `table_data_candidate`, `renderer_hints.table_template`, output Git 제외 기준을 확인하는지
6. 실제 표 데이터, 물품명, 수량, 금액, 대상 목록을 저장소에 기록하지 않는지

## 작업 제한

- 실제 기관 양식 사용 금지
- 실제 기관 HWPX/HWP 원본 Git 추가 금지
- 실제 Excel/한셀 파일 생성 금지
- 실제 표 데이터, 물품명, 수량, 금액, 대상 목록 기록 금지
- 실제 문서 원문 사용 금지
- 실제 개인정보 또는 내부 운영정보 사용 금지
- 실제 문서번호, 기관명, 담당자명, 수신자명 기록 금지
- 실제 파일명 또는 내부 경로 기록 금지
- HWPX output 재생성 금지
- Email/API/Make.com 연동 금지
- routing 결과 변경 금지
- HWPX payload 반영 금지
- fixture JSON 추가 금지
- renderer 또는 normalizer 코드 변경 금지

## 완료 조건

- 실제 양식 수동 리허설이 복사본 없음으로 보류되었음이 유지됨
- `docs/136`~`docs/138` 결정이 진입점 문서에 연결됨
- 실제 구현, 실제 연동, 실제 output 생성으로 오해될 문구가 없음
- 실제 파일, 실제 원문, 실제 표 데이터 추가 없음
- local template과 output Git 제외 상태 유지 여부 확인
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

다음 단계는 `docs/139` 형태로 최신 표 데이터 후보 관련 결정의 진입점 문서 연결 상태를 통합 점검하는 것입니다.

실제 HWPX 작업 복사본이 나중에 준비되면 `docs/131`, `docs/133`, `docs/134` 기준으로 `table_scope: frame_only` preview를 별도 재개합니다.
