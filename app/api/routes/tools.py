from fastapi import APIRouter

from app.tools.catalog import get_tool_catalog

router = APIRouter()

@router.get("/tools")
async def tools():

    return {
        "tools": await get_tool_catalog()
    }