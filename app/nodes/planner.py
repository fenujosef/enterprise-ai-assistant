import json

from app.agents.planner_schema import Plan
from app.graph.state import GraphState
from app.llm.groq_client import get_llm
from app.prompts.planner_prompt import PLANNER_PROMPT


llm = get_llm()


def planner(state: GraphState) -> GraphState:

    prompt = PLANNER_PROMPT.invoke(
        {
            "question": state["question"],
            "reflection": state["reflection"],
        }
    )

    response = llm.invoke(prompt)

    data = json.loads(response.content)

    plan = Plan.model_validate(data)

    state["plan"] = plan.model_dump()

    return state