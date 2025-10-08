from langchain.tools import BaseTool
import tableauserverclient as TSC
import os

class TableauAgent(BaseTool):
    name = "tableau_agent"
    description = "Fetch customer analytics from Tableau by customer number"

    def _run(self, customer_number: str):
        tableau_auth = TSC.PersonalAccessTokenAuth(
            os.getenv("TABLEAU_TOKEN_NAME"),
            os.getenv("TABLEAU_TOKEN"),
            os.getenv("TABLEAU_SITE_ID")
        )
        server = TSC.Server(os.getenv("TABLEAU_SERVER"), use_server_version=True)
        with server.auth.sign_in(tableau_auth):
            # Replace with actual Tableau query
            return {"customer_number": customer_number, "sales_metrics": "Sample metrics"}

    async def _arun(self, customer_number: str):
        return self._run(customer_number)
