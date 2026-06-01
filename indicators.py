def calculate_ema(prices, period):

    multiplier = 2 / (period + 1)

    ema = [sum(prices[:period]) / period]

    for price in prices[period:]:

        ema.append(
            (price - ema[-1]) * multiplier + ema[-1]
        )

    return ema[-1]
  def calculate_rsi(prices, period=14):

    gains = []
    losses = []

    for i in range(1, len(prices)):

        diff = prices[i] - prices[i - 1]

        if diff > 0:
            gains.append(diff)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(abs(diff))

    avg_gain = sum(gains[-period:]) / period
    avg_loss = sum(losses[-period:]) / period

    if avg_loss == 0:
        return 100

    rs = avg_gain / avg_loss

    return 100 - (100 / (1 + rs))
