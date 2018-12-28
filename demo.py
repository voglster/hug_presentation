import hug

data = []

@hug.get('/save', examples='text_to_save=testing123')
def save(text_to_save):
    data.append(text_to_save)
    return True

@hug.get('/data')
def get_data():
    return data

@hug.get('/clear')
def get_data():
    data.clear()