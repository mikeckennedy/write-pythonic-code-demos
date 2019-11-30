import collections
import datetime
import random

import sys

DataPoint = collections.namedtuple("DataPoint", "id x y temp quality")


def main():
    # #############################
    print("Creating data...", end=' ')
    sys.stdout.flush()

    data_list = []  # 500,000 DataPoint items
    random.seed(0)
    for d_id in range(500000):
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        temp = random.randint(-10, 50)
        quality = random.random()
        data_list.append(DataPoint(d_id, x, y, temp, quality))

    print("done.")
    sys.stdout.flush()

    # Reordering data for random access
    print("Reordering data for random access ...", end=' ')
    sys.stdout.flush()

    data_list.sort(key=lambda d: d.quality)

    print("done.")

    # Create a set of random IDs to locate without duplication
    interesting_ids = {random.randint(0, len(data_list)-1) for _ in range(0, 100)}
    print("Creating {} interesting IDs to seek.".format(len(interesting_ids)))

    # Locating data in list
    print("Locating data in list...", end=' ')
    sys.stdout.flush()

    t0 = datetime.datetime.now()
    interesting_points = []
    for i in interesting_ids:
        pt = find_point_by_id_in_list(data_list, i)
        interesting_points.append(pt)

    t1 = datetime.datetime.now()
    dt_list = (t1 - t0).total_seconds()

    print("done.")
    sys.stdout.flush()

    print("dt: {} sec".format(dt_list))
    print(interesting_points)

    # #############################

    # let's try this with a dictionary...
    # 1. Create dictionary via comprehension, key = id

    t0 = datetime.datetime.now()
    data_dict = {d.id: d for d in data_list}

    # 2. locate the data in dictionary
    interesting_points.clear()
    for d_id in interesting_ids:
        d = data_dict[d_id]
        interesting_points.append(d)

    t1 = datetime.datetime.now()
    dt_dict = (t1 - t0).total_seconds()

    print("done.")
    sys.stdout.flush()

    print("dt: {} sec".format(dt_dict))
    print(interesting_points)
    print()
    print("Speedup from dict: {:,.0f}x".format(round(dt_list / dt_dict)))


def find_point_by_id_in_list(data_list, i):
    for d in data_list:
        if d.id == i:
            return d

    return None


if __name__ == '__main__':
    main()

# ################# TYPICAL OUTPUT ###################
# Python 3
# OS X, Macbook Pro
#
# Creating data... done.
# Sorting data... done.
# Creating 100 interesting IDs to seek.
# Locating data in list... done.
# DT: 7.339648 sec
# [DataPoint(id=244225, x=308, y=736, temp=15, quality=0.2616059911451657), ...]
# Creating dictionary...done.
# Locating data in dictionary... done.
# DT: 8e-05 sec
# [DataPoint(id=244225, x=308, y=736, temp=15, quality=0.2616059911451657), ...]
#
# Speedup from dict: 91,746x
