from app.nodes.planner import planner


state = {
    "question": "Find the payment service repository and send its details to the backend team.",
    "rewritten_question": "",
    "context": "",
    "answer": "",
    "retrieval_attempts": 0,
    "chat_history": [],
    "tool_name": "",
    "tool_input": "",
    "tool_output": "",
    "plan": []
}


result = planner(state)

print("\nGenerated Plan:\n")

for step in result["plan"]["steps"]:
    print(f"\nStep {step['step']}")
    print(f"Action: {step['action']}")
    print(f"Tool: {step['tool']}")
    print(f"Input: {step['input']}")