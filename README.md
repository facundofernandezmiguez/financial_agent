# Asistente Financiero con IA

## 🚀 Descripción
Agenticia es un asistente financiero inteligente que combina el poder de múltiples agentes de IA para proporcionar recomendaciones de inversión informadas y análisis financiero. El sistema utiliza dos agentes especializados:
- Un agente de búsqueda web para obtener información actualizada del mercado
- Un agente financiero para analizar datos específicos de acciones y empresas

## 🛠️ Características
- Análisis de datos financieros en tiempo real
- Recomendaciones de inversión personalizadas
- Búsqueda web integrada para contexto del mercado
- Visualización de datos en formato tabular
- Información detallada de empresas y acciones

## 📋 Requisitos Previos
- Python 3.8 o superior
- Claves API:
  - GROQ API key
  - PHI API key

## 🔧 Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tuusuario/agenticia.git
cd agenticia
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar variables de entorno:
Crear un archivo `.env` con:
```
GROQ_API_KEY=tu_clave_api_groq
PHI_API_KEY=tu_clave_api_phi
```

## 🚀 Uso
El asistente puede ayudarte a tomar decisiones de inversión basadas en tu perfil de riesgo y capital disponible. Por ejemplo:
```python
python financial_agent.py
```

## 🔍 Tecnologías Utilizadas
- Groq LLM (llama-3.1-70b-versatile)
- phidata para gestión de agentes de IA
- yfinance para datos financieros
- DuckDuckGo para búsqueda web

