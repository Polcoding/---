# HWPX 템플릿 manifest

## 목적

이 문서는 향후 HWPX placeholder 템플릿 파일을 관리하기 위한 manifest 초안입니다.

현재 단계에서는 실제 HWPX 파일을 Git에 등록하지 않습니다.

로컬 placeholder HWPX 템플릿은 검증에 사용할 수 있지만, `.gitignore`로 제외된 로컬 파일이므로 이 manifest에는 실제 파일명 대신 문서 유형과 정책만 기록합니다.

## 템플릿 목록

| template_id | 문서유형 | 예상 파일명 | 상태 | 비고 |
|---|---|---|---|---|
| hwpx_official_letter_basic | 일반 공문 | [확인 필요] | 설계 중 | 실제 파일 없음 |
| hwpx_survey_request_letter | 현황조사 지시 공문 | [확인 필요] | 설계 중 | 실제 파일 없음 |
| hwpx_one_page_report_basic | 원페이지 보고서 | [로컬 placeholder 파일] | 로컬 검증 완료 | Git 등록 안 함 |
| hwpx_project_plan_basic | 추진계획서 | [로컬 placeholder 파일] | 로컬 검증 완료 | Git 등록 안 함 |
| hwpx_result_report_basic | 결과보고서 | [로컬 placeholder 파일] | 로컬 검증 완료 | Git 등록 안 함 |
| hwpx_review_report_basic | 검토보고서 | [로컬 placeholder 파일] | 로컬 검증 완료 | Git 등록 안 함 |

## manifest 작성 원칙

- 실제 기관 양식 파일명을 기록하지 않습니다.
- 실제 기관 양식명을 기록하지 않습니다.
- 로컬 placeholder HWPX 파일은 Git 제외 상태를 유지합니다.
- 로컬 검증 완료 상태는 문서로 기록하되 실제 파일은 등록하지 않습니다.
- 실제 기관 원본 양식은 등록하지 않습니다.

## 보관 금지

- 실제 기관 HWPX 양식 원본
- 실제 공문 원본
- 실제 문서번호나 결재정보가 포함된 문서
- 실제 개인정보가 포함된 문서
- 대외비 또는 비공개 문서
- 내부망 자료
- 실제 업무 원본 파일

## 향후 등록 전 검수 조건

- 모든 동적 값이 placeholder인지 확인
- 실제 개인정보가 없는지 확인
- 실제 기관명, 담당자명, 문서번호가 없는지 확인
- 문서 서식이 테스트용인지 확인
- Git 커밋 전에 검수 체크리스트를 통과했는지 확인

## 테스트 템플릿 등록 전 조건

테스트 HWPX 템플릿을 manifest에 등록하기 전 다음 조건을 만족해야 합니다.

- HWPX 테스트 템플릿 안전 체크리스트 통과
- 모든 동적 값 placeholder 처리
- 실제 기관 양식 원본이 아님
- 실제 공문 원문이 없음
- 실제 개인정보나 내부 운영정보 없음
- 사용자가 Git 포함을 명시적으로 승인
