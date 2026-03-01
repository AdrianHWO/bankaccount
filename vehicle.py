class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("Vehicle is stopping")


class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels

    def start(self):
        print("Car is starting")


class Bike(Vehicle):
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels

    def stop(self):
        print("Bike is stopping")


car = Car("Ford", "Kia", 2025, 4, 4)
print(car.__dict__)
car.start()

bike = Bike("Honda", "Scoopy", 2018, 2)
print(bike.__dict__)
bike.stop()
