# mapped review_report HWPX 렌더링 결과

## 목적

보안 검토가 필요한 `review_report`는 기본적으로 실제 HWPX 렌더링을 차단합니다.

이 문서는 placeholder 보안 승인 신호가 있는 fixture 1건만 대상으로 실제 HWPX 렌더링 연결을 확인합니다.

## 대상

| 항목 | 값 |
|---|---|
| fixture | `normalizers/fixtures/approved_review_report_request.json` |
| routing | `ready_for_draft` |
| document_type | `review_report` |
| template | `templates/hwpx/placeholder_review_report.hwpx` |
| output | `renderers/hwpx_renderer/output/mapped_approved_review_report_poc.hwpx` |

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

- `renderers/hwpx_renderer/output/mapped_approved_review_report_poc.hwpx`: Git 제외 대상
- `normalizers/output/mapped_hwpx_render_summary.json`: Git 제외 대상
- 로컬 HWPX 템플릿: Git 제외 대상

## 보안 검수

- 실제 기관 양식 원본 사용 여부: 사용하지 않음
- 실제 문서 원문 사용 여부: 사용하지 않음
- 실제 개인정보 사용 여부: 사용하지 않음
- 실제 기관명, 업체명, 담당자명 사용 여부: 사용하지 않음
- 실제 승인자명, 결재번호, 문서번호 사용 여부: 사용하지 않음
- 실제 검토의견 원문 사용 여부: 사용하지 않음
- 실제 예산액, 일정, 실적 수치 생성 여부: 생성하지 않음
- Email/API/Make.com 연동 여부: 수행하지 않음

## 사용자 수동 검수 결과

사용자가 생성된 HWPX를 한컴에서 직접 열람했습니다.

확인 결과:

- 파일 열림: 정상
- 글자 겹침: 없음
- 1~10번 항목 제목 표시: 정상
- 검토 배경, 검토 범위, 검토 항목, 검토 의견, 위험 요소, 필요 검토, 향후 조치 표시: 정상
- 내용 앞 `-` 표기: 5번 위험요소 항목 보정 후 정상
- 남은 `{{placeholder}}`: 없음

## 결론

placeholder 보안 승인 신호가 있는 `review_report` 1건은 자동 치환과 한컴 수동 검수 기준으로 HWPX 렌더링에 성공했습니다.

다음 단계는 HWPX 4종 mapped 렌더링 완료 상태를 통합 문서로 정리하는 것입니다.
