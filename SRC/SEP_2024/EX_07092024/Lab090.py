class MathUtils():
    def add(self,a,b):
        return a+b

    def add(self,a,b,c=0):
        return a+b+c


math = MathUtils()
op1 = math.add(3,5)
print(op1)