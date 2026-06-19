# 실제 HWPX 렌더링 연결 여부 결정

## 목적

이 문서는 입력 정규화 PoC에서 생성한 HWPX payload를 실제 HWPX 렌더러에 연결할지 여부와 사용자 확인 지점을 정합니다.

현재까지는 mapper payload가 validation과 dry-run을 통과했지만, 실제 HWPX 파일 생성은 사용자가 한컴에서 열람해야 하는 단계이므로 별도 gate로 분리합니다.

## 결론

실제 HWPX 렌더링 연결 테스트는 가능하지만, 바로 자동 실행하지 않습니다.

다음 단계에서는 사용자가 허용한 경우에만 `ready_for_draft` 케이스 1건부터 실제 HWPX 생성 테스트를 진행합니다.

우선 대상:

- `safe_one_page_report_request.json`
- routing: `ready_for_draft`
- document_type: `one_page_report`
- template 후보: `templates/hwpx/placeholder_one_page_report.hwpx`

보류 대상:

- `needs_more_input` 케이스는 실제값이 부족하므로 HWPX 생성 전 사람이 목적과 사용 방식을 확인합니다.
- `needs_security_review` 케이스는 렌더링하지 않습니다.
- `blocked` 케이스는 렌더링하지 않습니다.

## 렌더링 허용 기준

| routing | 실제 HWPX 생성 | 판단 |
|---|---|---|
| `ready_for_draft` | 조건부 허용 | 사용자 확인 후 1건부터 테스트 |
| `needs_more_input` | 보류 | `[확인 필요]` 렌더링 목적이 명확할 때만 허용 |
| `needs_security_review` | 금지 | 사람 보안 검토 전 렌더링 금지 |
| `blocked` | 금지 | 처리 중단 |

## 사용자 확인 필요 지점

실제 HWPX 생성 전 사용자가 확인해야 할 사항:

- 로컬 placeholder 템플릿이 준비되어 있는가
- output HWPX가 GitHub Desktop Changes에 나타나지 않는가
- 생성된 HWPX를 한컴에서 직접 열어볼 수 있는가
- 글자 겹침, 줄바꿈, 문단 간격, placeholder 잔존 여부를 확인할 수 있는가
- 실제 원문, 개인정보, 실제 기관 양식 원본이 사용되지 않았는가

## 연결 방식

권장 방식은 기존 `renderers/hwpx_renderer/render_hwpx_poc.py`를 바로 수정하지 않고, normalizers 쪽에 별도 연결 PoC를 둡니다.

권장 파일:

```text
normalizers/render_mapped_hwpx_poc.py
```

역할:

1. `safe_one_page_report_request.json`을 정규화
2. HWPX payload로 매핑
3. 기존 HWPX validation 실행
4. template 존재 여부 확인
5. `replace_placeholders_in_hwpx` 호출
6. output HWPX를 `renderers/hwpx_renderer/output/`에 생성
7. summary JSON은 `normalizers/output/`에 생성

## output 정책

생성될 수 있는 파일:

- `renderers/hwpx_renderer/output/mapped_safe_one_page_report_poc.hwpx`
- `normalizers/output/mapped_hwpx_render_summary.json`

두 산출물은 Git 제외 대상이어야 합니다.

## 중단 조건

다음 중 하나라도 해당하면 실제 HWPX 생성 테스트를 중단합니다.

- template 후보가 없음
- validation 실패
- routing이 `ready_for_draft`가 아님
- 실제 원문 또는 개인정보 의심
- output HWPX가 Git 추적 대상으로 나타남
- 사용자가 한컴 열람 확인을 진행할 수 없는 상태

## 다음 단계

다음 단계는 사용자가 허용하면 `normalizers/render_mapped_hwpx_poc.py`를 작성하고, `ready_for_draft` 원페이지 보고서 1건만 실제 HWPX 생성 테스트를 진행하는 것입니다.

사용자 확인이 필요한 단계이므로 자동으로 대량 렌더링하지 않습니다.
