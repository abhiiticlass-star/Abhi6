def breakout_signal(price, support, resistance):

    if price > resistance:
        return "UP"

    if price < support:
        return "DOWN"

    return None
