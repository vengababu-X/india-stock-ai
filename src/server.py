from flask import Flask, jsonify
import pandas as pd
from joblib import load
from features import add_indicators

app = Flask(__name__)
model = load("model.joblib")

@app.route("/signal/<symbol>")
def signal(symbol):
    df = pd.read_csv(f"data/{symbol}.csv")
    df = add_indicators(df)

    latest = df.iloc[-1][["rsi","ema20","ema50","macd"]].values.reshape(1, -1)
    prediction = model.predict(latest)[0]

    return jsonify({
        "symbol": symbol,
        "signal": "BUY" if prediction == 1 else "SELL"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
