# ###############################
# Truthiness of an element:
# ###############################


def print_truthiness(exp):
    print(("TRUE" if exp else "FALSE") + f" <-- {exp}")


# bools

# sequences

# objects and numbers

# None-ness


# custom types
class TruthableClass:
    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(item)
