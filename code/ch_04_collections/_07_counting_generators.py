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

# crash! no len()
# print(len(high_values))

# could use a list, but expensive!
# lst = list(high_values)
# print(len(lst))

# pythonic counting!
count = sum(1 for _ in high_values)
print(count)
