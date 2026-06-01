import time

cache = {}

def get_cache(key):

    if key not in cache:
        return None

    data = cache[key]

    if time.time() > data["expiry"]:
        return None

    return data["value"]


def set_cache(key, value, ttl=60):

    cache[key] = {
        "value": value,
        "expiry": time.time() + ttl
    }
