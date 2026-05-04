from yahooquery import Ticker

def fetch_financial_metrics(symbol):
    try:
        stock = Ticker(symbol)
        price_data = stock.price
        
        # Yahooquery returns a string for the symbol value if the ticker is totally invalid
        if isinstance(price_data, dict) and symbol in price_data and isinstance(price_data[symbol], str):
            return None
            
        info = price_data.get(symbol, {}) if isinstance(price_data, dict) else {}
        if not info or 'regularMarketPrice' not in info:
            return None
            
        summary = stock.summary_detail.get(symbol, {}) if isinstance(stock.summary_detail, dict) else {}
        key_stats = stock.key_stats.get(symbol, {}) if isinstance(stock.key_stats, dict) else {}

        current_price = info.get('regularMarketPrice', 0)
        prev_close = info.get('regularMarketPreviousClose', 0)
        
        change = current_price - prev_close
        percent_change = (change / prev_close * 100) if prev_close else 0
        
        def format_large_number(num):
            if num is None: return "N/A"
            if num >= 1e12: return f"{num/1e12:.2f}T"
            if num >= 1e9: return f"{num/1e9:.2f}B"
            if num >= 1e6: return f"{num/1e6:.2f}M"
            return str(num)

        def f_2(num):
            return f"{num:.2f}" if isinstance(num, (int, float)) else 'N/A'

        return {
            "price": current_price,
            "change": change,
            "percent_change": percent_change,
            "open": f_2(summary.get('open') or info.get('regularMarketOpen')),
            "high": f_2(summary.get('dayHigh') or info.get('regularMarketDayHigh')),
            "low": f_2(summary.get('dayLow') or info.get('regularMarketDayLow')),
            "pe_ratio": f_2(summary.get('trailingPE')),
            "market_cap": format_large_number(summary.get('marketCap') or info.get('marketCap')),
            "avg_vol": format_large_number(summary.get('averageVolume') or info.get('regularMarketVolume')),
            "52_high": f_2(summary.get('fiftyTwoWeekHigh')),
            "52_low": f_2(summary.get('fiftyTwoWeekLow')),
            "eps": f_2(key_stats.get('trailingEps')),
            "dividend_yield": f"{summary.get('dividendYield', 0) * 100:.2f}%" if summary.get('dividendYield') else 'N/A',
            "beta": f_2(summary.get('beta')),
            "currency": info.get('currency', 'USD') 
        }
    except Exception as e:
        print(f"Error fetching yahooquery data: {e}")
        return None
