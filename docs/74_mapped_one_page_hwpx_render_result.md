# mapped one_page_report HWPX 렌더링 결과

## 목적

입력 정규화 PoC에서 생성한 `ready_for_draft` 원페이지 보고서 payload를 실제 HWPX 렌더러에 연결해 1건만 렌더링합니다.

이번 단계에서는 실제 원문, 실제 개인정보, 실제 기관 양식 원본을 사용하지 않았습니다.

## 대상

| 항목 | 값 |
|---|---|
| fixture | `normalizers/fixtures/safe_one_page_report_request.json` |
| routing | `ready_for_draft` |
| document_type | `one_page_report` |
| template | `templates/hwpx/placeholder_one_page_report.hwpx` |
| output | `renderers/hwpx_renderer/output/mapped_safe_one_page_report_poc.hwpx` |

## 실행 결과

Codex 번들 Python으로 `normalizers/render_mapped_hwpx_poc.py`를 실행했습니다.

| 항목 | 결과 |
|---|---|
| status | `rendered` |
| replaced_count | 16 |
| remaining_placeholders | 0 |
| errors | 없음 |

처리된 text-like 파일:

- `version.xml`
- `Contents/header.xml`
- `Contents/section0.xml`
- `Preview/PrvText.txt`
- `settings.xml`
- `META-INF/container.xml`
- `META-INF/manifest.xml`

## Git 제외 확인

- `renderers/hwpx_renderer/output/mapped_safe_one_page_report_poc.hwpx`: Git 제외 대상
- `normalizers/output/mapped_hwpx_render_summary.json`: Git 제외 대상
- 로컬 HWPX 템플릿: Git 제외 대상

## 보안 검수

- 실제 기관 양식 원본 사용 여부: 사용하지 않음
- 실제 문서 원문 사용 여부: 사용하지 않음
- 실제 개인정보 사용 여부: 사용하지 않음
- 실제 기관명, 업체명, 담당자명 사용 여부: 사용하지 않음
- 실제 문서번호, 민원번호, 접수번호, 사건번호 사용 여부: 사용하지 않음
- 실제 예산액, 실적 수치, 수량 생성 여부: 생성하지 않음
- Email/API/Make.com 연동 여부: 수행하지 않음

## 사용자 수동 검수 필요

생성된 HWPX는 한컴에서 직접 열람해야 합니다.

확인 대상:

- 파일 열림 여부
- 글자 겹침 여부
- 줄바꿈과 문단 간격
- 제목과 항목 배치
- `[확인 필요]` 표시가 의도대로 보이는지
- 남은 `{{placeholder}}`가 없는지

## 결론

정규화 결과에서 생성된 mapper payload를 실제 HWPX 렌더러에 연결해 원페이지 보고서 1건을 생성했습니다.

자동 치환 기준으로는 성공이며, 다음 단계는 사용자의 한컴 수동 열람 검수입니다.
