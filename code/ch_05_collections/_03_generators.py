# ############ yield and generators #############
# Create by Michael Kennedy (@mkennedy)
from typing import Iterator, Iterable


# Fibonacci numbers:
# 1, 1, 2, 3, 5, 8, 13, 21, ...

def main():
    print("Classical fib")
    for n in fib(20):
        print(n, end=',')
    print()

    print("Gen fib")
    for n in fib_g():
        print(n, end=',')
        if n > 6764:
            break
    print()

    print("Even numbers")
    print(list(even_gen([1, 2, 3, 4, 5, 6, 7, 100, 9, 70])))

    print("Even fib")
    for n in even_fib():
        print(n, end=',')
        if n > 6764:
            break
    print()


# classic_fibonacci
def fib(limit: int) -> list[int]:
    current = 0
    nxt = 1
    nums = []

    while len(nums) < limit:
        current, nxt = nxt, current + nxt
        nums.append(current)

    return nums


# can we do better?
def fib_g() -> Iterator[int]:
    current = 0
    nxt = 1

    while True:
        current, nxt = nxt, current + nxt
        yield current


# generator are composible:
def even_gen(numbers: Iterable[int]) -> Iterator[int]:
    for n in numbers:
        if n % 2 == 0:
            yield n


# consume both generators as a pipeline here
def even_fib() -> Iterator[int]:
    return even_gen(fib_g())


if __name__ == '__main__':
    main()
