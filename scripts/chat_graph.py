from app.graph.graph import graph

def main():

    print("\nEnterprise AI Assistant\n")

    # Conversation history lives for the duration of this chat session
    history = []

    while True:
        question = input("You: ")

        if question.lower() in ["exit", "quit"]:
            break

        result = graph.invoke(
            {
                "question": question,
                "rewritten_question": "",
                "context": "",
                "answer": "",
                "retrieval_attempts": 0,
                "chat_history": history,

                "action": "",
                "tool_name": "",
                "tool_input": "",
                "tool_output": "",

                "plan": {"steps": []},
                "current_step": 0,
                "step_results": [],
            }
        )

        # Save the updated history for the next turn
        history = result["chat_history"]


        print("\nRewritten Question:")
        print(result["rewritten_question"])

        print("\nAssistant:\n")
        print(result["answer"])

        print("\nTool Selected:")
        print(result["tool_name"])

        print()

if __name__ == "__main__":
    main()