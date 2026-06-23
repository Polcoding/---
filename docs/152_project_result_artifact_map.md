# 프로젝트 결과물 지도

## 목적

현재 저장소에서 실제로 확인할 수 있는 결과물, 아직 보류 중인 항목, 사용자가 직접 확인해야 하는 지점을 한 페이지에서 찾을 수 있게 정리합니다.

이 문서는 실제 업무 문서 산출물이 아니라, 비식별 placeholder 기반 PoC와 문서 산출물의 위치를 안내하는 지도입니다.

## 한눈에 보는 상태

```text
[확인 가능] 문서/체크리스트/샘플 JSON/PoC 요약
[사용자 확인 필요] 실제 HWPX 열람, 실제 양식 적합성, 기관 서식값
[보류] 실제 원본 처리, 실제 업무용 HWPX output commit, Email/API/Make.com 연동
```

## 먼저 볼 파일

| 목적 | 파일 | 보면 알 수 있는 것 |
|---|---|---|
| 전체 현황 | `CURRENT_STATUS.md` | 현재 작동 경로, 진행률, 보류 항목 |
| 빠른 시작 | `docs/143_user_quick_start.md` | 처음 열 파일과 멈출 지점 |
| 사용자 A-to-Z | `docs/140_user_operation_atoz_guide.md` | 사용자가 직접 할 일과 Codex가 할 일 |
| 최소 demo 결과 | `docs/139_minimum_demo_run_result.md` | normalizer부터 renderer dry-run까지의 요약 |
| 재개 게이트 | `docs/150_manual_preview_resume_gate.md` | 실제 HWPX preview를 다시 시작할 조건 |

## 문서 결과물

| 구분 | 파일 |
|---|---|
| 사용자 안내 통합 점검 | `docs/142_user_guidance_integrated_review.md` |
| quick start 경계 | `docs/144_quick_start_rehearsal_boundary.md` |
| 사용자 안내 closeout | `docs/145_user_guidance_closeout.md` |
| 수동 preview 또는 리허설 유지 판단 | `docs/146_next_manual_preview_or_rehearsal_decision.md` |
| 문서 기반 리허설 결과 | `docs/147_document_only_user_rehearsal_result.md` |
| 문서 기반 리허설 closeout | `docs/148_document_only_rehearsal_closeout.md` |
| 문서 기반 hold 상태 | `docs/149_document_only_rehearsal_hold_state.md` |
| 수동 preview 재개 게이트 | `docs/150_manual_preview_resume_gate.md` |
| 수동 preview 재개 게이트 closeout | `docs/151_manual_preview_resume_gate_closeout.md` |

## 체크리스트 결과물

| 구분 | 파일 |
|---|---|
| 사용자 운영 리허설 | `checklists/user_operation_atoz_rehearsal_checklist.md` |
| 수동 preview 재개 게이트 | `checklists/manual_preview_resume_gate_checklist.md` |
| HWPX 수동 preview gap log 기준 | `checklists/hwpx_manual_preview_gap_log_checklist.md` |
| renderer dry-run 결과 점검 | `checklists/hwpx_renderer_dry_run_result_checklist.md` |
| payload validation 결과 점검 | `checklists/hwpx_payload_validation_poc_result_checklist.md` |

## PoC 코드와 증거

| 단계 | 코드 | 요약 output |
|---|---|---|
| 입력 정규화 | `normalizers/input_normalizer_poc.py` | `normalizers/output/normalization_summary.json` |
| HWPX payload mapping | `normalizers/hwpx_payload_mapper_poc.py` | `normalizers/output/hwpx_payload_mapping_summary.json` |
| HWPX payload validation | `normalizers/validate_hwpx_payload_poc.py` | `normalizers/output/hwpx_payload_validation_summary.json` |
| HWPX renderer dry-run | `normalizers/hwpx_renderer_dry_run_poc.py` | `normalizers/output/hwpx_renderer_dry_run_summary.json` |
| mapped HWPX PoC 렌더링 | `normalizers/render_mapped_hwpx_poc.py` | `normalizers/output/mapped_hwpx_render_summary.json` |
| placeholder confirmed values 검증 | `normalizers/validate_placeholder_confirmed_values_poc.py` | `normalizers/output/placeholder_confirmed_values_summary.json` |

output 요약 파일과 `renderers/hwpx_renderer/output/*.hwpx`는 로컬 검증 산출물이며 Git 제외 상태로 유지합니다.

## 샘플 JSON

| 문서 유형 | 파일 |
|---|---|
| 원페이지 보고서 | `examples/json/sample_one_page_report.json` |
| 추진계획서 | `examples/json/sample_project_plan.json` |
| 결과보고서 | `examples/json/sample_result_report.json` |
| 검토보고서 | `examples/json/sample_review_report.json` |

샘플 JSON은 실제값이 아니라 placeholder 기반 검증 입력입니다.

## 사용자 확인 필요 지점

아래 항목은 Codex가 대신 확정하지 않습니다.

- 실제 기관 양식 사용 여부
- 저장소 밖 비식별 작업 복사본 준비 여부
- 한컴에서 열었을 때 글자 겹침, 줄바꿈, 표 폭, 여백이 적정한지 여부
- 기관 표준 글꼴, 자간, 줄간격, 문단 간격 값
- 표 내부 데이터 자동화를 Excel/한셀 연동 후보로 별도 진행할지 여부

## 보류 항목

현재 단계에서는 다음을 실행하지 않습니다.

- 실제 기관 HWPX/HWP 원본 Git 추가
- 실제 업무용 HWPX output commit
- 실제 업무 원문 처리
- 실제 개인정보, 문서번호, 기관명, 담당자명 기록
- 실제 표 데이터, 수량, 금액, 대상 목록 기록
- Email/API/Make.com/Gmail/Outlook 실제 연동
- 실제 자동 발송, 결재, 계약, 업체 선정, 예산 집행

## push 빈도

이 지도는 현재 결과물 확인성을 높이기 위한 문서입니다.

작은 문서 하나가 추가될 때마다 멈추지 않고, 결과물 지도와 주요 진입점 정합성까지 함께 확인한 뒤 commit/push 여부를 판단합니다.

## 다음 추천

결과물 지도와 `README.md`, `CURRENT_STATUS.md`, `AGENTS.md`, `tasks/NEXT_STEP.md`의 정합성 점검은 `docs/153_project_result_artifact_map_review.md`에 이미 정리했습니다.

현재 추천은 결과물 지도를 최신 진입점으로 유지하고, 실제 HWPX 수동 preview는 비식별 작업 복사본 준비가 명시될 때만 재개하는 것입니다.
