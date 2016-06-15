# ############ yield and generators #############
# Create by Michael Kennedy (@mkennedy)


# Fibonacci numbers:
# 1, 1, 2, 3, 5, 8, 13, 21, ...


def classic_fibonacci(limit):
    nums = []
    current, nxt = 0, 1

    while current < limit:
        current, nxt = nxt, nxt + current
        nums.append(current)

    return nums


# can we do better?

# generator are composible:

# consume both generators as a pipeline here


if __name__ == '__main__':

    print("Classic")
    for m in classic_fibonacci(100):
        print(m, end=', ')
    print()

    print("generator")

    print("composed")

    print()
