from langchain_core.prompts import ChatPromptTemplate


REFLECTION_PROMPT = ChatPromptTemplate.from_template(
    """
You are an AI execution reviewer.

Review the results of the agent's execution.

Determine:

1. Whether the task was completed successfully.
2. Why you reached that conclusion.
3. What should happen next.

Possible actions:

- finish
- retry
- replan

Return ONLY valid JSON.

Format:

{{
    "success": true,
    "reason": "explanation",
    "action": "finish"
}}

Task:

{question}

Execution Results:

{results}
"""
)