# x=10
# y=20
# print(x>y)
# print(x<y)

# a=20
# b=30
# print(a>=b)  # 20>30 or 20=30


number1 = int(input("enter a number1\n"))
number2 = int(input("enter a number2\n"))

if number1 > number2:
    print(f"{number1} is greater than {number2}")
elif number1 < number2:
    print(f"{number1} is less than {number2}")
else:
    print(f"{number1} is equal to {number2}")
