class Animal:
    def __init__(self, gender, name, age):
        self.gender = gender
        self.name = name
        self.age = age

class Pet(Animal):
    def __init__(self, gender, name, age, owner):
        super().__init__(gender, name, age)
        self.owner = owner

class Cat(Pet):
    def __init__(self, gender, name, age, owner):
        super().__init__(gender, name, age, owner)

    def info(self):
        print(f"{self.gender}, name is {self.name}, {self.age} years, owner is {self.owner}.")
        print(f"{self.name} is a cat!")

class Dog(Pet):
    def __init__(self, gender, name, age, owner):
        super().__init__(gender, name, age, owner)

    def info(self):
        print(f"{self.gender}, name is {self.name}, {self.age} years, owner is {self.owner}.")
        print(f"{self.name} is a dog!")

cat = Cat('Girl','Michelle', 3, 'Jack')
cat.info()

dog = Dog('Boy','Sam', 7, 'Suzanne')
dog.info()