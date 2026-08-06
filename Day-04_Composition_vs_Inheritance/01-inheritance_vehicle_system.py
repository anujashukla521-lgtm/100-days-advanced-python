class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Speed: {self.speed}")

class Car(Vehicle):
    def __init__(self, brand, speed):
        super().__init__(brand, speed)
        self.no_of_doors = 4

    def drive(self):
        print(f"No of doors: {self.no_of_doors}")

class Bike(Vehicle):
    def __init__(self, brand, speed):
        super().__init__(brand, speed)
        self.helmet_required = "Yes"

    def ride(self):
        print(f"Helmet required: {self.helmet_required}")

car = Car("Toyota", 120)
bike = Bike("Hero", 100)

car.display_info()
car.drive()

bike.display_info()
bike.ride()