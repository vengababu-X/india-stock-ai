import ta

def add_indicators(df):
    df["rsi"] = ta.momentum.RSIIndicator(df["Close"]).rsi()
    df["ema20"] = ta.trend.EMAIndicator(df["Close"], 20).ema_indicator()
    df["ema50"] = ta.trend.EMAIndicator(df["Close"], 50).ema_indicator()
    df["macd"] = ta.trend.MACD(df["Close"]).macd_diff()
    df = df.dropna()
    return df
