# Agenticia - AI-Powered Financial Assistant

An intelligent financial assistant powered by Large Language Models (LLMs) that combines market research and financial analysis capabilities through a user-friendly interface.

## 🚀 Features

- **Web Search Agent**: Researches market trends and financial news using DuckDuckGo integration
- **Financial Analysis Agent**: Provides stock analysis and investment recommendations using real-time market data
- **Interactive Playground**: User-friendly interface to interact with both agents
- **Real-time Data**: Integration with YFinance for up-to-date market information
- **Multilingual Support**: Capable of processing queries and providing responses in multiple languages

## 🛠️ Technology Stack

- Python 3.12+
- Groq LLM (llama-3.3-70b-versatile model)
- Phi Framework for AI Agents
- YFinance for real-time market data
- DuckDuckGo for web search capabilities
- FastAPI & Uvicorn for the web interface

## 📋 Prerequisites

- Python 3.12 or higher
- Groq API key
- Phi API key

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/facundofernandezmiguez/agenticia.git
cd agenticia
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Unix or MacOS
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your API keys:
```env
GROQ_API_KEY=your_groq_api_key
PHI_API_KEY=your_phi_api_key
```

## 🚀 Usage

Run the application:
```bash
python playground.py
```

The interactive playground will be available at `http://localhost:8000`

## 📝 Example Queries

- "What are the current market trends in tech stocks?"
- "Analyze the performance of AAPL stock"
- "I have $1000 to invest, what do you recommend?"
- "What are the top-performing stocks in the renewable energy sector?"

## 🤝 Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.


