# HWPX 최소 PoC 렌더러 안내

## 목적

이 폴더는 HWPX 템플릿을 읽고, 비식별 초안을 검토용 HWPX로 생성하기 위한 최소 PoC 코드를 보관합니다.

기본 경로는 placeholder 기반 HWPX 템플릿 치환입니다. 추가로, 사용자가 제공한 placeholder 없는 샘플 HWPX에서 샘플별 anchor profile을 찾아 비식별 초안 문단을 영역별로 주입하는 로컬 PoC도 포함합니다.

## 현재 범위

- HWPX 템플릿 파일 존재 여부 확인
- HWPX 패키지 구조 검사
- XML 파일 내 placeholder 탐색
- 허용된 placeholder만 치환
- 보안 검증 통과 시에만 렌더링
- 템플릿이 없으면 렌더링 중단 및 보고
- 보고서 4종 샘플의 placeholder 기반 치환 검증
- placeholder 없는 샘플 HWPX에 profile-aware 비식별 초안 문단 분산 주입
- 샘플양식1/2 전용 anchor profile 기반 영역별 분산 주입
- 저장소 밖 샘플 HWPX를 `--template` 인자로 받아 ignored output 생성

## 현재 단계에서 하지 않는 것

- 실제 기관 HWPX 양식 사용
- 실제 업무용 또는 발송용 HWPX 생성
- 실제 공문 원문 처리
- 실제 개인정보 처리
- placeholder 없는 실제 기관 양식의 표/본문 영역별 자동 재배치
- HWPX 표 내부 실제 데이터 자동 입력
- Excel/한셀 자동 연동
- `table_data_candidate` 필드나 HWPX payload 구조 확장
- API 호출
- 이메일 자동화
- Make.com 자동화

## 입력

- examples/json/sample_official_letter.json
- examples/json/sample_one_page_report.json
- examples/json/sample_project_plan.json
- examples/json/sample_result_report.json
- examples/json/sample_review_report.json
- templates/hwpx/placeholder 템플릿 파일
- 저장소 밖 비식별 샘플 HWPX 파일

`renderer_hints.table_template`은 서식 또는 표시 후보 힌트입니다. 실제 표 데이터, 물품명, 수량, 금액, 대상 목록을 자동 입력하라는 의미가 아닙니다.

placeholder 없는 샘플 HWPX에 비식별 초안을 주입할 때는 다음 형식을 사용합니다.

```powershell
python .\renderers\hwpx_renderer\render_autofill_sample_poc.py --template "[저장소 밖 샘플 HWPX 경로]" --topic "[비식별 주제]" --output .\renderers\hwpx_renderer\output\autofill_sample_poc.hwpx
```

이 명령은 외부 AI 호출 없이 `[확인 필요]` 중심의 비식별 초안 문단을 샘플양식별 anchor profile에 따라 HWPX section XML의 해당 영역 뒤에 추가합니다. anchor 후보를 찾지 못하면 안전하게 section 끝에 추가합니다.

샘플양식1처럼 목차와 본문에 같은 제목이 반복되는 양식은 본문 쪽 마지막 anchor를 사용하며, 삽입 줄의 첫 기호(`-`, `□`, `○`, `❍`, `※`)와 맞는 문단 스타일을 우선 복제합니다.

샘플양식2처럼 템플릿이 이미 `❍` 문단 bullet을 제공하는 양식은 내용 문자열에 `-`를 붙이지 않아 bullet 중복을 피합니다.

샘플양식 2종을 한 번에 생성할 때는 다음 명령을 사용합니다.

```powershell
python .\renderers\hwpx_renderer\render_autofill_batch_poc.py --topic "[비식별 주제]"
```

간단 실행은 `--topic` 없이 주제만 넣어도 됩니다.

```powershell
python .\renderers\hwpx_renderer\render_autofill_batch_poc.py "[비식별 주제]"
```

선택 입력을 일부 제공하면 해당 값만 반영하고, 나머지는 `[확인 필요]`로 남깁니다.

```powershell
python .\renderers\hwpx_renderer\render_autofill_batch_poc.py "[비식별 주제]" --purpose "[비식별 목적]" --target "[비식별 대상]" --period "[확인된 범위의 기간]" --cooperation "[비식별 협조사항]"
```

샘플양식1에는 `--background`, `--scope`도 선택적으로 반영할 수 있습니다. 실제 연락처, 실제 문서번호, 실제 기관명, 실제 수량ㆍ금액처럼 보이는 값은 차단 대상입니다.

여러 비식별 주제로 샘플양식 1/2를 회귀검증할 때는 다음 명령을 사용합니다.

```powershell
python .\renderers\hwpx_renderer\render_autofill_regression_poc.py
```

이 명령은 기본 비식별 주제 4개를 샘플양식 1/2에 적용하고, ignored output 폴더 아래에 HWPX 8건과 `autofill_regression_summary.json`을 생성합니다.

## 출력

- renderers/hwpx_renderer/output/*.hwpx
- renderers/hwpx_renderer/output/*.json
- renderers/hwpx_renderer/output/*.md

## 주의

output 산출물은 로컬 테스트 결과이며 Git 추적 대상에서 제외합니다.

한컴에서 output 또는 로컬 placeholder HWPX를 여는 수동 preview는 `docs/150_manual_preview_resume_gate.md` 조건 충족 후에만 진행합니다. 이 renderer 안내는 실제 업무용 HWPX 생성 승인이나 실제 원본 투입 지시가 아닙니다.

output/.gitignore 내용:

```text
*.hwpx
*.hwp
*.json
*.md
!.gitkeep
```
