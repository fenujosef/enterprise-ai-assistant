from pydantic import BaseModel, Field


class RouterDecision(BaseModel):
    action: str
    tool: str
    input: str
    arguments: dict = Field(default_factory=dict)