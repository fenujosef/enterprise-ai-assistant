from app.nodes.plan_executor import plan_executor


state = {
    "question": "Calculate two values.",
    "rewritten_question": "",
    "context": "",
    "answer": "",
    "retrieval_attempts": 0,
    "chat_history": [],

    "action": "plan",

    "tool_name": "",
    "tool_input": "",
    "tool_output": "",

    "plan": {
        "steps": [
            {
                "step": 1,
                "action": "Calculate 25 multiplied by 18",
                "tool": "calculator",
                "input": "25 * 18"
            },
            {
                "step": 2,
                "action": "Add 50 to the previous result",
                "tool": "calculator",
                "input": "{step_1_result} + 50"
            }
        ]
    },

    "current_step": 0,
    "step_results": []
}


while state["current_step"] < len(state["plan"]["steps"]):

    state = plan_executor(state)


print("\nExecution Results:\n")

for result in state["step_results"]:

    print(f"Step {result['step']}")
    print(f"Tool: {result['tool']}")
    print(f"Input: {result['input']}")
    print(f"Result: {result['result']}")
    print()