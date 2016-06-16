def biggest(x, y):
    if x > y:
        return x
    else:
        return y


print(biggest(1, 7))


# what about more than 2?
def biggest(x, *args):
    big = x
    for y in args:
        if y > big:
            big = y
    return big


print(biggest(1, 7, 42, 99, -2, 11))
