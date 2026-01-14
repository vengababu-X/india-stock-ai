from sklearn.ensemble import RandomForestClassifier
from joblib import dump, load

def train_model(df):
    X = df[["rsi", "ema20", "ema50", "macd"]]
    y = (df["Close"].shift(-1) > df["Close"]).astype(int)

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    model.fit(X[:-1], y[:-1])
    dump(model, "model.joblib")
    return model

def load_model():
    return load("model.joblib")
