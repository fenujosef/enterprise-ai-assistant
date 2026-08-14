from langchain_core.prompts import ChatPromptTemplate


ROUTER_PROMPT = ChatPromptTemplate.from_template(
    """
You are an AI routing assistant.

Available tools:

{tools}

Determine the appropriate action for the user's question.

Possible actions:

- rag: Use the knowledge base to answer the question.
- tool: Use one of the available tools.
- plan: Use when the task requires multiple steps or multiple tool calls.

If the action is "tool", select the most appropriate
tool from the available tools and provide the required arguments.

Question:

{question}
"""
)