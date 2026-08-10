from langgraph.graph import StateGraph, START, END
from app.graph.state import GraphState
from app.nodes.retrieve import retrieve
from app.nodes.generate import generate
from app.nodes.rewrite import rewrite
from app.nodes.agent import agent
from app.nodes.planner import planner
from app.nodes.plan_executor import plan_executor
from app.nodes.tool_executor import tool_executor
from app.nodes.reflection import reflection
from app.nodes.tool_discovery import tool_discovery


def route_after_agent(state):
    """Decide the next node after the agent."""

    if state["action"] == "plan":
        return "plan"

    if state["action"] == "tool":
        return "tool"

    return "rewrite"

def route_after_execution(state):

    if state["current_step"] < len(state["plan"]["steps"]):
        return "continue"

    return "done"

def route_after_reflection(state):

    action = state["reflection_action"]

    if action == "replan":
        return "replan"

    if action == "retry" and state["retry_count"] < 2:
        return "retry"
    
    return "finish"



graph_builder = StateGraph(GraphState)

graph_builder.add_node("retrieve", retrieve)
graph_builder.add_node("generate", generate)
graph_builder.add_node("rewrite", rewrite)
graph_builder.add_node("agent", agent)
graph_builder.add_node("planner", planner)
graph_builder.add_node("plan_executor", plan_executor)
graph_builder.add_node("tool_executor", tool_executor)
graph_builder.add_node("reflection", reflection)
graph_builder.add_node("tool_discovery", tool_discovery)

graph_builder.add_edge(START, "tool_discovery")
graph_builder.add_edge("tool_discovery", "agent")
graph_builder.add_conditional_edges("agent", route_after_agent, {"tool": "tool_executor","plan": "planner", "rewrite":"rewrite"})
graph_builder.add_edge("tool_executor", "generate")
graph_builder.add_edge("planner", "plan_executor")
graph_builder.add_conditional_edges("plan_executor",route_after_execution,{"continue": "plan_executor", "done": "reflection",})
graph_builder.add_conditional_edges("reflection", route_after_reflection, {"retry": "plan_executor", "replan": "planner", "finish": "generate"})
graph_builder.add_edge("rewrite", "retrieve")
graph_builder.add_edge("retrieve", "generate")
graph_builder.add_edge("generate", END)

graph = graph_builder.compile()