# HWPX 템플릿 폴더 안내

## 목적

이 폴더는 HWPX 공문과 보고서 4종의 placeholder 템플릿 정책, manifest, style profile 기준을 관리하기 위한 위치입니다.

현재 단계에서는 실제 기관 HWPX 원본을 보관하지 않습니다. 로컬 placeholder HWPX 템플릿은 검증용으로 둘 수 있지만 Git 제외 상태를 유지해야 합니다.

## 보관 가능 파일

향후 보관 가능한 파일 유형:

- 비식별 공문 템플릿 후보
- placeholder 기반 HWPX 템플릿 후보
- 실제 개인정보나 내부 운영정보가 없는 테스트용 템플릿
- 문서번호, 기관명, 담당자명 등이 placeholder 처리된 템플릿

## 보관 금지 파일

다음 파일은 이 폴더에 보관하지 않습니다.

- 실제 공문 원본
- 실제 기관 양식 원본
- 실제 문서번호 또는 결재정보가 포함된 문서
- 민원자료
- 개인정보 포함 문서
- 업체 견적자료
- 대외비 또는 비공개 문서
- 내부망 자료
- 실제 업무 원본 파일

## placeholder 원칙

- 모든 템플릿에는 실제 값 대신 placeholder를 사용합니다.
- 예: {{title}}, {{body_sections}}, {{attachments}}, {{checklist}}
- 실제 기관명, 담당자명, 연락처, 문서번호, 차량번호, 장비명, 수량은 사용하지 않습니다.

## 현재 상태

- 현재 단계: Phase 4 문서 템플릿 안정화 검토
- 실제 기관 HWPX 원본: Git 추가 금지
- 로컬 placeholder HWPX 템플릿: Git 제외 상태로만 검증 허용
- 렌더링 코드: `renderers/hwpx_renderer/`의 placeholder 기반 로컬 PoC
- 최근 점검: `docs/125_hwpx_template_manifest_placeholder_consistency_review.md`
- 최근 점검: `docs/126_style_profile_confirmation_value_collection_criteria.md`
- 최근 점검: `docs/127_hwpx_manual_preview_gap_log_criteria.md`
- 최근 점검: `docs/128_external_hwpx_candidate_manual_procedure_and_hold_criteria.md`
- 최근 점검: `docs/129_local_template_gitignore_repeat_verification_criteria.md`
- 다음 점검: Phase 4 문서 템플릿 안정화 통합 점검과 실제 양식 수동 리허설 진입 여부 판단
