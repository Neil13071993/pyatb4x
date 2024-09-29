#class Person:

 #   name = "nilesh"

 #   def walk(self,name):
 #       self.name = nilesh
  #      print(self.name)

#nilesh = Person()
#print(nilesh.name)

#cunstructor is basically used to change the value of insatance variable.
#print("_____________________")
class Person:

    def __init__(self,name):
        self.name = name

    def walk(self,name):
        print(self.name)

nilesh = Person("nilesh")
pramod = Person("pramod")
print(nilesh.name)
print(pramod.name)
