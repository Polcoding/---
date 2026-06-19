# dry-run 결과 보관 정책

## 목적

이 문서는 입력 정규화와 HWPX 렌더러 연결 dry-run 결과를 어떤 파일로 보관할지 정합니다.

핵심 원칙은 Git에는 재현 가능한 fixture와 코드, 결과 문서만 남기고 실행 산출물은 output에 두어 제외하는 것입니다.

## 결론

dry-run summary JSON은 Git에 포함하지 않습니다.

Git에 포함하는 항목:

- `normalizers/*.py`
- `normalizers/fixtures/*.json`
- `normalizers/README.md`
- 결과 문서와 체크리스트

Git에서 제외하는 항목:

- `normalizers/output/*.json`
- `normalizers/__pycache__/`
- 기존 renderer output 산출물
- 로컬 HWPX placeholder 템플릿

## mapper payload fixture 판단

현재 단계에서는 mapper payload를 별도 Git 포함 fixture로 만들지 않습니다.

이유:

- mapper payload는 `normalizers/fixtures/*.json`에서 재생성 가능합니다.
- payload fixture를 추가하면 같은 정보가 중복되어 관리됩니다.
- 현재 필요한 검증은 `normalizers/hwpx_payload_mapper_poc.py`와 `normalizers/validate_hwpx_payload_poc.py` 실행으로 재현 가능합니다.
- 실제 HWPX 렌더링 전까지는 output summary만으로 충분합니다.

## output summary 보관 방식

| 산출물 | Git 포함 여부 | 이유 |
|---|---|---|
| `normalization_summary.json` | 제외 | 실행 결과 산출물 |
| `hwpx_payload_mapping_summary.json` | 제외 | mapper 실행 결과 산출물 |
| `hwpx_payload_validation_summary.json` | 제외 | validation 실행 결과 산출물 |
| `hwpx_renderer_dry_run_summary.json` | 제외 | dry-run 실행 결과 산출물 |

필요할 때 스크립트를 다시 실행해 재생성합니다.

## fixture 보관 방식

현재 유지하는 fixture 5종:

- `safe_one_page_report_request.json`
- `missing_project_plan_request.json`
- `missing_result_report_request.json`
- `review_report_needs_security_review.json`
- `blocked_real_value_like_request.json`

fixture 추가 기준:

- 새 문서 유형을 지원할 때
- 새 routing 상태를 추가할 때
- 실제 HWPX 렌더링 연결 전에 회귀 테스트가 필요한 경우

fixture 추가 금지 기준:

- 실제 원문 포함
- 실제 개인정보 포함
- 실제 기관명, 업체명, 담당자명 포함
- 실제 문서번호, 민원번호, 사건번호 포함
- 실제 예산액, 실적 수치, 수량 포함

## 실제 HWPX 렌더링 전 기준점

실제 HWPX 렌더링 연결 전에는 다음을 기준점으로 둡니다.

- 정규화 PoC fixture 5종 통과
- mapper PoC fixture 5종 통과
- payload validation PoC fixture 5종 통과
- renderer dry-run PoC fixture 5종 통과
- output summary Git 제외 확인
- 로컬 HWPX 템플릿 Git 제외 확인

## 다음 단계

다음 작업은 실제 HWPX 렌더링 연결 여부를 결정하는 것입니다.

다만 실제 HWPX 파일을 생성하는 단계는 사용자가 확인할 필요가 있는 작업이므로, 먼저 렌더링 연결 범위와 사용자 확인 지점을 문서로 정리합니다.
