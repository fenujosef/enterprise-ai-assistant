import json

from app.agents.reflection_schema import ReflectionDecision
from app.graph.state import GraphState
from app.llm.groq_client import get_llm
from app.prompts.reflection_prompt import REFLECTION_PROMPT


llm = get_llm()

def reflection(state: GraphState) -> GraphState:

    prompt = REFLECTION_PROMPT.invoke(
        {
            "question": state["question"],
            "results": str(state["step_results"])
        }
    )

    response = llm.invoke(prompt)

    data = json.loads(response.content)

    decision = ReflectionDecision.model_validate(data)

    state["reflection"] = decision.reason

    if decision.action == "retry":
        state["retry_count"] += 1

    return state