from abc import ABC, abstractmethod

class Appliance(ABC):
    def brand(self):
        print("Samsung")

    @abstractmethod
    def operate(self):
        pass

class WashingMachine(Appliance):
    def operate(self):
        print("Washing machine started")

class Refrigerator(Appliance):
    def operate(self):
        print("Refrigerator started")

w = WashingMachine()
r = Refrigerator()

w.brand()
w.operate()
r.brand()
r.operate()