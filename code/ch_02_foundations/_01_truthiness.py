# ###############################
# Truthiness of an element:
# ###############################


def print_truthiness(msg, exp):
    print(("TRUE" if exp else "FALSE") + " <-- " + msg)


print_truthiness("Testing True", True)
print_truthiness("Testing False", False)
# for sequences

seq = []
print_truthiness("Empty list", seq)
seq.append("The cat")
print_truthiness("1 item list", seq)

# for objects and numbers
print_truthiness("Zero", 0)
print_truthiness("Eleven", 11)
print_truthiness("-Eleven", -11)

# for None
print_truthiness("For none", None)


# custom types
class AClass:
    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(item)

    def __bool__(self):
        return True if self.data else False

a = AClass()

print_truthiness("Empty AClass", a)
a.add("Thing")
print_truthiness("nonempty AClass", a)


