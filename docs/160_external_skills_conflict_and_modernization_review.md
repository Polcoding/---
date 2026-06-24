# 외부 skill 충돌 점검과 구현 전환 검토

## 목적

기존 저장소 작업 방식과 새로 설치ㆍ검토한 외부 skill, `hwpx-cli`가 서로 충돌하지 않는지 확인하고, 구식으로 남아 있던 수동 확인 방식을 구현 가능한 저장소 내부 PoC로 전환합니다.

## 결론

현재 저장소의 핵심 흐름은 유지합니다.

다만 외부 skill과 `hwpx-cli`에서 확인한 HWPX 패키지 구조 분석 방식과 샘플 HWPX 자동 채우기 최소 흐름은 저장소 내부 Python PoC로 흡수했습니다.

즉, Node 기반 `hwpx-cli`를 운영 의존성으로 넣지 않고도 HWPX section, paragraph, table, placeholder 구조를 자동 확인하고, placeholder 없는 샘플 HWPX에도 샘플별 anchor profile에 따라 비식별 초안 문단을 영역별로 주입할 수 있게 했습니다.

## 충돌 점검 결과

| 항목 | 판단 | 처리 |
|---|---|---|
| 기존 Python renderer | 유지ㆍ확장 | placeholder 치환과 placeholder-free profile-aware 샘플 주입 output 생성 담당 |
| normalizers PoC | 유지ㆍ확장 | HWPX template 구조 분석 PoC 추가 |
| Codex skill | 참고 | 작업 절차와 구조 분석 아이디어만 반영 |
| `hwpx-cli` | 저장소 밖 보조 도구 | 운영 의존성으로 추가하지 않음 |
| MCP | 보류 | 현재 단계에서 켜지 않음 |
| `hwpx-cli read`, `hwpx-to-md` | 제한 | 실제 원문 또는 실제 기관 양식에는 실행 금지 |
| 수동 구조 확인만 하던 방식 | 교체 | Python 구조 분석기로 자동 확인 |
| placeholder 없는 샘플 HWPX | 부분 지원 | 샘플별 anchor profile 기반 비식별 초안 분산 주입 PoC로 local output 생성 |

## 새로 구현한 내부 PoC

파일:

- `normalizers/hwpx_template_structure_analyzer_poc.py`
- `normalizers/test_hwpx_template_structure_analyzer_poc.py`
- `renderers/hwpx_renderer/autofill_package.py`
- `renderers/hwpx_renderer/render_autofill_sample_poc.py`
- `renderers/hwpx_renderer/test_autofill_package.py`

기능:

- HWPX를 ZIP 패키지로 열기
- `Contents/section*.xml` 탐색
- XML parser 기반 section, paragraph, text node, table 수 확인
- `{{placeholder}}` 후보 목록 확인
- 한컴 서식 분리로 같은 문단 안에서 여러 text node로 나뉜 placeholder 감지
- `Preview/PrvText.txt`는 존재와 길이만 확인하고 본문을 저장하지 않음
- missing template은 `template_required`로 안전 중단
- 결과 summary는 `normalizers/output/`에 ignored 산출물로만 저장
- `--template ... --no-output`으로 저장소 밖 비식별 후보를 파일 출력 없이 선확인
- placeholder 없는 샘플 HWPX는 기존 패키지를 복사하고 첫 section XML의 샘플별 anchor profile 뒤에 비식별 초안 문단을 분산 추가
- 샘플 autofill output은 `renderers/hwpx_renderer/output/`의 ignored HWPX로만 생성

## 왜 전면 교체하지 않았는가

전면 교체하지 않은 대상은 실제 운영 안전성과 직접 연결된 부분입니다.

- 기존 Python renderer는 이미 보고서 4종 placeholder 치환 검증을 통과했습니다.
- `hwpx-cli`는 빌드와 `info` 실행은 확인했지만 npm 배포와 Windows checkout 문제가 남아 있습니다.
- 외부 skill은 구조 설명 중심이며, 저장소 보안 원칙보다 우선할 수 없습니다.

따라서 교체 기준은 다음처럼 잡습니다.

```text
구조 분석: 외부 아이디어를 내부 Python PoC로 흡수
렌더링: 기존 Python renderer 유지ㆍ확장
샘플 자동 채우기: placeholder-free HWPX에는 profile-aware 비식별 초안 문단 분산 주입 PoC 적용
외부 도구: 저장소 밖 비교ㆍ참고 후보
실제 원문 처리: 계속 금지
```

## 실행 결과

구조 분석기 테스트:

```text
Ran 4 tests
OK
```

local template 후보 4종 분석 결과:

| 문서 유형 | 상태 | section | paragraph | table | placeholder |
|---|---|---:|---:|---:|---:|
| `one_page_report` | analyzed | 1 | 22 | 0 | 8 |
| `project_plan` | analyzed | 1 | 31 | 0 | 11 |
| `result_report` | analyzed | 1 | 28 | 0 | 10 |
| `review_report` | analyzed | 1 | 22 | 0 | 8 |

placeholder 없는 샘플 HWPX autofill 테스트:

```text
Ran 8 tests
OK
```

제공 샘플 HWPX 2종 로컬 실행 결과:

| 샘플 | 상태 | 삽입 문단 | 출력 |
|---|---|---:|---|
| 샘플 HWPX 1 | rendered | 11 | 5개 anchor 영역, 표 13→13 |
| 샘플 HWPX 2 | rendered | 12 | 5개 anchor 영역, 표 2→2 |

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 실제 문서번호 추가 없음
- 실제 공문 또는 보고서 원문 추가 없음
- 실제 HWPX/HWP 원본 추가 없음
- `hwpx-cli` Node 의존성 저장소 추가 없음
- 구조 분석 결과는 본문 텍스트가 아니라 메타정보만 기록
- 샘플 autofill output은 Git 제외 폴더에만 생성
- 샘플 원본 HWPX는 저장소에 복사하지 않음

## 다음 판단

다음 단계는 외부 도구를 더 붙이는 것이 아니라, 새 Python 구조 분석기와 placeholder-free profile-aware 샘플 주입 PoC를 수동 preview 재개 게이트와 template intake 체크리스트의 보조 확인 항목으로 사용하는 것입니다.

실제 비식별 HWPX 작업 복사본이 준비되기 전까지는 `read`, `hwpx-to-md`, MCP, 실제 원문 기반 자동 변환은 계속 보류합니다.
