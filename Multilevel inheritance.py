# Superclass: Vehicle
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")


# Child class: Car (inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        # Call the constructor of the superclass (Vehicle)
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_car_info(self):
        self.display_info()
        print(f"Number of Doors: {self.num_doors}")


# Child class: SportsCar (inherits from Car)
class SportsCar(Car):
    def __init__(self, make, model, year, num_doors, top_speed):
        # Call the constructor of the superclass (Car)
        super().__init__(make, model, year, num_doors)
        self.top_speed = top_speed

    def display_sports_car_info(self):
        self.display_car_info()
        print(f"Top Speed: {self.top_speed} mph")


# Create an instance of SportsCar and display its information
sports_car = SportsCar("Ferrari", "488 GTB", 2023g, 2, 205)
sports_car.display_sports_car_info()
