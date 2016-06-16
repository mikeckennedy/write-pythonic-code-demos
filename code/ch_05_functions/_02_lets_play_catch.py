# noinspection PyProtectedMember
import ch_05_functions._02_lets_play_catch_support as s


def main():
    run_with_checks()
    # run_with_handling()
    # run_with_handling_separate_errors()


def run_with_handling():
    data = s.download_file()
    print("downloaded data -> {}".format(data))


def run_with_handling_separate_errors():
    data = s.download_file()
    print("downloaded data -> {}".format(data))


def run_with_checks():
    data = s.download_file()
    print("downloaded data -> {}".format(data))


if __name__ == '__main__':
    print("Let's play catch: ")
    print()
    main()
