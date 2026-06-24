# 저장소 밖 HWPX placeholder 변환 절차

## 목적

이 문서는 실제 기관 HWP/HWPX 양식 원본을 저장소에 넣지 않고, 저장소 밖 로컬 복사본을 placeholder 템플릿 후보로 바꾸는 작업 순서를 정리합니다.

현재 단계에서는 실제 원본 파일을 사용하지 않고 절차만 확정합니다.

## 핵심 원칙

최신 저장소 밖 실제 양식 후보 수동 절차와 보류 조건은 `docs/128_external_hwpx_candidate_manual_procedure_and_hold_criteria.md`를 함께 따릅니다. 수동 preview 재개 여부는 `docs/150_manual_preview_resume_gate.md` 조건을 먼저 확인합니다. 외부 HWPX 자동 채우기 skill 또는 `hwpx-cli` 참고 자료는 `docs/158_hwpx_autofill_conversion_adoption_review.md` 기준으로 구조 분석 참고용으로만 봅니다.

- 실제 기관 양식 원본은 이 저장소에 복사하지 않습니다.
- 실제 기관 양식 원본은 외부 AI, Custom GPT Knowledge, API 입력으로 사용하지 않습니다.
- 저장소 밖 로컬 작업 폴더에서만 복사본을 다룹니다.
- Git에 남길 수 있는 것은 절차 문서, 체크리스트, 코드, placeholder 기반 샘플뿐입니다.
- 실제 HWPX 템플릿과 output HWPX는 Git에서 제외합니다.
- 외부 skill, MCP, `hwpx-cli`에 실제 원본이나 실제 기관 양식을 바로 넣지 않습니다.

## 권장 작업 위치

실제 원본이 필요한 경우 저장소 안이 아니라 별도 로컬 폴더를 사용합니다.

예시:

```text
[사용자 로컬 작업 폴더]\hwpx_template_intake\
```

주의:

- 위 경로는 예시이며 저장소에 만들지 않습니다.
- 실제 파일명, 실제 기관명, 실제 문서명을 폴더명이나 파일명에 쓰지 않습니다.
- 작업 폴더는 GitHub Desktop Changes에 나타나지 않는 위치여야 합니다.

## 파일명 원칙

저장소 밖 작업 폴더에서도 실제 기관명이나 실제 문서명을 파일명에 쓰지 않습니다.

권장:

```text
source_original_do_not_commit.hwpx
working_copy_deidentified.hwpx
placeholder_candidate_[document_type].hwpx
```

금지:

```text
[실제 기관명]_[실제 문서명].hwpx
[실제 부서명]_[실제 양식명].hwpx
[실제 문서번호].hwpx
```

## 변환 절차

1. 원본 분류
   - A/B/C/D 등급을 먼저 판단합니다.
   - C등급은 내부 참고만 가능하며 외부 AI 입력, 샘플화, placeholder 후보에서 제외합니다.
   - D등급은 외부 처리 금지이며 즉시 중단합니다.

2. 저장소 밖 복사본 생성
   - 원본은 수정하지 않습니다.
   - 저장소 밖 로컬 작업 폴더에 복사본을 만듭니다.
   - 복사본 파일명에도 실제 기관명, 실제 문서번호, 실제 문서명을 쓰지 않습니다.

3. 식별 요소 제거
   - 실제 본문 원문을 삭제합니다.
   - 실제 기관명, 관서명, 부서명, 업체명, 개인명을 삭제합니다.
   - 실제 문서번호, 시행일자, 접수번호, 사건번호, 민원번호를 삭제합니다.
   - 실제 결재선, 직인, 로고, 담당자명, 연락처, 이메일을 삭제합니다.
   - 실제 예산액, 실적 수치, 장비명, 차량번호, 내부 운영정보를 삭제합니다.

4. placeholder 삽입
   - 동적 값은 중립적 placeholder로 바꿉니다.
   - 예: `{{title}}`, `{{background}}`, `{{main_points}}`, `{{future_plan}}`
   - placeholder 이름에 실제 기관, 실제 부서, 실제 업무명, 실제 사건명을 넣지 않습니다.
   - 여러 줄이 들어갈 placeholder는 가능한 한 서로 다른 문단에 둡니다.
   - 외부 자동 채우기 자료가 있더라도 placeholder 후보 위치와 HWPX 구조 이해에만 사용합니다.

5. 파일 속성 및 미리보기 확인
   - HWPX 미리보기, 문서 정보, 속성, 마지막 저장자 정보에 실제 정보가 남아 있지 않은지 확인합니다.
   - 파일 내부 검색이 가능하면 실제 기관명, 실제 사람 이름, 실제 문서번호를 검색합니다.
   - 확인이 어려우면 Git에 올리지 않고 로컬 검증 전용으로만 둡니다.

6. 저장소 안 이동 여부 판단
   - 기본값은 이동하지 않음입니다.
   - 테스트가 필요하면 `templates/hwpx/placeholder_[document_type].hwpx`에 로컬로 둘 수 있습니다.
   - `.hwpx`는 `.gitignore`로 제외되어야 하며 GitHub Desktop Changes에 나타나면 작업을 중단합니다.

7. 렌더링 검증
   - placeholder 기반 샘플 JSON만 사용합니다.
   - `remaining_placeholders`가 0인지 확인합니다.
   - output HWPX가 GitHub Desktop Changes에 나타나지 않는지 확인합니다.

8. 한컴 수동 검수
   - `docs/150_manual_preview_resume_gate.md` 조건 충족 후에만 진행합니다.
   - 글자 겹침, 줄간격, 문단 간격, 번호체계, 표 표시를 확인합니다.
   - 겹침이 있으면 실제 데이터를 넣지 말고 placeholder 길이와 문단 배치를 조정합니다.

9. 결과 문서화
   - 실제 원본 파일명, 실제 양식명, 실제 원문 내용을 기록하지 않습니다.
   - 문서 유형, placeholder 구성, 검수 결과, 보안 판단만 기록합니다.

## C/D등급 중단 기준

다음 자료는 placeholder 변환 후보로 삼지 않습니다.

- 민원인 실명, 연락처, 주소가 포함된 문서
- 민원번호, 접수번호, 사건번호가 포함된 문서
- 감사, 징계, 인사, 수사, 보안 관련 문서
- 대외비, 비공개, 내부전용 표시 문서
- 차량번호, 장비현황, 순찰구역, 배치 위치, 내부 운영시간이 포함된 문서
- 내부망 주소, 시스템명, 계정, 비밀번호, API 키가 포함된 문서
- 특정 개인, 기관, 업체, 사건을 쉽게 추정할 수 있는 문서

## GitHub Desktop 확인 순서

작업 후 GitHub Desktop에서 다음을 확인합니다.

1. 실제 원본 HWP/HWPX 파일이 Changes에 없는지
2. `templates/hwpx/*.hwpx`가 Changes에 없는지
3. `renderers/hwpx_renderer/output/*` 산출물이 Changes에 없는지
4. 문서, 체크리스트, 코드 변경만 Changes에 있는지
5. 의도하지 않은 `__pycache__`, 임시 파일, 잠금 파일이 없는지

## 완료 기준

- 실제 원본을 저장소에 추가하지 않음
- 저장소 밖 복사본 절차가 명확함
- 실제 식별 요소 제거 기준이 명확함
- placeholder 이름이 중립적임
- 외부 HWPX 자동 채우기 자료가 구조 분석 참고용으로만 남음
- 로컬 HWPX 템플릿과 output HWPX가 Git 제외 상태임
- 다음 단계에서 사용자가 저장소 밖에서 안전하게 복사본을 만들 수 있음
- 반복 작업 전 Git 제외 상태 검증 기준은 `docs/129_local_template_gitignore_repeat_verification_criteria.md`에서 확인함
- 한컴 수동 preview 재개 전 `docs/150_manual_preview_resume_gate.md` 조건을 확인함
