#import re
import json

from app.agents.router_schema import RouterDecision
from app.graph.state import GraphState
from app.llm.groq_client import get_llm
from app.prompts.router_prompt import ROUTER_PROMPT
from app.observability.logger import observe_node


llm = get_llm()
structured_llm = llm.with_structured_output(RouterDecision, method="json_schema")


@observe_node("agent")
def agent(state: GraphState) -> GraphState:
    """Decide whether a tool should be used."""

    tools = state["action"]

    prompt = ROUTER_PROMPT.invoke(
        {
            "question": state["question"],
            "tools": str(tools),
        }
    )

    # response = llm.invoke(prompt)

    # data = json.loads(response.content)

    # decision = RouterDecision.model_validate(data)
    decision = structured_llm.invoke(prompt)

    state["action"] = decision.action
    state["tool_name"] = decision.tool
    state["tool_input"] = decision.input
    state["tool_arguments"] = decision.arguments

    return state