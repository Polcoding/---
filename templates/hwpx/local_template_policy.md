# HWPX 로컬 템플릿 보관 정책

## 목적

이 문서는 HWPX 테스트 템플릿 파일을 로컬에서 안전하게 관리하기 위한 정책입니다.

현재 단계에서는 실제 HWPX 파일을 Git 저장소에 보관하지 않습니다.

## 로컬 보관 원칙

- 실제 HWPX 파일은 기본적으로 Git에 커밋하지 않습니다.
- 테스트 템플릿은 placeholder 기반이어야 합니다.
- 실제 기관 양식 원본은 이 폴더에 보관하지 않습니다.
- 실제 개인정보나 내부 운영정보가 포함된 파일은 이 폴더에 보관하지 않습니다.
- .hwpx와 .hwp 파일은 .gitignore로 기본 제외합니다.

## 실제 원본 처리 원칙

저장소 밖 실제 양식 후보 수동 절차와 보류 조건은 `docs/128_external_hwpx_candidate_manual_procedure_and_hold_criteria.md` 기준을 함께 따릅니다.

- 실제 기관 양식 원본은 저장소 밖 로컬 작업 폴더에서만 다룹니다.
- 원본은 직접 수정하지 않고 복사본에서 실제 내용과 식별 요소를 제거합니다.
- 비식별 placeholder 후보가 되더라도 기본적으로 Git에 추가하지 않습니다.
- GitHub Desktop Changes에 HWP/HWPX 파일이 나타나면 작업을 중단하고 제외 상태를 다시 확인합니다.

## 반복 검증 필요성

로컬 placeholder 템플릿과 output 산출물은 반복 작업 중에도 Git 제외 상태를 다시 확인해야 합니다. 반복 검증 기준은 `docs/129_local_template_gitignore_repeat_verification_criteria.md`를 따릅니다.

현재 폴더별 ignore 역할:

- `templates/hwpx/.gitignore`: `.hwpx`, `.hwp`, 임시 파일 제외
- `renderers/hwpx_renderer/output/.gitignore`: renderer output 제외
- `normalizers/output/.gitignore`: normalizer output 제외

root `.gitignore`가 없더라도 위 폴더별 규칙으로 로컬 HWPX 템플릿과 output 산출물을 제외합니다. GitHub Desktop Changes에 HWP/HWPX/output 파일이 보이면 commit 또는 push하지 않습니다.

## 서식값 수집 기록 원칙

- style profile 서식값 수집 기록에는 실제 원본 파일명, 실제 기관명, 실제 문서번호를 남기지 않습니다.
- 글꼴, 자간, 줄간격, 문단 간격, 표 서식 값이 확인되지 않았으면 `[확인 필요]`로 둡니다.
- 확인된 값도 바로 renderer나 normalizer에 연결하지 않고, 사람 검토와 별도 승인 후 반영합니다.
- 폰트 파일, HWP/HWPX 원본, 이미지 원본은 저장소에 추가하지 않습니다.

## 수동 preview gap 기록 원칙

- HWPX preview에서 발견한 gap은 `docs/127_hwpx_manual_preview_gap_log_criteria.md` 기준으로 기록합니다.
- gap log에는 실제 원본 파일명, 실제 기관명, 실제 문서번호, 실제 본문을 남기지 않습니다.
- 로컬 placeholder HWPX 템플릿과 output 산출물은 Git 제외 상태를 유지합니다.
- gap이 발견되어도 실제 서식값을 임의 확정하지 않고, 사용자 재확인 또는 보류 상태로 둡니다.
- 표가 포함된 템플릿은 현재 단계에서 표 내부 값이 아니라 표 위치, 폭, 줄바꿈, 겹침, 여백만 확인합니다.
- 표 내부 데이터와 계산은 향후 Excel/한셀 연동 후보로 분리하며, 실제 물품명, 수량, 금액, 대상 목록은 기록하지 않습니다.
