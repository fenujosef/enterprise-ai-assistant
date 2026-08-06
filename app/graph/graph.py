from langgraph.graph import StateGraph, START, END
from app.graph.state import GraphState
from app.nodes.retrieve import retrieve
from app.nodes.generate import generate
from app.nodes.rewrite import rewrite


graph_builder = StateGraph(GraphState)

graph_builder.add_node("retrieve", retrieve)
graph_builder.add_node("generate", generate)
graph_builder.add_node("rewrite", rewrite)

graph_builder.add_edge(START, "rewrite")
graph_builder.add_edge("rewrite", "retrieve")
graph_builder.add_edge("retrieve", "generate")
graph_builder.add_edge("generate", END)

graph = graph_builder.compile()