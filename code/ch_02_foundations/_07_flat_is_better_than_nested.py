# noinspection PyProtectedMember
import _07_flat_support_file as s


def main():
    download_nested()
    # download_flat()


def download_nested():
    print("Let's try to download a file")
    if s.check_download_url():
        if s.check_network():
            if s.check_dns():
                if s.check_access_allowed():
                    print("Sweet, we can download ...")
                else:
                    print("No access")
            else:
                print("No DNS")
        else:
            print("No network")
    else:
        print("Bad url")


if __name__ == '__main__':
    main()
