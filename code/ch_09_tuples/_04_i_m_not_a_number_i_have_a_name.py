def main():
    for d in get_data_tricky():
        print("id={}, rating={}, position=({}, {})".format(1, 1, 1, 1))


def get_data_tricky():
    data = [
        (1, 19.2, 11.1, 50),
        (2, 18.9, 12.0, 45),
        (3, 20.1, 14.0, 55),
    ]

    return data


if __name__ == '__main__':
    main()
