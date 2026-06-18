# 다음 작업

## 목표

one_page_report의 실제 HWPX 렌더러 지원 여부를 확인하고, 누락된 경우 최소 범위만 보강합니다.

## 확인 대상

- renderers/hwpx_renderer/template_package.py
- renderers/hwpx_renderer/render_hwpx_poc.py
- examples/json/sample_one_page_report.json
- docs/45_one_page_report_hwpx_template_strategy.md

## 확인 항목

1. document_type=one_page_report 전용 placeholder map 존재 여부
2. 다음 placeholder 지원 여부
   - {{title}}
   - {{report_summary}}
   - {{background}}
   - {{main_points}}
   - {{review_opinion}}
   - {{issues_or_considerations}}
   - {{next_steps}}
   - {{action_items}}
   - {{missing_fields}}
   - {{checklist}}
   - {{security_review}}
   - {{draft_status}}
   - {{human_review_required}}
3. 배열 필드의 개조식 문자열 변환 여부
4. 값 누락 시 [확인 필요] 또는 안전한 빈 문자열 처리 여부
5. templates/hwpx/placeholder_one_page_report.hwpx 후보 인식 여부
6. 템플릿이 없을 때 template_required 상태로 안전하게 종료하는지
7. 기존 official_letter와 project_plan 렌더링을 깨뜨리지 않는지

## 작업 제한

- 실제 기관 양식 사용 금지
- 실제 원문 또는 개인정보 사용 금지
- 실제 HWPX 템플릿 Git 추가 금지
- Email/API/Make.com 연동 금지
- 확인되지 않은 서식값 임의 생성 금지

## 완료 조건

- one_page_report 지원 여부 보고
- 누락된 경우 최소 범위 코드 보강
- 기존 렌더러 회귀 테스트
- 보안 테스트 통과
- 다음 단계로 로컬 placeholder_one_page_report.hwpx 수동 준비 가능 상태
