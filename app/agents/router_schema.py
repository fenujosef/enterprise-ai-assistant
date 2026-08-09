from pydantic import BaseModel


class RouterDecision(BaseModel):
    action: str
    tool: str
    input: str