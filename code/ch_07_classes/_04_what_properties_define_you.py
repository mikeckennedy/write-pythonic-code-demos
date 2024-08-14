class NotSoPythonicPet:
    def __init__(self, name, age):
        self.__age = age
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name or 'Unnamed Pet'

    @property
    def age(self) -> str:
        return self.__age

    @age.setter
    def age(self, new_age: int):
        self.__age = max(0, min(100, new_age))

    @property
    def is_old(self) -> bool:
        return self.__age > 10

    def __str__(self):
        return f"A pet whose name is {self.name} whose age is {self.age} years old, that's old? {self.is_old}."


print("Here is my pet cow:")
cow = NotSoPythonicPet("Betsy", 4)
print(f"She is named {cow.name} and {cow.age} years old.")
# cow.name = "Renamed cow!"  # Bang crash pow!
cow.age = 10
print(cow)
cow.age = -1
print(cow)
cow.age = 10_000
print(cow)
