# Phase 1 완료 기준 및 Phase 2 진입 조건

## 목적

이 문서는 현재 저장소의 실제 진행 상태를 기준으로 Phase 1 완료 기준과 Phase 2 진입 조건을 정리합니다.

Phase 1은 실제 운영 자동화가 아니라, 안전한 초안 생성 체계와 placeholder 기반 로컬 렌더링 PoC를 검증하는 단계입니다.

## 현재 진행도 판단

| 영역 | 현재 상태 | 진행도 |
|---|---|---:|
| 보안 정책과 금지 기준 | A/B/C/D 등급, 비식별화, 금지 작업 기준 정리 | 높음 |
| Custom GPT 테스트판 | Instructions, Conversation Starters, 테스트 기준 준비 | 높음 |
| 샘플 JSON | 핵심 문서 유형별 placeholder 샘플 준비 | 높음 |
| 렌더러 PoC | XLSX, Markdown, Email, HWPX 로컬 PoC 작성 | 높음 |
| HWPX 보고서 4종 | 원페이지 보고서, 추진계획서, 결과보고서, 검토보고서 치환 및 수동 검수 완료 | 높음 |
| 실제 기관 양식 전환 절차 | 저장소 밖 복사본, placeholder 변환, Git 제외 절차 문서화 | 중간 |
| 입력 정규화 | 스키마, fixture, 최소 PoC 작성 및 회귀 테스트 기준 정리 | 중간 |
| 보안 필터 구현 | 요구사항 문서화 및 placeholder 기반 최소 PoC 작성 | 중간 |
| HWPX payload 매핑 | mapper, validation, renderer dry-run PoC 작성 | 중간 |
| API/Make.com 연동 | 의도적으로 보류 | 낮음 |

전체 실사용 시스템 기준 진행도는 약 45~55%로 봅니다.

Phase 1 준비 저장소 기준 진행도는 완료로 봅니다.

이 문서는 Phase 1 완료 및 Phase 2 진입 판단 당시의 기준 문서입니다.

최신 기준에서는 Phase 2 최소 PoC와 Phase 3 안전 게이트 문서화를 마무리했고, Phase 4 문서 템플릿 안정화 진입 판단, HWPX template manifestㆍ공통 placeholder 정합성 점검, style profile 확인 필요 값 유지 기준 정리까지 완료했습니다. 현재 최신 진행 상태는 `docs/126_style_profile_confirmation_value_collection_criteria.md`와 `tasks/NEXT_STEP.md`를 따릅니다.

## Phase 1 완료로 볼 수 있는 항목

다음 항목은 현재 완료로 판단합니다.

- 프로젝트 목적과 작업 규칙 정리
- 실제 원문, 개인정보, 기관정보 저장소 추가 금지 원칙 정리
- Custom GPT Instructions v0.1 준비
- Conversation Starters 준비
- 보안등급 A/B/C/D 기준 정리
- 비식별화 규칙 정리
- 문서 패턴 라이브러리 정리
- 문체 정책 정리
- AI 출력 JSON 스키마 정리
- placeholder 기반 샘플 JSON 준비
- XLSX 렌더러 PoC 검증
- Markdown 미리보기 렌더러 PoC 검증
- Email 초안 렌더러 PoC 검증
- HWPX 최소 렌더러 PoC 검증
- HWPX 보고서 4종 로컬 placeholder 치환 검증
- HWPX 보고서 4종 한컴 수동 열람 검수
- 로컬 HWPX 템플릿과 output HWPX Git 제외 확인
- 실제 기관 양식 투입 전 안전 절차 문서화
- 저장소 밖 HWPX placeholder 변환 절차 문서화
- 입력 정규화 스키마와 최소 PoC 작성
- 보안 필터 요구사항과 최소 PoC 작성
- HWPX payload mapper, validation, renderer dry-run PoC 작성
- Phase 2 최소 운영 흐름과 사용자 입력 템플릿 정리

## Phase 1에서 아직 미완료 또는 보류할 항목

다음 항목은 Phase 1 완료를 막지는 않으며, Phase 2 이후 단계에서 별도 검토가 필요합니다.

- 실제 기관 표준 글꼴, 자간, 줄간격, 문단 간격 값 확인
- 실제 표 구조 자동 치환 방식 확정
- 실제 기관 양식 원본을 저장소 밖에서 비식별 복사본으로 바꾸는 수동 리허설
- API 호출 전 차단 흐름 설계
- 운영 로그와 감사 추적 설계
- `placeholder_confirmed_values`를 실제 `missing_fields` 생성 결과에 반영할지 여부

## Phase 2 정의

Phase 2는 실제 API/Make.com 연동이 아닙니다.

현재 진행 중인 Phase 2 최소 PoC 범위는 다음과 같습니다.

1. 저장소 밖 실제 원본 처리 절차를 더 작은 단위로 검증
2. 사용자의 짧은 업무 지시를 표준 입력 JSON으로 바꾸는 입력 정규화
3. 보안 필터 요구사항과 최소 PoC 검증
4. HWPX 보고서 4종에 필요한 최소 입력 필드와 누락값 처리 규칙 유지
5. HWPX payload mapper, validation, renderer dry-run 연결
6. `placeholder_confirmed_values` read-only 판정 helper 검토

## Phase 2 진입 조건

Phase 2 진입 조건은 이미 충족한 것으로 봅니다.

다만 다음 조건은 Phase 2 작업을 계속할 때마다 확인해야 합니다.

- 실제 원본이 저장소에 추가되지 않았는지 확인
- 로컬 HWPX 템플릿과 output HWPX가 Git 제외 상태인지 확인
- 현재 변경 묶음을 GitHub Desktop에서 검토
- 실제 원본 없는 연습 파일 또는 비식별 복사본으로 저장소 밖 절차 확인
- C/D등급 문서는 작업 대상에서 제외한다는 원칙 재확인
- API/Make.com/Email 자동화는 아직 시작하지 않는다는 범위 재확인

## 작성 당시 Phase 2에서 먼저 할 일

초기 추천 순서 중 입력 정규화, 보안 필터 요구사항, HWPX payload 연결 dry-run은 완료되었습니다.

작성 당시 추천 순서는 다음과 같았습니다.

1. `placeholder_confirmed_values` fixture schema 확장 여부 검토
2. 신규 fixture를 추가할 경우 helper 전용 검증으로 둘지 판단
3. 기존 fixture 회귀 테스트 유지
4. `missing_fields`, routing, HWPX payload, dry-run 결과 미변경 확인
5. helper 판정 결과를 실제 `missing_fields`에 반영할지 여부는 계속 별도 검토

## 아직 시작하지 않을 것

- 실제 기관 양식 원본 Git 추가
- 실제 공문 또는 보고서 원문 저장
- Custom GPT Knowledge에 실제 문서 업로드
- Make.com 시나리오 작성
- OpenAI API 실제 호출
- Gmail, Outlook, SMTP 연동
- 실제 이메일 발송
- 실제 결재, 계약, 업체 선정, 예산 집행 자동화

## 결론

현재 저장소는 Phase 1의 핵심 목표를 완료했습니다.

이 문서 작성 당시의 다음 단계는 운영 자동화가 아니라 Phase 2 최소 PoC 보강이었습니다.

현재 최신 다음 단계는 HWPX 보고서 4종 수동 preview 서식 gap log와 점검 기준을 문서로 정리하는 것입니다. 실제 API, Make.com, Email 자동화와 실제 기관 HWPX 원본 투입은 계속 보류합니다.
