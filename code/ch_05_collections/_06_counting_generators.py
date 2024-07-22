import collections
import uuid

Measurement = collections.namedtuple('Measurement', 'id x y value')

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

# generator expression
high_values = (
    m.value
    for m in measurements
    if m.value >= 70
)

# print("First time")
# for m in high_values:
#     print(m, end=',')
#
#
# print("Second time")
# for m in high_values:
#     print(m, end=',')

# print(len(high_values)) # crash

# could use a list, but expensive!
# print(len(list(high_values)))

# pythonic counting!
# print(sum(high_values))
print(sum(1 for _ in high_values))
