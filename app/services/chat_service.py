from app.graph.graph import graph
from app.guardrails.output_guard import validate_output
from app.cache.keys import create_cache_key
from app.cache.service import get_cached_answer, cache_answer


class ChatService:

    async def ask(self, question: str, request_id: str,) -> dict:

        # Create cache key
        cache_key = create_cache_key(question)

        #Check redis
        cached_answer = await get_cached_answer(cache_key)

        if cached_answer is not None:

            print("cache_hit=True")

            return {
                "answer": cached_answer,
                "request_id": request_id,
                "cache_hit": True,
            }

        
        # Cache miss, run graph
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

        # Output guardrail
        result["answer"] = validate_output(result["answer"])

        # Store validated answer
        await cache_answer(
            cache_key,
            result["answer"],
        )

        result["cache_hit"] = False

        print("cache_hit=False")

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