# region Fix up path, so it doesn't matter where/how you run this code
import sys
from pathlib import Path

sys.path.insert(0, Path(__file__).parent.absolute().as_posix())
# endregion
import _02_lets_play_catch_support as s  # noqa: F401


def main():
    run_with_checks()
    run_with_handling()
    run_with_handling_separate_errors()


def run_with_checks():
    ...
    # TODO: We should check it's all OK network, dns, url, and then download it.


def run_with_handling():
    ...
    # TODO: We should catch errors!


def run_with_handling_separate_errors():
    ...
    # TODO: We should consider PermissionError, ConnectionError, ValueError, and others


if __name__ == '__main__':
    print("Let's play catch: ")
    print()
    main()
