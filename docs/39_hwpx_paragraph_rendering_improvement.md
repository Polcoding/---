# HWPX 본문 문단 렌더링 개선

## 목적

Step 28 수동검수에서 발견된 HWPX 본문 문단 겹침, 번호체계 표시 불량, 자간ㆍ줄간격 문제를 개선하기 위한 문단별 placeholder 전략을 정리합니다.

## 발견된 문제

- {{body_sections}} 단일 placeholder에 여러 본문 문단이 한꺼번에 치환됨
- 1번 문단과 2번 문단이 붙어 보임
- 하위 항목 “가.”가 안정적으로 표시되지 않음
- 자간 또는 줄간격이 겹쳐 보여 공문서 본문으로 사용하기 어려움

## 원인

HWPX 템플릿의 한 문단 또는 한 텍스트 영역에 여러 문단 문자열을 삽입하면, HWPX 내부 문단 구조와 줄바꿈 구조가 제대로 유지되지 않을 수 있습니다.

## 개선 방향

- 본문 문단별 placeholder를 사용합니다.
- HWPX 템플릿에서 각 placeholder를 별도 문단에 배치합니다.
- 하위 항목도 별도 placeholder로 분리합니다.
- {{body_sections}}는 fallback 또는 간단 미리보기용으로만 사용합니다.

## 권장 placeholder 구조

```text
{{body_section_1}}

{{body_section_2}}

  {{body_section_2_child_1}}

{{body_section_3}}
```

## 렌더러 보강 내용

- body_sections 배열을 문단별 placeholder map으로 변환합니다.
- children 항목은 child placeholder로 변환합니다.
- 기존 {{body_sections}}는 fallback 용도로 유지합니다.
- HWPX 템플릿이 문단별 placeholder를 사용할 경우 각 문단이 별도 문단으로 유지될 수 있습니다.
- 실제 문단 표시 품질은 한컴에서 수동 검수해야 합니다.

## 로컬 HWPX 템플릿 수정 필요 사항

기존 템플릿에 {{body_sections}} 하나만 있는 경우 문단 겹침이 재발할 수 있습니다.

로컬 HWPX 템플릿을 다음 구조로 수정해야 합니다.

```text
{{body_section_1}}

{{body_section_2}}

  {{body_section_2_child_1}}

붙임  {{attachments}}

{{checklist}}
```

주의:

- 로컬 HWPX 템플릿은 Git에 포함하지 않습니다.
- 실제 기관 양식을 사용하지 않습니다.

## 문단별 placeholder 재테스트 결과

| 항목 | 결과 | 판정 |
|---|---|---|
| 로컬 템플릿 존재 여부 | templates/hwpx/placeholder_official_letter.hwpx 존재 | 통과 |
| 템플릿 Git 제외 여부 | .gitignore에 따라 로컬 템플릿이 ignored 상태 | 통과 |
| HWPX 렌더러 실행 여부 | renderers/hwpx_renderer/render_hwpx_poc.py 실행 완료 | 통과 |
| 문단별 placeholder 치환 여부 | body section 2개, child placeholder 1개 생성 및 치환 | 통과 |
| 남은 placeholder 여부 | remaining_placeholders 0개 | 통과 |
| output HWPX Git 제외 여부 | output .hwpx가 ignored 상태 | 통과 |
| 수동 문단 분리 확인 | 1번 문단과 2번 문단이 정상적으로 분리되어 보임 | 통과 |
| 하위 항목 표시 확인 | “가. 제출방법”이 별도 하위 항목으로 정상 표시됨 | 통과 |
| 자간ㆍ줄간격 확인 | 글자가 겹쳐 보이는 문제는 확인되지 않음 | 통과 |
| 붙임 표기 확인 | 붙임 표기가 정상적으로 표시됨 | 통과 |

## 다음 수동 검수 필요 사항

- 기관 표준 글꼴, 자간, 줄간격, 문단 간격 기준값 확인
- 실제 기관 템플릿 적용 전 테스트 전용 템플릿과 기관 표준 서식 차이 검토

## Step 29 결론

HWPX 본문 문단 분리 개선 1차 성공

문단별 placeholder 구조 적용 후 1번 문단과 2번 문단이 분리되어 보이고, 하위 항목 “가. 제출방법”도 별도 하위 항목으로 정상 표시되는 것을 수동 확인했습니다.

남은 보완사항은 실제 기관 표준 서식값 확인입니다.

## Step 29 완료 기준

- 문단별 placeholder 전략이 문서화됨
- 렌더러가 문단별 placeholder map을 만들 수 있도록 보강됨
- 로컬 HWPX 템플릿을 문단별 placeholder 구조로 수정할 수 있음
- 실제 원문이나 개인정보를 추가하지 않음
- 실제 HWPX output은 Git에 포함하지 않음

## Step 29 완료 체크리스트

- [x] 단일 body_sections 치환 한계가 문서화되었는가
- [x] 문단별 placeholder 전략이 작성되었는가
- [x] 렌더러가 문단별 placeholder map을 생성하는가
- [x] 기존 body_sections fallback이 유지되는가
- [x] 로컬 HWPX 템플릿 수정 필요 사항이 문서화되었는가
- [x] 실제 원문이나 개인정보를 추가하지 않았는가
- [x] 실제 HWPX 템플릿 파일을 Git에 추가하지 않았는가
- [x] README 링크가 반영되었는가
