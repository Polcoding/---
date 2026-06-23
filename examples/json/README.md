# JSON 샘플 폴더 안내

## 목적

이 폴더는 향후 렌더러 검증에 사용할 placeholder 기반 AI 출력 JSON 샘플을 보관합니다.

## 보관 가능 파일

- placeholder 기반 공문 샘플 JSON
- placeholder 기반 추진계획서 샘플 JSON
- placeholder 기반 업체 메일 샘플 JSON
- placeholder 기반 조사표 샘플 JSON
- 보안 차단 테스트용 샘플 JSON

## 보관 금지 파일

- 실제 공문 원문
- 실제 개인정보가 포함된 JSON
- 실제 기관명, 업체명, 담당자명이 포함된 JSON
- 실제 문서번호, 민원번호, 차량번호가 포함된 JSON
- 실제 장비명, 수량, 금액이 포함된 JSON
- 실제 업무자료를 변환한 JSON

## 현재 상태

- 현재 단계: 설계 및 검증 샘플 준비 단계
- 보고서 샘플 4종: HWPX placeholder 렌더러 검증용 샘플로 유지
- 표 데이터 후보: `docs/137_report_sample_json_table_data_candidate_review.md` 기준으로 샘플 JSON 직접 수정 보류
- 실제 HWPX/XLSX 업무 산출물 생성: 없음

## 표 데이터 후보 기준

`renderer_hints.table_template`은 서식 또는 표시 후보 힌트입니다.

현재 단계에서는 샘플 JSON에 새 `table_data_candidate` 필드를 추가하지 않습니다. 실제 표 데이터, 물품명, 수량, 금액, 대상 목록도 기록하지 않습니다.
