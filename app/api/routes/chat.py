import json

from fastapi.responses import StreamingResponse

from fastapi import APIRouter

from app.api.schemas import ChatRequest, ChatResponse
from app.services.chat_service import ChatService


router = APIRouter()
chat_service = ChatService()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    result = await chat_service.ask(
        request.question
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