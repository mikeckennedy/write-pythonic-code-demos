class NotSoPythonicPet:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"A pet whose name is {self.name}."


cow = NotSoPythonicPet('betsy')
print(cow)
