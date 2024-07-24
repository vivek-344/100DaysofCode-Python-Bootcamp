import time


def decorator(function):
    def wrapper():
        time.sleep(2)
        function()
        function()
        print(f"Ran {function.__name__} function twice.")
    return wrapper


@decorator
def say_hello():
    print("Hello!")


@decorator
def say_bye():
    print("Bye!")


def greetings():
    print("How are you?")


say_hello()
say_bye()
decorated_greetings = decorator(greetings)
decorated_greetings()
