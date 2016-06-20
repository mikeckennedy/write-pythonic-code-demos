class NotSoPythonicPet:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    # self.name = None
        # self.age = 0

    # def set_name(self, name):
    #     self.name = name
    #
    # def set_age(self, age):
    #     self.age = age

    def __str__(self):
        return "A pet whose name is {} and age is {}.".format(
            self.name, self.age
        )


cow = NotSoPythonicPet('betsy', 7)
# cow.set_name('betsy')
# cow.set_age(7)
# cow.happiness = 11
print(cow)
