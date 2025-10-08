from langchain.tools import BaseTool
from office365.sharepoint.client_context import ClientContext
import os

class SharePointAgent(BaseTool):
    name = "sharepoint_agent"
    description = "Fetch customer info from SharePoint by customer number"

    def _run(self, customer_number: str):
        ctx = ClientContext(os.getenv("SHAREPOINT_SITE_URL")).with_client_credentials(
            os.getenv("SHAREPOINT_CLIENT_ID"),
            os.getenv("SHAREPOINT_CLIENT_SECRET")
        )
        list_obj = ctx.web.lists.get_by_title("CustomerList")
        items = list_obj.items.filter(f"CustomerNumber eq '{customer_number}'").get().execute_query()
        return [i.properties for i in items]

    async def _arun(self, customer_number: str):
        return self._run(customer_number)
