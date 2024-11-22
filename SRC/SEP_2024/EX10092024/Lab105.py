try:
    num1 = int(input("enter num 1\n"))
    num2 = int(input("enter num 2\n"))
    result = num1/num2
except ValueError as ve:
    print("Value Error, you have entered string instead we want int")

except ZeroDivisionError as zde:
    print("Zero division Error, dont use num2 value as 0")
finally:
    print("this code will always be executed")