import time

def time_decorator(func):

    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f" time taken by this function {start_time-end_time}")
    return wrapper()
@time_decorator
def test_UI_1():
    print("add a function, time taken by this function")
    time.sleep(2) #it will wait for 2 seconds.

