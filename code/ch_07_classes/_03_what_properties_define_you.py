class NotSoPythonicPet:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


print("Here is my pet cow:")
cow = NotSoPythonicPet("Betsy", 4)
print(f"She is named {cow.get_name()} and {cow.get_age()} years old.")
print()


class PetSnake:
    def __init__(self, name, age):
        self.__age = age
        self.__name = name
        self._protected_val = 2

    @property
    def is_protected(self):
        return self._protected_val > 5

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        print("---> Getting current age")
        return self.__age

    @age.setter
    def age(self, value):
        print(f"---> Setting age to {value}")
        self.__age = value


print("Here is my pet snake:")
py = PetSnake("Slide", 6)
print(f"She is named {py.name} and {py.age} years old.")
py.age = 7
print(f"She is named {py.name} and {py.age} years old.")
print(py.is_protected)
