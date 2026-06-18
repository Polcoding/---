# 원페이지 보고서 HWPX 템플릿 전략

## 목적

이 문서는 HWPX 보고서 자동화의 최우선 대상인 원페이지 보고서를 placeholder 기반 HWPX 템플릿으로 생성하기 위한 전략을 정리합니다.

이번 단계에서는 실제 HWPX 파일을 생성하지 않습니다.

## 입력 JSON

사용할 입력은 다음 파일입니다.

- examples/json/sample_one_page_report.json

## 기본 원칙

- 실제 보고서 원문을 사용하지 않습니다.
- 실제 기관 양식을 사용하지 않습니다.
- 모든 값은 placeholder 기반입니다.
- 예산, 일정, 실적, 담당자는 임의 생성하지 않습니다.
- 생성 결과는 실제 보고서가 아니라 검토용 초안입니다.
- output HWPX는 Git 커밋 대상에서 제외합니다.

## 원페이지 보고서 기본 구조

원페이지 보고서는 다음 영역을 기본 후보로 둡니다.

- 제목
- 보고 개요
- 추진 배경
- 주요 내용
- 검토 의견
- 문제점 또는 고려사항
- 향후 계획
- 조치 필요사항 또는 협조사항
- 확인 필요 사항
- 검토 체크리스트

## 권장 placeholder

다음 placeholder를 사용합니다.

- {{title}}
- {{report_summary}}
- {{background}}
- {{main_points}}
- {{review_opinion}}
- {{issues_or_considerations}}
- {{next_steps}}
- {{action_items}}
- {{missing_fields}}
- {{checklist}}
- {{security_review}}
- {{draft_status}}
- {{human_review_required}}

## 문체 기준

- 개조식 중심
- 짧은 문장
- 명사형 표현
- 불필요한 조사 최소화
- 구어체 지양
- 확정되지 않은 정보는 [확인 필요]
- 기대효과나 성과를 과장하지 않음
- 실제 사용 전 담당자 검토 필요

## 렌더러 보강 준비 방향

향후 구현 단계에서 검토할 준비 항목은 다음과 같습니다.

- document_type이 one_page_report인 입력을 식별할 수 있어야 합니다.
- renderer_hints.template_id가 hwpx_one_page_report_basic인 경우 원페이지 보고서 템플릿 후보로 연결합니다.
- documents[0]의 보고서 필드를 위 placeholder와 대응시킵니다.
- missing_fields, security_review, draft_status, human_review_required는 본문과 분리된 검토용 영역으로 관리합니다.
- 실제 HWPX output은 Git 커밋 대상에서 제외하고, 별도 검수 후에만 산출물 보관 여부를 판단합니다.

## 렌더러 보강 내용

one_page_report 입력을 처리하기 위해 다음 placeholder map을 별도로 구성합니다.

| placeholder | JSON 경로 | 처리 기준 |
|---|---|---|
| {{title}} | documents[0].title | 값이 없으면 [확인 필요] |
| {{report_summary}} | documents[0].report_summary | key-value 목록 문자열 |
| {{background}} | documents[0].background | 값이 없으면 [확인 필요] |
| {{main_points}} | documents[0].main_points | 배열을 개조식 문자열로 변환 |
| {{review_opinion}} | documents[0].review_opinion | 확정 판단이 아니어야 함 |
| {{issues_or_considerations}} | documents[0].issues_or_considerations | 배열을 개조식 문자열로 변환 |
| {{next_steps}} | documents[0].next_steps | 배열을 개조식 문자열로 변환 |
| {{action_items}} | documents[0].action_items | 조치사항 목록 문자열 |
| {{missing_fields}} | missing_fields | 확인 필요 항목 목록 |
| {{checklist}} | documents[0].checklist 또는 checklist | 검토 항목 목록 |
| {{security_review}} | security_review | 보안 검토 요약 |
| {{draft_status}} | draft_status | 초안 상태 |
| {{human_review_required}} | human_review_required | 사람 검토 필요 여부 |

렌더링 후보 템플릿은 templates/hwpx/placeholder_one_page_report.hwpx입니다.

해당 템플릿이 없으면 실제 HWPX 생성을 시도하지 않고 template_required 상태로 중단합니다.

## Step 32 완료 기준

- one_page_report placeholder 전략이 문서화됨
- HWPX 렌더러가 one_page_report를 처리할 수 있도록 준비됨
- 실제 HWPX 파일은 Git에 추가하지 않음
- 실제 원문이나 개인정보를 추가하지 않음

## 원페이지 보고서 렌더링 준비 테스트 결과

| 항목 | 결과 | 판정 |
|---|---|---|
| sample_one_page_report.json 존재 여부 | examples/json/sample_one_page_report.json 확인됨 | 통과 |
| placeholder_one_page_report.hwpx 존재 여부 | templates/hwpx/placeholder_one_page_report.hwpx 없음 | template_required |
| 보안 검증 결과 | validate_for_hwpx_rendering 통과, 차단 사유 없음 | 통과 |
| 렌더링 수행 여부 | 템플릿이 없어 HWPX placeholder 치환 및 output 생성 미수행 | 안전 중단 |
| output Git 제외 여부 | renderers/hwpx_renderer/output/.gitignore에서 *.hwpx, *.json, *.md 제외 확인 | 통과 |

## 현재 결과 해석

현재 templates/hwpx/placeholder_one_page_report.hwpx 템플릿이 없으므로 HWPX 생성은 수행하지 않았습니다.

렌더러는 one_page_report 입력을 식별하고 placeholder map을 구성할 수 있도록 준비되어 있으며, 템플릿이 없는 경우 template_required 상태로 중단하는 흐름을 사용합니다.

원페이지 보고서 렌더링 시도 중 기존 template_required_report.md 재작성 단계에서 파일 권한 오류가 발생했으나, 이는 output 보고서 파일 재작성 단계의 문제이며 HWPX output은 생성되지 않았습니다.

다음 단계에서는 실제 기관 양식이 아닌 로컬 placeholder HWPX 템플릿을 수동 준비한 뒤, 보안 검수 후 placeholder 치환 결과와 남은 placeholder 수를 기록해야 합니다.

## Step 32 결론

Step 32는 원페이지 보고서 HWPX 자동화를 위한 placeholder 전략과 렌더러 준비 단계입니다.

다음 단계에서는 사용자가 로컬에서 placeholder_one_page_report.hwpx 테스트 템플릿을 수동으로 준비한 뒤 치환 테스트를 수행할 수 있습니다.
