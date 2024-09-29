#Take a input and create a class person

class person():
    def __init__(self):
        self.name = input("Enter the name\n")
        self.age = input("Enter the age\n")
        self.occupation = input("Enter the occupation\n")
        self.phone = input("Enter the phone\n")

    def name_of_the_function_to_display(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")
        print(f"occupation is {self.occupation}")
        print(f"phone  is {self.phone}")

#Create an Object
person1 = person()

# Call the display
person1.name_of_the_function_to_display()

