class PythonicPetStaticStyle:
    age: int = 0
    name: str = ''
    lifecycle: str = 'baby'

    def __str__(self):
        return f"A pet whose name is {self.name} whose age is {self.age} years old."


cow = PythonicPetStaticStyle()
cow.name = 'Static Betsy'
print(cow)

print(f"Static value: {PythonicPetStaticStyle.name}")
PythonicPetStaticStyle.name = 'Default name'
print(f"Static value: {PythonicPetStaticStyle.name}")
cow2 = PythonicPetStaticStyle()
print(cow2)
cow2.name = 'New cow!'
print(cow2)
