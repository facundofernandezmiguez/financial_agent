# Agenticia 🤖 - Tu Asistente Financiero con IA

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Groq](https://img.shields.io/badge/LLM-Groq-orange.svg)](https://groq.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Descripción
Agenticia es un asistente financiero de última generación que aprovecha el poder de múltiples agentes de IA para proporcionar recomendaciones de inversión informadas y análisis financiero en tiempo real. El sistema implementa una arquitectura multi-agente que combina:

- 📊 **Agente Financiero**: Análisis profundo de datos bursátiles y métricas empresariales
- 🔍 **Agente de Búsqueda Web**: Recopilación de noticias y tendencias del mercado en tiempo real
- 🤝 **Sistema Colaborativo**: Integración inteligente de insights de ambos agentes

## 🛠️ Características Principales

- **Análisis de Mercado en Tiempo Real**
  - Datos financieros actualizados mediante yfinance
  - Recomendaciones basadas en tendencias actuales
  - Visualización clara de métricas clave

- **Búsqueda Web Inteligente**
  - Integración con DuckDuckGo para noticias relevantes
  - Contextualización de eventos del mercado
  - Fuentes verificadas y actualizadas

- **Recomendaciones Personalizadas**
  - Análisis adaptado a tu perfil de riesgo
  - Sugerencias basadas en tu capital disponible
  - Estrategias de diversificación inteligente

## 📋 Requisitos Previos
- Python 3.8 o superior
- Claves API:
  - GROQ API key
  - PHI API key

## 🔧 Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/facundofernandezmiguez/agenticia.git
cd agenticia
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar variables de entorno:
Crear un archivo `.env` con:
```bash
GROQ_API_KEY=tu_clave_api_groq
PHI_API_KEY=tu_clave_api_phi
```

## 💡 Ejemplos de Uso

```python
# Obtener recomendación personalizada
python financial_agent.py --capital 1000 --risk_profile "aggressive"

# Análisis de una acción específica
python financial_agent.py --stock "AAPL" --analysis "full"
```

## 🔒 Seguridad

- Todas las claves API se manejan de forma segura mediante variables de entorno
- No se almacena información sensible del usuario
- Comunicación cifrada con las APIs

## 🤝 Contribuciones

Las contribuciones son bienvenidas! Por favor, lee nuestra guía de contribución antes de enviar un PR.


