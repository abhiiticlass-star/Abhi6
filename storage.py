import json
import os

FILE = "signals.json"

def load_data():

    if not os.path.exists(FILE):
        return {"history": []}

    try:
        with open(FILE, "r") as f:
            return json.load(f)

    except:
        return {"history": []}


def save_data(data):

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)
