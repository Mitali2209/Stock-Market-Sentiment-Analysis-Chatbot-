# 📈 StockSense AI 

StockSense AI is a full-stack, AI-powered financial dashboard that bridges the gap between raw market data and actionable insights. Built with **FastAPI** and **Vanilla JavaScript**, it integrates real-time stock metrics, news sentiment analysis, and a highly specialized AI assistant powered by **Google Gemini 2.0 Flash**.

Unlike standard chatbots, StockSense AI uses **Dynamic Context Injection**—meaning the AI "sees" the exact real-time dashboard data you are viewing to provide highly contextual, hyper-relevant financial analysis.

![StockSense AI Dashboard](link-to-your-screenshot-here.png)

## ✨ Key Features

*   **🤖 Context-Aware AI Chatbot:** Powered by Google Gemini, the chatbot acts as a professional financial analyst. It dynamically reads your currently viewed stock metrics and news feed to answer queries with precise market context.
*   **📊 Real-Time Market Data:** Integrates with `yfinance` to pull live stock prices, historical charts, Market Cap, P/E Ratios, Beta, EPS, and more.
*   **🧠 Automated News Sentiment Analysis:** Scrapes the latest financial news for a queried stock and runs it through a sentiment engine to calculate a bullish/bearish "Sentiment Score", visualized via a dynamic strength meter and doughnut chart.
*   **🎓 Educational "Layman's Terms" UI:** Designed for both experts and beginners. Hovering over complex financial metrics reveals interactive tooltips that explain concepts in plain English.
*   **⚡ Smart Query Classification:** The backend intelligently categorizes user prompts (greeting, simple definition, or deep analysis) to optimize API token usage and enforce strict, readable markdown formatting.
*   **🛡️ Multi-Model Fallback:** Engineered for high availability. If the primary AI model hits rate limits, the system automatically degrades to lighter backup models to ensure uninterrupted service.

## 🛠️ Technology Stack

**Frontend:**
*   HTML5 / CSS3 (Custom Variables, Glassmorphism UI)
*   Vanilla JavaScript (ES6+)
*   [Chart.js](https://www.chartjs.org/) (Data visualization)

**Backend:**
*   [Python 3.x](https://www.python.org/)
*   [FastAPI](https://fastapi.tiangolo.com/) (High-performance API routing)
*   [Uvicorn](https://www.uvicorn.org/) (ASGI server)
*   [yfinance](https://pypi.org/project/yfinance/) (Real-time financial data)
*   [Google GenAI SDK](https://ai.google.dev/) (LLM Integration)

## 🚀 Getting Started

### Prerequisites
*   Python 3.8+
*   A Google Gemini API Key

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/stocksense-ai.git
   cd stocksense-ai
