# ############ lambda expressions #############
# Create by Michael Kennedy (@mkennedy)

import collections
import typing
import uuid

Measurement = collections.namedtuple('Measurement', 'id x y value')


def main():
    print("Find odd numbers via method:")
    # Use find_special_numbers() for 25 odds
    print(find_special_numbers(is_odd, limit=25))
    print()

    print("Find divisible by 6 via lambda:")
    # Use find_special_numbers() for 25 n*6 numbers via Lambdas
    print(find_special_numbers(lambda n: n % 6 == 0, limit=25))
    print()

    # df.do_thing(lambda n: n).do_thing2(lambda x: x)

    print("Sorted list of words: ")
    list_of_words = ['CPython', 'read', 'improvements,', 'issues.', 'on', 'comprehensive', 'porting', 'potential',
                     'user-facing', 'of', 'other', 'for', 'smaller', 'deprecations,', 'a', 'optimizations,', 'changes,',
                     'including', 'and', 'Please', 'many', 'list']

    # Can we just call sort on the list?
    list_of_words.sort()
    print("Bad sort", list_of_words)

    # More control here.
    # Sort better
    list_of_words.sort(key=lambda word: word.lower())
    print("Good sort", list_of_words)
    # Sort size
    list_of_words.sort(key=lambda word: len(word))
    print("Size sort", list_of_words)
    print()

    # More complex sort of measurements
    # Sort by value
    m2 = sorted(measurements, key=lambda m: m.value, reverse=True)
    print("sorted by value", m2)
    # Sort by value and distance
    m3 = sorted(measurements, key=lambda m: (m.value, m.x*m.x + m.y+m.y), reverse=True)
    print("sorted by value and distance", m3)

    print("Done")


def find_special_numbers(special_selector: typing.Callable[[int], bool], limit: int = 10):
    found = []
    n = 0
    while len(found) < limit:
        if special_selector(n):
            found.append(n)
        n += 1
    return found


def is_odd(number: int) -> bool:
    return number % 2 != 0


measurements = [
    Measurement(str(uuid.uuid4()), 1, 1, 72),
    Measurement(str(uuid.uuid4()), 2, 1, 40),
    Measurement(str(uuid.uuid4()), 3, 1, 11),
    Measurement(str(uuid.uuid4()), 2, 1, 90),
    Measurement(str(uuid.uuid4()), 5, 5, 90),
    Measurement(str(uuid.uuid4()), 2, 2, 60),
    Measurement(str(uuid.uuid4()), 2, 3, 73),
    Measurement(str(uuid.uuid4()), 3, 1, 40),
    Measurement(str(uuid.uuid4()), 3, 2, 44),
    Measurement(str(uuid.uuid4()), 3, 3, 90)
]

if __name__ == '__main__':
    main()
