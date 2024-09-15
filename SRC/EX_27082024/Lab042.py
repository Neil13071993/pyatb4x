def my_decorator(func):


    def wrapper():
        print("before the function is called")
        print("add helmet", "gloves", "dashcam")
        #drive_bike()
        func()
        print("after the function is called")
        print("secure driving")
    return wrapper()

@my_decorator
def drive_bike():
    print("I am driving")

