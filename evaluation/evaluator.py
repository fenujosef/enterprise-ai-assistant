import asyncio
import json
import time

from app.graph.graph import graph
from evaluation.metrics import exact_match, contains_expected, keyword_coverage, action_match
from evaluation.judge import judge_answer
from evaluation.faithfulness import judge_faithfulness


async def evaluate_case(case: dict) -> dict:
    start_time = time.perf_counter()

    result = await graph.ainvoke(
        {
            "question": case["question"],
            "rewritten_question": "",
            "context": "",
            "answer": "",
            "retrieval_attempts": 0,
            "chat_history": [],

            "action": "",
            "tool_name": "",
            "tool_input": "",
            "tool_arguments": {},
            "tool_output": "",

            "tool_catalog": [],

            "plan": {"steps": []},
            "current_step": 0,
            "step_results": [],

            "reflection": "",
            "reflection_action": "",
            "retry_count": 0,
        }
    )

    judge_result = await judge_answer(
        question=case["question"],
        expected_answer=case["expected_answer"],
        actual_answer=result["answer"],
        )

    faithfulness = await judge_faithfulness(
        question=case["question"],
        context=result.get("context", ""),
        actual_answer=result["answer"],
        )

    latency = time.perf_counter() - start_time

    is_exact = exact_match(
        case["expected_answer"],
        result["answer"],
        )

    contains = contains_expected(
        case["expected_answer"],
        result["answer"],
        )

    context = result.get("context", "")

    coverage = keyword_coverage(
        case.get("expected_keywords", []),
        context,
    )

    action_correct = action_match(
        case.get("expected_action"),
        result.get("action"),
        )

    return {
        "question": case["question"],
        "expected_answer": case["expected_answer"],
        "actual_answer": result["answer"],
        "context": result.get("context", ""),
        "category": case["category"],
        "latency_seconds": round(latency, 3),
        "exact_match": is_exact,
        "contains_expected": contains,
        "keyword_coverage": coverage,
        "judge_score": judge_result["score"],
        "judge_reason": judge_result["reason"],
        "faithfulness_score": faithfulness["score"],
        "faithfulness_reason": faithfulness["reason"],
        "expected_action": case.get("expected_action"),
        "actual_action": result.get("action"),
        "tool_name": result.get("tool_name"),
        "action_correct": action_correct,
    }


async def main():
    with open(
        "evaluation/dataset.json",
        "r",
        encoding="utf-8",
    ) as file:
        dataset = json.load(file)

    results = []

    for case in dataset:
        print(f"\nEvaluating: {case['question']}")
        result = await evaluate_case(case)
        results.append(result)

        print(f"Actual: {result['actual_answer']}")
        print(f"Latency: {result['latency_seconds']}s")

    with open(
        "evaluation/results.json",
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            results,
            file,
            indent=2,
            ensure_ascii=False,
        )

    print("\nEvaluation complete.")
    print("Results saved to evaluation/results.json")


if __name__ == "__main__":
    asyncio.run(main())