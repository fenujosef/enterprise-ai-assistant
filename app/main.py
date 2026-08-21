from contextlib import asynccontextmanager

import logging
from fastapi import FastAPI

from fastapi import Request
from fastapi.responses import JSONResponse

from app.guardrails.input_guard import GuardrailViolation

from app.api.routes.chat import router as chat_router
from app.api.routes.health import router as health_router
from app.api.routes.tools import router as tools_router
from app.mcp.client import initialize_mcp, close_mcp



logger = logging.getLogger("enterprise_ai")


@asynccontextmanager
async def lifespan(app: FastAPI):

    # Startup
    await initialize_mcp()

    yield

    # Shutdown
    await close_mcp()


app = FastAPI(
    title="Enterprise AI Assistant",
    version="1.0.0",
    lifespan=lifespan,
)


app.include_router(chat_router)
app.include_router(health_router)
app.include_router(tools_router)



@app.exception_handler(GuardrailViolation)
async def guardrail_exception_handler(
    request: Request,
    exc: GuardrailViolation,
):

    logger.warning(
        "guardrail_blocked path=%s reason=%s",
        request.url.path,
        str(exc),
    )

    return JSONResponse(
        status_code=400,
        content={
            "error": "Request blocked by security policy."
        },
    )

