from pydantic import BaseModel


class PlanStep(BaseModel):
    step: int
    action: str
    tool: str | None = None
    input: str


class Plan(BaseModel):
    steps: list[PlanStep]