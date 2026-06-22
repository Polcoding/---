# Phase 2 반복 운영 기준

## 목적

Phase 2 최소 PoC 수동 리허설이 통과된 상태를 기준으로, 이후 같은 흐름을 반복 실행할 때 매번 확인할 기준을 정리합니다.

이 문서는 운영 자동화 승인 문서가 아닙니다. 현재 단계는 placeholder 기반 로컬 PoC 반복 실행 기준을 고정하는 단계입니다.

## 현재 기준 상태

현재 저장소의 기준 상태:

- HWPX 보고서 4종 placeholder 기반 렌더링 완료
- mapped HWPX 보고서 4종 한컴 수동 검수 완료
- Phase 2 수동 리허설 1회 완료
- `remaining_placeholders` 0 확인
- output 및 로컬 HWPX 템플릿 Git 제외 확인
- `placeholder_confirmed_values` helper는 read-only 검증용으로 유지
- API, Make.com, Email 자동화는 보류

## 반복 실행 시 매번 확인할 기준

### Codex 확인 항목

Codex는 반복 실행 전에 다음을 확인합니다.

```powershell
git status --short
git status --short --ignored normalizers\output renderers\hwpx_renderer\output templates\hwpx
```

확인 기준:

- 추적 중인 변경 파일이 있으면 먼저 보고
- `normalizers/output/*` ignored
- `renderers/hwpx_renderer/output/*` ignored
- `templates/hwpx/*.hwpx` ignored
- Python cache가 tracked 변경에 포함되지 않음

반복 실행 명령:

```powershell
python .\normalizers\validate_placeholder_confirmed_values_poc.py
python .\normalizers\input_normalizer_poc.py
python .\normalizers\hwpx_payload_mapper_poc.py
python .\normalizers\validate_hwpx_payload_poc.py
python .\normalizers\hwpx_renderer_dry_run_poc.py
python .\normalizers\render_mapped_hwpx_poc.py
```

기대 결과:

- helper fixture 통과
- routing fixture 6종 통과
- blocked fixture payload 미생성
- `needs_security_review` fixture HWPX 렌더링 제외
- mapped HWPX 4종 `rendered`
- mapped HWPX 4종 `remaining_placeholders` 0

### 사용자 확인 항목

사용자는 HWPX output을 한컴에서 열고 다음을 확인합니다.

| 확인 | 항목 |
|---|---|
| [ ] | 파일 열림 |
| [ ] | 글자 겹침 없음 |
| [ ] | 항목 순서 정상 |
| [ ] | 줄바꿈과 문단 배치 정상 |
| [ ] | 내용 앞 `-` 표기 일관성 |
| [ ] | 남은 `{{placeholder}}` 없음 |
| [ ] | `[확인 필요]`가 실제값처럼 오인되지 않음 |
| [ ] | 실제 개인정보, 기관정보, 문서번호 없음 |

사용자 확인은 자동화하지 않습니다.

## HWPX output 4종 재생성 기준

다음 경우에는 HWPX output 4종을 다시 생성합니다.

- `normalizers/` 코드 변경
- `renderers/hwpx_renderer/` 코드 변경
- HWPX placeholder map 변경
- 로컬 placeholder HWPX 템플릿 변경
- fixture 변경
- 문서 유형별 입력 구조 변경
- 사용자가 기존 output의 글자 겹침, 항목 순서, bullet 표기 문제를 보고

다음 경우에는 HWPX output 재생성을 생략할 수 있습니다.

- 문서 설명만 수정
- README 링크만 추가
- 체크리스트 문구만 수정
- 보안 정책 설명만 수정
- `placeholder_confirmed_values`의 문서 기준만 수정하고 코드 연결이 없는 경우

## GitHub Desktop push 전 기준

push 전 GitHub Desktop Changes에 보여도 되는 항목:

- `docs/*.md`
- `checklists/*.md`
- `README.md`
- `tasks/NEXT_STEP.md`
- 명시적으로 수정한 PoC 코드
- placeholder fixture JSON

push 전 GitHub Desktop Changes에 보이면 안 되는 항목:

- `templates/hwpx/*.hwpx`
- `templates/hwpx/*.hwp`
- `renderers/hwpx_renderer/output/*`
- `normalizers/output/*`
- `__pycache__/`
- 실제 기관 양식 원본
- 실제 공문 또는 보고서 원문

## 계속 보류할 범위

다음은 반복 운영 기준 정리 이후에도 계속 보류합니다.

- 실제 기관 HWPX 양식 원본 Git 추가
- 실제 공문 또는 보고서 원문 처리
- 실제 개인정보, 민원정보, 내부 운영정보 처리
- OpenAI API 실제 호출
- Make.com 실제 시나리오 구현
- Gmail, Outlook, SMTP 연동
- 실제 이메일 자동 발송
- 실제 결재, 계약, 업체 선정, 예산 집행 자동화
- `placeholder_confirmed_values`를 `missing_fields`, routing, HWPX payload에 즉시 연결

## placeholder_confirmed_values 판단

`placeholder_confirmed_values`는 아직 실제 normalizer 흐름에 연결하지 않습니다.

현재 유지 기준:

- read-only helper 검증만 허용
- helper fixture는 기존 routing fixture 6종과 분리
- metadata schema는 문서 후보로만 유지
- `missing_fields` 자동 제외 금지
- routing 결과 변경 금지
- HWPX payload 반영 금지

연결 재검토 조건:

- 반복 운영 기준이 안정적으로 유지됨
- fixture 확장 후 기존 routing 회귀 없음
- 사용자가 `missing_fields` 정리 필요성을 반복적으로 확인
- helper 결과를 dry-run preview로만 보여줄지 먼저 결정

## 다음 최소 개선 후보

현재 우선순위는 다음과 같습니다.

| 우선순위 | 후보 | 판단 |
|---|---|---|
| 1 | Phase 2 반복 운영 로그 템플릿 | 추천 |
| 2 | fixture 확장 후보 재검토 | 추천 가능 |
| 3 | `placeholder_confirmed_values` dry-run preview 문서화 | 보류 후 검토 |
| 4 | `placeholder_confirmed_values` routing 연결 | 보류 |
| 5 | API, Make.com, Email 자동화 | 보류 |

추천 다음 작업:

1. 반복 운영 로그 템플릿 작성
2. 반복 실행 시 어떤 명령을 실행했고 어떤 HWPX output을 확인했는지 기록
3. 사용자가 한컴에서 확인한 결과를 짧게 남김
4. 이상 발생 시 파일명, 항목 번호, 증상을 표준 형식으로 남김

## 완료 기준

Phase 2 반복 운영 기준은 다음 조건을 만족하면 완료로 봅니다.

- Codex 확인 항목과 사용자 확인 항목이 분리됨
- HWPX output 재생성 기준이 정리됨
- GitHub Desktop push 전 기준이 정리됨
- 계속 보류할 범위가 명시됨
- `placeholder_confirmed_values` 미연결 상태가 재확인됨
- 다음 최소 개선 후보가 우선순위로 정리됨
