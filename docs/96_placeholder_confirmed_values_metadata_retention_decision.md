# placeholder_confirmed_values metadata 유지 결정

## 목적

`placeholder_confirmed_values_review` metadata를 코드에 연결하지 않고 문서 기준으로 유지할지, 또는 dry-run preview 전용 출력으로만 둘지 검토합니다.

## 검토 결론

현재 단계에서는 metadata를 코드에 연결하지 않습니다.

dry-run preview 전용 출력도 아직 만들지 않습니다.

즉, `placeholder_confirmed_values_review`는 문서 기준 schema 후보로만 유지합니다.

## 판단 이유

- 기존 `hwpx_renderer_dry_run_poc.py`는 HWPX 렌더러 전제조건 확인에 집중하고 있습니다.
- dry-run preview에 metadata를 넣으면 기존 summary 의미가 넓어집니다.
- 별도 preview 파일을 만들면 output 종류가 늘어나고 검증 기준도 추가됩니다.
- 현재 helper 검증은 이미 `validate_placeholder_confirmed_values_poc.py`에서 분리되어 있습니다.
- 아직 `placeholder_confirmed_values`를 기존 routing fixture 6종에 섞지 않기로 했습니다.
- `missing_fields`, routing, HWPX payload를 바꾸지 않는 원칙이 더 중요합니다.

## 유지 방식

현재 유지 방식은 다음과 같습니다.

| 구분 | 결정 |
|---|---|
| schema | 문서 기준 후보로 유지 |
| normalizer 연결 | 보류 |
| dry-run preview 출력 | 보류 |
| 기존 dry-run summary 변경 | 없음 |
| 기존 routing fixture 6종 변경 | 없음 |
| helper fixture | 별도 하위 폴더에서 유지 |

## 계속 사용하는 검증 축

### helper 검증

```powershell
python .\normalizers\validate_placeholder_confirmed_values_poc.py
```

역할:

- safe helper fixture 검증
- invalid helper fixture 검증
- `placeholder_confirmed_values` 형식 판정 확인

### 기존 회귀 검증

```powershell
python .\normalizers\input_normalizer_poc.py
python .\normalizers\hwpx_payload_mapper_poc.py
python .\normalizers\validate_hwpx_payload_poc.py
python .\normalizers\hwpx_renderer_dry_run_poc.py
```

역할:

- 문서 유형 판정
- routing 유지
- `missing_fields` 유지
- HWPX payload 검증
- HWPX renderer dry-run 검증

## dry-run preview를 보류하는 조건

다음 조건이 충족되기 전까지 preview 출력을 만들지 않습니다.

- metadata 소비자가 명확해짐
- preview summary의 사용 목적이 기존 dry-run summary와 분리됨
- preview output 파일명이 정해짐
- preview output이 Git 제외 상태로 관리됨
- 기존 회귀 테스트와 혼동되지 않는 검증 절차가 정리됨

## 향후 허용 가능한 preview 방식

나중에 필요해지면 다음처럼 별도 파일로만 검토합니다.

```text
normalizers/output/placeholder_confirmed_values_metadata_preview.json
```

이 파일도 output 산출물이므로 Git에 포함하지 않습니다.

## 현재 단계에서 하지 않는 것

- `input_normalizer_poc.py`에 metadata 추가
- `security_filter_poc.py`에 helper 결과 연결
- `hwpx_payload_mapper_poc.py`에 metadata 반영
- `hwpx_renderer_dry_run_poc.py` summary 구조 변경
- 기존 routing fixture 6종 schema 변경
- `missing_fields` 자동 제외
- routing 결과 변경

## 보안 검수

- 실제 개인정보 추가 없음
- 실제 기관명, 업체명, 담당자명 추가 없음
- 실제 문서번호, 민원번호, 사건번호 추가 없음
- 실제 날짜, 예산, 실적 수치 추가 없음
- 실제 공문 원문 또는 보고서 원문 추가 없음
- 실제 HWPX 원본 추가 없음
- API, Make.com, Email 자동화 코드 추가 없음

## 결론

`placeholder_confirmed_values_review`는 현재 문서 기준 schema 후보로 유지합니다.

다음 단계는 `placeholder_confirmed_values` 흐름을 더 진행하기보다, Phase 2 최소 PoC의 전체 상태를 다시 묶어 어느 지점까지 구현하고 어디부터 보류할지 정리하는 것입니다.
