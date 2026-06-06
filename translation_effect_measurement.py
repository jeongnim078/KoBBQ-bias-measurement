import pandas as pd
import numpy as np

print("==================================================")
print(" 1단계 번역 효과(Translation Effect) 측정 시작")
print("==================================================")

# 1. 두 버전의 요약 데이터 로드
# bbq_en_path: 영어 원본 BBQ 요약본
# ko_template_path: 기계번역(직역)된 KoBBQ 요약본
bbq_en_path = "bias_summary_bbq_en_fixed.xlsx"
ko_template_path = "bias_summary.xlsx"

print(f"영어 원본 요약 로드 중: {bbq_en_path}")
df_en = pd.read_excel(bbq_en_path)

print(f"기계번역 요약 로드 중: {ko_template_path}")
df_ko = pd.read_excel(ko_template_path)

# 2. 분석에 필요한 핵심 컬럼 추출 및 이름 표준화
# 영어 데이터 정제
df_en_sub = df_en[['범주(영문)', 'BiasA', 'BiasD (정상교정본)']].copy()
df_en_sub.columns = ['category', 'en_BiasA', 'en_BiasD']

# 기계번역 데이터 정제
df_ko_sub = df_ko[['범주(영문)', 'BiasA', 'BiasD']].copy()
df_ko_sub.columns = ['category', 'ko_BiasA', 'ko_BiasD']

# 3. 범주(Category) 기준으로 두 데이터 병합 (Merge)
df_effect = pd.merge(df_ko_sub, df_en_sub, on='category', how='inner')

# 4. 1단계 번역 효과 계산 (공식: KoBBQ 점수 - BBQ 점수)
# Delta BiasA: 번역 후 모호한 맥락에서 편향적 선택이 얼마나 증가했는가
# Delta BiasD: 번역 후 명확한 맥락에서 편향 격차가 얼마나 심화되었는가
df_effect['Delta_BiasA'] = df_effect['ko_BiasA'] - df_effect['en_BiasA']
df_effect['Delta_BiasD'] = df_effect['ko_BiasD'] - df_effect['en_BiasD']

# 5. 보기 편하게 한글 범주명 매핑 추가
category_map = {
    'age': '연령', 
    'disability_status': '장애 지위', 
    'gender_identity': '성별 정체성',
    'physical_appearance': '신체 외형', 
    'ses': '사회경제적 지위', 
    'sexual_orientation': '성적 지향'
}
df_effect['범주(한글)'] = df_effect['category'].map(category_map)

# 컬럼 순서 재배치 및 가독성 확보
df_effect = df_effect[[
    'category', '범주(한글)', 
    'en_BiasA', 'ko_BiasA', 'Delta_BiasA',
    'en_BiasD', 'ko_BiasD', 'Delta_BiasD'
]]

# 소수점 4자리로 깔끔하게 반올림
df_effect = df_effect.round(4)

# 6. 통계적 총평 및 엑셀 파일 저장
output_path = "translation_effect_phase1_results.xlsx"
df_effect.to_excel(output_path, index=False)

print("\n" + "="*60)
print("✓ 1단계 번역 효과 측정 및 분석 완료!")
print(f"  - 결과 저장 파일: {output_path}")
print("="*60)

# 터미널 프리뷰 출력
print("\n[1단계 번역 효과 측정 결과 테이블]")
print(df_effect[[
    '범주(한글)', 'en_BiasA', 'ko_BiasA', 'Delta_BiasA', 'Delta_BiasD'
]].to_string(index=False))

print("\n💡 해석 가이드:")
print("  - Delta_BiasA > 0 : 번역 과정에서 모델의 잠재적 '고정관념 동조 경향'이 증가함.")
print("  - Delta_BiasD > 0 : 번역 과정에서 모델이 '사실 왜곡 및 편향적 오답'을 낼 확률이 증가함.")