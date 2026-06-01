import requests
import os

API_KEY = os.getenv("TWELVE_DATA_API_KEY")

BASE_URL = "https://api.twelvedata.com/time_series"


def get_candles(symbol, interval="1min", outputsize=200):

    params = {
        "symbol": symbol,
        "interval": interval,
        "outputsize": outputsize,
        "apikey": API_KEY,
        "format": "JSON"
    }

    response = requests.get(BASE_URL, params=params, timeout=20)

    data = response.json()

    if "values" not in data:
        return None

    candles = []

    for row in reversed(data["values"]):

        candles.append({
            "datetime": row["datetime"],
            "open": float(row["open"]),
            "high": float(row["high"]),
            "low": float(row["low"]),
            "close": float(row["close"])
        })

    return candles
