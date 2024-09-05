# Match statement
# switch in Java
## match variable:
#     case pattern1:
#         # code block
#     case pattern2:
#         # code block
# Write a program to ask the user which browser he want to run automation

browser_name = input("enter the name of the browser \n")
match browser_name:
    case "firefox":
        print("execute the firefox code")
    case "chrome":
        print("execute the chrome code")
    case "edge":
        print("execute the edge code")
    case "safari":
        print("execute the safari code")
    case _:
        print("browser not found")

        # or

browser_name = input("enter the name of the browser \n")
browser_name=browser_name.lower()
match browser_name:
    case "firefox":
        print("execute the firefox code")
    case "chrome":
        print("execute the chrome code")
    case "edge":
        print("execute the edge code")
    case "safari":
        print("execute the safari code")
    case _:
        print("browser not found")