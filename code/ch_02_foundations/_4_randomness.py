import random

letters = "abcdefghijklmnopqrstuvwxyz1234567890"

# BAD: C-style
index = random.randint(0, len(letters)-1)
item = letters[index]
print(item)

# Pythonic version
item = random.choice(letters)
print(item)


