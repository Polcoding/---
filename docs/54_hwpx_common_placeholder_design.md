# HWPX 공통 placeholder 설계

## 목적

이 문서는 HWPX 보고서 템플릿에서 공통으로 사용할 placeholder 설계 원칙을 정리합니다.

AI는 내용과 구조를 만들고, HWPX 템플릿은 폰트, 자간, 줄간격, 표, 문단 배치를 담당합니다.

## 설계 원칙

- placeholder는 실제 값이 아니라 JSON 필드와 템플릿 위치를 연결하는 식별자입니다.
- 실제 기관명, 실제 문서번호, 실제 담당자명, 실제 연락처를 placeholder 이름에 넣지 않습니다.
- 확인되지 않은 값은 `[확인 필요]`, `null`, 또는 안전한 빈 문자열로 처리합니다.
- 여러 줄이 들어갈 placeholder는 가능한 한 독립 문단에 둡니다.
- 글자 겹침이 생기면 실제 서식값을 임의로 만들지 않고, placeholder 배치나 문자열 변환 범위를 줄입니다.
- HWPX 템플릿은 로컬에만 두고 Git에 추가하지 않습니다.

## 공통 메타 placeholder

| placeholder | 용도 | 비고 |
|---|---|---|
| `{{title}}` | 문서 제목 | 모든 보고서 공통 |
| `{{document_number}}` | 문서번호 | 미확인 시 `[확인 필요]` |
| `{{execution_date}}` | 시행일자 또는 작성일 | 미확인 시 `[확인 필요]` |
| `{{recipient}}` | 수신처 | 공문 계열에서 사용 |
| `{{reference}}` | 참조 | 공문 계열에서 사용 |
| `{{attachments}}` | 붙임 | 없으면 빈 문자열 또는 `[확인 필요]` |
| `{{missing_fields}}` | 확인 필요 사항 | 검토용 메타 |
| `{{checklist}}` | 검토 체크리스트 | 검토용 메타 |
| `{{security_review}}` | 보안 검토 결과 | 검토용 메타 |
| `{{draft_status}}` | 초안 상태 | 검토용 메타 |
| `{{human_review_required}}` | 사람 검토 필요 여부 | 항상 사람 검토 전제 |

## 보고서 공통 placeholder

| placeholder | 용도 |
|---|---|
| `{{background}}` | 추진 배경 또는 검토 배경 |
| `{{purpose}}` | 추진 목적 |
| `{{overview_table}}` | 추진개요 표 |
| `{{main_contents}}` | 주요 내용 |
| `{{review_items}}` | 검토 항목 |
| `{{future_plan}}` | 향후 계획 |
| `{{schedule_table}}` | 일정 표 |
| `{{budget_table}}` | 예산 표 |

## 문서 유형별 핵심 placeholder

### 원페이지 보고서

| placeholder | 용도 |
|---|---|
| `{{report_summary}}` | 보고 개요 |
| `{{main_points}}` | 주요 내용 |
| `{{review_opinion}}` | 검토 의견 |
| `{{issues_or_considerations}}` | 문제점 및 고려사항 |
| `{{next_steps}}` | 향후 계획 |
| `{{action_items}}` | 조치 필요사항 |

### 추진계획서

| placeholder | 용도 |
|---|---|
| `{{background}}` | 추진 배경 |
| `{{purpose}}` | 추진 목적 |
| `{{overview_table}}` | 추진 개요 |
| `{{main_contents}}` | 주요 내용 |
| `{{detailed_plan}}` | 세부 추진계획 |
| `{{schedule_table}}` | 추진 일정 |
| `{{budget_table}}` | 소요 예산 |
| `{{expected_effects}}` | 기대 효과 |
| `{{review_items}}` | 검토 사항 |
| `{{future_plan}}` | 향후 계획 |

### 결과보고서

| placeholder | 용도 |
|---|---|
| `{{linked_plan_reference}}` | 기존 계획 연결 |
| `{{planned_items}}` | 계획 항목 |
| `{{actual_results}}` | 실제 결과 |
| `{{comparison_to_plan}}` | 계획 대비 결과 |
| `{{main_outcomes}}` | 주요 성과 |
| `{{issues}}` | 문제점 |
| `{{improvements}}` | 개선사항 |
| `{{future_plan}}` | 향후 계획 |

### 검토보고서

| placeholder | 용도 |
|---|---|
| `{{review_background}}` | 검토 배경 |
| `{{review_scope}}` | 검토 범위 |
| `{{review_items}}` | 검토 항목 |
| `{{review_opinion}}` | 검토 의견 |
| `{{risks}}` | 위험요소 |
| `{{required_reviews}}` | 필요 검토 |
| `{{next_actions}}` | 후속조치 |

## 배열 필드 변환 원칙

JSON 배열은 HWPX에 넣기 전에 개조식 문자열로 변환합니다.

권장 형식:

```text
- [항목 1]
- [항목 2]
- [확인 필요]
```

주의사항:

- 항목 수가 많으면 HWPX 문단 겹침 가능성이 커집니다.
- 원페이지 보고서처럼 짧은 양식은 핵심 항목만 출력합니다.
- 상세 데이터는 별도 붙임 또는 XLSX 조사표로 분리하는 것을 검토합니다.
- 예산, 일정, 실적, 담당자, 수량은 입력값이 없으면 임의로 만들지 않습니다.

## HWPX 배치 원칙

- `{{title}}`은 제목 문단에 둡니다.
- 본문 placeholder는 가능한 한 서로 다른 문단에 둡니다.
- 표 영역 placeholder는 표 안 셀 하나에 과도하게 긴 배열을 넣지 않습니다.
- 붙임 영역은 본문 영역과 분리합니다.
- 검토용 메타 placeholder는 실제 제출 본문에 바로 노출하지 않는 구성을 우선합니다.

## 겹침 발생 시 조정 순서

1. placeholder가 같은 문단에 과도하게 몰려 있는지 확인합니다.
2. 배열 필드 출력 항목 수를 줄입니다.
3. 긴 설명문을 짧은 개조식으로 바꿉니다.
4. 문단별 placeholder를 더 세분화합니다.
5. 실제 기관 서식값은 확인 전까지 임의로 변경하지 않습니다.

## 금지 사항

- 실제 기관 양식 원본 Git 추가
- 실제 공문 또는 보고서 원문 복사
- 실제 개인정보, 민원정보, 내부 운영정보 사용
- 실제 문서번호, 시행일자, 담당자명, 연락처 사용
- 확인되지 않은 서식값 임의 생성
- output HWPX를 Git에 추가
- 이메일/API/Make.com 자동화와 연결
