import hug

strings = []

@hug.get("/save", examples=['new_string=test1','new_string=test2'])
def save(new_string):
    strings.append(new_string)
    return True

@hug.get("/data")
def recall():
    return strings

@hug.get("/clear")
def clear():
    strings.clear()
    return True
