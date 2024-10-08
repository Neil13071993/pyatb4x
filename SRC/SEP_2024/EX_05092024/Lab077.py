class Father:
    key = "2BHK"

    def car(self):
        print("Father car, ALTO",self.key)

class Son(Father):
    key2 = "3BHK"

    def home(self):
        print("3BHK")

    def truck(self):
        print("Truck")

father_object = Father()
father_object.car()

son_object = Son()
son_object.car()