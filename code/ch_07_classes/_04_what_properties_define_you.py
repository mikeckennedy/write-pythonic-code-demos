class NotSoPythonicPet:
    def __init__(self, name, age):
        self.__age = age
        self.__name = name

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


print("Here is my pet cow:")
cow = NotSoPythonicPet("Betsy", 4)
print(f"She is named {cow.get_name()} and {cow.get_age()} years old.")
print()
