from fastapi import FastAPI
from main import app as compiled_graph, CustState

api = FastAPI(title="Customer Info Bot")

@api.get("/query/{customer_number}")
def query_customer(customer_number: str):
    """
    Forward the customer_number to the LangGraph workflow
    and return the aggregated result.
    """
    # create the state object with the path parameter
    initial_state = CustState(customer_number=customer_number)

    # IMPORTANT: run the compiled graph, not the module
    final_state = compiled_graph.run(initial_state)

    # return all fields as JSON
    return final_state.dict()

