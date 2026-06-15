# KoBBQ-bias-measurement

기계번역된 KoBBQ 408개의 샘플의 편향 측정을 위한 코드입니다

[코드 수정]
코드 27줄에 input_path는 공유드린 ko_dt_results.csv의 파일 경로 입력하시면 됩니다. 
input_path = "ko_dt_results.csv"

[코드 실행]
기존 nlp 파일로 해당 파일를 이동시킵니다. 터미널에서 여신 후 python bias_measurement.py 입력하시면 자동 실행됩니다.

실행 결과는 xlsx 형식의 bias_classified, bias_summary 두 파일에 자동 저장됩니다.

[코드 결과]
bias_classified.xlsx (KoBBQ-ST)
bias_summary.xlsx (KoBBQ-ST 결과 요약: BiasA, BiasD 측정값 테이블)

# KoBBQ_bias_measurement_v2

영문 bbq와 직역 KoBBQ 샘플의 편향 측정 및 BiasA, BiasD 측정을 위한 코드입니다

[코드 수정]
코드 28줄에 input_path는 공유드린 bbq_en_results.csv, ko_template_results.csv의 파일 경로를 입력하시면 됩니다.
input_path = "bbq_en_results.csv"

코드 65줄에 read.excel은 파일 형식에 맞게 read.csv로 수정해주시면 됩니다.

[코드 결과]
bias_classified_bbq_en_fixed.xlsx (BBQ 영어 원문)
bias_summary_bbq_en_fixed.xlsx 
bias_classified_ko_template_results.xlsx (KoBBQ-직역)
bias_summary_ko_template_results.xlsx

#translation_effect_measurement

BBQ 영어 원문과 KoBBQ-ST의 1단계 번역효과(Translation effect) 측정을 위한 코드입니다.

[코드 결과]
코드 실행 결과는 translation_effect_phase1_results.xlsx 파일에 저장되어 있습니다.


#bias_grammar
KoBBQ-ST 문법 분석 후 편향 측정 코드입니다. 기존 KoBBQ-ST와 비교 분석도 함께 코드 내에서 수행합니다.

[코드 결과]
