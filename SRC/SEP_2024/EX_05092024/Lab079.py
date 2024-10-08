# Multiple Inheritance

class Grand_Father:
    gold = ("2kg")

    def BHK1(self):
        print("1BHK")

class Father(Grand_Father):
    diamond = ("6 karat")

    def BHK2(self):
        print("2BHK")

class son(Father):
    btc = "50 coins"

    def BHK3(self):
        print("3BHK")


s_ref = son()
s_ref.BHK2()
father_obj = Father()
print(father_obj.diamond)
