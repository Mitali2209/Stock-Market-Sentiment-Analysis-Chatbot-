import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("FINNHUB_API_KEY")

def fetch_financial_metrics(symbol):
    try:
        quote_url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={API_KEY}"
        quote_data = requests.get(quote_url, timeout=10).json()
        
        # Check if invalid ticker (Finnhub returns d: None and c: 0 for invalid tickers)
        if quote_data.get('d') is None and quote_data.get('c') == 0:
            return None
            
        metric_url = f"https://finnhub.io/api/v1/stock/metric?symbol={symbol}&metric=all&token={API_KEY}"
        metric_res = requests.get(metric_url, timeout=10).json()
        metric_data = metric_res.get('metric', {})

        current_price = quote_data.get('c', 0)
        prev_close = quote_data.get('pc', 0)
        change = quote_data.get('d', 0)
        percent_change = quote_data.get('dp', 0)
        
        def format_large_number(num):
            if num is None: return "N/A"
            if num >= 1e12: return f"{num/1e12:.2f}T"
            if num >= 1e9: return f"{num/1e9:.2f}B"
            if num >= 1e6: return f"{num/1e6:.2f}M"
            return str(num)

        def f_2(num):
            return f"{num:.2f}" if isinstance(num, (int, float)) else 'N/A'

        mkt_cap = metric_data.get('marketCapitalization')
        if mkt_cap: mkt_cap = mkt_cap * 1000000

        vol = metric_data.get('10DayAverageTradingVolume')
        if vol: vol = vol * 1000000

        div = metric_data.get('dividendYieldIndicatedAnnual')
        div_str = f"{div:.2f}%" if div else 'N/A'

        return {
            "price": current_price,
            "change": change,
            "percent_change": percent_change,
            "open": f_2(quote_data.get('o')),
            "high": f_2(quote_data.get('h')),
            "low": f_2(quote_data.get('l')),
            "pe_ratio": f_2(metric_data.get('peTTM') or metric_data.get('peBasicExclExtraTTM')),
            "market_cap": format_large_number(mkt_cap),
            "avg_vol": format_large_number(vol),
            "52_high": f_2(metric_data.get('52WeekHigh')),
            "52_low": f_2(metric_data.get('52WeekLow')),
            "eps": f_2(metric_data.get('epsTTM') or metric_data.get('epsBasicExclExtraItemsTTM')),
            "dividend_yield": div_str,
            "beta": f_2(metric_data.get('beta')),
            "currency": "USD" 
        }
    except Exception as e:
        print(f"Error fetching Finnhub data: {e}")
        return None
