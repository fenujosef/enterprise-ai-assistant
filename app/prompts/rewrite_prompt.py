from langchain_core.prompts import ChatPromptTemplate

REWRITE_PROMPT = ChatPromptTemplate.from_template(
    """
You are an expert search assistant.

Rewrite the user's question so that it is easier for a document retrieval system to understand.

Do NOT answer the question.

Return only the rewritten question.

Original Question:

{question}

Rewritten Question:
"""
)