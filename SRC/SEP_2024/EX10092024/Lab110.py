# Custome Exception - Own

class MyCustomeException(Exception):

     def __init__(self,message):
         self.message = message
         super().__init__(message)

balance = 100
withdraw = int(input("Enter the amount you want to withdraw"))
if withdraw > balance:
    raise MyCustomeException("Balance is low")
else:
    print("Remaining Balance",(balance-withdraw))

