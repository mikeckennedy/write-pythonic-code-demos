# there is no really decent use of this
# don't use else, it's not worth it.

print("Running through the while: ", end='')
count = 0
while count < 5:
    print('.', end='')
    count += 1

print()
print("Breaking out of the while: ", end='')
count = 0
while count < 5:
    print('.', end='')
    count += 1
    if count > 3:
        break

print()
