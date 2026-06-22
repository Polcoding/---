# normalizers 회귀 테스트 재검증 결과 체크리스트

## 목적

`docs/109_normalizers_regression_recheck_result.md` 기준으로 Phase 2 마무리 전 normalizers 회귀 테스트 재검증 결과를 확인합니다.

## 실행 확인

| 완료 | 항목 |
|---|---|
| [x] | `validate_placeholder_confirmed_values_poc.py`를 실행했는가 |
| [x] | `input_normalizer_poc.py`를 실행했는가 |
| [x] | `hwpx_payload_mapper_poc.py`를 실행했는가 |
| [x] | `validate_hwpx_payload_poc.py`를 실행했는가 |
| [x] | `hwpx_renderer_dry_run_poc.py`를 실행했는가 |
| [x] | `render_mapped_hwpx_poc.py`를 실행했는가 |

## 결과 확인

| 완료 | 항목 |
|---|---|
| [x] | helper safe/invalid fixture가 통과했는가 |
| [x] | routing fixture 6종이 통과했는가 |
| [x] | `needs_security_review` fixture가 payload 미생성 상태로 유지되는가 |
| [x] | `blocked` fixture가 payload 미생성 상태로 유지되는가 |
| [x] | 생성된 payload 4종이 validation을 통과했는가 |
| [x] | dry-run 상태가 기대값과 일치하는가 |
| [x] | mapped HWPX 4종이 모두 `rendered`인가 |
| [x] | mapped HWPX 4종의 `remaining_placeholders`가 0인가 |
| [x] | mapped HWPX 4종의 `errors`가 0인가 |

## 권한 및 산출물 확인

| 완료 | 항목 |
|---|---|
| [x] | sandbox summary 쓰기 제한을 확인했는가 |
| [x] | 필요한 summary JSON을 권한 승인 후 갱신했는가 |
| [x] | tracked Python cache 변경을 원복했는가 |
| [x] | `normalizers/output/*`가 Git 제외 상태인가 |
| [x] | `renderers/hwpx_renderer/output/*`가 Git 제외 상태인가 |
| [x] | `templates/hwpx/*.hwpx`가 Git 제외 상태인가 |

## 변경 제한 확인

| 완료 | 항목 |
|---|---|
| [x] | normalizer 코드를 변경하지 않았는가 |
| [x] | renderer 코드를 변경하지 않았는가 |
| [x] | fixture JSON을 변경하지 않았는가 |
| [x] | routing 결과를 변경하지 않았는가 |
| [x] | HWPX payload 구조를 변경하지 않았는가 |
| [x] | `placeholder_confirmed_values` normalizer 연결을 하지 않았는가 |

## 보안 검수

| 완료 | 항목 |
|---|---|
| [x] | 실제 개인정보를 추가하지 않았는가 |
| [x] | 실제 기관명, 업체명, 담당자명을 추가하지 않았는가 |
| [x] | 실제 문서번호, 민원번호, 사건번호를 추가하지 않았는가 |
| [x] | 실제 날짜, 예산, 실적 수치를 추가하지 않았는가 |
| [x] | 실제 공문 원문 또는 보고서 원문을 추가하지 않았는가 |
| [x] | 실제 HWPX 원본 파일을 추가하지 않았는가 |
| [x] | Email, API, Make.com 연동을 하지 않았는가 |

## 다음 단계 확인

| 완료 | 항목 |
|---|---|
| [x] | Phase 2 마무리 판단을 다음 후보로 정리했는가 |
| [x] | Phase 3 진입 조건 문서화 여부를 다음 후보로 유지했는가 |
