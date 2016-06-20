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
print("She is named {} and {} years old.".format(cow.get_name(), cow.get_age()))
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
        print("---> Setting age to {}".format(value))
        self.__age = value


print("Here is my pet snake:")
py = PetSnake("Slide", 6)
print("She is named {} and {} years old.".format(py.name, py.age))
py.age = 7
print("She is named {} and {} years old.".format(py.name, py.age))
print(py.is_protected)