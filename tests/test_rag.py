from tests.ragpipeline import RAGPipeline


pipeline = RAGPipeline()

while True:
    question = input("You: ")
    answer = pipeline.ask(question)
    print(answer)