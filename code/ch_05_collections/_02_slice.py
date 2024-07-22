# region Fix up path, so it doesn't matter where/how you run this code
import sys
from pathlib import Path


sys.path.insert(0, Path(__file__).parent.absolute().as_posix())
# endregion
from _02_slice_support import session_factory, Measurement  # noqa E402


def main():
    nums = list(range(1, 20))

    print("All nums")
    ...

    print("First 5 nums")
    ...

    print("2->7 nums")
    ...

    print("Last 3 nums (less good) with len")
    ...

    print("Last 3 nums (pythonic)")
    ...

    print("Top measurements from the database")
    ...


if __name__ == '__main__':
    main()
