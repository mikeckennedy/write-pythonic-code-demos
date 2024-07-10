# add arbitrary additional kw arguments
def display_greeting(name, greeting='Hello', times=1, **kwargs):
    times = max(1, times)
    for _ in range(0, times):
        print("{} {}!".format(greeting, name))
    print("kwargs = {}".format(kwargs))

display_greeting(greeting="Hey, you're out of order",
                 name="Michael", additional=2, mode=7)

print()

# from dictionary
data = {
    'name': 'Ted',
    'greeting': 'Long time no see bro!',
    'times': 6
}

display_greeting(**data)
