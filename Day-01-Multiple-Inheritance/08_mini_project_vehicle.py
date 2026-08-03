class Engine:
    def start_engine(self):
        print("Engine started")

    def stop_engine(self):
        print("Engine stopped")

class GPS:
    def show_location(self):
        print("Current location: kanpur")

    def navigate_destination(self, destination):
        print(f"Navigating to {destination}")

class SmartCar(Engine, GPS):
    def car_information(self):
        print("Tesla Model 5")

    def drive(self):
        print("Car is driving")

car = SmartCar()
print("========SMART CAR========")
car.start_engine()
car.stop_engine()
car.show_location()
car.navigate_destination("Lucknow")
car.car_information()
car.drive()