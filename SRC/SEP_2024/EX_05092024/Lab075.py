class Myclass:
    Balance = 0
    # Public variable (#instance Variable)
    public_var = "I am PUBLIC"
    # Private variable
    __private_var = "I am PRIVATE"
    __password = "1234"
    # Private variable
    _protected_var = "I am PROTECTED"


object = Myclass
print(object.public_var)
print(object.Balance)
print(object._protected_var)
# print(object.private_var)
# print(object.password)
