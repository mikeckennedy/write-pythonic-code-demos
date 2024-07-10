def main():
    a = add_items_bad("a", 3)
    print(a)
    add_items_bad("b", 2, a)
    print(a)

    # danger revealed here
    d = add_items_bad("d", 4)
    print(d)

    print(id(a), id(d), id(a) == id(d))

    print("Try again")
    a = add_items_good("a", 3)
    print(a)
    add_items_good("b", 2, a)
    print(a)

    # danger revealed here
    d = add_items_good("d", 4)
    print(d)

    print(id(a), id(d), id(a) == id(d))


# notice even PyCharm knows... alt-enter fixes.
def add_items_bad(name, times=1, lst=[]):
    for _ in range(0, times):
        lst.append(name)
    return lst


# Ah, better
def add_items_good(name, times=1, lst=None):
    if lst is None:
        lst = []

    for _ in range(0, times):
        lst.append(name)
    return lst


if __name__ == '__main__':
    main()
