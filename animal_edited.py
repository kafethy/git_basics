class Animal:
    def __repr__(self):
        return f'{self.__class__.__name__}()'


class Person(Animal):
    def __init__(self, name, tax_number=None):
        self.name = name
        self.tax_number = tax_number

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, tax_number={self.tax_number})'


class Enterprise(Animal):
    def __init__(self, name):
        self.name = name
        self.owned_pets = []

    def own_pet(self, pet):
        if isinstance(pet, Pet):
            self.owned_pets.append(pet)
            pet.change_owner(self)

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r})'


class Vaccine(Animal):
    def __init__(self, name, manufacturer):
        self.name = name
        self.manufacturer = manufacturer

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, manufacturer={self.manufacturer!r})'


class Chip(Animal):
    def __init__(self, chip_id):
        self.chip_id = chip_id

    def __repr__(self):
        return f'{self.__class__.__name__}(chip_id={self.chip_id})'


class AnimalChip(Chip):
    def __init__(self, chip_id, animal):
        super().__init__(chip_id)
        self.animal = animal

    def __repr__(self):
        return f'{self.__class__.__name__}(chip_id={self.chip_id}, animal={self.animal!r})'


class DogChip(AnimalChip):
    def __repr__(self):
        return f'{self.__class__.__name__}(chip_id={self.chip_id}, animal={self.animal!r})'


class CatChip(AnimalChip):
    def __repr__(self):
        return f'{self.__class__.__name__}(chip_id={self.chip_id}, animal={self.animal!r})'


class Pet(Animal):
    def __init__(self, name, owner):
        super().__init__()
        self.name = name
        self.change_owner(owner)

    def change_owner(self, new_owner):
        self.owner = new_owner

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if isinstance(value, (Person, Enterprise)):
            self.__owner = value
        else:
            err = f'{value!r} must be an instance or subclass of Person or Enterprise.'
            raise ValueError(err)

    def __repr__(self):
        clsname = self.__class__.__name__
        return f'{clsname}(name={self.name!r}, owner={self.owner!r})'


if __name__ == '__main__':
    jack = Person("Jack Sparrow", tax_number="67493967692")
    pet_store = Enterprise("Pet Store")
    dog = Pet("Sam", owner=jack)
    cat = Pet("Maria", owner=jack)
    pet_store.own_pet(dog)

    print(jack)
    print(pet_store)
    print(dog)
    print(cat)
