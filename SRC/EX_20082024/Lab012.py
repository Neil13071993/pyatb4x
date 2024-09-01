# write programme to find max between Three number
# number1 = input("enter the number1\n")
number1 = int(input("enter the number1\n"))

# number2 = input("enter the number2\n")
number2 = int(input("enter the number2\n"))
number3 = int(input("enter the number3\n"))

if number1 > number2 and number1 > number3:
    print("Max is", number1)
elif number2 > number1 and number2 > number3:
    print("Max is", number2)
else:
    print("Max is", number3)

result = max(number1, number2, number3)
print(result)
