name = 'Michael'
age = 43

# absolutely not pythonic:
# crash: print("Hi, I'm " + name + " and I'm " + age + " years old.")
print("Hi, I'm " + name + " and I'm " + str(age) + " years old.")

# closer, but not using modern features IMO
# limitations: Only ints, strs, and doubles can be formatted
print("Hi, I'm %s and I'm %d years old." % (name, age))

# pythonic
print("Hi, I'm {} and I'm {} years old.".format(name, age))
print("Hi, I'm {1} years old and my name is {0}, yeah {1} years.".format(name, age))

# if you have a dictionary then this is still better:
data = {'day': 'Saturday', 'office': 'Home office', 'other': 'UNUSED'}
print("On {day} I was working in my {office}!".format(**data))

# finally, in Python 3.6, you can:
# print(f"On {day} I was working in my {office}!")
