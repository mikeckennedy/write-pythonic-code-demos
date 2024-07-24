# add arbitrary additional kw arguments
def display_greeting(name, greeting='Hello', times=1):
    times = max(1, times)
    for _ in range(0, times):
        print(f"{greeting} {name}!")
    print(f"kwargs = {kwargs}")


# TODO: Can this work?
display_greeting(greeting="Hey, you're out of order",
                 name="Michael", additional=2, mode=7)

print()

# from dictionary
data = {
    'name': 'Ted',
    'greeting': 'Long time no see bro!',
    'times': 6
}

# TODO: And what about this one? ^^^^
