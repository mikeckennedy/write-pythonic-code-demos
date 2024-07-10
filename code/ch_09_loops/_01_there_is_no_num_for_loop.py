# There is no such concept in Python:

# data = [1, 7, 11]
# for i = 0; i<len(data); i++:
#     print("Now i is " + i)
#     print("The value is {}".format(data[i]))

# Often new comers attempt to build one:

data = [1, 7, 11]

# NOT pythonic: faking it with a while
i = 0
while i < len(data):
    print("Now i is {}".format(i))
    print("The value is {}".format(data[i]))
    i += 1
print()

# don't be that person
for item in data:
    print("The value is {}".format(item))
