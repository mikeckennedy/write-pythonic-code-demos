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


def run_with_checks() -> bool:
    # We should check it's all OK network, dns, url, and then download it.
    # Look before you leap (LBYL)
    if not s.check_network():
        print("Sorry no network!")
        return False

    if not s.check_download_url():
        print("Sorry no url specified!")
        return False

    if not s.check_access_allowed():
        print("Sorry you don't have permissions!")
        return False

    if not s.check_dns():
        print("Sorry server doesn't have DNS records!")
        return False

    data = s.download_file()
    print("Download success!", data)
    return True


def run_with_handling():
    # We should catch errors!
    # Easier to ask for forgiveness than permission (EAFP)
    try:
        data = s.download_file()
        print("Download success!", data)
    except Exception as e:
        print(f"Error: No downloadie! {e}")


def run_with_handling_separate_errors():
    # Easier to ask for forgiveness than permission (EAFP)
    # We should consider PermissionError, ConnectionError, ValueError, and others
    try:
        data = s.download_file()
        print("Download success!", data)
    except ConnectionError:
        print("Sorry no network!")
    except PermissionError as pe:
        print(f"Sorry you don't have permissions! Details {pe}")
    except Exception as e:
        print(f"Error: Download didn't work. Details: {e}")


if __name__ == '__main__':
    print("Let's play catch: ")
    print()
    main()
