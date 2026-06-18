# 다음 작업

## 목표

실제 기관 양식 원본을 저장소에 넣지 않고, 저장소 밖 로컬 복사본을 placeholder 템플릿 후보로 바꾸는 절차를 소규모로 점검합니다.

## 현재 완료 상태

- `one_page_report`: 로컬 placeholder 치환 및 수동 검수 완료
- `project_plan`: 로컬 placeholder 치환 및 수동 검수 완료
- `result_report`: 로컬 placeholder 치환 및 수동 검수 완료
- `review_report`: 로컬 placeholder 치환 및 수동 검수 완료
- HWPX 보고서 4종 완료 상태 및 안전 리허설 문서화 완료

## 확인 대상

- `docs/57_hwpx_report_4types_completion_and_safety_rehearsal.md`
- `docs/53_real_hwpx_template_intake_safety_procedure.md`
- `checklists/real_hwpx_template_intake_checklist.md`
- `templates/hwpx/local_template_policy.md`

## 확인 항목

1. 실제 원본을 저장소에 추가하지 않는지
2. 저장소 밖 로컬 복사본만 작업 대상으로 삼는지
3. 실제 내용, 기관명, 문서번호, 결재선, 직인, 로고를 제거하는 절차가 명확한지
4. placeholder 이름이 실제 대상을 추정하게 만들지 않는지
5. 로컬 HWPX 템플릿이 Git 제외 상태인지
6. output HWPX가 Git 제외 상태인지
7. C/D등급 문서를 즉시 중단 대상으로 처리하는지

## 작업 제한

- 실제 기관 양식 사용 금지
- 실제 문서 원문 사용 금지
- 실제 개인정보 또는 내부 운영정보 사용 금지
- 실제 HWPX 템플릿 Git 추가 금지
- Email/API/Make.com 연동 금지
- 확인되지 않은 서식값 임의 생성 금지

## 완료 조건

- 저장소 밖 로컬 복사본 기반 절차 점검
- 실제 원본 미사용 확인
- Git 제외 상태 재확인
- 다음 단계 진행 여부 판단

## 다음 단계 후보

현재 추천은 실제 기관 양식 원본을 저장소에 넣지 않고, 사용자가 직접 저장소 밖에서 비식별 placeholder 복사본을 만드는 절차를 먼저 확정하는 것입니다.
