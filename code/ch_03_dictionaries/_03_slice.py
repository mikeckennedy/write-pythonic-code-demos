# noinspection PyProtectedMember
from ch_03_dictionaries._03_slice_support import session_factory, Measurement


def fibonacci(limit):
    numbers = []
    current, nxt = 0, 1

    while current < limit:
        current, nxt = nxt, nxt + current
        numbers.append(current)

    return numbers


nums = fibonacci(200)

print("All nums")
print(nums)
print()

print("First 5 nums: nums[:5]")
print(nums[:5])
print()

print("2->7 nums: nums[2:8]")
print(nums[2:8])
print()

print("Last 3 nums (less good): nums[len(nums)-3:]")
print(nums[len(nums) - 3:])
print()

print("Last 3 nums (pythonic): nums[-3:]")
print(nums[-3:])
print()

s = session_factory()
measurements = s.query(Measurement). \
    filter(Measurement.value > .9). \
    order_by(Measurement.value.desc())

top_three = measurements[:3]
print([m.value for m in top_three])
