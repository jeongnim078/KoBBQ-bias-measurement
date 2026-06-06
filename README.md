# KoBBQ-bias-measurement

기계번역된 KoBBQ 408개의 샘플의 편향 측정을 위한 코드입니다

[코드 수정]
코드 27줄에 input_path는 공유드린 ko_dt_results.csv의 파일 경로 입력하시면 됩니다. 
input_path = "ko_dt_results.csv"

[코드 실행]
기존 nlp 파일로 해당 파일를 이동시킵니다. 터미널에서 여신 후 python bias_measurement.py 입력하시면 자동 실행됩니다.

실행 결과는 xlsx 형식의 bias_classified, bias_summary 두 파일에 자동 저장됩니다.


# KoBBQ_bias_measurement_v2

영문 bbq와 직역 KoBBQ 샘플의 편향 측정 및 BiasA, BiasD 측정을 위한 코드입니다

[코드 수정]
코드 28줄에 input_path는 공유드린 bbq_en_results.csv, ko_template_results.csv의 파일 경로를 입력하시면 됩니다.
input_path = "bbq_en_results.csv"

코드 65줄에 read.excel은 파일 형식에 맞게 read.csv로 수정해주시면 됩니다.
