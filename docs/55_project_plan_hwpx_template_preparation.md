# 추진계획서 HWPX 최소 템플릿 준비

## 목적

이 문서는 `project_plan` 문서 유형의 로컬 HWPX placeholder 템플릿을 준비하기 위한 기준을 정리합니다.

원페이지 보고서, 결과보고서, 검토보고서 로컬 치환 검수 이후 남아 있는 핵심 HWPX 보고서 유형은 추진계획서입니다.

## 현재 확인 결과

- `examples/json/sample_project_plan.json` 존재 확인
- `renderers/hwpx_renderer/render_hwpx_poc.py`의 `SAMPLES`에 `sample_project_plan.json` 등록 확인
- 템플릿 후보 `templates/hwpx/placeholder_project_plan.hwpx` 인식 확인
- 로컬 placeholder 템플릿 생성 완료
- 템플릿 준비 후 `project_plan` 렌더링 성공 확인
- `templates/hwpx/*.hwpx`는 Git 제외 확인
- `renderers/hwpx_renderer/output/*.hwpx`, `*.json`, `*.md`는 Git 제외 확인
- 일반 샌드박스 권한에서는 ignored 템플릿/output 폴더 쓰기가 거부될 수 있어 승인 권한으로 렌더러 실행 확인

## 지원 placeholder

현재 렌더러의 공통 placeholder map으로 다음 항목을 지원합니다.

- `{{title}}`
- `{{background}}`
- `{{purpose}}`
- `{{overview_table}}`
- `{{main_contents}}`
- `{{detailed_plan}}`
- `{{schedule_table}}`
- `{{budget_table}}`
- `{{expected_effects}}`
- `{{review_items}}`
- `{{future_plan}}`
- `{{attachments}}`
- `{{checklist}}`
- `{{missing_fields}}`
- `{{security_review}}`
- `{{draft_status}}`
- `{{human_review_required}}`

## 준비할 로컬 파일

- `templates/hwpx/placeholder_project_plan.hwpx`

이 파일은 로컬 검증용 HWPX 템플릿이며 Git에 추가하지 않습니다.

## 한컴 템플릿 최소 내용

각 placeholder는 가능한 한 서로 다른 문단에 배치합니다.

```text
{{title}}

1. 추진 배경
{{background}}

2. 추진 목적
{{purpose}}

3. 추진 개요
{{overview_table}}

4. 주요 내용
{{main_contents}}

5. 세부 추진계획
{{detailed_plan}}

6. 추진 일정
{{schedule_table}}

7. 소요 예산
{{budget_table}}

8. 기대 효과
{{expected_effects}}

9. 검토 사항
{{review_items}}

10. 향후 계획
{{future_plan}}
```

## 선택 placeholder

아래 항목은 검토용 메타정보입니다.

실제 제출 본문에 그대로 노출하지 않을 경우 템플릿에 넣지 않아도 됩니다.

```text
확인 필요 사항
{{missing_fields}}

검토 체크리스트
{{checklist}}

보안 검토
{{security_review}}

초안 상태
{{draft_status}}

사람 검토 필요 여부
{{human_review_required}}
```

## 작성 주의사항

- 실제 기관 양식 원본을 사용하지 않습니다.
- 실제 추진계획서 원문을 사용하지 않습니다.
- 실제 기관명, 담당자명, 연락처, 문서번호를 넣지 않습니다.
- 예산, 일정, 수량, 담당자를 임의로 작성하지 않습니다.
- 여러 줄 placeholder는 서로 다른 문단에 배치합니다.
- 표 서식값이 확인되지 않았으면 임의로 만들지 않습니다.
- `overview_table`, `schedule_table`, `budget_table`은 처음에는 텍스트 치환으로 검증하고, 실제 표 구조 자동화는 별도 단계에서 검토합니다.

## 렌더링 확인 항목

1. `templates/hwpx/placeholder_project_plan.hwpx`가 존재하는지
2. 해당 파일이 GitHub Desktop Changes에 나타나지 않는지
3. HWPX zip 패키지로 열리는지
4. 위 placeholder가 템플릿에 포함되어 있는지
5. 렌더러 실행 결과가 `rendered`인지
6. `remaining_placeholders`가 `[]`인지
7. output HWPX가 GitHub Desktop Changes에 나타나지 않는지
8. 한컴 열람 시 글자 겹침, 줄간격, 문단 간격 문제가 없는지

## 로컬 실행 전 확인

현재 세션에서는 일반 샌드박스 권한으로 `renderers/hwpx_renderer/output/` 폴더에 새 파일을 쓰는 작업이 거부되었습니다.

렌더링을 다시 실행하기 전에 다음을 확인합니다.

- 한컴에서 기존 output HWPX 파일을 모두 닫았는지
- output 폴더나 파일이 읽기 전용 또는 보호 상태가 아닌지
- GitHub Desktop, 백신, 동기화 프로그램이 output 폴더를 잠그고 있지 않은지
- output 폴더의 파일이 Git에 추적되지 않고 ignored 상태인지

## 현재 결론

`project_plan`은 코드상 템플릿 후보와 주요 placeholder를 이미 지원합니다.

현재 필요한 작업은 생성된 output HWPX를 한컴에서 열어 수동 열람 검수를 진행하는 것입니다.
