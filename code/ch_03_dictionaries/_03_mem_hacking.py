# ############ __slots__ for improved memory usage #############
# Create by Michael Kennedy (@mkennedy)
#
# Overview:
# Custom types store their data in individualized, dynamic dictionaries
# via self.__dict__. Using __slots__ to limit available attribute names
# and move the name/key storage outside the instance to a type level
# can significantly improve memory usage. See EOF for perf numbers.
#

import collections
import datetime

ImmutableThingTuple = collections.namedtuple("ImmutableThingTuple", "a b c d")


class MutableThing:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


class ImmutableThing:
    __slots__ = ['a', 'b', 'c', 'd']

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


print("Uncomment just 1 of these 4 loops below")
print("after the program pauses on input, check the process memory")

count = 1000000
data = []

t0 = datetime.datetime.now()

# Loop 1: Tuples
print("tuple")
for n in range(count):
    data.append((1 + n, 2 + n, 3 + n, 4 + n))

# # Loop 2: Named tuple
# print("named tuple")
# for n in range(count):
#     data.append(ImmutableThingTuple(1 + n, 2 + n, 3 + n, 4 + n))
#
# # Loop 3: Standard mutable class
# print("standard class")
# for n in range(count):
#     data.append(MutableThing(1 + n, 2 + n, 3 + n, 4 + n))
#
# # Loop 4: Slot based immutable class
# print("slot based class")
# for n in range(count):
#   data.append(ImmutableThing(1 + n, 2 + n, 3 + n, 4 + n))

t1 = datetime.datetime.now()

input("Finished, waiting... done in {:,} s".format((t1 - t0).total_seconds()))

# Sample output on OS X + Python 3
# Hardware: Macbook Pro 2013 edition

# straight tuple:  207 MB, 0.528455 s
# named tuple:     215 MB, 1.519358 s
# class (dynamic): 370 MB, 1.680248 s
# slot class:      120 MB, 1.438989 s

# And on Windows 10 + Python 3, same hardware (memory is "working set")
# tuple: 153 MB
# named: 153 MB
# class: 248 MB
# slots: 145 MB

# Interesting real-world story of benefits of slots:
# http://tech.oyster.com/save-ram-with-python-slots/
