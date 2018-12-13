import hug


@hug.get("/hello")
def hello():
    return "World"

