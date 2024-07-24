# start with no defaults...

# Use this to make it keyword only:
# def display_greeting(*, name='', greeting="Hello", times=1):

def display_greeting(name='', greeting="Hello", times=1):
    times = max(1, times)
    for _ in range(0, times):
        print(f"{greeting} {name}".strip())


# display_greeting with some variations
display_greeting('Michael', 'Well, long time no see', 1)
display_greeting('Michael', 'Hey there', 3)

# display_greeting with one param and more
display_greeting('Sarah', 'Hi')
display_greeting('Sarah')

# display_greeting with keywords only
display_greeting(times=3)
display_greeting(greeting='So glad to see you')
display_greeting(greeting='So glad to see you', name='Zoe')
