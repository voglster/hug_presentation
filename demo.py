import hug

data = []

@hug.get("/save", examples="word=test")
def save(word):
    data.append(word)
    return True

@hug.get("/data")
def get_data():
    return data

@hug.get("/clear")
def clear_data():
    data.clear()
    return True