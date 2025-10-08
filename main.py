# main.py
from langgraph.graph import StateGraph
from pydantic import BaseModel

class CustState(BaseModel):
    customer_number: str
    excel_result: str | None = None
    sharepoint_result: str | None = None
    tableau_result: str | None = None

def excel_agent(state: CustState) -> CustState:
    state.excel_result = f"Excel info for {state.customer_number}"
    return state

def sharepoint_agent(state: CustState) -> CustState:
    state.sharepoint_result = f"SharePoint info for {state.customer_number}"
    return state

def tableau_agent(state: CustState) -> CustState:
    state.tableau_result = f"Tableau info for {state.customer_number}"
    return state

def aggregate_results(state: CustState) -> CustState:
    return state

graph = StateGraph(CustState)
graph.add_node("excel_agent", excel_agent)
graph.add_node("sharepoint_agent", sharepoint_agent)
graph.add_node("tableau_agent", tableau_agent)
graph.add_node("aggregate_results", aggregate_results)

graph.set_entry_point("excel_agent")
graph.add_edge("excel_agent", "sharepoint_agent")
graph.add_edge("sharepoint_agent", "tableau_agent")
graph.add_edge("tableau_agent", "aggregate_results")

# Compile the graph and expose it as `app`
app = graph.compile()
