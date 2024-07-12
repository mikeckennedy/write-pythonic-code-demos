# ###############################
# Truthiness of symbols:
# ###############################
from pathlib import Path


def print_truthiness(exp):
    print(("TRUE" if exp else "FALSE") + f" <-- {repr(exp)}")


# bools
print_truthiness(False)
print_truthiness(True)
print()

# sequences
print_truthiness([])
print_truthiness([1, 1, 2, 3, 5, 8])
print_truthiness(set())
print_truthiness({1, 1, 2, 3, 5, 8})
print()

# objects and numbers
print_truthiness("")
print_truthiness("Some string")
print_truthiness(7)
print_truthiness(1_000_000)
print_truthiness(0)
print_truthiness(0.0)
print_truthiness(0.0000000001)
print_truthiness(Path(__file__).parent)
print()

# None-ness
print_truthiness(None)


# custom types
class TruthfulObject:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def __repr__(self):
        return f'<TruthfulObject {repr(self.data)}>'

    def __bool__(self):
        return bool(self.data)


t = TruthfulObject()
t.add(1)
t.add(1)
t.add(2)
t.add(3)
t.add(5)
f = TruthfulObject()

print_truthiness(t)
print_truthiness(f)
