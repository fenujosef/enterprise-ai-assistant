from pydantic import BaseModel


class ReflectionDecision(BaseModel):
    success: bool
    reason: str
    action: str