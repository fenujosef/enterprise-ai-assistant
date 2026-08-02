from langchain_core.prompts import ChatPromptTemplate

RAG_PROMPT = ChatPromptTemplate.from_template(
       """
You are an enterprise AI assistant.

Answer ONLY using the provided context.

If the answer is not found in the context, say:

"I couldn't find that information in the provided documents."

Context:

{context}

Question:

{question}

Answer:
"""
)