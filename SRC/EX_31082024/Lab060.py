class Person:
    #Attributes
    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    Phone_no = None
    Address = None

    #Behaviour
    def talk(self):   # NRNG  # self - this , self will be first argument in every behaviour.
        print ("I can talk")

    def sleep(self,name):
        print(" I am a Method")
        print("sleep",name)

    def sleep2(self,name):
        print("I am a Method")
        return None
    def walk(self):
        print(" I am walking")

    def walk_return(self):
        return "I am walking"

    # Create object off the class
    # ObjectRef = Classname()  -> Objec

tushar = Person()
tushar.name = "tushar"
print(tushar.name)
tushar.talk()

nilesh = Person()
nilesh.name = "Nilesh"
print(nilesh.name)
nilesh.talk()

