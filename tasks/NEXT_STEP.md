# 다음 작업

## 현재 상태

비식별 HWPX 작업 복사본이 없으므로 실제 양식 수동 리허설은 계속 보류합니다.

복사본 없음 보류 기록은 `docs/134_actual_hwpx_manual_rehearsal_no_copy_hold.md`에 정리되어 있습니다.

HWPX 보고서와 Excel/한셀 표 데이터 역할 분리 범위는 `docs/135_hwp_report_and_hancell_table_data_scope.md`에 정리되어 있습니다.

HWPX 보고서 4종 사용자 입력 템플릿의 표 데이터 후보 표시 기준은 `docs/136_table_data_candidate_user_input_display_criteria.md`에 정리되어 있습니다.

보고서 샘플 JSON 4종에는 표 데이터 후보 필드를 직접 추가하지 않기로 `docs/137_report_sample_json_table_data_candidate_review.md`에 정리되어 있습니다.

## 목표

복사본 없이 가능한 다음 내부 작업으로, renderer와 normalizer 안내 문서가 표 데이터 후보를 실제 구현 지시처럼 오해하게 만들지 않는지 점검합니다.

이번 단계는 실제 HWPX/HWP 원본을 저장소에 넣거나 실제 Excel/한셀 파일을 만드는 단계가 아닙니다. renderer, normalizer, fixture, routing, HWPX payload, output도 변경하지 않습니다.

## 확인 대상

- `renderers/hwpx_renderer/README.md`
- `normalizers/README.md`
- `docs/21_template_renderer_requirements.md`
- `docs/22_renderer_validation_samples.md`
- `docs/70_hwpx_renderer_dry_run_scope.md`
- `docs/137_report_sample_json_table_data_candidate_review.md`
- `docs/136_table_data_candidate_user_input_display_criteria.md`
- `examples/json/README.md`
- `checklists/report_sample_json_validation_checklist.md`
- `README.md`
- `AGENTS.md`

## 확인 항목

1. renderer 안내 문서가 표 데이터 후보를 실제 HWPX 표 내부 데이터 자동 입력으로 오해하게 만들지 않는지
2. normalizer 안내 문서가 표 데이터 후보를 routing, `missing_fields`, HWPX payload 변경 대상으로 오해하게 만들지 않는지
3. `renderer_hints.table_template`이 실제 표 데이터가 아니라 서식 또는 표시 후보 힌트로 설명되어 있는지
4. 실제 output 재생성이나 HWPX 렌더러 실행이 필요하지 않은지
5. 실제 Excel/한셀 파일 생성이나 자동 연동 구현으로 넘어가지 않는지
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
- renderer와 normalizer 안내 문서가 표 데이터 후보를 구현 지시처럼 오해하게 만들지 않음
- `renderer_hints.table_template` 설명이 `docs/136`, `docs/137`과 충돌하지 않음
- 실제 파일, 실제 원문, 실제 표 데이터 추가 없음
- local template과 output Git 제외 상태 유지 여부 확인
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

다음 단계는 `docs/138` 형태로 renderer와 normalizer 안내 문서의 표 데이터 후보 오해 가능성 점검 결과를 정리하는 것입니다.

실제 HWPX 작업 복사본이 나중에 준비되면 `docs/131`, `docs/133`, `docs/134` 기준으로 `table_scope: frame_only` preview를 별도 재개합니다.
