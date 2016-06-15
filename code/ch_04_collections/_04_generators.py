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
def generator_fibonacci():
    current, nxt = 0, 1

    while True:
        current, nxt = nxt, nxt + current
        yield current


# generator are composible:
def even_generator(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n


# consume both generators as a pipeline here
def even_fib():
    for n in even_generator(generator_fibonacci()):
        yield n

if __name__ == '__main__':

    print("Classic")
    for m in classic_fibonacci(100):
        print(m, end=', ')
    print()

    print("generator")
    for m in generator_fibonacci():
        print(m, end=', ')
        if m > 100:
            break
    print()

    print("composed")
    for m in even_fib():
        print(m, end=', ')
        if m > 1000000:
            break
    print()
