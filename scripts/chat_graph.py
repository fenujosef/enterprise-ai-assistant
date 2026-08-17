import asyncio

from app.graph.graph import graph
from app.mcp.client import initialize_mcp, close_mcp
from app.observability.logger import create_request_id

async def main():

    await initialize_mcp()

    try:

        print("\nEnterprise AI Assistant\n")

        # Conversation history lives for the duration of this chat session
        history = []

        while True:
            question = input("You: ")

            if question.lower() in ["exit", "quit"]:
                break

            request_id = create_request_id()

            result = await graph.ainvoke(
                {
                    "question": question,
                    "request_id": request_id,
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
                    "replan_count": 0,
                }
            )

            # Save the updated history for the next turn
            #history = result["chat_history"]


            print("\nRewritten Question:")
            print(result["rewritten_question"])

            print("\nAssistant:\n")
            print(result["answer"])

            print("\nTool Selected:")
            print(result["tool_name"])

            print()

    finally:

        await close_mcp()

if __name__ == "__main__":
    asyncio.run(main())