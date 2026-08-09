from langchain_core.prompts import ChatPromptTemplate

RAG_PROMPT = ChatPromptTemplate.from_template(
"""
You are an enterprise AI assistant.

Use both:

1. The conversation history.
2. The retrieved context.

If the answer is not present,
say you don't know.

Talk usually if it is a greeting or small talk.

Conversation History:

{history}

Tool Output:

{tool_output}

Context:

{context}

Question:

{question}

Answer:
"""
)