# Hierarchical Inheritance

class Father():
    def BHK1(self):
        print("1BHK")

class nilesh(Father):
    def BHK2(self):
        print("2BHK")

class yogesh(Father):
    def BHK3(self):
        print("3BHK")

class shailesh(Father):
    def no_house(self):
        print("no_house")


Nilesh = nilesh()
Nilesh.BHK2()
Nilesh.BHK1()

Yogesh = yogesh()
Yogesh.BHK3()
Yogesh.BHK1()
