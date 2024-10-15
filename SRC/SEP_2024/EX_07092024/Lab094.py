from abc import ABC, abstractmethod

class Engine():
    @abstractmethod
    def start(self):
        pass

    def stop(self):
        pass


class Car(Engine):
    @abstractmethod
    def start(self):
        print("start")

    def stop(self):
        print("stop")

    def drive(self):
        self.start()
        self.stop()

car = Car()
car.drive()