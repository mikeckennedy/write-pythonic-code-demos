# but sometimes, fairly rarely, you really need just an
# increasing number of integers.

for i in range(0, 10):
    print(i, end=', ')
print()

print(range(1, 7))

# think of the above as:
# for i = 0; i<10; i++:
#     print(i, end=', ')

# So, use range to model for int loops
