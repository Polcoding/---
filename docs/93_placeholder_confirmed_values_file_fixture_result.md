# placeholder_confirmed_values 파일 기반 fixture 분리 결과

## 목적

`placeholder_confirmed_values` helper 전용 검증 케이스를 코드 내부 상수에서 파일 기반 fixture로 분리했습니다.

목표는 helper 검증을 더 추적 가능하게 만들되, 기존 routing fixture 6종 회귀 테스트에는 섞지 않는 것입니다.

## 변경 파일

- `normalizers/fixtures/placeholder_confirmed_values/placeholder_confirmed_values_safe.json`
- `normalizers/fixtures/placeholder_confirmed_values/placeholder_confirmed_values_invalid.json`
- `normalizers/validate_placeholder_confirmed_values_poc.py`

## fixture 위치

helper 전용 fixture는 다음 하위 폴더에 둡니다.

```text
normalizers/fixtures/placeholder_confirmed_values/
```

기존 routing fixture 6종은 계속 다음 위치에 둡니다.

```text
normalizers/fixtures/*.json
```

이 구조는 기존 `input_normalizer_poc.py`의 `*.json` 검색 범위와 충돌하지 않습니다.

## fixture 구성

### safe fixture

`placeholder_confirmed_values_safe.json`은 다음 케이스를 포함합니다.

- 안전한 placeholder-confirmed mapping
- 단일 안전 placeholder 값

### invalid fixture

`placeholder_confirmed_values_invalid.json`은 다음 케이스를 포함합니다.

- 대괄호 없는 일반 문자열
- 빈 placeholder
- 실제값 marker가 포함된 placeholder 설명
- mapping이 아닌 입력
- 단일 unsafe 문자열

## 검증 방식

`normalizers/validate_placeholder_confirmed_values_poc.py`는 이제 helper fixture 하위 폴더의 JSON 파일을 읽습니다.

검증 기준:

- mapping 입력은 `find_invalid_placeholder_confirmed_values(values)`로 검증
- 단일 값 입력은 `is_placeholder_confirmed_value(value)`로 검증
- 각 케이스의 기대 결과와 실제 결과가 일치해야 통과

## 실행 결과

다음 명령을 실행했습니다.

```powershell
python .\normalizers\validate_placeholder_confirmed_values_poc.py
python .\normalizers\input_normalizer_poc.py
```

결과:

| 구분 | 결과 |
|---|---|
| helper safe fixture | 통과 |
| helper invalid fixture | 통과 |
| 기존 routing fixture 6종 | 통과 |

참고:

- `normalizers/output/placeholder_confirmed_values_summary.json` 생성은 기존 output 권한 상태로 생략되었습니다.
- 콘솔 기준 검증 결과는 모두 통과했습니다.
- output 산출물은 Git 제외 상태입니다.

## 현재 단계에서 유지하는 보류 원칙

- `missing_fields` 자동 제외 없음
- routing 결과 변경 없음
- HWPX payload 반영 없음
- 기존 fixture 6종 schema 변경 없음
- `project_plan` ready 경로 개방 없음
- `result_report` ready 경로 개방 없음

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX 원본 추가 없음
- API, Make.com, Email 자동화 코드 추가 없음

## 결론

helper 전용 검증 케이스를 파일 기반 fixture로 분리했습니다.

기존 routing fixture 6종과 helper fixture는 분리되어 있으며, 기존 회귀 테스트 결과는 유지되었습니다.

후속 작업에서 helper 결과를 normalizer 흐름에 연결하기 전의 허용 조건과 금지 조건을 `docs/94_placeholder_confirmed_values_normalizer_connection_policy.md`에 정리했습니다.

다음 단계는 read-only metadata schema 후보를 문서화하는 것입니다.
