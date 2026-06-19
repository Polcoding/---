# Phase 2 최소 운영 흐름

## 목적

이 문서는 현재 저장소의 실제 구현 상태를 기준으로 Phase 2에서 사용할 최소 운영 흐름을 정리합니다.

Phase 2는 API, Make.com, Email 자동화 단계가 아닙니다. 비식별 업무 지시를 정규화하고, 보안 필터를 거친 뒤, HWPX 보고서 초안 output을 만들고, 사람이 한컴에서 검토하는 흐름입니다.

## 운영 범위

포함:

- 비식별 수동 입력
- 입력 정규화
- 보안 필터 라우팅
- HWPX payload 매핑
- HWPX payload validation
- HWPX 렌더러 dry-run
- 로컬 placeholder HWPX 템플릿 기반 렌더링
- 사용자 한컴 수동 검수

제외:

- 실제 공문 원문 저장
- 실제 기관 HWPX 양식 원본 Git 추가
- 실제 개인정보 또는 내부 운영정보 처리
- OpenAI API 호출
- Make.com 연동
- Email 자동 발송
- 결재, 계약, 업체 선정, 예산 집행, 법률 판단 자동화

## 최소 흐름

```text
비식별 사용자 입력
→ 입력 정규화
→ 보안 필터
→ routing_decision 확인
→ HWPX payload 매핑
→ payload validation
→ HWPX renderer dry-run
→ 로컬 placeholder HWPX 렌더링
→ 사용자 한컴 수동 검수
→ 사람 수정ㆍ승인 후 실무 적용 여부 판단
```

## 단계별 책임

| 단계 | 담당 구성 | 책임 | 중단 조건 |
|---|---|---|---|
| 입력 | 사용자 | 실제값 제거 후 비식별 지시 제공 | 실제 원문, 개인정보, 내부정보 포함 |
| 입력 정규화 | `normalizers/input_normalizer_poc.py` | 문서 유형, 누락값, 보안 신호 분리 | 문서 유형 불명확 또는 금지 자동화 |
| 보안 필터 | `normalizers/security_filter_poc.py` | routing 상태 판단 | `needs_security_review`, `blocked` |
| payload 매핑 | `normalizers/hwpx_payload_mapper_poc.py` | 정규화 결과를 HWPX 렌더러 입력 구조로 변환 | payload 생성 불가 routing |
| validation | `normalizers/validate_hwpx_payload_poc.py` | 렌더링 전 보안ㆍ필수 구조 확인 | 민감정보 flag 또는 구조 오류 |
| dry-run | `normalizers/hwpx_renderer_dry_run_poc.py` | 실제 HWPX 생성 전 템플릿 후보와 placeholder map 확인 | 템플릿 필요, 보안 보류 |
| 렌더링 | `normalizers/render_mapped_hwpx_poc.py` | 허용 fixture만 로컬 HWPX output 생성 | 허용 routing 아님 |
| 수동 검수 | 사용자 | 한컴에서 열림, 겹침, placeholder 잔여 확인 | 글자 겹침, 서식 오류, 민감정보 의심 |

## routing 운영 기준

| routing | 운영 동작 | HWPX payload | HWPX 렌더링 |
|---|---|---|---|
| `ready_for_draft` | 초안 생성 가능 | 생성 | 가능 |
| `needs_more_input` | `[확인 필요]` 중심 초안 가능 | 생성 | 제한 가능 |
| `needs_security_review` | 사람 보안 검토 필요 | 미생성 | 금지 |
| `blocked` | 처리 중단 | 미생성 | 금지 |

`needs_more_input`은 실제값을 추정하지 않고 `[확인 필요]` 중심으로만 렌더링합니다.

## review_report 예외 조건

`review_report`는 기본적으로 `needs_security_review`입니다.

다음 placeholder 보안 승인 신호가 있을 때만 `ready_for_draft`로 제한 허용합니다.

```json
{
  "security_gate": {
    "human_security_review_completed": true,
    "review_basis": "[비식별 보안 검토 완료]",
    "approved_for_placeholder_rendering": true
  }
}
```

이 신호는 실제 승인자명, 실제 결재번호, 실제 검토의견 원문을 대체하지 않습니다.

## 사용자 확인 지점

[사용자 확인 필요]

HWPX output 생성 후 사용자는 한컴에서 다음을 확인합니다.

- 파일 열림 여부
- 글자 겹침 여부
- 제목과 항목 순서
- 줄바꿈과 문단 배치
- 내용 앞 `-` 표기 일관성
- 남은 `{{placeholder}}` 여부
- `[확인 필요]` 값이 실제값처럼 오인되지 않는지
- 실제 개인정보, 기관정보, 문서번호가 들어가지 않았는지

## 산출물 보관 정책

Git에 포함:

- 정책 문서
- 체크리스트
- placeholder fixture
- renderer/normalizer PoC 코드

Git에서 제외:

- `templates/hwpx/*.hwpx`
- `renderers/hwpx_renderer/output/*.hwpx`
- `normalizers/output/*`

로컬 HWPX 템플릿과 output HWPX는 사용자 PC에서만 검증합니다.

## 회귀 테스트 기준

Phase 2 최소 운영 흐름은 다음 기준을 통과해야 합니다.

- `docs/81_normalizers_regression_test_suite.md`의 fixture 6종 통과
- `review_report` 승인/미승인 경로 분리 유지
- blocked fixture payload 미생성 유지
- mapped HWPX 4종 `remaining_placeholders` 0 유지
- output summary와 HWPX 산출물 Git 제외 유지

## 운영 판단

현재 저장소는 다음까지 가능합니다.

- placeholder 기반 입력 정규화
- 보안 필터 라우팅
- HWPX 보고서 4종 payload 매핑
- 로컬 placeholder HWPX 렌더링
- 사용자 수동 검수

현재 저장소는 다음을 아직 하지 않습니다.

- 실제 업무 원문 처리
- 실제 기관 양식 원본 자동 변환
- 외부 AI API 호출
- Make.com 시나리오 실행
- 자동 발송 또는 자동 결재

## 결론

Phase 2 최소 운영 흐름은 HWPX 보고서 4종을 우선 대상으로 하며, 모든 output은 사람이 검토하는 초안입니다.

다음 단계는 이 흐름을 기준으로 사용자 입력 체크리스트와 운영 전 수동 점검표를 정리하는 것입니다.
