# add arbitrary additional kw arguments
def display_greeting(name='', greeting="Hello", **kwargs):
    # print(type(kwargs), kwargs)
    text = f"{greeting} {name}"
    if 'additional' in kwargs:
        text += f" additionally, {kwargs['additional']}!"
    print(text.strip())
    # print(f'You also said: {kwargs}')


display_greeting(name='Michael', greeting='Whazzzup')

# Can this work?
display_greeting(greeting="Hey, you're out of order",
                 name="Michael", additional="remember the milk", mode=7)

print()

# from dictionary
data = {
    'name': 'Ted',
    'greeting': 'Long time no see bro!',
    'additional': "More stuff",
    'still_other': 7,
}

# And what about this one? ^^^^

# NOT the way!
display_greeting(
    name=data.get('name'),
    greeting=data.get('greeting'),
    additional=data.get('additional'),
    still_other=data.get('still_other'),
)

# The way!
display_greeting(**data)
