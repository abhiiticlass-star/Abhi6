from datetime import datetime
import pytz

def get_market_status():

    india = pytz.timezone("Asia/Kolkata")
    now = datetime.now(india)

    if now.weekday() == 5:
        return False

    if now.weekday() == 6:
        return False

    return True
