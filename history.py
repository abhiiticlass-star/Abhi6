from storage import load_data, save_data

MAX_HISTORY = 10


def add_history(entry):

    data = load_data()

    data["history"].insert(0, entry)

    data["history"] = data["history"][:MAX_HISTORY]

    save_data(data)


def get_history():

    data = load_data()

    return data["history"]
