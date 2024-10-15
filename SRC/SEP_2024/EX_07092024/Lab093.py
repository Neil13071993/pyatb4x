from abc import ABC, abstractmethod
class pyATB(ABC):
    @abstractmethod
    def payfee(self):
        pass

    def enrolled(self):
        print("Enrolled")

class Amit(pyATB):
    def payfee(self):
        print("Paid")


shubham = Amit()
shubham.enrolled()
