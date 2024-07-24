import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970


# Write your code below 👇

def speed_calc_decorator(function):
    def wrapper_function():
        time_now = time.time()
        function()
        speed = time.time() - time_now
        print(f"{function.__name__} run speed: {speed}")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        var = i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        var = i * i


fast_function()
slow_function()