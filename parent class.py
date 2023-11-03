# Parent class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}")


# Child class (inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def display_info(self):
        super().display_info()
        print(f"Year: {self.year}")


# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2023)

# Call the display_info method to print car information
my_car.display_info()
