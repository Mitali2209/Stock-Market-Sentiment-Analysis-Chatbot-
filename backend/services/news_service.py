
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("FINNHUB_API_KEY")

import datetime

def fetch_news(symbol):
    """
    Fetch news using Finnhub.
    """
    try:
        end_date = datetime.datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
        url = f"https://finnhub.io/api/v1/company-news?symbol={symbol}&from={start_date}&to={end_date}&token={API_KEY}"
        news_data = requests.get(url, timeout=10).json()
        
        if not news_data:
            print(f"DEBUG: No news found for {symbol} via Finnhub")
            return []

        articles = []
        # Take up to 8 articles for better distribution
        for item in news_data[:8]:
            articles.append({
                "title": item.get("headline", "No Title"),
                "url": item.get("url", "#")
            })

        return articles
    except Exception as e:
        print(f"DEBUG: News Error (Finnhub): {e}")
        return []

def get_stock_symbol(stock_name):
    """
    Still use Finnhub for symbol search as it handles company names better than yfinance.
    """
    try:
        url = f"https://finnhub.io/api/v1/search?q={stock_name}&token={API_KEY}"
        data = requests.get(url).json()

        if data.get("count", 0) == 0 and " " in stock_name:
            return get_stock_symbol(stock_name.split()[0])

        if data.get("count", 0) > 0:
            results = data["result"]
            query_upper = stock_name.upper()

            def score_result(res):
                symbol = res.get("symbol", "").upper()
                desc = res.get("description", "").upper()
                score = 0
                
                if symbol == query_upper:
                    score += 100
                
                base_symbol = symbol.split(".")[0] if "." in symbol else symbol
                if base_symbol == query_upper:
                    score += 50
                    
                desc_words = desc.split()
                if query_upper in desc_words:
                    score += 40
                elif query_upper in desc:
                    score += 10
                    
                if "." not in symbol:
                    score += 5
                elif symbol.endswith(".NS") or symbol.endswith(".BO"):
                    score += 4
                
                return score

            results_sorted = sorted(results, key=score_result, reverse=True)
            best_result = results_sorted[0]
            
            return best_result["symbol"], best_result["description"]
    except Exception as e:
        print(f"DEBUG: Symbol Search Error: {e}")
    
    return None, None