import json

from app.llm.groq_client import get_llm


llm = get_llm()


JUDGE_PROMPT = """
You are an evaluator for an enterprise AI assistant.

Evaluate the answer using the question, expected answer,
and actual answer.

Question:
{question}

Expected Answer:
{expected_answer}

Actual Answer:
{actual_answer}

Return ONLY valid JSON:

{{
    "score": 0.0,
    "reason": "brief explanation"
}}

The score must be between 0.0 and 1.0.

Scoring:
1.0 = completely correct
0.75 = mostly correct
0.5 = partially correct
0.25 = mostly incorrect
0.0 = completely incorrect
"""


async def judge_answer(
    question: str,
    expected_answer: str,
    actual_answer: str,
) -> dict:

    prompt = JUDGE_PROMPT.format(
        question = question,
        expected_answer = expected_answer,
        actual_answer = actual_answer,
    )

    response = await llm.ainvoke(prompt)

    return json.loads(response.content)