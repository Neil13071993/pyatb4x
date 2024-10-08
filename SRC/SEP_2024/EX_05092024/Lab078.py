class Parent:
    gold = "2Kg"

    def BHK2(self):
        print("2BHK")

class Child(Parent):

    def BHK3(self):
        print("3BHK")

child_object = Child()
print(child_object.gold)
child_object.BHK2()
child_object.BHK3()

father_object = Parent()
father_object.BHK2()