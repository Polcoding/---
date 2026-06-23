# 다음 작업

## 현재 상태

`CURRENT_STATUS.md`에 현재 시스템 현황판을 만들었습니다.

2026-06-23 기준으로 다음 최소 PoC 경로는 실제로 실행 확인했습니다.

```text
비식별 요청 fixture
-> 입력 정규화
-> 보안 필터
-> HWPX payload mapper
-> payload validation
-> HWPX renderer dry-run
```

실제 HWPX 산출물 생성, 실제 기관 양식 적용, 실제 이메일/API/Make.com 연동은 아직 진행하지 않습니다.

## 목표

문서만 계속 늘리는 흐름을 줄이고, 사용자가 현재 결과물을 쉽게 확인할 수 있도록 최소 demo 경로를 고정합니다.

## 확인 대상

- `CURRENT_STATUS.md`
- `normalizers/README.md`
- `normalizers/output/placeholder_confirmed_values_summary.json`
- `normalizers/output/normalization_summary.json`
- `normalizers/output/hwpx_payload_mapping_summary.json`
- `normalizers/output/hwpx_payload_validation_summary.json`
- `normalizers/output/hwpx_renderer_dry_run_summary.json`
- `renderers/hwpx_renderer/README.md`
- `templates/hwpx/local_template_policy.md`

## 확인 항목

1. `CURRENT_STATUS.md`가 실제 실행 결과와 모순되지 않는지
2. 최소 demo 경로가 `normalizers/README.md`의 실행 순서와 맞는지
3. summary JSON 5종이 실제값 없이 placeholder, 비식별 fixture, 안전 상태만 포함하는지
4. HWPX renderer dry-run이 실제 HWPX 파일 생성이 아니라 사전 상태 확인임이 명확한지
5. local HWPX template과 output 산출물이 Git 제외 상태인지
6. 사용자가 직접 확인해야 하는 항목이 `[사용자 확인 필요]` 성격으로 분리되어 있는지

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

## 완료 조건

- 현재 작동 범위가 `CURRENT_STATUS.md`에 명확히 보임
- 최소 PoC 실행 경로와 증거 파일이 확인됨
- 실제 구현물과 보류 항목이 분리됨
- output과 local HWPX 파일의 Git 제외 상태 유지 여부 확인
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

다음 단계는 `CURRENT_STATUS.md` 기준으로 최소 demo 결과 문서를 만들지 여부를 결정하는 것입니다.

추천 방향은 실제 HWPX 파일을 새로 만들기보다, 먼저 `normalizers/output/*summary.json`의 핵심 결과를 사람이 보기 쉬운 demo 결과 문서로 요약하는 것입니다.
