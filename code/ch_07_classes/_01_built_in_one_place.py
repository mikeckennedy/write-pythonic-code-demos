class PythonicPet:
    def __init__(self, name: str, age: int = 0):
        # Make sure all the fields are defined in the initializer:
        self.age = age
        self.name = name
        self.lifecycle = 'baby'

        if age > 0:
            self.lifecycle = "mid"

    def set_age(self, age: int):
        if age < 0 or age > 300:
            raise Exception("No way a pet is that age!")

        self.age = age

    def __str__(self):
        return f"A pet whose name is {self.name} whose age is {self.age} years old."


cow = PythonicPet('Betsy')
# cow.age = 11 # No!
# cow.set_age(7)
print(cow)
