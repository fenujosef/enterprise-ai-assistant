from tests.ragpipeline import RAGPipeline


pipeline = RAGPipeline()

def test_rag_pipeline():

    question = "What is the vacation policy?"

    result = pipeline.ask(question)

    assert result is not None
    assert isinstance(result, str)
    assert len(result.strip()) > 0