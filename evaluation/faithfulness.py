import json
from pydantic import BaseModel, Field

from app.llm.groq_client import get_llm


llm = get_llm()


class FaithfulnessResult(BaseModel):
    score: float = Field(ge=0.0, le=1.0)
    reason: str


FAITHFULNESS_PROMPT = """
You are evaluating the faithfulness of an enterprise RAG system.

Determine whether the actual answer is fully supported by the
retrieved context.

Context:
{context}

Question:
{question}

Actual Answer:
{actual_answer}

Return ONLY valid JSON:

{{
    "score": 0.0,
    "reason": "brief explanation"
}}

Scoring:

1.0 = answer is fully supported by the context
0.75 = mostly supported, with a minor unsupported detail
0.5 = partially supported
0.25 = mostly unsupported
0.0 = completely unsupported
"""


async def judge_faithfulness(
    question: str,
    context: str,
    actual_answer: str,
) -> dict:

    prompt = FAITHFULNESS_PROMPT.format(
        question=question,
        context=context,
        actual_answer=actual_answer,
    )

    response = await llm.ainvoke(prompt)

    content = response.content.strip()

    print("\n--- Faithfulness Judge Response ---")
    print(content)
    print("-----------------------------------")

    # Remove markdown JSON fences if the model adds them
    if content.startswith("```json"):
        content = content[7:]

    elif content.startswith("```"):
        content = content[3:]

    if content.endswith("```"):
        content = content[:-3]

    content = content.strip()

    try:
        result = FaithfulnessResult.model_validate_json(content)

    except Exception as exc:

        raise ValueError(
            f"Invalid faithfulness judge response:\n"
            f"{content}\n\n"
            f"Validation error: {exc}"
        ) from exc

    return result.model_dump()
