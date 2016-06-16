# start with no defaults...
def display_greeting(name, greeting, times):
    times = max(1, times)
    for _ in range(0, times):
        print("{} {}!".format(greeting, name))

display_greeting("Jeff", 'Good morning', 3)
display_greeting("Michael", "G'day", 1)

display_greeting("Mark")
display_greeting("Mark", "Good afternoon")
display_greeting("Mark", "Good afternoon", 2)

