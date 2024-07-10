# noinspection PyProtectedMember
import ch_05_functions._02_lets_play_catch_support as s


def main():
    # run_with_checks()
    # run_with_handling()
    run_with_handling_separate_errors()


def run_with_checks():
    if not s.check_network():
        print("Cannot download, no network")
        return
    if not s.check_dns():
        print("Cannot download, no dns")
        return
    if not s.check_download_url():
        print("Cannot download, no url set")
        return

    data = s.download_file()
    print("downloaded data -> {}".format(data))


def run_with_handling():
    try:
        data = s.download_file()
        print("downloaded data -> {}".format(data))
    except Exception as x:
        print("Cannot download: {} -> {}".format(type(x), x))


def run_with_handling_separate_errors():
    try:
        data = s.download_file()
        print("downloaded data -> {}".format(data))
    except PermissionError:
        print("Cannot download, you don't have permission...")
    except ConnectionError as ce:
        print("Cannot download, problem with network: {}".format(ce))
    except Exception as x:
        print("Cannot download: {} -> {}".format(type(x), x))


if __name__ == '__main__':
    print("Let's play catch: ")
    print()
    main()
