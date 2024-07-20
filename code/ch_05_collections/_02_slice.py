# region Fix up path, so it doesn't matter where/how you run this code
import sys
from pathlib import Path

from sqlalchemy.orm import Session

sys.path.insert(0, Path(__file__).parent.absolute().as_posix())
# endregion
from _02_slice_support import session_factory, Measurement  # noqa E402


def main():
    nums = fibonacci(200)

    print("All nums")
    print(nums)

    print("First 5 nums")
    # first_five = nums[0:5]
    first_five = nums[:5]
    print(first_five)

    print("2->7 nums")
    print(nums[2:8])

    print("Last 3 nums (less good) with len")
    # print(nums[len(nums)-3:len(nums)])
    print(nums[len(nums) - 3:])

    print("Last 3 nums (pythonic)")
    print(nums[-3:])

    print("Top measurements from the database")
    session: Session = session_factory()
    # noinspection PyUnresolvedReferences
    results = session.query(Measurement). \
        filter(Measurement.value > .9). \
        order_by(Measurement.value.desc())

    print([m.value for m in results[:3]])

    session.close()


def fibonacci(limit):
    numbers = []
    current, nxt = 0, 1

    while current < limit:
        current, nxt = nxt, nxt + current
        numbers.append(current)

    return numbers


if __name__ == '__main__':
    main()
