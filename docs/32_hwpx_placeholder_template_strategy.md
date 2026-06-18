# HWPX placeholder 템플릿 전략

## 목적

이 문서는 HWPX 렌더러 PoC 구현 전에 placeholder 기반 HWPX 템플릿을 어떻게 설계할지 정리합니다.

이번 단계에서는 실제 HWPX 파일을 생성하지 않습니다.

실제 기관 양식, 실제 공문 원문, 실제 개인정보를 사용하지 않고, 향후 테스트용 placeholder 템플릿을 만들기 위한 기준만 정의합니다.

## 기본 원칙

- 실제 기관 HWPX 양식 원본을 저장소에 추가하지 않습니다.
- 실제 공문 원문을 템플릿에 넣지 않습니다.
- 모든 값은 placeholder로 표현합니다.
- 확인되지 않은 서식값은 [확인 필요]로 표시합니다.
- AI는 내용 구조를 생성하고, HWPX 템플릿은 서식을 유지합니다.
- 생성 결과는 실제 발송용이 아니라 사람 검토용 초안입니다.
- 개인정보, 내부 운영정보, 대외비 자료는 HWPX 템플릿에 포함하지 않습니다.
- 실제 HWPX 파일 생성은 이후 별도 승인된 PoC 단계에서만 검토합니다.

## HWPX 템플릿 유형

| template_id | 문서유형 | 용도 | 구현 우선순위 |
|---|---|---|---|
| hwpx_one_page_report_basic | 원페이지 보고서 | 보고서 초안 | 1 |
| hwpx_project_plan_basic | 추진계획서 | 계획서 초안 | 1 |
| hwpx_result_report_basic | 결과보고서 | 결과보고 초안 | 1 |
| hwpx_review_report_basic | 검토보고서 | 검토자료 초안 | 2 |
| hwpx_official_letter_basic | 일반 공문 | 공문 초안 | 3 |
| hwpx_survey_request_letter | 현황조사 지시 공문 | 조사 요청 공문 | 3 |

실제 HWPX 파일은 아직 만들지 않습니다.

template_id는 실제 파일명이 아니라 설계용 식별자입니다.

보고서 HWPX 자동화의 최우선 흐름은 원페이지 보고서, 추진계획서, 결과보고서입니다. 검토보고서는 핵심 문서 후보에 포함하되, 계획ㆍ결과 보고서 placeholder 구조가 안정화된 뒤 확장합니다.

## 공통 placeholder 목록

- {{document_number}}
- {{execution_date}}
- {{recipient}}
- {{reference}}
- {{title}}
- {{body_sections}}
- {{sub_sections}}
- {{overview_table}}
- {{schedule_table}}
- {{budget_table}}
- {{attachments}}
- {{closing}}
- {{checklist}}
- {{missing_fields}}
- {{security_review}}
- {{draft_status}}
- {{human_review_required}}

## placeholder 사용 원칙

- placeholder에는 실제 값을 넣지 않습니다.
- 문서번호, 시행일자, 수신처, 담당자명은 모두 placeholder로 유지합니다.
- 확인되지 않은 값은 [확인 필요]로 둡니다.
- 개인정보나 내부 운영정보를 placeholder 이름으로도 구체화하지 않습니다.
- placeholder는 AI 출력 JSON과 HWPX 템플릿 영역을 연결하기 위한 식별자로만 사용합니다.

## 공문 템플릿 placeholder 구조

일반 공문과 현황조사 지시 공문에 필요한 영역을 정의합니다.

| 영역 | 역할 | 주요 placeholder |
|---|---|---|
| 상단 정보 영역 | 문서번호, 시행일자, 수신, 참조 표시 | {{document_number}}, {{execution_date}}, {{recipient}}, {{reference}} |
| 제목 영역 | 공문 제목 표시 | {{title}} |
| 본문 영역 | 본문 문단 표시 | {{body_sections}} |
| 하위 항목 영역 | 가., 나., 1), 2) 등 하위 항목 표시 | {{sub_sections}} |
| 붙임 영역 | 붙임 목록 표시 | {{attachments}}, {{closing}} |
| 발송 전 체크리스트 영역 | 검토 항목 표시 | {{checklist}} |
| 메타정보 영역 | 확인 필요 사항과 보안 점검 결과 관리 | {{missing_fields}}, {{security_review}}, {{draft_status}}, {{human_review_required}} |

메타정보 영역은 실제 공문 본문에 그대로 노출하지 않고, 검토용 정보로 관리할 수 있습니다.

## 추진계획서 템플릿 placeholder 구조

| 영역 | JSON 필드 또는 placeholder | 비고 |
|---|---|---|
| 제목 | {{title}} | 계획서 제목 |
| 추진배경 | {{background}} | 확인 필요 사항은 표시 |
| 추진목적 | {{purpose}} | 목적 문장 |
| 추진개요 | {{overview_table}} | 표 구조 |
| 주요내용 | {{main_contents}} | 개조식 구성 |
| 세부 추진계획 | {{detailed_plan}} | 단계별 계획 |
| 추진일정 | {{schedule_table}} | 일정 미정 시 [확인 필요] |
| 소요예산 | {{budget_table}} | 금액 임의 생성 금지 |
| 기대효과 | {{expected_effects}} | 과장 표현 금지 |
| 검토사항 | {{review_items}} | 추가 검토 필요 항목 |
| 향후계획 | {{future_plan}} | 후속 조치 |
| 붙임 | {{attachments}} | 붙임 목록 |
| 체크리스트 | {{checklist}} | 최종 검토용 |

## 결과보고서 템플릿 placeholder 구조

| 영역 | JSON 필드 또는 placeholder | 비고 |
|---|---|---|
| 제목 | {{title}} | 결과보고서 제목 |
| 추진개요 | {{overview_table}} | 사업 개요 |
| 기존 계획 연결 | {{linked_project_plan}} | 실제 원문이나 실제 파일명 대신 placeholder 사용 |
| 계획 대비 결과 | {{plan_result_mapping}} | 계획 항목과 결과 항목 대응 |
| 추진결과 | {{results}} | 실제 수치 임의 생성 금지 |
| 주요성과 | {{main_outcomes}} | 과장 표현 금지 |
| 문제점 및 개선사항 | {{issues}}, {{improvements}} | 개조식 정리 |
| 향후계획 | {{future_plan}} | 후속 조치 |
| 붙임 | {{attachments}} | 붙임 목록 |
| 체크리스트 | {{checklist}} | 검토용 |

결과보고서에서는 기존 추진계획서와의 연결 여부를 placeholder로만 관리합니다. 실제 계획서 원문, 실제 문서번호, 실제 파일 경로, 실제 담당자명은 템플릿에 넣지 않습니다.

## 공문 번호체계 규칙

다음 번호체계를 유지해야 합니다.

- 1.
- 가.
- 1)
- 가)

상위 문단에서 3), 4)처럼 잘못된 번호체계를 사용하지 않습니다.

예시 구조:

```text
1. [본문 내용]

  가. [하위 항목]

    1) [세부 항목]
```

## 붙임 표기 규칙

다음 형식을 사용합니다.

```text
붙임  1. [문서명] 1부.
      2. [문서명] 1부.  끝.
```

- 붙임이 없으면 붙임 영역을 생성하지 않거나 [확인 필요]로 표시합니다.
- 붙임이 여러 개면 번호 순서를 유지합니다.
- 끝. 위치가 깨지지 않도록 검수해야 합니다.

## 서식 유지 전략

- 폰트는 HWPX 템플릿에서 관리합니다.
- 글씨 크기는 HWPX 템플릿에서 관리합니다.
- 자간은 HWPX 템플릿에서 관리합니다.
- 줄간격은 HWPX 템플릿에서 관리합니다.
- 문단 간격은 HWPX 템플릿에서 관리합니다.
- 표 양식은 HWPX 템플릿에서 관리합니다.
- AI는 실제 서식값을 생성하지 않습니다.
- 확인되지 않은 서식값은 [확인 필요]로 둡니다.
- HWPX 렌더러는 템플릿의 기존 스타일을 최대한 보존해야 합니다.

## 공공기관 문체 반영 전략

- 구어체보다 공문체를 사용합니다.
- 장황한 설명보다 개조식 표현을 우선합니다.
- 확정되지 않은 내용은 [확인 필요]로 표시합니다.
- 예산, 일정, 담당자, 수량은 임의 생성하지 않습니다.
- 불필요한 조사와 감정적 표현을 줄입니다.
- 행정문서에서 자주 쓰는 표현을 사용하되, 확정적 표현은 피합니다.

권장 표현:

- [업무 목적]을 위하여 [대상]에 대한 [요청 내용]을 추진하고자 함
- [제출기한]까지 [제출방법]으로 제출하여 주시기 바랍니다
- [활용 목적]을 위한 기초자료로 활용하고자 함
- 관련 사항은 [담당부서] 검토 후 확정 예정임
- 실제 발송 전 담당부서 검토 및 내부 승인 필요

지양 표현:

- 꼭 부탁드립니다
- 문제 없습니다
- 확정되었습니다
- 선정 예정입니다
- 예산은 확보되어 있습니다
- 바로 발송하면 됩니다

## 이번 단계에서 하지 않는 것

- 실제 HWPX 파일 생성
- HWPX 편집 코드 작성
- 실제 기관 양식 적용
- 실제 공문 원문 처리
- 실제 개인정보 처리
- API 호출
- 이메일 자동화
- Make.com 자동화
- Custom GPT Knowledge 업로드

## Step 22 결론

Step 22는 HWPX 실제 구현 전 placeholder 전략 확정 단계입니다.

다음 단계로 넘어가려면 다음 조건이 필요합니다.

- placeholder 템플릿 전략 확정
- 템플릿 manifest 작성
- 검수 체크리스트 작성
- 실제 기관 양식 미사용 원칙 확인
- 사용자의 HWPX 최소 PoC 구현 승인

현재 추천은 HWPX 코드를 바로 작성하기보다, placeholder 템플릿 전략을 기준으로 최소 PoC 범위를 한 번 더 검토한 뒤 진행하는 것입니다.
