# 공공기관 행정문서 AI 자동화 시스템

## 프로젝트 한 줄 정의

비식별화된 업무 지시를 받아 공공기관 행정문서 초안을 만들고, 사람이 최종 검토ㆍ수정ㆍ승인하는 행정 비서형 AI 시스템의 HWPX 보고서 우선 로컬 PoC 및 Phase 4 문서 템플릿 안정화 저장소입니다.

현재 실제로 작동 확인된 범위와 아직 결과물이 아닌 범위는 `CURRENT_STATUS.md`를 먼저 확인합니다.

## Codex 작업 시작 전 토큰 가드

새 작업을 시작할 때는 전체 `docs/` 또는 `checklists/`를 먼저 훑지 말고, 토큰 컨텍스트 가드를 먼저 확인합니다.

```powershell
.\scripts\show_context_guard.ps1
```

Windows 실행 정책 때문에 `.ps1` 직접 실행이 막히면 다음처럼 실행합니다.

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\show_context_guard.ps1
```

작업 유형이 분명하면 다음 중 하나를 사용합니다.

```powershell
.\scripts\show_context_guard.ps1 -TaskType docs
.\scripts\show_context_guard.ps1 -TaskType hwpx-policy
.\scripts\show_context_guard.ps1 -TaskType normalizer
.\scripts\show_context_guard.ps1 -TaskType renderer
.\scripts\show_context_guard.ps1 -TaskType security
.\scripts\show_context_guard.ps1 -TaskType review
```

가드는 파일 접근을 막는 장치가 아닙니다. 최신 진입점부터 작게 읽고, 보안ㆍHWPXㆍ실제 원본 가능성이 있으면 즉시 사용자 확인 또는 컨텍스트 확장으로 전환하기 위한 안내입니다.

## 이번 저장소의 목적

이 저장소는 실제 업무 자동화 운영물이 아닙니다. 안전한 Custom GPT 테스트판, placeholder 기반 샘플 JSON, 로컬 PoC 렌더러, 입력 정규화 PoC, 테스트 결과 문서, 보안 기준을 정리합니다.

핵심 메시지는 다음과 같습니다.

> 이 프로젝트는 AI가 공문을 마음대로 작성하는 시스템이 아니라, 비식별 업무 지시를 받아 공공기관 행정문서 초안을 만들고 사람이 최종 승인하는 시스템입니다.

## 현재 저장소에서 하는 일

- Custom GPT에 붙여넣을 Instructions v0.1 작성
- GPT 이름, 설명, 대화 시작 문구 정리
- 처리 가능 업무와 처리 금지 업무 기준 정리
- 개인정보와 민감정보 비식별화 규칙 정리
- 테스트용 업무 지시 샘플과 모범 출력 예시 작성
- 테스트 결과 평가표 작성
- placeholder 기반 HWPX/XLSX/Markdown/Email 로컬 PoC 렌더러 검증
- HWPX 보고서 템플릿 자동화 우선순위 검증
- HWPX 보고서 4종 placeholder 템플릿 치환 및 한컴 수동 검수
- 비식별 입력 정규화, 보안 필터, HWPX payload 매핑, renderer dry-run 최소 PoC 검증
- Phase 2 최소 운영 흐름과 사용자 입력 템플릿 정리
- Phase 3 외부 연동 보류 기준과 no-send dry-run 기준 정리
- Phase 4 문서 템플릿 안정화 진입 판단과 구형 문서 업데이트 기준 정리
- 저장소 밖 실제 양식 후보 수동 절차와 보류 조건 정리
- local template policy와 Git 제외 상태 반복 검증 기준 정리
- Phase 4 문서 템플릿 안정화 통합 점검과 실제 양식 수동 리허설 조건부 진입 판단
- 실제 양식 수동 리허설 사용자 확인 패킷과 gap log 빈 양식 정리
- 실제 양식 수동 리허설 전 사용자 준비 확인 기록
- HWPX 일원화 유지와 표 데이터 Excel/한셀 연동 후보 분리 결정
- 비식별 HWPX 작업 복사본 없음에 따른 실제 양식 수동 리허설 보류 기록
- HWPX 보고서와 Excel/한셀 표 데이터 역할 분리 범위 정리
- HWPX 보고서 4종 사용자 입력 템플릿의 표 데이터 후보 표시 기준 정리
- 보고서 샘플 JSON 4종의 표 데이터 후보 직접 반영 보류 결정
- renderer와 normalizer 안내 문서의 표 데이터 후보 오해 가능성 점검
- 실행 가능한 최소 PoC 경로와 현재 결과물 범위를 `CURRENT_STATUS.md`에 정리
- 사용자 입력 항목을 `[사용자 확인 필요]`, `[Codex 처리 가능]`, `[보류]`로 구분
- 외부 HWPX 자동 채우기 skill, 샘플 HWPX, `hwpx-cli` 참고 자료를 현재 보안 원칙과 placeholder 렌더러 흐름에 맞춰 채택 검토
- 설치된 skill, 저장소 밖 `hwpx-cli`, 기존 Python PoC가 충돌하지 않도록 외부 도구 격리 기준 정리
- 외부 구조 분석 아이디어를 Python 기반 HWPX template 구조 분석 PoC로 저장소 내부 구현
- placeholder 없는 제공 샘플 HWPX 2종에 대해 profile-aware 비식별 초안 주입 output을 생성하고 한컴 수동 확인 완료
- 샘플 HWPX 1/2에 대해 주제만 넣는 간단 실행 경로와 비식별 주제 4개 회귀검증 경로 확인
- 샘플 HWPX 1/2 batch 실행에서 목적, 대상, 기간, 협조사항 등 선택 입력값 반영 가능

## 현재 자동화 우선순위

이 저장소의 최우선 자동화 대상은 Email이 아니라 HWPX 기반 보고서 템플릿입니다.

우선순위는 다음과 같이 관리합니다.

| 우선순위 | 대상 | 출력 형식 | 비고 |
|---|---|---|---|
| 1 | 원페이지 보고서 | HWPX | 최우선 자동화 대상 |
| 2 | 추진계획서 | HWPX | 핵심 계획 문서 |
| 3 | 결과보고서 | HWPX | 기존 계획 대비 결과 정리 |
| 4 | 검토보고서 | HWPX | 내부 검토자료 |
| 5 | 조사표 | XLSX | 보조 자동화 대상 |
| 6 | 협조 요청 메일 | Email | 보조 초안 작성, 정중한 실무 메일체 |

결과보고서는 가능한 경우 기존 추진계획서의 추진개요, 세부계획, 일정, 예산, 기대효과 항목과 대응되도록 정리합니다.

협조 요청 메일은 공문체가 아니라 정중한 실무 메일체로 작성하며, 실제 자동 발송이 아니라 사람이 검토하는 초안으로만 관리합니다.

HWPX 보고서 안의 표는 현재 단계에서 표 틀과 배치 검수 대상으로만 다룹니다. 표 내부 데이터, 수량, 금액, 대상 목록 자동화는 향후 Excel/한셀 연동 후보로 분리합니다.

## 현재 진행 위치

- Phase 1 문서화와 placeholder 기반 HWPX 보고서 4종 검증은 완료된 상태입니다.
- Phase 2 최소 PoC는 입력 정규화, 보안 필터, HWPX payload 매핑, dry-run, 한컴 수동 검토 흐름을 다듬는 단계로 문서 기준 마무리했습니다.
- Phase 2 운영 문서 묶음 최종 정리와 READMEㆍAGENTS 최신화 필요 여부 확인까지 완료했습니다.
- Phase 2 마무리 전 normalizers 회귀 테스트 묶음 재검증을 완료했습니다.
- Phase 2 최소 PoC는 문서 기준 마무리 가능 상태로 판단했습니다.
- Phase 3 진입 조건 및 안전 게이트 문서화를 완료했습니다.
- Phase 3 저장소 밖 HWPX 양식 취급 기준과 사용자 수동 preview 기준 구체화를 완료했습니다.
- Phase 3 상태별 중단 기준을 반복 운영 문서에 반영했습니다.
- Phase 3 운영 문서 묶음 통합 점검을 완료했습니다.
- Phase 3 외부 연동 필요성과 보류 기준 검토를 완료했습니다.
- Phase 3 로그와 감사 추적 기준 구체화를 완료했습니다.
- Phase 3 테스트 계정과 테스트 데이터 기준 구체화를 완료했습니다.
- Phase 3 실제 원문 차단과 비식별 입력 확인 절차 구체화를 완료했습니다.
- Phase 3 사용자 preview와 사람 승인 지점 통합 기준 구체화를 완료했습니다.
- Phase 3 외부 전송 없는 no-send dry-run 기준 구체화를 완료했습니다.
- Phase 3 외부 연동 구현 범위 승인 판단을 완료했습니다.
- Phase 3 마무리 판단 및 Phase 4 진입 여부 결정을 완료했습니다.
- Phase 4 문서 템플릿 안정화 진입 판단을 완료했습니다.
- 프로젝트 방향 재확인과 구형 진입점 문서 업데이트 기준 정리를 완료했습니다.
- HWPX 보고서 4종 template manifest와 공통 placeholder 정합성 점검을 완료했습니다.
- style profile의 `[확인 필요]` 값 유지 기준과 수집 체크리스트 정리를 완료했습니다.
- HWPX 보고서 4종 수동 preview 서식 gap log와 점검 기준 정리를 완료했습니다.
- 저장소 밖 실제 양식 후보 수동 절차와 보류 조건 재정렬을 완료했습니다.
- local template policy와 Git 제외 상태 반복 검증 기준 정리를 완료했습니다.
- Phase 4 문서 템플릿 안정화 통합 점검과 실제 양식 수동 리허설 조건부 진입 판단을 완료했습니다.
- 실제 양식 수동 리허설 사용자 확인 패킷과 gap log 빈 양식 정리를 완료했습니다.
- 실제 양식 수동 리허설 준비 확인 기록을 남겼으나, 이후 실제 preview용 비식별 작업 복사본 없음이 확인되어 수동 리허설은 보류로 전환했습니다.
- HWPX 일원화 유지와 표 데이터 Excel/한셀 연동 후보 분리 결정을 완료했습니다.
- 현재 기준으로 비식별 HWPX 작업 복사본이 없어 실제 양식 수동 리허설은 보류로 기록했습니다.
- HWPX 보고서와 Excel/한셀 표 데이터 역할 분리 범위를 정리했습니다.
- HWPX 보고서 4종 사용자 입력 템플릿의 표 데이터 후보 표시 기준을 실제값 없이 정리했습니다.
- `examples/json` 보고서 샘플 4종에는 표 데이터 후보 필드를 직접 추가하지 않기로 정리했습니다.
- renderer와 normalizer 안내 문서가 표 데이터 후보를 실제 구현 지시처럼 오해하지 않도록 보강했습니다.
- 현재 기준으로 실제 작동 확인된 최소 경로는 `CURRENT_STATUS.md`에 정리했습니다.
- 사용자 입력 템플릿과 반복 운영 로그는 `[사용자 확인 필요]`, `[Codex 처리 가능]`, `[보류]` 역할 구분을 사용합니다.
- 사용자용 A-to-Z 운영 안내는 `docs/140_user_operation_atoz_guide.md`에 정리했습니다.
- 사용자 quick start, 비식별 요청 예시, 문서 기반 리허설 경계와 hold 상태를 `docs/141`부터 `docs/149`까지 정리했습니다.
- 수동 preview 재개 게이트와 체크리스트, 결과물 지도, 사용자 가시 산출물 closeout을 `docs/150`부터 `docs/154`까지 정리했습니다.
- 구형 다음 단계 문구 점검, 사용자 가시 산출물 보안ㆍGit 제외 검증, 현황판 진행률 점검을 `docs/155`부터 `docs/157`까지 정리했습니다.
- 사용자 quick start, A-to-Z 안내, 리허설 체크리스트에서도 HWPX 열람 전 `docs/150_manual_preview_resume_gate.md` 조건을 먼저 확인하도록 정리했습니다.
- 현재 작업 운영 기준은 작은 확인마다 멈추지 않고, push 기준점이 생길 때까지 같은 변경 묶음 안에서 다음 추천 작업을 계속 진행하는 방식입니다.
- 외부 HWPX 자동 채우기 skill, 샘플 HWPX 구조, `hwpx-cli` 참고 방향은 `docs/158_hwpx_autofill_conversion_adoption_review.md`에 정리했습니다.
- 외부 도구와 기존 PoC의 충돌 방지 기준은 `docs/159_external_tool_isolation_and_conflict_policy.md`에 정리했습니다.
- 외부 skill과 기존 작업의 충돌 점검 및 내부 구현 전환 결과는 `docs/160_external_skills_conflict_and_modernization_review.md`에 정리했습니다.
- 제공 샘플 HWPX 2종의 profile-aware output은 샘플1 글자 겹침 없음, 샘플2 bullet 중복 없음으로 수동 확인했습니다.

## 현재도 하지 않는 일

- 실제 이메일 발송 자동화
- Make.com, Gmail, Outlook, OpenAI API 실제 연동 코드 작성
- 실제 공공기관 원문 문서 업로드 또는 학습
- 실제 개인정보, 민감정보, 내부자료, 대외비 자료 사용
- 결재, 계약, 업체 선정, 예산 집행, 법률 판단, 민원 처리 결론 자동화
- 실제 기관 양식 원본 기반 문서 서식 렌더링 엔진 구현
- HWPX 표 내부 실제 데이터 자동 입력 또는 Excel/한셀 자동 연동

## 전체 시스템 아키텍처 개요

```text
사용자 입력
→ 입력 정규화
→ 보안ㆍ개인정보 필터
→ 업무 유형 분류
→ AI 초안 생성
→ 문서 템플릿 렌더링
→ 사용자 검토
→ 사람 승인 후 실무 적용
```

현재 단계에서는 위 흐름 중 Custom GPT Instructions, 테스트 입력, 평가 기준, 보안 원칙, 개발 문서, placeholder 기반 로컬 PoC 렌더러, 입력 정규화 PoC, dry-run 검증, Phase 4 문서 템플릿 안정화 검토, HWPX 표 틀 중심 preview 기준만 다룹니다.

## 폴더 구조

```text
.
├── README.md
├── AGENTS.md
├── docs/
├── prompts/
├── examples/
├── checklists/
├── templates/
├── renderers/
├── normalizers/
└── tasks/
```

## 빠른 시작 방법

1. `prompts/custom_gpt_instructions_v0.1.md`의 내용을 Custom GPT Instructions에 붙여넣습니다.
2. `prompts/conversation_starters.md`의 문구를 Conversation Starters에 등록합니다.
3. Custom GPT의 Knowledge는 비워 둡니다.
4. Capabilities와 Actions/Apps는 초기 테스트에서 사용하지 않습니다.
5. `docs/08_custom_gpt_test_execution_guide.md`에 따라 Preview에서 테스트 1~5를 실행합니다.
6. `docs/05_evaluation_sheet.md`로 결과를 채점합니다.
7. `checklists/custom_gpt_manual_test_checklist.md`로 실행 상태를 확인합니다.
8. `checklists/security_review_checklist.md`로 민감정보 포함 여부를 확인합니다.

## Custom GPT 테스트 흐름

```text
Instructions 복사
→ Conversation Starters 복사
→ Knowledge 비워 둠
→ Capabilities 비활성 권장
→ Actions/Apps 미사용
→ Preview 테스트 1~5 실행
→ 평가표 채점
→ 위험 응답 기록
→ Instructions 개선
→ 재테스트
```

## 문서 목록

- `CURRENT_STATUS.md`: 현재 시스템 현황판
- `AGENTS.md`: Codex 작업 규칙
- `docs/00_chatgpt_handoff.md`: ChatGPT 프로젝트 인수인계
- `docs/00_project_overview.md`: 전체 프로젝트 설명
- `docs/01_custom_gpt_setup.md`: Custom GPT 설정 절차
- `docs/02_security_policy.md`: 처리 가능 업무와 금지 업무 기준
- `docs/03_deidentification_rules.md`: 비식별화 규칙
- `docs/04_test_cases.md`: 테스트 케이스
- `docs/05_evaluation_sheet.md`: 평가표
- `docs/06_future_architecture.md`: 향후 아키텍처
- `docs/07_make_api_next_steps.md`: 자동화 전 준비사항
- `docs/08_custom_gpt_test_execution_guide.md`: Custom GPT Preview 수동 테스트 절차
- `docs/09_phase1_review_and_next_steps.md`: 1단계 검수 후 다음 스텝
- `docs/11_document_inventory.md`: 원천 문서 인벤토리 기준
- `docs/12_security_classification.md`: 문서 보안 분류 기준
- `docs/13_deidentified_style_samples.md`: 비식별 문체 샘플
- `docs/14_document_pattern_library.md`: 문서 패턴 라이브러리
- `docs/15_style_specification.md`: 문체 명세
- `docs/16_knowledge_candidate_review.md`: Knowledge 후보 검토 기준
- `docs/18_ai_output_json_schema.md`: AI 출력 JSON 스키마 정의
- `docs/19_xlsx_template_poc_plan.md`: XLSX 조사표 템플릿 PoC 설계
- `docs/20_hwpx_template_poc_plan.md`: HWPX 공문 템플릿 PoC 설계
- `docs/21_template_renderer_requirements.md`: 템플릿 렌더러 요구사항
- `docs/22_renderer_validation_samples.md`: 렌더러 검증용 샘플 JSON
- `docs/23_poc_readiness_review.md`: PoC 구현 전 통합 검수
- `docs/24_sample_json_validation_report.md`: 샘플 JSON 세부 검수 보고서
- `docs/25_xlsx_renderer_poc_result.md`: XLSX 렌더러 PoC 결과
- `docs/26_markdown_renderer_poc_result.md`: Markdown 미리보기 렌더러 PoC 결과
- `docs/27_email_renderer_poc_result.md`: Email 초안 렌더러 PoC 결과
- `docs/28_local_poc_integration_test_report.md`: 로컬 PoC 통합 검수 보고서
- `docs/29_xlsx_renderer_v02_result.md`: XLSX 렌더러 v0.2 결과
- `docs/30_hwpx_renderer_preimplementation_review.md`: HWPX 렌더러 PoC 구현 전 재검수
- `docs/31_hwpx_style_and_language_requirements.md`: HWPX 서식 및 공문체 요구사항
- `docs/32_hwpx_placeholder_template_strategy.md`: HWPX placeholder 템플릿 전략
- `docs/33_hwpx_minimal_poc_scope.md`: HWPX 최소 PoC 구현 범위
- `docs/34_hwpx_minimal_poc_result.md`: HWPX 최소 PoC 결과
- `docs/35_hwpx_test_template_preparation_guide.md`: HWPX 테스트 템플릿 준비 가이드
- `docs/36_hwpx_placeholder_render_test_result.md`: HWPX placeholder 렌더링 테스트 결과
- `docs/37_hwpx_placeholder_actual_render_test_result.md`: HWPX placeholder 실제 치환 테스트 결과
- `docs/38_hwpx_rendered_output_review.md`: HWPX 렌더링 결과 수동 검수 보고서
- `docs/39_hwpx_paragraph_rendering_improvement.md`: HWPX 본문 문단 렌더링 개선
- `docs/40_hwpx_institution_style_values_review.md`: HWPX 기관 표준 서식값 확인 기준
- `docs/42_channel_style_policy.md`: 채널별 문체 정책
- `docs/43_report_template_automation_priority.md`: HWPX 보고서 템플릿 자동화 우선순위
- `docs/44_report_sample_json_set.md`: HWPX 보고서용 샘플 JSON 세트
- `docs/45_one_page_report_hwpx_template_strategy.md`: 원페이지 보고서 HWPX 템플릿 전략
- `docs/46_one_page_report_hwpx_render_test_result.md`: 원페이지 보고서 HWPX 렌더링 테스트 결과
- `docs/47_result_review_report_hwpx_support_check.md`: 결과보고서ㆍ검토보고서 HWPX 렌더러 지원 확인
- `docs/48_git_push_timing_and_summary.md`: GitHub Desktop push 타이밍과 summary 기준
- `docs/49_result_report_hwpx_template_preparation.md`: 결과보고서 HWPX 최소 템플릿 준비
- `docs/50_result_report_hwpx_render_test_result.md`: 결과보고서 HWPX 렌더링 테스트 결과
- `docs/51_review_report_hwpx_template_preparation.md`: 검토보고서 HWPX 최소 템플릿 준비
- `docs/52_review_report_hwpx_render_test_result.md`: 검토보고서 HWPX 렌더링 테스트 결과
- `docs/53_real_hwpx_template_intake_safety_procedure.md`: 실제 HWPX 양식 투입 전 안전 절차
- `docs/54_hwpx_common_placeholder_design.md`: HWPX 공통 placeholder 설계
- `docs/55_project_plan_hwpx_template_preparation.md`: 추진계획서 HWPX 최소 템플릿 준비
- `docs/56_project_plan_hwpx_render_test_result.md`: 추진계획서 HWPX 렌더링 테스트 결과
- `docs/57_hwpx_report_4types_completion_and_safety_rehearsal.md`: HWPX 보고서 4종 완료 상태 및 안전 리허설
- `docs/58_external_hwpx_placeholder_conversion_runbook.md`: 저장소 밖 HWPX placeholder 변환 절차
- `docs/59_phase1_completion_and_phase2_entry_criteria.md`: Phase 1 완료 기준 및 Phase 2 진입 조건
- `docs/60_hwpx_report_input_requirements.md`: HWPX 보고서 4종 입력 요구사항
- `docs/61_input_normalization_schema.md`: 입력 정규화 스키마 초안
- `docs/62_security_filter_requirements.md`: Phase 2 보안 필터 요구사항
- `docs/63_input_normalization_test_cases.md`: 입력 정규화 테스트 케이스
- `docs/64_hwpx_report_normalized_input_examples.md`: HWPX 보고서 4종 정규화 예시
- `docs/65_input_normalization_minimal_poc_scope.md`: 입력 정규화 최소 PoC 범위
- `docs/66_input_normalization_poc_result.md`: 입력 정규화 PoC 결과
- `docs/67_normalized_to_hwpx_payload_mapping_scope.md`: 정규화 결과와 HWPX 렌더러 입력 매핑 범위
- `docs/68_hwpx_payload_mapper_poc_result.md`: HWPX payload mapper PoC 결과
- `docs/69_hwpx_payload_validation_poc_result.md`: HWPX payload validation PoC 결과
- `docs/70_hwpx_renderer_dry_run_scope.md`: HWPX 렌더러 연결 dry-run 범위
- `docs/71_hwpx_renderer_dry_run_result.md`: HWPX 렌더러 연결 dry-run 결과
- `docs/72_dry_run_artifact_retention_policy.md`: dry-run 결과 보관 정책
- `docs/73_hwpx_render_connection_decision.md`: 실제 HWPX 렌더링 연결 여부 결정
- `docs/74_mapped_one_page_hwpx_render_result.md`: mapped one_page_report HWPX 렌더링 결과
- `docs/75_mapped_project_plan_hwpx_render_result.md`: mapped project_plan HWPX 렌더링 결과
- `docs/76_mapped_result_report_hwpx_render_result.md`: mapped result_report HWPX 렌더링 결과
- `docs/77_mapped_review_report_render_policy.md`: mapped review_report 렌더링 정책
- `docs/78_approved_review_report_dry_run_result.md`: approved review_report dry-run 결과
- `docs/79_mapped_review_report_hwpx_render_result.md`: mapped review_report HWPX 렌더링 결과
- `docs/80_mapped_hwpx_4types_completion_summary.md`: HWPX 4종 mapped 렌더링 완료 요약
- `docs/81_normalizers_regression_test_suite.md`: normalizers 회귀 테스트 묶음
- `docs/82_phase2_minimal_operation_flow.md`: Phase 2 최소 운영 흐름
- `docs/83_phase2_user_input_and_manual_operation_checkpoints.md`: Phase 2 사용자 입력 및 수동 운영 점검표
- `docs/84_hwpx_report_user_input_templates.md`: HWPX 보고서 4종 사용자 입력 템플릿
- `docs/85_normalizers_fixture_expansion_review.md`: normalizers fixture 확장 후보 검토
- `docs/86_missing_fields_rule_improvement_review.md`: missing_fields 생성 규칙 개선 검토
- `docs/87_placeholder_confirmed_values_design_review.md`: placeholder_confirmed_values 도입 검토
- `docs/88_placeholder_pattern_collision_rules.md`: placeholder 형식 판정 및 실제값 충돌 규칙
- `docs/89_placeholder_confirmed_values_code_adoption_decision.md`: placeholder_confirmed_values 코드 도입 여부 재검토
- `docs/90_project_reorganization_after_superpowers.md`: Superpowers 재적용 후 프로젝트 재정비 요약
- `docs/91_placeholder_confirmed_values_helper_result.md`: placeholder_confirmed_values read-only helper 구현 결과
- `docs/92_placeholder_confirmed_values_fixture_schema_review.md`: placeholder_confirmed_values fixture schema 검토
- `docs/93_placeholder_confirmed_values_file_fixture_result.md`: placeholder_confirmed_values 파일 기반 fixture 분리 결과
- `docs/94_placeholder_confirmed_values_normalizer_connection_policy.md`: placeholder_confirmed_values normalizer 연결 정책
- `docs/95_placeholder_confirmed_values_readonly_metadata_schema.md`: placeholder_confirmed_values read-only metadata schema
- `docs/96_placeholder_confirmed_values_metadata_retention_decision.md`: placeholder_confirmed_values metadata 유지 결정
- `docs/97_phase2_minimal_poc_checkpoint.md`: Phase 2 최소 PoC checkpoint
- `docs/98_phase2_manual_rehearsal_runbook.md`: Phase 2 수동 리허설 runbook
- `docs/99_phase2_manual_rehearsal_result.md`: Phase 2 수동 리허설 실행 결과
- `docs/100_phase2_repeat_operation_criteria.md`: Phase 2 반복 운영 기준
- `docs/101_phase2_repeat_operation_log_template.md`: Phase 2 반복 운영 로그 템플릿
- `docs/102_fixture_expansion_decision_after_repeat_run.md`: fixture 확장 후보 재검토 결과
- `docs/103_missing_fields_rule_decision_after_helper.md`: missing_fields 생성 규칙 재검토 결과
- `docs/104_missing_fields_user_display_guidance.md`: missing_fields 사용자 확인 표시 기준
- `docs/105_missing_fields_repeat_log_reflection_result.md`: missing_fields 반복 운영 로그 반영 결과
- `docs/106_missing_fields_manual_operation_checkpoints_reflection.md`: missing_fields 수동 운영 점검표 반영 결과
- `docs/107_missing_fields_phase2_docs_integrated_review.md`: missing_fields Phase 2 운영 문서 통합 점검
- `docs/108_phase2_operating_docs_final_review.md`: Phase 2 운영 문서 최종 정리
- `docs/109_normalizers_regression_recheck_result.md`: normalizers 회귀 테스트 재검증 결과
- `docs/110_phase2_closeout_and_phase3_entry_decision.md`: Phase 2 마무리 판단 및 Phase 3 진입 조건 결정
- `docs/111_phase3_entry_safety_gate.md`: Phase 3 진입 조건 및 안전 게이트
- `docs/112_phase3_external_hwpx_and_manual_preview_criteria.md`: Phase 3 저장소 밖 HWPX 취급 및 수동 preview 기준
- `docs/113_phase3_state_stop_repeat_docs_reflection.md`: Phase 3 상태별 중단 기준 반복 운영 문서 반영 결과
- `docs/114_phase3_operating_docs_integrated_review.md`: Phase 3 운영 문서 통합 점검
- `docs/115_phase3_external_integration_hold_criteria.md`: Phase 3 외부 연동 필요성과 보류 기준
- `docs/116_phase3_log_and_audit_trace_criteria.md`: Phase 3 로그와 감사 추적 기준
- `docs/117_phase3_test_account_and_test_data_criteria.md`: Phase 3 테스트 계정과 테스트 데이터 기준
- `docs/118_phase3_source_blocking_and_deidentified_input_check_procedure.md`: Phase 3 실제 원문 차단과 비식별 입력 확인 절차
- `docs/119_phase3_user_preview_and_human_approval_integration.md`: Phase 3 사용자 preview와 사람 승인 지점 통합 기준
- `docs/120_phase3_no_send_dry_run_criteria.md`: Phase 3 외부 전송 없는 no-send dry-run 기준
- `docs/121_phase3_external_integration_scope_approval_judgment.md`: Phase 3 외부 연동 구현 범위 승인 판단
- `docs/122_phase3_closeout_and_phase4_entry_decision.md`: Phase 3 마무리 판단 및 Phase 4 진입 여부 결정
- `docs/123_phase4_template_stabilization_entry_judgment.md`: Phase 4 문서 템플릿 안정화 진입 판단
- `docs/124_project_direction_and_legacy_update_review.md`: 프로젝트 방향 재확인 및 구형 문서 업데이트 검토
- `docs/125_hwpx_template_manifest_placeholder_consistency_review.md`: HWPX template manifest와 공통 placeholder 정합성 점검
- `docs/126_style_profile_confirmation_value_collection_criteria.md`: style profile 확인 필요 값 유지 기준과 서식값 수집 체크리스트 점검
- `docs/127_hwpx_manual_preview_gap_log_criteria.md`: HWPX 보고서 4종 수동 preview 서식 gap log 기준
- `docs/128_external_hwpx_candidate_manual_procedure_and_hold_criteria.md`: 저장소 밖 실제 양식 후보 수동 절차와 보류 조건
- `docs/129_local_template_gitignore_repeat_verification_criteria.md`: local template policy와 Git 제외 상태 반복 검증 기준
- `docs/130_phase4_template_stabilization_integrated_review.md`: Phase 4 문서 템플릿 안정화 통합 점검
- `docs/131_actual_hwpx_manual_rehearsal_user_confirmation_packet.md`: 실제 양식 수동 리허설 사용자 확인 패킷
- `docs/132_actual_hwpx_manual_rehearsal_readiness_confirmation.md`: 실제 양식 수동 리허설 준비 확인 결과
- `docs/133_hwpx_only_table_frame_decision.md`: HWPX 일원화와 표 틀 우선 결정
- `docs/134_actual_hwpx_manual_rehearsal_no_copy_hold.md`: 실제 양식 수동 리허설 복사본 없음 보류 기록
- `docs/135_hwp_report_and_hancell_table_data_scope.md`: HWPX 보고서와 Excel/한셀 표 데이터 역할 분리 범위
- `docs/136_table_data_candidate_user_input_display_criteria.md`: HWPX 보고서 사용자 입력 템플릿의 표 데이터 후보 표시 기준
- `docs/137_report_sample_json_table_data_candidate_review.md`: 보고서 샘플 JSON 표 데이터 후보 표시 반영 검토
- `docs/138_renderer_normalizer_table_data_candidate_scope_review.md`: renderer와 normalizer 안내 문서의 표 데이터 후보 오해 가능성 점검
- `docs/139_minimum_demo_run_result.md`: 최소 demo 실행 결과 요약
- `docs/140_user_operation_atoz_guide.md`: 사용자가 직접 해야 하는 일과 Codex가 처리할 일을 구분한 A-to-Z 운영 안내
- `docs/141_user_rehearsal_prompt_examples.md`: 실제값 없이 따라 할 수 있는 문서 유형별 비식별 요청 예시
- `docs/142_user_guidance_integrated_review.md`: 사용자 안내 3종 통합 점검
- `docs/143_user_quick_start.md`: 처음 볼 순서와 멈출 지점을 줄인 사용자 quick start
- `docs/144_quick_start_rehearsal_boundary.md`: 문서만으로 가능한 확인과 HWPX 열람 필요 지점 분리
- `docs/145_user_guidance_closeout.md`: 사용자 안내 묶음 closeout
- `docs/146_next_manual_preview_or_rehearsal_decision.md`: 실제 HWPX 수동 preview 또는 문서 기반 리허설 유지 판단
- `docs/147_document_only_user_rehearsal_result.md`: 실제 HWPX 없는 문서 기반 사용자 리허설 결과
- `docs/148_document_only_rehearsal_closeout.md`: 문서 기반 리허설 closeout
- `docs/149_document_only_rehearsal_hold_state.md`: 비식별 작업 복사본 준비 전 문서 기반 리허설 hold 상태
- `docs/150_manual_preview_resume_gate.md`: 수동 preview 재개 조건 게이트
- `docs/151_manual_preview_resume_gate_closeout.md`: 수동 preview 재개 게이트 검증 closeout
- `docs/152_project_result_artifact_map.md`: 현재 확인 가능한 결과물 지도
- `docs/153_project_result_artifact_map_review.md`: 결과물 지도와 주요 진입점 정합성 점검
- `docs/154_user_visible_artifact_bundle_closeout.md`: 사용자가 바로 볼 수 있는 산출물 묶음 closeout
- `docs/155_legacy_next_step_language_review.md`: 구형 다음 단계 문구 점검
- `docs/156_user_visible_artifact_security_and_git_check.md`: 사용자 가시 산출물 묶음 보안ㆍGit 제외 검증
- `docs/157_current_status_progress_review.md`: CURRENT_STATUS 진행률 점검
- `docs/158_hwpx_autofill_conversion_adoption_review.md`: HWPX 자동 채우기 외부 자료 채택 검토
- `docs/159_external_tool_isolation_and_conflict_policy.md`: 외부 도구 격리와 충돌 방지 기준
- `docs/160_external_skills_conflict_and_modernization_review.md`: 외부 skill 충돌 점검과 구현 전환 검토
- `prompts/`: GPT 프롬프트와 대화 시작 문구
- `examples/`: 안전한 요청, 제한 요청, 모범 출력 예시
- `examples/json/README.md`: 렌더러 검증용 JSON 샘플 안내
- [비식별 문체 샘플 작성 템플릿](templates/deidentified_sample_template.md)
- `templates/hwpx/template_manifest.md`: HWPX 템플릿 manifest
- `templates/hwpx/local_template_policy.md`: HWPX 로컬 템플릿 보관 정책
- `templates/hwpx/style_profile_manifest.md`: HWPX style profile manifest
- `checklists/phase1_completion_checklist.md`: 1단계 완료 체크리스트
- `checklists/security_review_checklist.md`: 보안 검토 체크리스트
- `checklists/before_automation_checklist.md`: 자동화 전 체크리스트
- `checklists/custom_gpt_manual_test_checklist.md`: Custom GPT 수동 테스트 체크리스트
- `checklists/codex_second_review_checklist.md`: Codex 2차 검수 체크리스트
- `checklists/source_document_review_checklist.md`: 원천 문서 검토 체크리스트
- `checklists/deidentification_review_checklist.md`: 비식별화 검토 체크리스트
- `checklists/knowledge_candidate_checklist.md`: Knowledge 후보 체크리스트
- `checklists/poc_implementation_readiness_checklist.md`: PoC 구현 준비 체크리스트
- `checklists/sample_json_validation_checklist.md`: 샘플 JSON 검수 체크리스트
- `checklists/local_poc_integration_checklist.md`: 로컬 PoC 통합 검수 체크리스트
- `checklists/hwpx_style_fidelity_checklist.md`: HWPX 서식 충실도 체크리스트
- `checklists/official_document_language_checklist.md`: 공공기관 문체 체크리스트
- `checklists/hwpx_placeholder_template_review_checklist.md`: HWPX placeholder 템플릿 검수 체크리스트
- `checklists/hwpx_minimal_poc_approval_checklist.md`: HWPX 최소 PoC 구현 승인 체크리스트
- `checklists/hwpx_test_template_safety_checklist.md`: HWPX 테스트 템플릿 안전 체크리스트
- `checklists/hwpx_rendered_output_manual_review_checklist.md`: HWPX 렌더링 결과 수동 검수 체크리스트
- `checklists/hwpx_institution_style_value_collection_checklist.md`: HWPX 기관 표준 서식값 수집 체크리스트
- `checklists/report_sample_json_validation_checklist.md`: 보고서 샘플 JSON 검수 체크리스트
- `checklists/one_page_report_hwpx_template_checklist.md`: 원페이지 보고서 HWPX 템플릿 검수 체크리스트
- `checklists/real_hwpx_template_intake_checklist.md`: 실제 HWPX 양식 투입 전 체크리스트
- `checklists/external_hwpx_placeholder_conversion_checklist.md`: 저장소 밖 HWPX placeholder 변환 체크리스트
- `checklists/hwpx_report_input_requirements_checklist.md`: HWPX 보고서 입력 요구사항 체크리스트
- `checklists/input_normalization_schema_checklist.md`: 입력 정규화 스키마 체크리스트
- `checklists/security_filter_requirements_checklist.md`: 보안 필터 요구사항 체크리스트
- `checklists/input_normalization_test_cases_checklist.md`: 입력 정규화 테스트 케이스 체크리스트
- `checklists/hwpx_report_normalized_input_examples_checklist.md`: HWPX 보고서 정규화 예시 체크리스트
- `checklists/input_normalization_minimal_poc_scope_checklist.md`: 입력 정규화 최소 PoC 범위 체크리스트
- `checklists/input_normalization_poc_result_checklist.md`: 입력 정규화 PoC 결과 체크리스트
- `checklists/normalized_to_hwpx_payload_mapping_scope_checklist.md`: 정규화 결과와 HWPX payload 매핑 범위 체크리스트
- `checklists/hwpx_payload_mapper_poc_result_checklist.md`: HWPX payload mapper PoC 결과 체크리스트
- `checklists/hwpx_payload_validation_poc_result_checklist.md`: HWPX payload validation PoC 결과 체크리스트
- `checklists/hwpx_renderer_dry_run_scope_checklist.md`: HWPX 렌더러 연결 dry-run 범위 체크리스트
- `checklists/hwpx_renderer_dry_run_result_checklist.md`: HWPX 렌더러 연결 dry-run 결과 체크리스트
- `checklists/dry_run_artifact_retention_policy_checklist.md`: dry-run 결과 보관 정책 체크리스트
- `checklists/hwpx_render_connection_decision_checklist.md`: 실제 HWPX 렌더링 연결 여부 체크리스트
- `checklists/mapped_one_page_hwpx_render_result_checklist.md`: mapped one_page_report HWPX 렌더링 결과 체크리스트
- `checklists/mapped_project_plan_hwpx_render_result_checklist.md`: mapped project_plan HWPX 렌더링 결과 체크리스트
- `checklists/mapped_result_report_hwpx_render_result_checklist.md`: mapped result_report HWPX 렌더링 결과 체크리스트
- `checklists/mapped_review_report_render_policy_checklist.md`: mapped review_report 렌더링 정책 체크리스트
- `checklists/approved_review_report_dry_run_result_checklist.md`: approved review_report dry-run 결과 체크리스트
- `checklists/mapped_review_report_hwpx_render_result_checklist.md`: mapped review_report HWPX 렌더링 결과 체크리스트
- `checklists/mapped_hwpx_4types_completion_checklist.md`: HWPX 4종 mapped 렌더링 완료 체크리스트
- `checklists/normalizers_regression_test_suite_checklist.md`: normalizers 회귀 테스트 묶음 체크리스트
- `checklists/phase2_minimal_operation_flow_checklist.md`: Phase 2 최소 운영 흐름 체크리스트
- `checklists/phase2_user_input_and_manual_operation_checklist.md`: Phase 2 사용자 입력 및 수동 운영 체크리스트
- `checklists/hwpx_report_user_input_templates_checklist.md`: HWPX 보고서 사용자 입력 템플릿 체크리스트
- `checklists/normalizers_fixture_expansion_review_checklist.md`: normalizers fixture 확장 후보 검토 체크리스트
- `checklists/missing_fields_rule_improvement_review_checklist.md`: missing_fields 생성 규칙 개선 검토 체크리스트
- `checklists/placeholder_confirmed_values_design_review_checklist.md`: placeholder_confirmed_values 도입 검토 체크리스트
- `checklists/placeholder_pattern_collision_rules_checklist.md`: placeholder 형식 및 충돌 규칙 체크리스트
- `checklists/placeholder_confirmed_values_code_adoption_decision_checklist.md`: placeholder_confirmed_values 코드 도입 여부 체크리스트
- `checklists/project_reorganization_after_superpowers_checklist.md`: 프로젝트 재정비 검수 체크리스트
- `checklists/placeholder_confirmed_values_helper_result_checklist.md`: placeholder_confirmed_values helper 구현 결과 체크리스트
- `checklists/placeholder_confirmed_values_fixture_schema_review_checklist.md`: placeholder_confirmed_values fixture schema 검토 체크리스트
- `checklists/placeholder_confirmed_values_file_fixture_result_checklist.md`: placeholder_confirmed_values 파일 기반 fixture 분리 체크리스트
- `checklists/placeholder_confirmed_values_normalizer_connection_policy_checklist.md`: placeholder_confirmed_values normalizer 연결 정책 체크리스트
- `checklists/placeholder_confirmed_values_readonly_metadata_schema_checklist.md`: placeholder_confirmed_values read-only metadata schema 체크리스트
- `checklists/placeholder_confirmed_values_metadata_retention_decision_checklist.md`: placeholder_confirmed_values metadata 유지 결정 체크리스트
- `checklists/phase2_minimal_poc_checkpoint_checklist.md`: Phase 2 최소 PoC checkpoint 체크리스트
- `checklists/phase2_manual_rehearsal_runbook_checklist.md`: Phase 2 수동 리허설 runbook 체크리스트
- `checklists/phase2_manual_rehearsal_result_checklist.md`: Phase 2 수동 리허설 실행 결과 체크리스트
- `checklists/phase2_repeat_operation_criteria_checklist.md`: Phase 2 반복 운영 기준 체크리스트
- `checklists/phase2_repeat_operation_log_template_checklist.md`: Phase 2 반복 운영 로그 템플릿 체크리스트
- `checklists/fixture_expansion_decision_after_repeat_run_checklist.md`: fixture 확장 후보 재검토 결과 체크리스트
- `checklists/missing_fields_rule_decision_after_helper_checklist.md`: missing_fields 생성 규칙 재검토 결과 체크리스트
- `checklists/missing_fields_user_display_guidance_checklist.md`: missing_fields 사용자 확인 표시 기준 체크리스트
- `checklists/missing_fields_repeat_log_reflection_result_checklist.md`: missing_fields 반복 운영 로그 반영 결과 체크리스트
- `checklists/missing_fields_manual_operation_checkpoints_reflection_checklist.md`: missing_fields 수동 운영 점검표 반영 결과 체크리스트
- `checklists/missing_fields_phase2_docs_integrated_review_checklist.md`: missing_fields Phase 2 운영 문서 통합 점검 체크리스트
- `checklists/phase2_operating_docs_final_review_checklist.md`: Phase 2 운영 문서 최종 정리 체크리스트
- `checklists/user_operation_atoz_rehearsal_checklist.md`: 사용자 운영 A-to-Z 리허설 체크리스트
- `checklists/manual_preview_resume_gate_checklist.md`: 수동 preview 재개 게이트 체크리스트
- `checklists/normalizers_regression_recheck_result_checklist.md`: normalizers 회귀 테스트 재검증 결과 체크리스트
- `checklists/phase2_closeout_and_phase3_entry_decision_checklist.md`: Phase 2 마무리 판단 및 Phase 3 진입 조건 결정 체크리스트
- `checklists/phase3_entry_safety_gate_checklist.md`: Phase 3 진입 조건 및 안전 게이트 체크리스트
- `checklists/phase3_external_hwpx_manual_preview_checklist.md`: Phase 3 저장소 밖 HWPX 취급 및 수동 preview 체크리스트
- `checklists/phase3_state_stop_repeat_docs_reflection_checklist.md`: Phase 3 상태별 중단 기준 반복 운영 문서 반영 체크리스트
- `checklists/phase3_operating_docs_integrated_review_checklist.md`: Phase 3 운영 문서 통합 점검 체크리스트
- `checklists/phase3_external_integration_hold_criteria_checklist.md`: Phase 3 외부 연동 필요성과 보류 기준 체크리스트
- `checklists/phase3_log_and_audit_trace_criteria_checklist.md`: Phase 3 로그와 감사 추적 기준 체크리스트
- `checklists/phase3_test_account_and_test_data_criteria_checklist.md`: Phase 3 테스트 계정과 테스트 데이터 기준 체크리스트
- `checklists/phase3_source_blocking_and_deidentified_input_checklist.md`: Phase 3 실제 원문 차단과 비식별 입력 확인 체크리스트
- `checklists/phase3_user_preview_and_human_approval_integration_checklist.md`: Phase 3 사용자 preview와 사람 승인 지점 통합 체크리스트
- `checklists/phase3_no_send_dry_run_criteria_checklist.md`: Phase 3 외부 전송 없는 no-send dry-run 기준 체크리스트
- `checklists/phase3_external_integration_scope_approval_judgment_checklist.md`: Phase 3 외부 연동 구현 범위 승인 판단 체크리스트
- `checklists/phase3_closeout_and_phase4_entry_decision_checklist.md`: Phase 3 마무리 판단 및 Phase 4 진입 여부 결정 체크리스트
- `checklists/phase4_template_stabilization_entry_judgment_checklist.md`: Phase 4 문서 템플릿 안정화 진입 판단 체크리스트
- `checklists/project_direction_and_legacy_update_review_checklist.md`: 프로젝트 방향 재확인 및 구형 문서 업데이트 검토 체크리스트
- `checklists/hwpx_template_manifest_placeholder_consistency_checklist.md`: HWPX template manifest와 공통 placeholder 정합성 체크리스트
- `checklists/style_profile_confirmation_value_collection_checklist.md`: style profile 확인 필요 값 유지와 서식값 수집 기준 체크리스트
- `checklists/hwpx_manual_preview_gap_log_checklist.md`: HWPX 수동 preview 서식 gap log 체크리스트
- `checklists/external_hwpx_candidate_manual_procedure_checklist.md`: 저장소 밖 실제 양식 후보 수동 절차 체크리스트
- `checklists/local_template_gitignore_repeat_verification_checklist.md`: local template policy와 Git 제외 상태 반복 검증 체크리스트
- `checklists/phase4_template_stabilization_integrated_review_checklist.md`: Phase 4 문서 템플릿 안정화 통합 점검 체크리스트
- `checklists/actual_hwpx_manual_rehearsal_user_confirmation_packet_checklist.md`: 실제 양식 수동 리허설 사용자 확인 패킷 체크리스트
- `checklists/actual_hwpx_manual_rehearsal_readiness_confirmation_checklist.md`: 실제 양식 수동 리허설 준비 확인 결과 체크리스트
- `checklists/hwpx_only_table_frame_decision_checklist.md`: HWPX 일원화와 표 틀 우선 결정 체크리스트
- `checklists/actual_hwpx_manual_rehearsal_no_copy_hold_checklist.md`: 실제 양식 수동 리허설 복사본 없음 보류 체크리스트
- `checklists/hwp_report_and_hancell_table_data_scope_checklist.md`: HWPX 보고서와 Excel/한셀 표 데이터 역할 분리 체크리스트
- `checklists/table_data_candidate_user_input_display_checklist.md`: 표 데이터 후보 사용자 입력 표시 체크리스트
- `checklists/report_sample_json_table_data_candidate_review_checklist.md`: 보고서 샘플 JSON 표 데이터 후보 반영 검토 체크리스트
- `checklists/renderer_normalizer_table_data_candidate_scope_checklist.md`: renderer와 normalizer 표 데이터 후보 범위 점검 체크리스트
- `templates/`: 비식별 샘플, 문서 인벤토리, 문체 명세 작성 템플릿
- `renderers/markdown_renderer/README.md`: Markdown 미리보기 렌더러 안내
- `renderers/email_renderer/README.md`: Email 초안 렌더러 안내
- `renderers/hwpx_renderer/README.md`: HWPX 최소 PoC 렌더러 안내
- `normalizers/README.md`: 입력 정규화 최소 PoC 안내
- `tasks/NEXT_STEP.md`: 다음 작업 목록

## 보안 주의사항

- 비식별화된 업무 지시만 사용합니다.
- 원문 학습이 아니라 서식ㆍ문체ㆍ구조 추출을 목표로 합니다.
- AI는 초안만 작성합니다.
- 사람이 최종 검토ㆍ승인합니다.
- 민감정보가 포함된 경우 처리 제한합니다.
- 확인되지 않은 정보는 `[확인 필요]`로 표시합니다.
- 사람이 직접 판단해야 하는 값은 `[사용자 확인 필요]`로 표시합니다.
- 현재 단계에서 자동화하지 않는 항목은 `[보류]`로 표시합니다.

## 작업 운영 기준

- 파일 또는 폴더 삭제처럼 되돌리기 어려운 작업은 먼저 사용자 확인 지점으로 분리합니다.
- 그 외 문서 보강, 정합성 점검, 보안 검수, Git 제외 검증은 저장소 범위 안에서 Codex가 계속 진행합니다.
- 작은 수정마다 commit/push하지 않고, 여러 관련 수정과 검증을 한 번에 묶는 기준을 우선합니다.
- 아직 push할 만한 기준점이 없으면 보고만 하고 멈추지 않고, 같은 변경 묶음 안에서 다음 추천 작업을 계속 진행합니다.

## 다음 단계

1. `docs/152_project_result_artifact_map.md`에서 현재 확인 가능한 결과물, 사용자 확인 필요 지점, 보류 항목을 먼저 봅니다.
2. `CURRENT_STATUS.md`와 `docs/139_minimum_demo_run_result.md`를 기준으로 현재 작동 확인된 최소 PoC 경로를 봅니다.
3. `docs/143_user_quick_start.md`에서 처음 볼 순서와 멈출 지점을 확인합니다.
4. `docs/144_quick_start_rehearsal_boundary.md`에서 문서만으로 가능한 확인과 HWPX 열람 필요 지점을 분리합니다.
5. `docs/140_user_operation_atoz_guide.md`에서 사용자가 직접 확인할 일과 Codex가 처리할 일을 구분합니다.
6. `docs/141_user_rehearsal_prompt_examples.md`에서 실제값 없는 요청 예시를 확인합니다.
7. `docs/150_manual_preview_resume_gate.md`에서 수동 preview 재개 조건을 확인합니다.
8. `docs/158_hwpx_autofill_conversion_adoption_review.md`에서 외부 HWPX 자동 채우기 자료를 현재 흐름에 어떻게 흡수할지 확인합니다.
9. 실제 HWPX 작업 복사본이 준비되기 전까지 실제 양식 수동 preview는 보류합니다.
10. 한컴 열람과 레이아웃 확인은 `docs/150_manual_preview_resume_gate.md` 조건 충족 후에만 진행합니다.
11. 표가 포함된 양식은 표 내부 값이 아니라 표 위치, 폭, 줄바꿈, 겹침, 여백만 확인합니다.
