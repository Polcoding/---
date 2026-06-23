# HWPX 렌더러 연결 dry-run 범위 체크리스트

## 목적

`docs/70_hwpx_renderer_dry_run_scope.md`가 실제 업무용 HWPX 생성 없이 안전한 연결 검증 범위를 정했는지 확인합니다.

## 범위 확인

| 완료 | 항목 |
|---|---|
| [x] | 실제 HWPX 파일을 생성하지 않는다고 명시했는가 |
| [x] | validation과 placeholder map 생성까지만 허용했는가 |
| [x] | template 후보 경로 계산과 존재 여부 확인만 허용했는가 |
| [x] | `replace_placeholders_in_hwpx` 호출을 금지했는가 |
| [x] | 기존 renderer output 덮어쓰기를 금지했는가 |

## 라우팅 확인

| 완료 | 항목 |
|---|---|
| [x] | `ready_for_draft` dry-run 기준이 작성되었는가 |
| [x] | `needs_more_input` dry-run 기준이 작성되었는가 |
| [x] | `needs_security_review` 제외 기준이 작성되었는가 |
| [x] | `blocked` 제외 기준이 작성되었는가 |

## 보안 검수

| 완료 | 항목 |
|---|---|
| [x] | 실제 개인정보를 포함하지 않았는가 |
| [x] | 실제 기관명, 업체명, 담당자명을 포함하지 않았는가 |
| [x] | 실제 문서번호, 민원번호, 접수번호, 사건번호를 포함하지 않았는가 |
| [x] | 실제 공문 또는 보고서 원문을 포함하지 않았는가 |
| [x] | 실제 HWPX 템플릿을 추가하지 않았는가 |

## 다음 단계 판단

| 완료 | 항목 |
|---|---|
| [x] | dry-run PoC 스크립트 작성으로 넘어갈 수 있는가 |
