def get_support_resistance(candles):

    lows = [c["low"] for c in candles[-50:]]
    highs = [c["high"] for c in candles[-50:]]

    support = min(lows)
    resistance = max(highs)

    return support, resistance
