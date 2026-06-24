# 현재 시스템 현황판

최종 확인일: 2026-06-24

## 한 줄 결론

이 저장소는 실제 업무 자동화 운영물이 아니라, 비식별 입력을 HWPX 보고서 초안 payload와 renderer dry-run까지 연결하는 로컬 PoC 저장소입니다.

현재 눈으로 확인 가능한 작동 경로는 다음입니다.

```text
비식별 요청 fixture
-> 입력 정규화
-> 보안 필터
-> HWPX payload mapper
-> payload validation
-> HWPX renderer dry-run
```

추가로 저장소 밖 샘플 HWPX에 대해 다음 로컬 PoC 경로가 확인되었습니다.

```text
저장소 밖 샘플 HWPX
-> section XML 분석
-> anchor 후보 탐색
-> anchor 뒤 비식별 초안 문단 주입
-> ignored 로컬 HWPX output 생성
```

실제 업무용 HWPX 산출물 생성, 실제 기관 양식 적용, 실제 이메일/API/Make.com 연동은 현재 단계의 결과물이 아닙니다.

## 전체 프로젝트 진행 도식

```mermaid
flowchart LR
    A["1. 기획ㆍ보안 원칙 정리<br/>완료"] --> B["2. 문서 유형ㆍ샘플 JSON 정리<br/>완료"]
    B --> C["3. HWPX placeholder 렌더러 PoC<br/>보고서 4종 확인"]
    C --> D["4. 입력 정규화ㆍ보안 필터<br/>작동 확인"]
    D --> E["5. HWPX payload mapperㆍvalidation<br/>작동 확인"]
    E --> F["6. renderer dry-run<br/>작동 확인"]
    F --> G["7. 사용자 가시 산출물 정리<br/>완료"]
    G --> H["8. 외부 HWPX 참고자료 채택 검토<br/>문서 기준 완료"]
    H --> I["9. placeholder 없는 샘플 HWPX profile-aware 주입 PoC<br/>작동ㆍ수동 확인"]
    I --> J["10. 실제 양식 안정화<br/>부분 진행ㆍ수동 확인 필요"]
    J --> K["11. 실제 운영 연동<br/>보류"]
```

## 현재 체감 진행률

진행률은 실제 운영 배포 기준이 아니라, 저장소 안에서 확인 가능한 PoC 구축 기준입니다.

| 영역 | 상태 | 체감 진행률 | 설명 |
|---|---|---:|---|
| 프로젝트 목표ㆍ보안 원칙 | 거의 완료 | 90% | 초안 생성 범위, 금지 범위, 비식별 원칙 정리 |
| 문서 유형ㆍ샘플 JSON | 거의 완료 | 85% | 보고서 4종 중심 샘플과 placeholder 구조 확보 |
| HWPX placeholder 렌더러 | 상당 부분 완료 | 80% | 보고서 4종 placeholder 치환과 dry-run 경로 확인 |
| placeholder 없는 샘플 HWPX profile-aware 주입 PoC | 수동 확인 통과 | 85% | 제공 샘플 HWPX 2종에 양식별 5개 anchor 영역 분산 주입, ignored output 생성, 샘플1 겹침 없음과 샘플2 bullet 중복 없음 확인 |
| 입력 정규화ㆍ보안 필터 | 작동 확인 | 75% | fixture 기반 routing, blocked, needs_security_review 확인 |
| payload mapperㆍvalidation | 작동 확인 | 75% | HWPX renderer 입력 형태로 변환 및 검증 가능 |
| 실제 HWPX 양식 안정화 | 진행 중 | 40% | local placeholder 템플릿과 샘플 주입 PoC는 있으나 실제 기관 양식 안정화는 수동 확인 필요 |
| 외부 HWPX 자동 채우기 자료 검토 | 구현 일부 반영 | 75% | 다운로드 skill, 샘플 구조, 저장소 밖 `hwpx-cli`, 내부 샘플 주입 PoC 확인 |
| 외부 도구 격리ㆍ충돌 방지 | 구현ㆍ문서 기준 완료 | 75% | repo 의존성 미추가, skill과 `hwpx-cli` 역할 분리, 내부 Python 구조 분석기 추가 |
| 표 데이터ㆍExcel/한셀 연동 | 후보 분리 | 15% | 지금은 표 틀만 보고, 실제 표 내부 데이터 자동화는 보류 |
| Email/API/Make.com 연동 | 의도적 보류 | 10% | no-send 원칙 유지, 실제 발송/외부 연동 없음 |
| 실제 운영 배포 | 미진입 | 0% | 사람 승인 전 자동 발송ㆍ결재ㆍ집행 없음 |

## 한눈에 보는 현재 위치

```text
[완료]    기획/보안/문체/샘플 JSON
[완료]    HWPX 보고서 4종 placeholder 기반 PoC
[완료]    normalizer -> payload -> validation -> dry-run 확인
[완료]    사용자 가시 산출물 지도/closeout 정리
[완료]    외부 HWPX 자동 채우기 자료 채택 검토
[완료]    외부 도구 격리와 충돌 방지 기준 정리
[완료]    HWPX template 구조 분석 내부 Python PoC
[완료]    placeholder 없는 샘플 HWPX profile-aware 비식별 초안 분산 주입 PoC와 샘플 1/2 수동 확인
[대기]    실제 양식 안정화와 한컴 수동 preview
[보류]    Email/API/Make.com/실제 운영 연동
```

현재 전체 프로젝트는 로컬 PoC 기준으로는 약 75% 수준입니다.

다만 실제 기관 양식 안정화, 실제 운영 화면, 외부 연동, 운영 로그까지 포함한 운영 시스템 기준으로 보면 약 30~35% 수준으로 보는 것이 안전합니다.

## 지금 실제로 되는 것

| 구분 | 현재 상태 | 근거 |
|---|---|---|
| 비식별 입력 정규화 | 작동 확인 | `normalizers/input_normalizer_poc.py` |
| 보안 필터 routing | 작동 확인 | 실제값 의심 fixture는 `blocked`, 보안 검토 필요 fixture는 `needs_security_review` |
| HWPX payload 생성 | 작동 확인 | `one_page_report`, `project_plan`, `result_report`, `review_report` payload 생성 또는 안전 스킵 |
| HWPX payload validation | 작동 확인 | 생성된 payload 4건 validation 통과 |
| HWPX renderer dry-run | 작동 확인 | 렌더링 전 상태 판정, placeholder count, template availability 확인 |
| local placeholder HWPX template 인식 | 작동 확인 | 보고서 4종 template_available `true` |
| placeholder 없는 샘플 HWPX profile-aware 주입 | 수동 확인 통과 | 샘플1은 5개 영역 11개 문단 분산 주입 후 겹침 없음, 샘플2는 5개 영역 12개 문단 분산 주입 후 bullet 중복 없음 |
| 실제값 placeholder 검증 helper | 작동 확인 | safe/invalid fixture 7건 기대 결과 통과 |

## 최근 검증된 실행 결과

| 명령 | 결과 | 증거 파일 |
|---|---|---|
| `python .\normalizers\validate_placeholder_confirmed_values_poc.py` | 7건 통과 | `normalizers/output/placeholder_confirmed_values_summary.json` |
| `python .\normalizers\input_normalizer_poc.py` | fixture 6건 통과 | `normalizers/output/normalization_summary.json` |
| `python .\normalizers\hwpx_payload_mapper_poc.py` | 생성 4건, 안전 스킵 2건 통과 | `normalizers/output/hwpx_payload_mapping_summary.json` |
| `python .\normalizers\validate_hwpx_payload_poc.py` | validation 4건, 안전 스킵 2건 통과 | `normalizers/output/hwpx_payload_validation_summary.json` |
| `python .\normalizers\hwpx_renderer_dry_run_poc.py` | dry-run ready 2건, missing_fields 포함 ready 2건, 안전 스킵 2건 | `normalizers/output/hwpx_renderer_dry_run_summary.json` |
| `python .\normalizers\render_mapped_hwpx_poc.py` | ignored 로컬 PoC HWPX 4건 렌더링 | `normalizers/output/mapped_hwpx_render_summary.json` |
| `python .\normalizers\test_hwpx_template_structure_analyzer_poc.py` | 테스트 4건 통과 | 콘솔 출력 |
| `python .\normalizers\hwpx_template_structure_analyzer_poc.py` | local template 후보 4종 구조 분석 | `normalizers/output/hwpx_template_structure_summary.json` |
| `python .\renderers\hwpx_renderer\test_autofill_package.py` | 테스트 15건 통과 | 콘솔 출력 |
| `python .\renderers\hwpx_renderer\render_autofill_batch_poc.py --topic [비식별 주제]` | 샘플 HWPX 2종 profile-aware ignored output 생성 | `renderers/hwpx_renderer/output/autofill_profile_sample*_latest.hwpx` |
| `python .\renderers\hwpx_renderer\render_autofill_batch_poc.py [비식별 주제]` | `--topic` 없이 주제만 넣어 샘플 HWPX 2종 생성 가능 | 콘솔 출력 |
| `python .\renderers\hwpx_renderer\render_autofill_regression_poc.py` | 비식별 주제 4개 x 샘플 2종, 총 8건 생성 통과 | `renderers/hwpx_renderer/output/regression/autofill_regression_summary.json` |
| `python .\normalizers\hwpx_template_structure_analyzer_poc.py --template [원본] --template [output] --no-output` | 샘플1 문단 179→190ㆍ표 13→13, 샘플2 문단 44→56ㆍ표 2→2 | 콘솔 출력 |

## dry-run에서 확인된 문서 유형

| 문서 유형 | fixture | dry-run 상태 | template |
|---|---|---|---|
| `one_page_report` | `safe_one_page_report_request.json` | `dry_run_ready` | `templates\hwpx\placeholder_one_page_report.hwpx` |
| `project_plan` | `missing_project_plan_request.json` | `dry_run_ready_with_missing_fields` | `templates\hwpx\placeholder_project_plan.hwpx` |
| `result_report` | `missing_result_report_request.json` | `dry_run_ready_with_missing_fields` | `templates\hwpx\placeholder_result_report.hwpx` |
| `review_report` | `approved_review_report_request.json` | `dry_run_ready` | `templates\hwpx\placeholder_review_report.hwpx` |

## 안전하게 멈추는 것

| 입력 상태 | 처리 결과 |
|---|---|
| 실제값 또는 금지 자동화 요청 의심 | `blocked`, payload 미생성 |
| 보안 검토 필요하지만 placeholder 렌더링 승인 없음 | `needs_security_review`, payload 미생성 |
| 필수값 미확정 | `needs_more_input`, placeholder와 missing_fields 유지 |
| 실제 HWPX 원본 또는 실제 업무 자료 없음 | 실제 양식 수동 preview 보류 |

## 아직 결과물이 아닌 것

- 실제 기관 HWPX/HWP 원본 기반 자동 렌더링
- 실제 업무 문서 원문 기반 초안
- 실제 개인정보, 문서번호, 기관명, 담당자명, 수신자명 포함 샘플
- 실제 업무용 HWPX 산출물 생성 및 배포
- Email, API, Make.com, Gmail, Outlook 실제 연동
- HWPX 표 내부 실제 데이터 자동 입력
- placeholder 없는 실제 기관 양식의 표/본문 영역별 자동 재배치
- Excel/한셀 파일 자동 생성 또는 연동

## 지금 기준으로 볼 수 있는 결과물

- `CURRENT_STATUS.md`: 현재 시스템 현황판
- `docs/139_minimum_demo_run_result.md`: 최소 demo 실행 결과 요약
- `docs/140_user_operation_atoz_guide.md`: 사용자 운영 A-to-Z 안내와 HWPX 열람 전 재개 게이트 확인 기준
- `docs/141_user_rehearsal_prompt_examples.md`: 문서 유형별 비식별 요청 예시
- `docs/142_user_guidance_integrated_review.md`: 사용자 안내 3종 통합 점검
- `docs/143_user_quick_start.md`: 사용자 quick start와 HWPX 열람 전 재개 게이트 확인 순서
- `docs/144_quick_start_rehearsal_boundary.md`: 문서만으로 가능한 리허설과 게이트 이후 HWPX 열람 필요 지점 분리
- `docs/145_user_guidance_closeout.md`: 사용자 안내 묶음 closeout
- `docs/146_next_manual_preview_or_rehearsal_decision.md`: 수동 preview 또는 문서 기반 리허설 유지 판단
- `docs/147_document_only_user_rehearsal_result.md`: 실제 HWPX 없는 문서 기반 사용자 리허설 결과
- `docs/148_document_only_rehearsal_closeout.md`: 문서 기반 리허설 closeout
- `docs/149_document_only_rehearsal_hold_state.md`: 비식별 작업 복사본 준비 전 문서 기반 리허설 hold 상태
- `docs/150_manual_preview_resume_gate.md`: 수동 preview 재개 조건 게이트
- `docs/151_manual_preview_resume_gate_closeout.md`: 수동 preview 재개 게이트 검증 closeout
- `docs/152_project_result_artifact_map.md`: 현재 확인 가능한 결과물 지도
- `docs/153_project_result_artifact_map_review.md`: 결과물 지도와 주요 진입점 정합성 점검
- `docs/154_user_visible_artifact_bundle_closeout.md`: 사용자가 바로 볼 수 있는 산출물 묶음과 재개 게이트 기준 closeout
- `docs/155_legacy_next_step_language_review.md`: 구형 다음 단계 문구 점검
- `docs/156_user_visible_artifact_security_and_git_check.md`: 사용자 가시 산출물 묶음 보안ㆍGit 제외 검증
- `docs/157_current_status_progress_review.md`: CURRENT_STATUS 진행률 점검
- `docs/158_hwpx_autofill_conversion_adoption_review.md`: HWPX 자동 채우기 외부 자료 채택 검토
- `docs/159_external_tool_isolation_and_conflict_policy.md`: 외부 도구 격리와 충돌 방지 기준
- `docs/160_external_skills_conflict_and_modernization_review.md`: 외부 skill 충돌 점검과 구현 전환 검토
- `checklists/user_operation_atoz_rehearsal_checklist.md`: A-to-Z 안내 기준 사용자 리허설 체크리스트
- `checklists/manual_preview_resume_gate_checklist.md`: 수동 preview 재개 게이트 체크리스트
- `normalizers/output/*summary.json`: 최근 dry-run과 검증 요약
- `examples/json/sample_*_report.json`: 보고서 4종 placeholder 샘플 JSON
- `normalizers/`: 입력 정규화, 보안 필터, payload mapper, dry-run PoC
- `renderers/hwpx_renderer/`: HWPX placeholder 렌더러와 placeholder-free profile-aware 샘플 주입 PoC
- `templates/hwpx/`: 로컬 placeholder HWPX 템플릿 보관 위치

## 사용자 확인이 필요한 지점

아래 항목은 Codex가 대신 확정하지 않습니다.

1. 실제 기관 양식을 사용할지 여부
2. 실제 양식을 사용할 경우 저장소 밖에서 비식별 작업 복사본을 만들었는지 여부
3. 한컴에서 열었을 때 글자 겹침, 줄바꿈, 표 폭, 여백이 실제 업무용으로 acceptable한지 여부
4. 기관 표준 글꼴, 자간, 줄간격, 문단 간격 값
5. 표 내부 데이터 자동화를 Excel/한셀 연동 후보로 별도 진행할지 여부

## 사용자 입력 역할 구분

현재 사용자 입력과 반복 운영 로그는 다음 세 표시를 사용합니다.

| 표시 | 의미 | 처리 기준 |
|---|---|---|
| `[사용자 확인 필요]` | 사람이 직접 판단하거나 확인해야 하는 값 | Codex가 임의 작성하지 않음 |
| `[Codex 처리 가능]` | 비식별 placeholder 입력으로 구조화 가능한 항목 | 초안 구조화, 누락값 목록화, 보안 주의문구 정리 가능 |
| `[보류]` | 현재 단계에서 자동화하지 않는 항목 | 실제 HWPX 원본, 실제 표 데이터, 외부 연동은 실행하지 않음 |

## 앞으로의 작업 방식

- 매번 commit/push용 문서만 늘리지 않고, 실행 가능한 PoC 결과 또는 사용자 확인 가능한 산출물이 있을 때 묶어서 진행합니다.
- `p` 또는 `P`는 push 완료 후 다음 추천 작업 진행 요청으로 해석합니다.
- 앞으로 진행상황을 보고할 때는 전체 진행 도식과 단계별 진행률 요약을 함께 보여줍니다.
- 앞으로는 관련 추천 작업을 최대한 묶어서 진행하고, commit/push 판단은 단계 완료나 의미 있는 검증 묶음이 생겼을 때만 정리합니다.
- closeout 하나 또는 작은 문구 정리만으로는 멈추지 않고, 다음 추천 작업까지 묶어서 진행합니다.
- 5분 단위의 작은 확인이나 단일 문구 정리 때문에 매번 멈추지 않고, 같은 단계 안의 여러 소작업을 하나의 변경 묶음으로 모읍니다.
- 파일 또는 폴더 삭제처럼 되돌리기 어려운 작업 외에는 Codex가 저장소 범위 안에서 계속 진행합니다.
- commit/push는 여러 관련 수정과 검증을 모아 한 번에 처리하는 기준을 우선합니다.
- push할 기준점이 아직 없으면 보고만 하고 멈추지 않고, 같은 변경 묶음 안에서 다음 추천 작업을 이어갑니다.
- 사용자가 직접 확인해야 하는 항목은 `[사용자 확인 필요]`로 명확히 표시합니다.
- 실제 업무용 HWPX 산출물, local template, output 파일은 Git에 올리지 않는 원칙을 유지합니다.

## 다음 추천 단계

1. `docs/152_project_result_artifact_map.md` 기준으로 현재 확인 가능한 결과물과 보류 항목을 먼저 확인합니다.
2. `docs/143_user_quick_start.md` 기준으로 처음 볼 순서와 멈출 지점을 확인합니다.
3. `docs/144_quick_start_rehearsal_boundary.md` 기준으로 문서만으로 가능한 확인과 재개 게이트 이후 HWPX 열람 필요 지점을 분리합니다.
4. `docs/140_user_operation_atoz_guide.md` 기준으로 사용자가 직접 확인할 지점을 봅니다.
5. `checklists/user_operation_atoz_rehearsal_checklist.md` 기준으로 실제 HWPX 없이도 현재 단계 확인을 리허설합니다.
6. `docs/141_user_rehearsal_prompt_examples.md` 기준으로 실제값 없는 요청 예시를 사용합니다.
7. `docs/150_manual_preview_resume_gate.md` 기준으로 수동 preview 재개 조건을 확인합니다.
8. 실제 HWPX 수동 preview는 비식별 작업 복사본이 준비되고 `docs/150_manual_preview_resume_gate.md` 조건이 충족될 때만 재개합니다.
