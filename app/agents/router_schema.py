from typing import Literal

from pydantic import BaseModel, Field


class RouterDecision(BaseModel):

    action: Literal["rag", "tool", "plan"]

    tool: str = ""

    input: str = ""

    arguments: dict = Field(
        default_factory=dict
    )