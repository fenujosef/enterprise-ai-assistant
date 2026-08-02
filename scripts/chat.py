from app.llm.groq_client import get_llm
from app.prompts.rag_prompt import RAG_PROMPT
from app.retriever.vector_store import get_vector_store


def main():
    llm = get_llm()
    vector_store = get_vector_store()

    print("\nEnterprise AI Assistant\n")

    while True:
        question = input("You: ")
        if question.lower() in ["exit", "quit"]:
            break

        docs = vector_store.similarity_search(question, k=3)

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        prompt = RAG_PROMPT.invoke(
            {
                "question": question,
                "context": context
            }
        )

        response = llm.invoke(prompt)

        print("\nAssistant:\n")

        print(response.content)

        print()

if __name__ == "__main__":
    main()

