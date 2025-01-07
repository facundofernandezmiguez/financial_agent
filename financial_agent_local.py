from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools import yfinance, duckduckgo
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

import os
from dotenv import load_dotenv

load_dotenv()

#Load environment variables
groq_api_key = os.getenv("GROQ_API_KEY")
phi_api_key = os.getenv("PHI_API_KEY")
model_id = os.getenv("MODEL_ID")

# Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Investigador de mercados financieros",
    model=Groq(id="llama-3.1-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=[
        "Busca información relevante sobre mercados y tendencias",
        "Explica las razones detrás de cada recomendación",
        "Considera múltiples factores de riesgo"
    ],
    show_tool_calls=True,
    markdown=True,
)   

# Financial Agent
finance_agent = Agent(
    name="Finance Agent",
    role="""Analista financiero experto.
           Proporciona análisis detallados del mercado y recomendaciones basadas en datos.""",
    model=Groq(id="llama-3.1-70b-versatile"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True,
        company_info=True
    )],
    instructions=[
        "Analiza datos financieros y proporciona recomendaciones detalladas",
        "Incluye siempre un resumen del mercado actual",
        "Explica las razones detrás de cada recomendación",
        "Considera múltiples factores de riesgo",
        "Utiliza tablas para mostrar datos relevantes",
        "Utiliza gráficos para visualizar tendencias y comportamientos"
    ],
    show_tool_calls=True,
    markdown=True,
)

# Multi-Agent System
multi_ai_agent = Agent(
    name="Multi-Agent System",
    role="Asesor financiero multi-agent",
    model=Groq(id="llama-3.1-70b-versatile"),
    team=[web_search_agent, finance_agent],
    instructions=[
        "Analiza datos financieros y proporciona recomendaciones detalladas",
        "Incluye siempre un resumen del mercado actual",
        "Explica las razones detrás de cada recomendación",
        "Considera múltiples factores de riesgo",    
        "Utiliza tablas para mostrar datos relevantes",
        "Utiliza gráficos para visualizar tendencias y comportamientos"
    ],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Tengo $100 para invertir en acciones de tecnología. Que recomiendas?", stream=True)