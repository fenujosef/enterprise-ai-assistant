from app.graph.graph import graph

def main():

    print("\nEnterprise AI Assistant\n")

    while True:
        question = input("You: ")

        if question.lower() in ["exit", "quit"]:
            break

        result = graph.invoke(
            {
                "question": question,
                "context": "",
                "answer": ""
            }
        )

        print("\nRewritten Question:")
        print(result["rewritten_question"])

        print("\nAssistant:\n")
        print(result["answer"])
        print()

if __name__ == "__main__":
    main()