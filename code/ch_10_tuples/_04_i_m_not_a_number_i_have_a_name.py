import collections

Rating = collections.namedtuple("Rating", "id, x, y, rating")


def main():
    # for d in get_data_tricky():
    #     print("id={}, rating={}, position=({}, {})".format(
    #         d[0], d[3], d[2], d[1]))

    for d in get_data_better():
        print("id={}, rating={}, position=({}, {})".format(
            d.id, d.rating, d.x, d.y))

        _, x, y, _ = d
        print(x, y)


def get_data_better():
    data = [
        Rating(1, 19.2, 11.1, 50),
        Rating(2, 18.9, 12.0, 45),
        Rating(3, 20.1, 14.0, 55),
    ]

    return data


def get_data_tricky():
    data = [
        (1, 19.2, 11.1, 50),
        (2, 18.9, 12.0, 45),
        (3, 20.1, 14.0, 55),
    ]

    return data


if __name__ == '__main__':
    main()
