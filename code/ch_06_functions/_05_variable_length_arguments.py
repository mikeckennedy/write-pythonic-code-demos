def biggest(x: int, y: int, *args):
    # print(type(args), args)
    numbers = [x, y] + list(args)
    # print(numbers)
    return max(numbers)


print(biggest(1, 7))

# what about more than 2?
# Arbitrarily many args.
print(biggest(1, 7, 11, 5, -2, 100, 73))
