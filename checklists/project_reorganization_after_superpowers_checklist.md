# Superpowers 재적용 후 프로젝트 재정비 체크리스트

## 목적

`docs/90_project_reorganization_after_superpowers.md` 기준으로 프로젝트 진입점과 다음 작업 방향이 최신 상태로 정리되었는지 확인합니다.

## 기준 파일 확인

| 완료 | 항목 |
|---|---|
| [x] | `AGENTS.md`가 Phase 2 최소 PoC 상태를 반영하는가 |
| [x] | `README.md`가 현재 단계와 다음 작업을 반영하는가 |
| [x] | `docs/00_project_overview.md`가 최신 다음 단계를 반영하는가 |
| [x] | `docs/00_chatgpt_handoff.md`가 최신 완료 상태를 반영하는가 |
| [x] | `renderers/README.md`가 실제 PoC 렌더러 존재 상태와 충돌하지 않는가 |
| [x] | `tasks/NEXT_STEP.md`가 다음 작업을 명확히 가리키는가 |

## 방향성 확인

| 완료 | 항목 |
|---|---|
| [x] | HWPX 보고서 4종 우선순위를 유지했는가 |
| [x] | Email과 XLSX가 보조 대상임을 유지했는가 |
| [x] | Phase 2가 API/Make.com/Email 자동화가 아님을 명시했는가 |
| [x] | `placeholder_confirmed_values` 다음 작업이 read-only helper로 제한되었는가 |
| [x] | `missing_fields`와 routing 결과를 즉시 바꾸지 않는 원칙을 유지했는가 |

## 보안 검수

| 완료 | 항목 |
|---|---|
| [x] | 실제 개인정보를 추가하지 않았는가 |
| [x] | 실제 기관명, 업체명, 담당자명을 추가하지 않았는가 |
| [x] | 실제 문서번호, 민원번호, 사건번호를 추가하지 않았는가 |
| [x] | 실제 공문 원문 또는 보고서 원문을 추가하지 않았는가 |
| [x] | 실제 HWPX 원본 파일을 추가하지 않았는가 |
| [x] | API, Make.com, Email 자동화 코드를 추가하지 않았는가 |

## 다음 단계 판단

| 완료 | 항목 |
|---|---|
| [x] | 다음 작업으로 read-only 판정 helper 최소 구현을 진행할 수 있는가 |
| [x] | 기존 fixture 회귀 테스트를 다음 작업 완료 조건으로 둘 수 있는가 |
| [x] | 로컬 HWPX template/output Git 제외 원칙을 유지할 수 있는가 |
