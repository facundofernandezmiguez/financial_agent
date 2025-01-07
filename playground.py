from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools import yfinance, duckduckgo
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.playground import Playground, serve_playground_app 

import os
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
groq_api_key = os.getenv("GROQ_API_KEY")
phi_api_key = os.getenv("PHI_API_KEY")

# Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Financial Market Researcher",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=[
        "Always include sources of information",
    ],
    show_tool_calls=True,
    markdown=True,
)   

# Financial Agent
finance_agent = Agent(
    name="Finance Agent",
    role="Expert Financial Analyst.",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True,
        company_info=True
    )],
    instructions=[
        "Use tables to display the data"
    ],
    show_tool_calls=True,
    markdown=True,
)

# Initialize the Playground application with our agents
app = Playground(agents=[web_search_agent, finance_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
