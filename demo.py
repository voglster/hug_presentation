import hug

list_of_strings = []

@hug.get('/save', examples='text_to_save=testing123')
def save(text_to_save):
    list_of_strings.append(text_to_save)
    return True


@hug.get('/data')
def data():
    return list_of_strings

@hug.get('/clear')
def clear():
    list_of_strings.clear()