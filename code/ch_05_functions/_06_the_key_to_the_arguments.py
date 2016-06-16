# add arbitrary additional kw arguments
def display_greeting(name, greeting='Hello', times=1):
    times = max(1, times)
    for _ in range(0, times):
        print("{} {}!".format(greeting, name))

display_greeting(greeting="Hey, you're out of order", name="Michael")

print()

# from dictionary
