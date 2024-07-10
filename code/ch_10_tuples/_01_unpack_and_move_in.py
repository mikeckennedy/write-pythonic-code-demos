# tuples are defined as:
t = (7, 11, "cat", [1, 1, 3, 5, 8])
print(t)
t = 7, 11, "cat", [1, 1, 3, 5, 8]
# print(t)
# t = 7,
# print(t, len(t))

# create a tuple, grab a value.
print(t[2])

# we can assign individual variables:
t = 7, "cat", 11
# n = [0]
# a = [1]

# show them
n, a, _ = t
print("n={}, a={}".format(n, a))

# can also assign on a single line:
x, y = 1, 2
print(x, y)

# You'll find this often in loops (remember numerical for-in loops):
for idx, item in enumerate(['hat', 'cat', 'mat', 'that']):
    print("{} -> {}".format(idx, item))
