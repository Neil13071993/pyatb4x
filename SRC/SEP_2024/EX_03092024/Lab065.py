class Calc():

    def __init__(self):
        print("DC")

    def sum(self, a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def mul(self,a,b):
        return a*b

    def div(self,a,b):
        return a/b

object_ref = Calc()
output_sum = object_ref.sum(3,4)
output_sub = object_ref.sub(3,4)
output_mul = object_ref.mul(3,4)
output_div = object_ref.div(3,4)

print(output_sum)
print(output_sub)
print(output_mul)
print(output_div)

# OR
print("_______________")

object_ref = Calc()
a = int(input("Enter the value of a"))
b = int(input("Enter the value of b"))
output_sum = object_ref.sum(a,b)
output_sub = object_ref.sub(a,b)
output_mul = object_ref.mul(a,b)
output_div = object_ref.div(a,b)

print(output_sum,output_sub,output_mul,output_div)
