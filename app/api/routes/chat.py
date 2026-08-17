import json

from fastapi.responses import StreamingResponse

from fastapi import APIRouter

from app.api.schemas import ChatRequest, ChatResponse
from app.services.chat_service import ChatService
from app.observability.logger import create_request_id
from app.guardrails.input_guard import validate_input
from app.guardrails.injection import validate_against_injection
from app.guardrails.pii import redact_input_pii


router = APIRouter()
chat_service = ChatService()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    request_id = create_request_id()

    question = validate_input(
        request.question
        )

    question = validate_against_injection(
        question
        )

    question = redact_input_pii(
        question
        )

    print(question)

    result = await chat_service.ask(
        question,
        request_id=request_id,
    )

    return ChatResponse(
        answer=result["answer"]
    )


@router.post("/chat/stream")
async def chat_stream(request: ChatRequest):

    async def event_generator():

        async for message, metadata in chat_service.stream(
            request.question
        ):
            if hasattr(message, "content") and message.content:
                yield f"data: {message.content}\n\n"

        yield "data: [DONE]\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        },
    )