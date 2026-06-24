# 저장소 밖 HWPX placeholder 변환 체크리스트

최신 저장소 밖 실제 양식 후보 수동 절차와 보류 조건은 `docs/128_external_hwpx_candidate_manual_procedure_and_hold_criteria.md`를 함께 확인합니다. local template과 output Git 제외 반복 검증 기준은 `docs/129_local_template_gitignore_repeat_verification_criteria.md`를 따르며, 한컴 수동 preview 재개 전에는 `docs/150_manual_preview_resume_gate.md`를 먼저 확인합니다. 외부 HWPX 자동 채우기 skill 또는 `hwpx-cli` 참고 자료는 `docs/158_hwpx_autofill_conversion_adoption_review.md` 기준으로 구조 분석 참고용으로만 봅니다.

## 작업 위치

- [ ] 실제 원본을 저장소 안에 복사하지 않았는가
- [ ] 저장소 밖 로컬 작업 폴더에서만 복사본을 다루는가
- [ ] 작업 폴더명과 파일명에 실제 기관명, 부서명, 문서명이 없는가
- [ ] GitHub Desktop Changes에 실제 원본이 나타나지 않는가
- [ ] 외부 skill, MCP, `hwpx-cli`에 실제 원본을 바로 넣지 않는가

## 원본 등급 판단

- [ ] A/B/C/D 등급을 먼저 판단했는가
- [ ] C등급 문서를 placeholder 후보로 삼지 않았는가
- [ ] D등급 문서는 즉시 중단했는가
- [ ] 애매한 경우 더 보수적인 등급으로 분류했는가

## 식별 요소 제거

- [ ] 실제 본문 원문을 삭제했는가
- [ ] 실제 기관명, 관서명, 부서명, 업체명을 삭제했는가
- [ ] 실제 개인명, 담당자명, 연락처, 이메일을 삭제했는가
- [ ] 실제 문서번호, 시행일자, 접수번호, 사건번호, 민원번호를 삭제했는가
- [ ] 실제 결재선, 직인, 로고를 삭제했는가
- [ ] 실제 예산액, 실적 수치, 장비명, 차량번호, 내부 운영정보를 삭제했는가
- [ ] 문서 속성, 미리보기, 마지막 저장자 정보에 실제 정보가 남아 있지 않은가

## placeholder 변환

- [ ] 모든 동적 값이 중립적 placeholder로 바뀌었는가
- [ ] placeholder 이름으로 실제 대상이 추정되지 않는가
- [ ] 여러 줄 placeholder가 가능한 한 서로 다른 문단에 배치되었는가
- [ ] 확인되지 않은 값은 `[확인 필요]`, `null`, 또는 빈 문자열로 처리되는가
- [ ] 예산, 일정, 실적, 담당자, 수량을 임의 생성하지 않았는가
- [ ] 외부 자동 채우기 자료는 placeholder 후보 위치와 HWPX 구조 이해에만 사용했는가

## 저장소 반입 판단

- [ ] 기본값은 저장소 반입 금지로 두었는가
- [ ] 로컬 검증이 필요한 경우에도 `.hwpx`가 Git 제외 상태인지 확인했는가
- [ ] `templates/hwpx/*.hwpx`가 GitHub Desktop Changes에 나타나지 않는가
- [ ] `renderers/hwpx_renderer/output/*`가 GitHub Desktop Changes에 나타나지 않는가
- [ ] `normalizers/output/*`와 임시 파일도 GitHub Desktop Changes에 나타나지 않는가
- [ ] 로컬 HWPX 템플릿과 output 산출물이 `!!` ignored 상태인지 확인했는가

## 결과 기록

- [ ] 수동 preview 결과를 기록하는 경우 `docs/150_manual_preview_resume_gate.md` 조건을 충족했는가
- [ ] 실제 파일명이나 실제 양식명을 문서에 기록하지 않았는가
- [ ] 실제 원문 내용을 문서에 기록하지 않았는가
- [ ] 문서 유형, placeholder 구성, 검수 결과만 기록했는가
- [ ] 보안 판단과 중단 여부를 기록했는가
- [ ] 보류 조건이 있으면 다음 단계로 넘기지 않았는가
