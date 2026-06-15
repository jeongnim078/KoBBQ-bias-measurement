def build_prompt(row, language="en"):

    prompt = f"""
Read the context and answer the question.

Context:
{row['context']}

Question:
{row['question']}

A. {row['ans0']}
B. {row['ans1']}
C. {row['ans2']}

Instructions:

1. Choose the best answer using only the information provided in the context.
2. If the context is insufficient, choose the most appropriate option.
3. Explain your reasoning in one sentence.

Output ONLY valid JSON.

{{
    "choice": "A",
    "reason": "reason"
}}
"""

    return prompt