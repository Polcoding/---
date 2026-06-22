# 향후 아키텍처

## 목적

향후 개발자가 전체 시스템 구현 방향을 이해할 수 있도록 단계와 구성요소를 정리합니다.

## 단계별 로드맵

| Phase | 이름 | 목표 |
|---:|---|---|
| 1 | 안전한 테스트판과 로컬 PoC | 프롬프트, 보안 기준, 샘플 JSON, HWPX/XLSX/Markdown/Email 로컬 렌더러 검증 |
| 2 | 입력 정규화와 보안 필터 설계 | 짧은 업무 지시를 표준 JSON으로 바꾸고 위험 입력을 차단하는 설계 |
| 3 | 저장소 밖 실제 양식 절차 검증 | 실제 원본을 저장소 밖에서 비식별 placeholder 복사본으로 바꾸는 절차 확인 |
| 4 | 문서 템플릿 안정화 | HWPX 보고서 4종의 필수 입력값, 누락값, 서식 정책 정리 |
| 5 | 보안 필터 PoC | 개인정보와 민감정보 탐지, A/B/C/D 등급 처리 흐름 구현 |
| 6 | 입력 정규화 PoC | 이메일ㆍ메모ㆍ문장을 표준 입력 형식으로 변환 |
| 7 | API 연결 검토 | 보안 검토를 통과한 입력만 API에 전달하는 구조 설계 |
| 8 | 이메일 자동화 검토 | 초안 회신 중심 자동화만 별도 승인 후 검토 |
| 9 | 로그와 감사 추적 | 처리 이력, 승인 이력, 오류 이력 관리 |

현재 기준에서는 API 연결, Make.com 연동, 이메일 자동화 구현을 시작하지 않습니다. 외부 연동 필요성과 보류 기준은 `docs/115_phase3_external_integration_hold_criteria.md`를 기준으로 검토하며, 로그와 감사 추적 기준은 `docs/116_phase3_log_and_audit_trace_criteria.md`에, 테스트 계정과 테스트 데이터 기준은 `docs/117_phase3_test_account_and_test_data_criteria.md`에, 실제 원문 차단과 비식별 입력 확인 절차는 `docs/118_phase3_source_blocking_and_deidentified_input_check_procedure.md`에, 사용자 preview와 사람 승인 지점 통합 기준은 `docs/119_phase3_user_preview_and_human_approval_integration.md`에, 외부 전송 없는 no-send dry-run 기준은 `docs/120_phase3_no_send_dry_run_criteria.md`에, 외부 연동 구현 범위 승인 판단은 `docs/121_phase3_external_integration_scope_approval_judgment.md`에, Phase 3 마무리 판단은 `docs/122_phase3_closeout_and_phase4_entry_decision.md`에, Phase 4 문서 템플릿 안정화 진입 판단은 `docs/123_phase4_template_stabilization_entry_judgment.md`에, 프로젝트 방향 재확인과 구형 문서 업데이트 기준은 `docs/124_project_direction_and_legacy_update_review.md`에, HWPX template manifest와 공통 placeholder 정합성은 `docs/125_hwpx_template_manifest_placeholder_consistency_review.md`에, style profile 확인 필요 값 유지 기준은 `docs/126_style_profile_confirmation_value_collection_criteria.md`에, HWPX 수동 preview gap log 기준은 `docs/127_hwpx_manual_preview_gap_log_criteria.md`에 문서 기준으로 정리했습니다. 다음 우선순위는 저장소 밖 실제 양식 후보 수동 절차와 보류 조건 정리입니다.

## 구성요소

### Input Adapter

이메일, 웹폼, 메모 등 다양한 입력을 시스템이 읽을 수 있는 형태로 받는 모듈입니다.

### Task Normalizer

사용자의 짧은 지시를 표준 업무 요청 형식으로 정리합니다. 예를 들면 요청 목적, 문서 유형, 대상, 기한, 확인 필요 항목을 분리합니다.

### Security Classifier

입력에 개인정보, 내부자료, 대외비, 계정 정보가 포함되어 있는지 확인하고 low, medium, high 위험도로 분류합니다.

### Redactor

민감정보를 placeholder로 치환합니다. 단순히 일부 문자를 가리는 것이 아니라 문맥에서 실제 사건성이 드러나지 않도록 줄입니다.

### Task Router

요청 유형에 따라 공문, 기획서, 조사표, 업체 메일 등 적절한 처리 흐름으로 보냅니다.

### Draft Generator

보안 검토를 통과한 입력으로 초안을 생성합니다. 확인되지 않은 정보는 `[확인 필요]`로 표시합니다.

### Template Renderer

문서의 폰트, 자간, 줄간격, 표 양식, 여백을 적용합니다. AI가 직접 서식을 맞추는 대신 템플릿 엔진이 담당합니다.

### Output Adapter

생성된 초안을 사용자에게 보여주거나 내부 검토 도구로 전달합니다. 1차 목표는 초안 회신이며, 자동 발송은 별도 승인 이후에만 검토합니다.

### Audit Logger

요청, 위험도 판정, 비식별화 결과, 사용자 승인 여부를 기록합니다. 로그에는 원문 민감정보를 저장하지 않는 방향으로 설계해야 합니다.

## 권장 구현 순서

1. Phase 1 완료 기준과 Phase 2 진입 조건을 확인합니다.
2. 실제 원본 없는 연습 파일 또는 저장소 밖 비식별 복사본으로 안전 절차를 확인합니다.
3. HWPX 보고서 4종의 필수 입력값과 누락값 처리 정책을 정리합니다.
4. 입력 정규화 스키마를 먼저 설계합니다.
5. 보안 필터 요구사항을 구현 전 문서로 확정합니다.
6. 조직 보안정책 검토 후 API 연동 범위를 결정합니다.
