"""
Agentic IA - Asistente Financiero Multi-Agente
Este módulo implementa un sistema de asistencia financiera basado en múltiples agentes de IA
que colaboran para proporcionar recomendaciones de inversión y análisis de mercado.
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import logging
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools import duckduckgo
import os   
from dotenv import load_dotenv

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class AgentConfig:
    """Configuración para los agentes de IA"""
    model_id: str = "llama-3.1-70b-versatile"
    show_tool_calls: bool = True
    markdown_output: bool = True

class FinancialAssistant:
    """
    Asistente financiero que utiliza múltiples agentes de IA para proporcionar
    recomendaciones de inversión y análisis de mercado.
    """
    
    def __init__(self, config: Optional[AgentConfig] = None):
        """
        Inicializa el asistente financiero.
        
        Args:
            config: Configuración opcional para los agentes
        """
        self.config = config or AgentConfig()
        self._load_environment()
        self._initialize_agents()
    
    def _load_environment(self) -> None:
        """Carga las variables de entorno necesarias"""
        try:
            load_dotenv()
            required_vars = ['PHI_API_KEY', 'GROQ_API_KEY']
            missing_vars = [var for var in required_vars if not os.getenv(var)]
            
            if missing_vars:
                raise EnvironmentError(f"Faltan variables de entorno: {', '.join(missing_vars)}")
                
            for var in required_vars:
                os.environ[var] = os.getenv(var)
                
        except Exception as e:
            logger.error(f"Error cargando variables de entorno: {str(e)}")
            raise

    def _initialize_agents(self) -> None:
        """Inicializa los agentes de IA con sus configuraciones específicas"""
        try:
            self.web_search_agent = Agent(
                name="Web Search Agent",
                role="Search the web for market trends and news",
                model=Groq(id=self.config.model_id),
                tools=[duckduckgo.DuckDuckGo()],
                instructions=["Always include sources", "Focus on recent and relevant financial news"],
                show_tool_calls=self.config.show_tool_calls,
                markdown=self.config.markdown_output,
            )

            self.finance_agent = Agent(
                name="Finance Agent",
                role="Analyze financial data and provide investment insights",
                model=Groq(id=self.config.model_id),
                tools=[YFinanceTools(
                    stock_price=True,
                    analyst_recommendations=True,
                    company_info=True
                )],
                instructions=[
                    "Use tables to display data",
                    "Always include risk warnings",
                    "Provide comprehensive analysis"
                ],
                show_tool_calls=self.config.show_tool_calls,
                markdown=self.config.markdown_output,
            )

            self.multi_ai_agent = Agent(
                team=[self.web_search_agent, self.finance_agent],
                model=Groq(id=self.config.model_id),
                instructions=[
                    "Combine insights from market news and financial data",
                    "Provide clear investment recommendations",
                    "Always include risk considerations",
                    "Use tables and formatting for clarity"
                ],
                show_tool_calls=self.config.show_tool_calls,
                markdown=self.config.markdown_output,
            )
            
        except Exception as e:
            logger.error(f"Error inicializando agentes: {str(e)}")
            raise

    def get_investment_recommendation(
        self,
        capital: float,
        risk_profile: str = "moderate",
        preferences: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Obtiene una recomendación de inversión personalizada.
        
        Args:
            capital: Cantidad disponible para invertir
            risk_profile: Perfil de riesgo del inversor ('conservative', 'moderate', 'aggressive')
            preferences: Preferencias adicionales del inversor
            
        Returns:
            str: Recomendación detallada de inversión
        """
        try:
            query = self._build_recommendation_query(capital, risk_profile, preferences)
            response = self.multi_ai_agent.print_response(query, stream=True)
            return response
            
        except Exception as e:
            logger.error(f"Error obteniendo recomendación: {str(e)}")
            raise

    def analyze_stock(self, symbol: str, analysis_type: str = "full") -> str:
        """
        Realiza un análisis detallado de una acción específica.
        
        Args:
            symbol: Símbolo de la acción a analizar
            analysis_type: Tipo de análisis ('basic', 'full', 'technical')
            
        Returns:
            str: Análisis detallado de la acción
        """
        try:
            query = f"Analyze {symbol} stock with {analysis_type} analysis. Include market context and risks."
            return self.multi_ai_agent.print_response(query, stream=True)
            
        except Exception as e:
            logger.error(f"Error analizando acción {symbol}: {str(e)}")
            raise

    def _build_recommendation_query(
        self,
        capital: float,
        risk_profile: str,
        preferences: Optional[Dict[str, Any]]
    ) -> str:
        """Construye la consulta para la recomendación de inversión"""
        query = f"I have ${capital} to invest with a {risk_profile} risk profile."
        if preferences:
            query += f" Additional preferences: {preferences}"
        return query

def main():
    """Función principal para ejecutar el asistente"""
    try:
        assistant = FinancialAssistant()
        
        # Ejemplo de uso
        capital = 1000
        risk_profile = "moderate"
        preferences = {"sectors": ["tech", "renewable energy"], "timeframe": "long-term"}
        
        print("🤖 Obteniendo recomendación de inversión...")
        recommendation = assistant.get_investment_recommendation(
            capital=capital,
            risk_profile=risk_profile,
            preferences=preferences
        )
        print(recommendation)
        
    except Exception as e:
        logger.error(f"Error en la ejecución principal: {str(e)}")
        raise

if __name__ == "__main__":
    main()