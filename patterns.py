def bullish_engulfing(candles):

    if len(candles) < 2:
        return False

    prev = candles[-2]
    curr = candles[-1]

    return (
        prev["close"] < prev["open"]
        and curr["close"] > curr["open"]
        and curr["open"] < prev["close"]
        and curr["close"] > prev["open"]
    )
  def bullish_engulfing(candles):

    if len(candles) < 2:
        return False

    prev = candles[-2]
    curr = candles[-1]

    return (
        prev["close"] < prev["open"]
        and curr["close"] > curr["open"]
        and curr["open"] < prev["close"]
        and curr["close"] > prev["open"]
    )
def doji(candle):

    body = abs(candle["close"] - candle["open"])
    range_size = candle["high"] - candle["low"]

    if range_size == 0:
        return False

    return body <= (range_size * 0.1)
