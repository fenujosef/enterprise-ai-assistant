from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes.chat import router as chat_router
from app.api.routes.health import router as health_router
from app.api.routes.tools import router as tools_router
from app.mcp.client import initialize_mcp, close_mcp


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