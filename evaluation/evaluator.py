import asyncio
import json
import time

from app.graph.graph import graph
from evaluation.metrics import exact_match, contains_expected


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

    latency = time.perf_counter() - start_time

    is_exact = exact_match(
        case["expected_answer"],
        result["answer"],
        )

    contains = contains_expected(
        case["expected_answer"],
        result["answer"],
        )

    return {
        "question": case["question"],
        "expected_answer": case["expected_answer"],
        "actual_answer": result["answer"],
        "category": case["category"],
        "latency_seconds": round(latency, 3),
        "exact_match": is_exact,
        "contains_expected": contains,
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