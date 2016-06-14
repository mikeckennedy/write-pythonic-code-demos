name = 'Michael'
age = 43

# Create the string "Hi, I'm Michael and I'm 43 years old."

# crash: print("Hi, I'm " + name + " and I'm " + age + " years old.")

# works, but not pythonic
print("Hi, I'm " + name + " and I'm " + str(age) + " years old.")


# probably pythonic
print("Hi, I'm %s and I'm %d years old." % (name, age))

# pythonic
print("Hi, I'm {} and I'm {} years old.".format(name, age))
print("Hi, I'm {1} years old and my name is {0}, yeah {1}.".format(name, age))

data = {'day': 'Saturday', 'office': 'Home office', 'other': 'UNUSED'}
# print: On Saturday I was working in my Home office!
print("On {day} I was working in my {office}!".format(**data))

# In Python 3.6
print("Hi, I'm {name} and I'm {age} years old.".format(name=name, age=age))
# print(f"Hi, I'm {name} and I'm {age} years old.")

