# no return type , no argument/parameter

def greet():
    print("Hello World")

result = greet()
print(result)

# no return type with argument.
def greet_by_name(name):
    print("Hello" , name)

greet_by_name("Nilesh")

# no return type with default programme
def say_hello_default_argument(name="pramod"):
    print("Hello", name)

say_hello_default_argument("nilesh")
say_hello_default_argument()

# multiple arguments
def multiple_args(name1="nilesh", name2="akshay", name3="yogesh"):
    print("Multiple arguments", name1,name2,name3)

multiple_args(name1="Jayesh", name2="Shubham", name3="MJ")

# Argument + return type
def sum_of_two_numbers(num1,num2):
    return(num1+num2)
result = sum_of_two_numbers(10,20)
print(result)