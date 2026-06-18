# 다음 작업

## 목표

실제 기관 HWPX 양식 원본을 투입하기 전에, 로컬 placeholder 템플릿 준비 절차와 공통 placeholder 설계를 기준으로 다음 문서 유형을 선택합니다.

## 확인 대상

- `docs/53_real_hwpx_template_intake_safety_procedure.md`
- `docs/54_hwpx_common_placeholder_design.md`
- `checklists/real_hwpx_template_intake_checklist.md`
- `templates/hwpx/local_template_policy.md`
- `templates/hwpx/.gitignore`
- `renderers/hwpx_renderer/output/.gitignore`

## 선택지

1. 추진계획서 로컬 placeholder 템플릿 준비
   - 파일 후보: `templates/hwpx/placeholder_project_plan.hwpx`
   - 목적: 남아 있는 핵심 보고서 문서 유형 보강

2. 실제 양식 투입 전 안전 리허설
   - 실제 원본 없이 체크리스트만 따라가며 절차 누락 여부 확인
   - 목적: 실제 기관 양식 원본을 다루기 전 작업 순서 확정

현재 추천은 1번입니다. 원페이지 보고서, 결과보고서, 검토보고서가 로컬 치환 검수를 통과했으므로, 핵심 우선순위에 남아 있는 추진계획서 템플릿을 확인하는 흐름이 자연스럽습니다.

## 확인 항목

1. 실제 기관 양식 원본을 사용하지 않는지
2. 로컬 HWPX 템플릿이 Git 제외 상태인지
3. output HWPX가 Git 제외 상태인지
4. placeholder 이름에 실제 기관명, 담당자명, 문서번호가 들어가지 않는지
5. 여러 줄 placeholder가 독립 문단에 배치되는지
6. 값 누락 시 `[확인 필요]`, `null`, 또는 안전한 빈 문자열로 처리되는지
7. 렌더러가 기존 문서 유형 렌더링을 깨뜨리지 않는지

## 작업 제한

- 실제 기관 양식 사용 금지
- 실제 문서 원문 사용 금지
- 실제 개인정보 또는 내부 운영정보 사용 금지
- 실제 HWPX 템플릿 Git 추가 금지
- Email/API/Make.com 연동 금지
- 확인되지 않은 서식값 임의 생성 금지

## 완료 조건

- 다음 문서 유형 선택
- 로컬 HWPX 템플릿 준비 여부 확인
- output HWPX Git 제외 확인
- 보안 테스트 통과
- 수동 열람 검수 결과 문서화 준비
