# Phase 2 최소 PoC checkpoint

## 목적

현재 저장소의 실제 파일 상태를 기준으로 Phase 2 최소 PoC의 중간 완료 지점을 정리합니다.

이 문서는 추가 구현 문서가 아니라, 지금까지 구현한 범위와 계속 보류할 범위를 구분하기 위한 checkpoint입니다.

## 현재 판단

Phase 2 최소 PoC는 HWPX 보고서 4종을 대상으로 하는 placeholder 기반 로컬 흐름까지 중간 완료 상태로 봅니다.

현재 완료된 흐름:

```text
비식별 fixture 입력
→ 입력 정규화
→ 보안 필터
→ HWPX payload 매핑
→ HWPX payload validation
→ HWPX renderer dry-run
→ mapped HWPX 렌더링
→ 사용자 한컴 수동 검수
```

이 흐름은 운영 자동화가 아니라 로컬 PoC입니다.

## 구현 완료 범위

| 영역 | 현재 상태 |
|---|---|
| HWPX 보고서 4종 | placeholder 기반 로컬 렌더링 및 한컴 수동 검수 완료 |
| 입력 정규화 | `normalizers/input_normalizer_poc.py` 최소 PoC 작성 |
| 보안 필터 | `normalizers/security_filter_poc.py` 최소 PoC 작성 |
| payload mapper | `normalizers/hwpx_payload_mapper_poc.py` 작성 |
| payload validation | `normalizers/validate_hwpx_payload_poc.py` 작성 |
| renderer dry-run | `normalizers/hwpx_renderer_dry_run_poc.py` 작성 |
| mapped 렌더링 | `normalizers/render_mapped_hwpx_poc.py`로 4종 렌더링 확인 |
| 회귀 테스트 | fixture 6종 기준 정리 |
| 사용자 입력 템플릿 | HWPX 보고서 4종 기준 문서화 |
| 수동 운영 점검 | 입력 전, output 전, output 후 점검표 문서화 |

## placeholder_confirmed_values 처리 상태

`placeholder_confirmed_values`는 현재 문서 기준과 helper 검증까지 완료했습니다.

| 항목 | 상태 |
|---|---|
| read-only helper | 구현 완료 |
| helper 전용 fixture | safe/invalid 파일 분리 완료 |
| fixture schema 후보 | 문서화 완료 |
| normalizer 연결 정책 | 연결 보류로 정리 |
| read-only metadata schema | 문서 기준 후보로 유지 |
| dry-run preview 출력 | 보류 |
| `missing_fields` 반영 | 보류 |
| routing 반영 | 보류 |
| HWPX payload 반영 | 보류 |

## 문서 기준으로 유지할 범위

다음은 현재 코드로 연결하지 않고 문서 기준으로 유지합니다.

- `placeholder_confirmed_values_review` metadata
- `placeholder_confirmed_values` fixture schema 후보
- helper 결과의 normalizer 연결 조건
- dry-run preview 전용 output 후보
- `missing_fields` 자동 제외 후보 규칙
- `project_plan`과 `result_report`의 ready 경로 개방 여부

## 계속 보류할 범위

다음은 Phase 2 최소 PoC checkpoint 이후에도 계속 보류합니다.

- 실제 기관 HWPX 양식 원본 Git 추가
- 실제 공문 또는 보고서 원문 처리
- 실제 개인정보, 민원정보, 내부 운영정보 처리
- OpenAI API 실제 호출
- Make.com 시나리오 구현
- Gmail, Outlook, SMTP 연동
- 실제 이메일 자동 발송
- 실제 결재, 계약, 업체 선정, 예산 집행 자동화
- 실제 기관 표준 글꼴, 자간, 줄간격 값 임의 확정

## 회귀 테스트 기준

checkpoint 이후에도 다음 테스트를 최소 회귀 기준으로 유지합니다.

```powershell
python .\normalizers\validate_placeholder_confirmed_values_poc.py
python .\normalizers\input_normalizer_poc.py
python .\normalizers\hwpx_payload_mapper_poc.py
python .\normalizers\validate_hwpx_payload_poc.py
python .\normalizers\hwpx_renderer_dry_run_poc.py
python .\normalizers\render_mapped_hwpx_poc.py
```

기대 기준:

- helper safe/invalid fixture 통과
- 기존 routing fixture 6종 통과
- `review_report` 승인/미승인 경로 분리 유지
- blocked fixture payload 미생성 유지
- HWPX 4종 mapped render 유지
- local template/output Git 제외 유지

검증 주의:

- `normalizers/output/` 또는 `renderers/hwpx_renderer/output/` 쓰기 권한이 거부되면 summary output 또는 HWPX output 생성이 실패할 수 있습니다.
- `output_error`가 발생하면 코드 보강 전에 로컬 output 폴더 쓰기 권한과 한컴에서 열려 있는 산출물 잠금 여부를 먼저 확인합니다.

## 다음에 구현할 가치가 있는 최소 단위

현재 시점에서 바로 코드 구현을 더 늘리기보다, 다음 최소 단위는 운영 절차 쪽이 더 안전합니다.

추천 후보:

1. Phase 2 최소 PoC 수동 리허설 절차 정리
2. 사용자 입력 → normalizers 실행 → HWPX output 확인까지의 실행 순서 문서화
3. GitHub Desktop Changes에서 확인해야 할 항목 정리
4. 사용자가 직접 확인해야 하는 지점을 `[사용자 확인 필요]`로 다시 표시

## 현재 하지 않는 추천

다음 작업은 아직 추천하지 않습니다.

- `placeholder_confirmed_values`를 `missing_fields`에 반영
- helper 결과를 routing에 반영
- HWPX payload에 metadata 추가
- API/Make.com/Email 자동화 시작
- 실제 기관 양식 원본으로 자동화 시도

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX 원본 추가 없음
- API, Make.com, Email 자동화 코드 추가 없음

## 결론

Phase 2 최소 PoC는 HWPX 보고서 4종 기준의 로컬 placeholder 흐름까지 중간 완료 지점에 도달했습니다.

다음 단계는 코드를 더 확장하기보다, 이 흐름을 사용자가 반복 실행할 수 있는 수동 리허설 절차로 정리하는 것입니다.
