# More often, you need the index and the value.

# How would you actually accomplish this? With range? No.
# for idx = 0; idx<len(data); idx++:
#     val = data[idx]
#     print(" {} --> {}".format(idx, val))

data = [1, 7, 11]

for idx, value in enumerate(data):
    print(" {} --> {}".format(idx+1, value))
