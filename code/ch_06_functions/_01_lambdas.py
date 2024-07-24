# ############ lambda expressions #############
# Create by Michael Kennedy (@mkennedy)

import collections
import uuid

Measurement = collections.namedtuple('Measurement', 'id x y value')


def main():
    print("Find odd numbers via method:")
    # TODO: Use find_special_numbers() for 25 odds
    print()

    print("Find divisible by 6 via lambda:")
    # TODO: Use find_special_numbers() for 25 n*6 numbers via Lambdas
    print()

    print("Sorted list of words: ")
    list_of_words = ['CPython', 'read', 'improvements,', 'issues.', 'on', 'comprehensive', 'porting', 'potential',
                     'user-facing', 'of', 'other', 'for', 'smaller', 'deprecations,', 'a', 'optimizations,', 'changes,',
                     'including', 'and', 'Please', 'many', 'list']

    # Can we just call sort on the list?
    # TODO: Sort list
    # More control here.
    # TODO: Sort better
    print()

    # More complex sort of measurements
    # TODO: Sort by value
    # TODO: Sort by value and distance

    print("Done")


def find_special_numbers(special_selector, limit=10):
    found = []
    n = 0
    while len(found) < limit:
        if special_selector(n):
            found.append(n)
        n += 1
    return found


measurements = [
    Measurement(str(uuid.uuid4()), 1, 1, 72),
    Measurement(str(uuid.uuid4()), 2, 1, 40),
    Measurement(str(uuid.uuid4()), 3, 1, 11),
    Measurement(str(uuid.uuid4()), 2, 1, 90),
    Measurement(str(uuid.uuid4()), 2, 2, 60),
    Measurement(str(uuid.uuid4()), 2, 3, 73),
    Measurement(str(uuid.uuid4()), 3, 1, 40),
    Measurement(str(uuid.uuid4()), 3, 2, 44),
    Measurement(str(uuid.uuid4()), 3, 3, 90)
]

if __name__ == '__main__':
    main()
