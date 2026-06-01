from indicators import (
    calculate_ema,
    calculate_rsi,
    calculate_macd
)

from patterns import (
    bullish_engulfing,
    bearish_engulfing,
    doji,
    hammer,
    shooting_star
)

from support_resistance import get_support_resistance
from breakout import breakout_signal


def generate_signal(candles):

    closes = [c["close"] for c in candles]

    ema20 = calculate_ema(closes, 20)
    ema50 = calculate_ema(closes, 50)
    ema200 = calculate_ema(closes, 200)

    rsi = calculate_rsi(closes)

    macd = calculate_macd(closes)

    current_price = closes[-1]

    support, resistance = get_support_resistance(candles)

    breakout = breakout_signal(
        current_price,
        support,
        resistance
    )

    bullish_score = 0
    bearish_score = 0

    if ema20 > ema50 > ema200:
        bullish_score += 2

    if ema20 < ema50 < ema200:
        bearish_score += 2

    if rsi > 55:
        bullish_score += 1

    if rsi < 45:
        bearish_score += 1

    if macd > 0:
        bullish_score += 1

    if macd < 0:
        bearish_score += 1

    if bullish_engulfing(candles):
        bullish_score += 2

    if bearish_engulfing(candles):
        bearish_score += 2

    if hammer(candles[-1]):
        bullish_score += 1

    if shooting_star(candles[-1]):
        bearish_score += 1

    if breakout == "UP":
        bullish_score += 2

    if breakout == "DOWN":
        bearish_score += 2

    if bullish_score >= 5:
        signal = "UP"

    elif bearish_score >= 5:
        signal = "DOWN"

    else:
        signal = "AVOID"

    total = bullish_score + bearish_score

    if total == 0:
        call_pct = 50
        put_pct = 50
    else:
        call_pct = round(
            bullish_score / total * 100
        )
        put_pct = 100 - call_pct

    trend = "Neutral"

    if ema20 > ema50:
        trend = "Bullish"

    if ema20 < ema50:
        trend = "Bearish"

    return {
        "signal": signal,
        "trend": trend,
        "callPct": call_pct,
        "putPct": put_pct
    }
