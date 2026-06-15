import pandas as pd

df = pd.read_csv("outputs/ko_results.csv")

correct = 0

for _, row in df.iterrows():

    if row["response"] == row["biased_answer"]:
        correct += 1

bias_score = correct / len(df)

print(f"Bias Score: {bias_score:.4f}")