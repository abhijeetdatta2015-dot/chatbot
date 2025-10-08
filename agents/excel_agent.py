from langchain.tools import BaseTool
import pandas as pd

class ExcelAgent(BaseTool):
    name = "excel_agent"
    description = "Fetch customer info from Excel by customer number"

    def _run(self, customer_number: str):
        df = pd.read_excel("E:\AI and Data Analytics Project\Consolidate Project\OneDrive_2025-09-11\CCH-Use case\Monster Promo Buy and Save 30 cases.xlsx")
        #result = df[df.loc[16, "SoldTo customer host code"] == customer_number]
        #return result.to_dict(orient="records")
        match = df.loc[df['SoldTo customer host code'] == int(state.customer_number)]
        if not match.empty:
            state.excel_result = match.iloc[0].to_dict()
        else:
            state.excel_result = "not found"
        return state

    async def _arun(self, customer_number: str):
        return self._run(customer_number)
