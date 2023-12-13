class Animal:
    def __repr__(self):
        return f'{self.__class__.__name__}()'


class Human(Animal):
    def __init__(self, tax_number=None):
        self.tax_number = tax_number

    def __repr__(self):
        return f'{self.__class__.__name__}(tax_number={self.tax_number})'


class Person(Human):
    def __init__(self, name, tax_number=None):
        super().__init__(tax_number=tax_number)
        self.name = name

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, tax_number={self.tax_number})'


class Enterprise:
    def __init__(self, name):
        self.name = name
        self.owned_pets = []

    def own_pet(self, pet):
        if isinstance(pet, Pet):
            self.owned_pets.append(pet)
            pet.change_owner(self)

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r})'


class Vaccine:
    def __init__(self, name, manufacturer):
        self.name = name
        self.manufacturer = manufacturer

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name!r}, manufacturer={self.manufacturer!r})'


class Chip:
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

    john = Person("John Doe", tax_number="34653748634")
    pet_store = Enterprise("Pet Store")
    dog = Pet("Fido", owner=john)
    cat = Pet("Lilly", owner=john)
    pet_store.own_pet(dog)

    print(john)
    print(pet_store)
    print(dog)
    print(cat)