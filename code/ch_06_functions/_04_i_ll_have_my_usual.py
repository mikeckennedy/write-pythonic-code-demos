# start with no defaults...
def display_greeting(name, greeting='Hello', times=1):
    times = max(1, times)
    for _ in range(0, times):
        print("{} {}!".format(greeting, name))

display_greeting("Jeff", 'Good morning', 3)
display_greeting("Michael", "G'day", 1)

display_greeting("Mark")
display_greeting("Mark", "Good afternoon")
display_greeting("Mark", "Good afternoon", 2)

display_greeting(greeting='Yo!', name='Michael', times=4)
display_greeting('Michael', times=2)

