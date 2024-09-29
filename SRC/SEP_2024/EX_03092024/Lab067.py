# patemeterised cunstructor  #error need to ask

class Calc():

    def __init__(self, a,b):
        self.a = a
        self.b = b

    def sum(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def mul(self,a,b):
        return a*b

    def div(self,a,b):
        return a/b


object_ref = Calc(3,4)
output = object_ref.sum
print(output)