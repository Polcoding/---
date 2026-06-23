# 템플릿 렌더러 요구사항

## 목적

- 이 문서는 AI가 생성한 JSON 초안을 HWPX, XLSX, 이메일, Markdown 등 실제 산출물 형태로 변환하기 위한 템플릿 렌더러 요구사항을 정의합니다.
- 이번 단계에서는 실제 렌더러 코드를 작성하지 않습니다.
- 실제 HWPX 또는 XLSX 파일을 생성하지 않습니다.
- 실제 기관 양식이나 실제 업무자료를 사용하지 않고, placeholder 기반 설계만 정리합니다.
- 렌더러는 AI가 생성한 문서 구조를 검증하고, 보안 위험을 차단한 뒤, 적절한 템플릿에 삽입하는 역할을 합니다.

## 기본 원칙

- AI는 문장, 목차, 표 데이터 후보 또는 구조, 확인 필요 사항을 생성합니다.
- 템플릿 렌더러는 폰트, 자간, 줄간격, 표 양식, 셀 서식, 붙임 표기 등 서식을 적용합니다.
- AI 출력 JSON은 렌더링 전에 반드시 검증합니다.
- 개인정보, 민감정보, 내부 운영정보가 감지되면 렌더링을 중단하거나 사람 검토로 전환합니다.
- 모든 산출물은 초안이며, 사람이 최종 검토해야 합니다.
- 확인되지 않은 값은 [확인 필요] 또는 null로 유지합니다.
- 렌더러는 날짜, 예산, 담당자, 업체명, 수량을 임의 생성하지 않습니다.
- 현재 HWPX 보고서 단계에서 표 데이터 후보는 실제 표 내부 데이터 자동 입력, Excel/한셀 연동, HWPX payload 확장을 의미하지 않습니다.

## 렌더러의 전체 흐름

1. 사용자 업무 지시 수신
2. AI 출력 JSON 생성
3. JSON 스키마 검증
4. 보안 위험 검증
5. missing_fields 확인
6. 출력 대상 선택
7. 템플릿 선택
8. placeholder 매핑
9. 렌더링 실행
10. 산출물 생성
11. 검수 체크리스트 첨부
12. 사람 최종 검토

## 렌더러 입력값

| 입력값 | 설명 | 예시 |
|---|---|---|
| ai_output_json | AI가 생성한 구조화된 문서 초안 | placeholder 기반 JSON |
| target_format | 출력 형식 | hwpx / xlsx / markdown / email |
| template_id | 사용할 템플릿 식별자 | [템플릿 ID 확인 필요] |
| security_review | 보안 검토 결과 | low / medium / high / blocked |
| missing_fields | 확인 필요 항목 | [확인 필요] 목록 |
| renderer_hints | 렌더링 힌트 | style_profile, table_template 등 |

`renderer_hints.table_template`은 서식 또는 표시 후보 힌트입니다. 실제 표 데이터, 물품명, 수량, 금액, 대상 목록을 생성하거나 입력하라는 의미가 아닙니다.

## 렌더러 출력값

| 출력값 | 설명 |
|---|---|
| rendered_document | 생성된 초안 문서 |
| render_status | success / warning / blocked / failed |
| warnings | 사람 검토가 필요한 경고 |
| blocked_reason | 차단 사유 |
| checklist | 발송 전 검수 항목 |
| missing_fields_report | 확인 필요 항목 보고 |
| audit_summary | 처리 요약 |

## JSON 스키마 검증 요구사항

렌더러는 docs/18_ai_output_json_schema.md 기준으로 AI 출력 JSON을 검증해야 합니다.

검증 항목:

- 필수 필드 존재 여부
- task_type 존재 여부
- document_type 존재 여부
- security_review 존재 여부
- missing_fields 존재 여부
- human_review_required 값 존재 여부
- documents 또는 email_draft 등 출력 대상 존재 여부
- renderer_hints 존재 여부
- 허용되지 않은 필드 포함 여부
- null 또는 [확인 필요] 허용 여부

검증 실패 시:

- 렌더링 중단
- render_status를 failed로 설정
- failed_reason에 누락 필드 또는 오류를 기록
- 사람 검토 필요로 표시

## 보안 검증 요구사항

렌더러는 렌더링 전에 반드시 보안 검증을 수행해야 합니다.

차단 조건:

- security_review.risk_level이 high 또는 blocked
- contains_personal_info가 true
- contains_sensitive_info가 true
- contains_internal_info가 true인 경우 수동 검토 필요
- 실제 개인정보처럼 보이는 값이 포함된 경우
- 실제 문서번호, 민원번호, 접수번호처럼 보이는 값이 포함된 경우
- 차량번호, 장비명, 수량, 운영정보처럼 보이는 값이 포함된 경우
- 내부망 주소, 시스템명, 계정, 비밀번호, API 키가 포함된 경우
- 계약, 선정, 예산 집행이 확정된 것처럼 보이는 표현이 포함된 경우

주의:
실제 예시값은 만들지 않습니다.

## 출력 형식별 렌더링 요구사항

### HWPX 렌더링

- 대상: 공문, 추진계획서, 결과보고서, 검토보고서
- 입력: AI 출력 JSON
- 템플릿: placeholder 기반 HWPX 템플릿
- 서식: HWPX 템플릿 담당
- 렌더링 전 보안 검증 필수
- 실제 HWPX 생성 코드는 이번 단계에서 작성하지 않음

### XLSX 렌더링

- 대상: 조사표, 작성요령, 검수체크리스트, 메타정보
- 입력: AI 출력 JSON의 현황조사표 구조
- 템플릿: placeholder 기반 XLSX 템플릿
- 서식: XLSX 템플릿 담당
- 렌더링 전 보안 검증 필수
- 실제 XLSX 생성 코드는 이번 단계에서 작성하지 않음

### Markdown 렌더링

- 대상: 미리보기, 검토용 초안
- 입력: AI 출력 JSON
- 용도: 사람 검토용 빠른 출력
- 실제 외부 발송용 문서로 사용하지 않음

### Email 렌더링

- 대상: 업체 연락 메일, 사용자 회신 메일
- 입력: email_draft JSON
- 개인정보ㆍ민감정보 제외 문구 필수
- 계약ㆍ선정 미확정 문구 필수
- 실제 자동 발송은 이번 단계에서 구현하지 않음

## 템플릿 선택 규칙

렌더러는 document_type과 target_format을 기준으로 템플릿을 선택합니다.

| document_type | target_format | template_id | 비고 |
|---|---|---|---|
| official_letter | hwpx | [템플릿 ID 확인 필요] | 공문 |
| survey_request_letter | hwpx | [템플릿 ID 확인 필요] | 현황조사 지시 공문 |
| project_plan | hwpx | [템플릿 ID 확인 필요] | 추진계획서 |
| result_report | hwpx | [템플릿 ID 확인 필요] | 결과보고서 |
| survey_table | xlsx | [템플릿 ID 확인 필요] | 현황조사표 |
| vendor_email | email | [템플릿 ID 확인 필요] | 업체 연락 메일 |
| preview | markdown | [템플릿 ID 확인 필요] | 검토용 미리보기 |

실제 템플릿 ID는 아직 확정하지 않고 [확인 필요]로 표시합니다.

## placeholder 매핑 요구사항

렌더러는 AI 출력 JSON 필드를 템플릿 placeholder에 매핑해야 합니다.

| JSON 필드 | placeholder | 적용 대상 |
|---|---|---|
| title | {{title}} | HWPX, XLSX, Markdown |
| body_sections | {{body_sections}} | HWPX |
| attachments | {{attachments}} | HWPX |
| rows | {{rows}} | XLSX |
| checklist | {{checklist}} | HWPX, XLSX, Markdown |
| missing_fields | {{missing_fields}} | 메타정보, 검토용 출력 |
| security_review | {{security_review}} | 메타정보, 검토용 출력 |
| email_draft.subject | {{subject}} | Email |
| email_draft.request_items | {{request_items}} | Email |

## 오류 처리 요구사항

| 오류 유형 | 처리 방식 |
|---|---|
| 필수 JSON 필드 누락 | 렌더링 중단 |
| 보안 위험 감지 | 렌더링 중단 또는 사람 검토 |
| 템플릿 ID 없음 | 렌더링 중단 |
| placeholder 매핑 실패 | warning 또는 failed 처리 |
| missing_fields 존재 | warning 처리 후 초안 생성 가능 |
| forbidden 표현 감지 | 사람 검토 또는 차단 |
| 출력 파일 생성 실패 | failed 처리 |
