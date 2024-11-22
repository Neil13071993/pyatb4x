class XYZ:
    def f1(self):
        try:
            a = int(input("Enter the value \n"))
        except Exception as e:
            print("Enter int only value of a")
        else:
            print(a)
        finally:
            print("Finally: Any how I will be printed")

x = XYZ()
x.f1()