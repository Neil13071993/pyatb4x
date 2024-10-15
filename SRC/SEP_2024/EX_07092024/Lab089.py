class GF():
    x = 10
    def home(self):
        print("old home")

class Father(GF):
    a = 10
    def home(self):
        print("1BHK")
        print(self.a)
        print(super().x)

class Son(Father):
    b = 10
    def home(self):
        super().home()
        print("No Home")
        print(self.b)
        print(super().a)



nilesh = Son()
nilesh.home()
print(nilesh.x)

