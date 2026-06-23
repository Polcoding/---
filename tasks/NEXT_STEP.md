# 다음 작업

## 현재 상태

`CURRENT_STATUS.md`에 현재 시스템 현황판이 있고, `docs/139_minimum_demo_run_result.md`에 최소 demo 실행 결과 요약을 추가했습니다.

현재 저장소에서 확인 가능한 최소 PoC 경로는 다음입니다.

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

최소 demo 결과를 기준으로 사용자가 직접 입력하거나 확인해야 하는 지점을 더 쉽게 정리합니다.

## 확인 대상

- `CURRENT_STATUS.md`
- `docs/139_minimum_demo_run_result.md`
- `docs/84_hwpx_report_user_input_templates.md`
- `checklists/phase2_user_input_and_manual_operation_checklist.md`
- `checklists/missing_fields_user_display_guidance_checklist.md`
- `normalizers/README.md`

## 확인 항목

1. demo 결과에서 사용자가 직접 채워야 하는 값이 무엇인지 명확한지
2. `missing_fields`가 사용자에게 보기 쉬운 확인 항목으로 이어지는지
3. 보고서 4종 사용자 입력 템플릿이 실제값을 요구하지 않고 placeholder 중심인지
4. 실제 HWPX 파일 생성 없이도 사용자가 현재 시스템 상태를 이해할 수 있는지
5. 수동 확인 필요 항목이 실제 기관 양식, 글자 겹침, 표 폭, 여백처럼 사람이 봐야 하는 항목으로 분리되어 있는지

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

- 사용자가 직접 입력해야 하는 값과 Codex가 처리할 수 있는 값이 분리됨
- demo 결과와 사용자 입력 템플릿의 연결이 명확함
- 실제 구현물과 보류 항목이 분리됨
- output과 local HWPX 파일의 Git 제외 상태 유지 여부 확인
- 다음 단계 진행 가능 여부 보고

## 다음 단계 후보

추천 방향은 `docs/84_hwpx_report_user_input_templates.md`를 현재 demo 결과와 맞춰 더 쉽게 정리하는 것입니다.

특히 사용자가 직접 확인해야 하는 항목은 `[사용자 확인 필요]`로 눈에 잘 보이게 표시하고, Codex가 자동으로 처리 가능한 항목과 분리합니다.
