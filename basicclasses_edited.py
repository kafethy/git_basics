class Vehicle:
    def __init__(self, model, year, brand):
        self.model = model
        self.year = year
        self.brand = brand

class Car(Vehicle):
    def __init__(self, model, year, brand, owner):
        super().__init__(model, year, brand)
        self.owner = owner

    def info(self):
        print(f"Model: {self.model}, Year: {self.year}, Brand: {self.brand}")
        print(f"Owner: {self.owner}")
        print(f"This is a car!")

class Motorcycle(Vehicle):
    def __init__(self, model, year, brand, owner):
        super().__init__(model, year, brand)
        self.owner = owner

    def info(self):
        print(f"Model: {self.model}, Year: {self.year}, Brand: {self.brand}")
        print(f"Owner: {self.owner}")
        print(f"This is a motorcycle!")

car = Car('Sedan', 2022, 'Toyota', 'John')
car.info()

motorcycle = Motorcycle('Cruiser', 2021, 'Harley-Davidson', 'Alice')
motorcycle.info()
