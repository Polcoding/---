# 실제 HWPX 양식 투입 전 체크리스트

최신 저장소 밖 실제 양식 후보 수동 절차와 보류 조건은 `docs/128_external_hwpx_candidate_manual_procedure_and_hold_criteria.md`를 함께 확인합니다. local template과 output Git 제외 반복 검증 기준은 `docs/129_local_template_gitignore_repeat_verification_criteria.md`를 따르며, 수동 preview 재개 여부는 `docs/150_manual_preview_resume_gate.md`를 먼저 확인합니다. 외부 HWPX 자동 채우기 skill 또는 `hwpx-cli` 참고 자료는 `docs/158_hwpx_autofill_conversion_adoption_review.md` 기준으로 구조 분석 참고용으로만 봅니다.

## 원본 분류

- [ ] 실제 양식 원본을 Git에 추가하지 않았는가
- [ ] 문서가 A/B등급 범위에서만 검토 가능한가
- [ ] C등급 내부 참고 문서를 외부 AI 입력이나 샘플 후보로 사용하지 않았는가
- [ ] D등급 외부 처리 금지 문서가 아닌가
- [ ] 판단이 애매한 자료를 더 보수적인 등급으로 분류했는가
- [ ] 외부 skill, MCP, `hwpx-cli`에 실제 원본을 바로 넣지 않았는가

## 실제 정보 제거

- [ ] 실제 기관명, 관서명, 업체명이 없는가
- [ ] 실제 사람 이름, 담당자명, 연락처, 이메일이 없는가
- [ ] 실제 문서번호, 민원번호, 접수번호, 사건번호가 없는가
- [ ] 실제 주소, 차량번호, 장비명, 내부 운영정보가 없는가
- [ ] 실제 예산액, 견적 금액, 계약 조건이 없는가
- [ ] 직인, 로고, 결재선 등 식별 가능한 양식 요소가 제거되었는가

## placeholder 처리

- [ ] 모든 동적 값이 placeholder로 바뀌었는가
- [ ] placeholder 이름만으로 실제 대상이 추정되지 않는가
- [ ] 여러 줄 placeholder가 가능한 한 서로 다른 문단에 배치되었는가
- [ ] 확인되지 않은 값은 `[확인 필요]`, `null`, 또는 빈 문자열로 처리되는가
- [ ] 예산, 일정, 담당자, 수량을 임의 생성하지 않았는가
- [ ] 외부 자동 채우기 자료가 placeholder 후보 위치 참고로만 사용되었는가

## Git 제외 확인

- [ ] `templates/hwpx/`의 `.hwpx`, `.hwp` 파일이 GitHub Desktop Changes에 나타나지 않는가
- [ ] `renderers/hwpx_renderer/output/` 산출물이 GitHub Desktop Changes에 나타나지 않는가
- [ ] `normalizers/output/` 산출물이 GitHub Desktop Changes에 나타나지 않는가
- [ ] 로컬 HWPX 템플릿과 output 산출물이 `!!` ignored 상태인지 확인했는가
- [ ] 실제 HWPX 원본 또는 output 파일을 강제로 추가하지 않았는가
- [ ] Git에 남는 것은 문서, 체크리스트, 코드, placeholder 샘플뿐인가

## 구조 선확인

- [ ] 비식별 HWPX 작업 복사본 후보가 준비된 경우에도 먼저 `hwpx_template_structure_analyzer_poc.py --template ... --no-output`으로 확인하는가
- [ ] 구조 선확인이 output 생성이나 수동 preview 재개 승인으로 오해되지 않는가
- [ ] 구조 선확인 결과에 본문 텍스트, 실제 원문, 개인정보, 실제 표 데이터를 저장하지 않는가
- [ ] 보류 조건이 있으면 렌더링 검수나 한컴 확인으로 넘어가지 않는가

## 렌더링 검수

- [ ] `docs/150_manual_preview_resume_gate.md` 조건을 충족했는가
- [ ] placeholder 기반 샘플 JSON만 사용했는가
- [ ] 렌더러가 `rendered` 또는 `template_required`처럼 안전한 상태를 반환하는가
- [ ] `remaining_placeholders`가 없는지 확인했는가
- [ ] output 파일을 한컴에서 열어 문단 분리와 번호체계를 확인했는가
- [ ] 글자 겹침, 줄간격, 표 깨짐, 붙임 표기 문제를 확인했는가

## 완료 판단

- [ ] 실제 원문이나 개인정보를 저장소에 추가하지 않았는가
- [ ] 실제 기관 양식 원본을 저장소에 추가하지 않았는가
- [ ] GitHub Desktop Changes에서 추적 대상 파일을 검토했는가
- [ ] 검수 결과를 문서화했는가
- [ ] 다음 단계 진행 전 사용자가 로컬 열람 결과를 확인했는가
- [ ] 보류 조건이 있으면 local template 또는 output 검증으로 넘어가지 않았는가
