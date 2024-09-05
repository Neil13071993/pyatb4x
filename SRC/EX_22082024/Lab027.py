user_type = input("Enter the user type, admin,manager, guest \n")
match user_type:
    case "admin" :
        print("Hello Sir")
    case "manager":
        print("Hello manager")
    case "guest":
        print("Hello guest")
    case _:
        print(" Whats up bro")