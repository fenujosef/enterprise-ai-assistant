from app.graph.graph import graph


class ChatService:

    async def ask(self, question: str, request_id: str,) -> dict:

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
            }
        )

        return result

    async def stream(self, question: str):

        async for event in graph.astream(
            {
                "question": question,
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
            },
            stream_mode="messages",
        ):

            yield event