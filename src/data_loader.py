import pandas as pd

def load_stock_csv(path):
    """
    Load historical stock data from CSV.
    Expected columns:
    Date, Open, High, Low, Close, Volume
    """
    df = pd.read_csv(path)
    df = df.dropna()
    return df
