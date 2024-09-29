class Car:

    def __init__(self,o_name,o_make,o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model


    def start_the_engine(self):
        print("Starting a car with name" + self.name)
        print("Starting a car with make" + self.make)
        print("Starting a car with model" + self.model)



lambo = Car("lambo", "V2","2024")
lambo.start_the_engine()


xuv = Car("XUV", "V6", "2023")
xuv.start_the_engine()
