# HWPX style profile 확인 필요 값 유지 기준과 서식값 수집 체크리스트 점검

## 목적

이 문서는 HWPX 보고서 4종 style profile의 `[확인 필요]` 값을 실제 확정값처럼 취급하지 않도록 유지 기준을 정리하고, 기관 표준 서식값 수집 체크리스트가 보안 원칙과 충돌하지 않는지 점검합니다.

이번 단계는 실제 서식값을 입력하거나 실제 기관 HWPX 원본을 투입하는 단계가 아닙니다. renderer, normalizer, fixture, routing, HWPX payload, output도 변경하지 않습니다.

## 확인 대상

- `docs/125_hwpx_template_manifest_placeholder_consistency_review.md`
- `checklists/hwpx_template_manifest_placeholder_consistency_checklist.md`
- `docs/40_hwpx_institution_style_values_review.md`
- `templates/hwpx/style_profile_manifest.md`
- `checklists/hwpx_institution_style_value_collection_checklist.md`
- `templates/hwpx/local_template_policy.md`
- `templates/hwpx/template_manifest.md`
- `templates/hwpx/README.md`
- `checklists/before_automation_checklist.md`

## 점검 결론

현재 저장소 기준으로 style profile 후보는 모두 미확정 상태이며, 실제 서식값을 임의 확정하지 않는 방향과 정합합니다.

다만 실제 양식 투입 전 단계에서 다음 기준을 더 명확히 둘 필요가 있었습니다.

| 항목 | 확인 내용 | 조치 |
|---|---|---|
| `[확인 필요]` 유지 기준 | 값이 확인되지 않은 상태와 실제 확정값의 경계가 더 필요함 | 상태 전환 기준 추가 |
| 수집 체크리스트 | 보안 항목은 있으나 수집 전 중단 조건과 기록 제한이 부족함 | 수집 전ㆍ기록 전ㆍ반영 전 점검 항목 보강 |
| style profile manifest | 후보 목록은 있으나 상태 전환 gate가 부족함 | 확정 전 유지 기준과 반영 조건 추가 |
| local template policy | 로컬 원본 Git 제외 원칙은 있으나 서식값 수집 기록 분리 기준이 부족함 | 수집 기록에 실제 파일명과 원본 정보를 남기지 않는 기준 추가 |

## style profile 상태 유지 기준

style profile 값은 다음 조건을 모두 만족하기 전까지 `[확인 필요]`로 유지합니다.

1. 사람이 저장소 밖 로컬 환경에서 기준 양식 또는 검토용 복사본을 직접 확인
2. 실제 기관명, 실제 문서번호, 결재정보, 담당자명, 원문 내용이 수집 기록에 포함되지 않음
3. 폰트 파일, HWP/HWPX 원본, 이미지 원본을 저장소에 추가하지 않음
4. 확인값이 특정 사건, 특정 부서, 특정 문서 원문을 추정하게 만들지 않음
5. 적용 대상 문서유형과 서식 항목이 명확함
6. 사람이 반영 가능 여부를 다시 검토함

하나라도 충족하지 못하면 style profile manifest와 관련 문서에는 `[확인 필요]`를 유지합니다.

## 상태 전환 기준

| 상태 | 의미 | Git 기록 가능 여부 | 다음 조치 |
|---|---|---|---|
| `[확인 필요]` | 아직 확인하지 않았거나 확인 근거가 불충분함 | 가능 | 기본 상태로 유지 |
| `수집 후보` | 사람이 저장소 밖에서 확인했으나 반영 전 검토가 필요함 | 비식별 요약만 가능 | 보안 검수 |
| `검토 완료 후보` | 값 자체는 확인됐으나 적용 영향 검토가 필요함 | 실제 원본 없이 일반 서식값만 가능 | 수동 preview 기준 검토 |
| `적용 승인` | 사용자가 명시적으로 반영을 승인함 | 별도 승인 후 가능 | 템플릿 또는 문서 기준 갱신 |

현재 저장소에서는 모든 style profile을 `[확인 필요]` 상태로 유지합니다.

## 문서유형별 style profile 판단

| style_profile_id | 문서유형 | 현재 상태 | 판단 |
|---|---|---|---|
| `style_one_page_report_basic` | 원페이지 보고서 | 확인 필요 | 유지 |
| `style_project_plan_basic` | 추진계획서 | 확인 필요 | 유지 |
| `style_result_report_basic` | 결과보고서 | 확인 필요 | 유지 |
| `style_review_report_basic` | 검토보고서 | 확인 필요 | 유지 |

공문 계열 style profile도 동일하게 `[확인 필요]` 상태를 유지합니다. 다만 현재 자동화 우선순위는 HWPX 보고서 4종입니다.

## 수집 가능 정보와 금지 정보

| 구분 | 허용 | 금지 |
|---|---|---|
| 서식 항목명 | 제목 글꼴, 본문 글씨 크기, 줄간격, 자간, 표 테두리 같은 일반 항목명 | 실제 기관 양식명, 실제 문서명 |
| 확인 상태 | `[확인 필요]`, 수집 후보, 검토 완료 후보 | 확인되지 않은 값을 확정값처럼 기록 |
| 출처 설명 | 저장소 밖 로컬 확인, 내부 기준 확인 필요 같은 일반 설명 | 실제 파일명, 실제 기관명, 실제 문서번호, 내부 경로 |
| 템플릿 파일 | placeholder 기반 로컬 검증 파일은 Git 제외 상태로만 사용 | 실제 HWP/HWPX 원본 Git 추가 |
| 폰트 | 글꼴명 확인 필요 상태 유지 | 폰트 파일 저장소 추가 |

## 수집 기록 원칙

- 수집 기록에는 실제 기관명, 실제 부서명, 실제 문서번호, 실제 파일명을 쓰지 않습니다.
- 실제 HWPX 원본의 본문 내용, 결재선, 로고, 직인, 수신자 정보는 기록하지 않습니다.
- 확인값을 바로 renderer나 normalizer에 연결하지 않습니다.
- 확인값은 먼저 수동 preview와 사람 검토 기준에 맞는지 확인합니다.
- 판단이 애매하면 `[확인 필요]`로 되돌립니다.

## 기존 문서와의 정합성

| 문서 | 판단 |
|---|---|
| `docs/40_hwpx_institution_style_values_review.md` | 기본 항목은 적절하며, 최신 기준 문서 연결 필요 |
| `templates/hwpx/style_profile_manifest.md` | style profile 후보 상태는 정합하며, 상태 전환 기준 보강 필요 |
| `checklists/hwpx_institution_style_value_collection_checklist.md` | 수집 항목은 적절하며, 수집 전 중단 조건과 기록 제한 보강 필요 |
| `templates/hwpx/local_template_policy.md` | 로컬 HWPX Git 제외 원칙은 정합하며, 서식값 수집 기록 분리 기준 보강 필요 |
| `templates/hwpx/template_manifest.md` | 보고서 4종 매핑은 정합하며, style profile 미확정 상태 유지 기준 보강 필요 |

## 코드 변경 판단

이번 점검에서는 코드 변경이 필요하지 않습니다.

변경하지 않는 항목:

- `normalizers/`
- `renderers/`
- `examples/json/`
- routing fixture
- HWPX payload mapper
- HWPX renderer output
- local HWPX template
- API, Make.com, Email 연동 코드

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX 원본 파일 추가 없음
- 실제 파일명, 내부 경로, 원본 양식명 추가 없음
- 폰트 파일 추가 없음
- API 키, 토큰, 인증정보 예시값 추가 없음
- Email, API, Make.com 연동 구현 없음

## 결론

HWPX 보고서 4종 style profile은 실제 서식값을 확인하기 전까지 모두 `[확인 필요]` 상태로 유지합니다.

HWPX 보고서 4종 수동 preview gap log 기준은 `docs/127_hwpx_manual_preview_gap_log_criteria.md`에 후속 반영했습니다.

저장소 밖 실제 양식 후보 수동 절차와 보류 조건은 `docs/128_external_hwpx_candidate_manual_procedure_and_hold_criteria.md`에 후속 반영했습니다.

다음 단계는 실제 HWPX output 재생성이 아니라, local template policy와 Git 제외 상태 반복 검증 기준을 문서로 정리하는 것입니다.
