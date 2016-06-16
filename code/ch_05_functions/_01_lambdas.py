# ############ lambda expressions #############
# Create by Michael Kennedy (@mkennedy)


def main():
    print("Find odd numbers via method:")
    # TODO ...
    print()

    print("Find divisible by 6 via lambda:")
    # TODO ...
    print()

    print("Sorted list of words: ")
    list_of_words = ['CPython', 'read', 'improvements,', 'issues.', 'on', 'comprehensive', 'porting', 'potential',
                     'user-facing', 'of', 'other', 'for', 'smaller', 'deprecations,', 'a', 'optimizations,', 'changes,',
                     'including', 'and', 'Please', 'many', 'list']

    # TODO ...
    list_of_words.sort()  # ? ;)
    print(list_of_words)

    print("Done")


def find_special_numbers(special_selector, limit=10):
    found = []
    n = 0
    while len(found) < limit:
        if special_selector(n):
            found.append(n)
        n += 1
    return found


def check_for_odd(n):
    return n % 2 == 1


if __name__ == '__main__':
    main()
