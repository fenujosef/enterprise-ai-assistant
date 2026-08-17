import json
from statistics import mean

def main():

    with open(
        "evaluation/results.json",
        "r",
        encoding="utf-8",
    ) as file:

        results = json.load(file)

    if not results:
        print("No evaluation results found.")
        return

    total = len(results)

    exact_matches = sum(
        result.get("exact_matches", False)
        for result in results
    )

    action_matches = sum(
        result.get("action_correct", False)
        for result in results
    )

    judge_scores = [
        result["judge_score"]
        for result in results
        if "judge_score" in results
    ]

    faithfulness_scores = [
        result["faithfulness_score"]
        for result in results
        if "faithfulness_score" in result
    ]

    retrieval_scores = [
        result["keyword_coverage"]
        for result in results
        if "keyword_coverage" in result
    ]

    latencies = [
        result["latency_seconds"]
        for result in results
    ]

    print("\n==============================")
    print("      EVALUATION REPORT")
    print("==============================")

    print(f"\nTotal cases: {total}")

    print(
        f"Exact match: "
        f"{exact_matches / total:.2%}"
    )

    if action_matches:
        print(
            f"Agent action accuracy: "
            f"{action_matches / total:.2%}"
        )

    if judge_scores:
        print(
            f"Average answer score: "
            f"{mean(judge_scores):.3f}"
        )

    if faithfulness_scores:
        print(
            f"Average faithfulness: "
            f"{mean(faithfulness_scores):.3f}"
        )

    if retrieval_scores:
        print(
            f"Average retrieval coverage: "
            f"{mean(retrieval_scores):.3f}"
        )

    print(
        f"Average latency: "
        f"{mean(latencies):.3f}s"
    )

if __name__ == "__main__":
    main()