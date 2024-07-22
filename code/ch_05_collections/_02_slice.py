# region Fix up path, so it doesn't matter where/how you run this code
import sys
from pathlib import Path

sys.path.insert(0, Path(__file__).parent.absolute().as_posix())
# endregion
from _02_slice_support import session_factory, Measurement  # noqa E402


def main():
    nums = list(range(1, 21))

    print("All nums")
    print(type(nums), nums)

    print("First 5 nums")
    # first_5 = []
    # for n in nums:
    #     if n > 5:
    #         break
    #     first_5.append(n)
    # print(first_5)
    # Better: first_5 = nums[0:5]
    first_5 = nums[:5]  # Best
    print(first_5)

    print("2->7 nums")
    print(nums[1:7])

    print("Last 3 nums (less good) with len")
    last_3 = nums[len(nums) - 3:len(nums)]
    print(last_3)

    print("Last 3 nums (pythonic)")
    print(nums[-1])
    print(nums[-3:])
    print()
    print("What if we are off by some index?")
    print(nums[10:1_000])

    print("Top 3 measurements from the database")

    with session_factory() as session:
        top_measurements = (
            session.query(Measurement)
            .filter(Measurement.value > 0.9)
            .order_by(Measurement.value.desc())
        )

        print(top_measurements[:3])

        session.commit()


if __name__ == '__main__':
    main()
