# 정규화 결과와 HWPX payload 매핑 범위 체크리스트

## 목적

`docs/67_normalized_to_hwpx_payload_mapping_scope.md`가 정규화 결과와 HWPX 렌더러 입력 JSON 사이의 변환 범위를 안전하게 제한했는지 확인합니다.

## 범위 확인

| 완료 | 항목 |
|---|---|
| [x] | 정규화 결과와 HWPX 렌더러 사이에 별도 변환 계층을 두었는가 |
| [x] | 대상 문서 유형을 HWPX 보고서 4종으로 제한했는가 |
| [x] | 공문, XLSX, Email은 이번 매핑 범위에서 제외했는가 |
| [x] | `routing_decision`별 payload 생성/중단 기준을 정했는가 |
| [x] | `needs_security_review`와 `blocked`는 렌더링하지 않는다고 명시했는가 |

## 매핑 확인

| 완료 | 항목 |
|---|---|
| [x] | 공통 필드 매핑이 작성되었는가 |
| [x] | `security_flags`와 `security_review` 연결 기준이 작성되었는가 |
| [x] | `draft_status` 매핑이 작성되었는가 |
| [x] | `documents[0]` 문서 유형별 매핑이 작성되었는가 |
| [x] | `renderer_hints` 매핑이 작성되었는가 |
| [x] | 매핑 fixture 기준이 작성되었는가 |

## 보안 검수

| 완료 | 항목 |
|---|---|
| [x] | 실제 개인정보를 포함하지 않았는가 |
| [x] | 실제 기관명, 업체명, 담당자명을 포함하지 않았는가 |
| [x] | 실제 문서번호, 민원번호, 접수번호, 사건번호를 포함하지 않았는가 |
| [x] | 실제 공문 또는 보고서 원문을 포함하지 않았는가 |
| [x] | 실제 예산액 또는 실적 수치를 포함하지 않았는가 |
| [x] | 실제 HWPX 템플릿을 추가하지 않았는가 |

## 다음 단계 판단

| 완료 | 항목 |
|---|---|
| [x] | `normalizers/hwpx_payload_mapper_poc.py` 작성으로 넘어갈 수 있는가 |
