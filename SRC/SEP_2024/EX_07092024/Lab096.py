class MathOperations():

    def div(self,a,b):
        return a/b

    def mult(self,a,b):
        return a*b

    @staticmethod
    def sum(a,b):
        return a+b

    @staticmethod
    def sub(a, b):
        return a - b

# Non Static in Nature - Object creation is mandatory
obj_ref = MathOperations()
output1 = obj_ref.div(5,10)
output2 = obj_ref.mult(5,10)
print(output1)
print(output2)
# Static methods can be called direclty without the Object.
print(MathOperations.sum(5,13))
print(MathOperations.sub(5,13))