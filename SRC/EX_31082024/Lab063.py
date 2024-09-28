# Constructor
# Special Function in Class,  __init__()
# It will be automatically called when you create an Object

class Dog:
    name = None
    age = None
    # Color = Black

    def __init__(self,name,age):
        print("Called, Object is created")
        self.name = name
        self.age = age

    def sleep(self):
        local_variable = 10
        print("sleeping")
        print("Who is sleeping ->", self.name,self.age)

dog1 = Dog("chaw",10)
print(dog1.name)
dog1.sleep()

dog2 = Dog("Mow",20)
print(dog2.name)
dog2.sleep()

