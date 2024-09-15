def add_before_ui_after_ui(func):
    def wrapper():
        print("before running UI TC")
        print("start the browser")
        func()
        print("ending running UI TC")
        print("Quit the browser")
    return wrapper()

@add_before_ui_after_ui
def test_ui():
    print("I will test the UI")
