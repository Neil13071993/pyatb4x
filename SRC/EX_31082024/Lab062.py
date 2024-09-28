class Dog: #class name will always start from capital letter

    name = None
    breed = None
    color = None

    def sleep(self):
        print("I am sleeping")

    def bark(self):
        print("I am barking")

    def eat(self):
        print("I am eating")

dog1 = Dog()
print(dog1.name)
dog1.name = "chaw"
print(dog1.name)
dog1.sleep()

print("------------")

dog2 = Dog()
print(dog2.name)
dog2.name = "mow"
print(dog2.name)
dog2.sleep()
