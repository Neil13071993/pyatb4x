# multiple inheritance
class Father():

    Key = "ABC"
    __password = "private"

    def __show_password(self):
        print(self.__password)
    def father_money(self):
        return 5
    def home(self):
        print("this is from father")

    def show_everything(self):
        self.__show_password()



class Mother():
    def mother_money(self):
        return 2

    def home(self):
        print("this is from mother")

class son(Mother,Father): #MRO = Method Resolution Order
    pass

class son2(Father,Mother):
    pass



s = son()
print(s.father_money())
print(s.mother_money())
print(s.home())
print(s.Key)
s.show_everything()

