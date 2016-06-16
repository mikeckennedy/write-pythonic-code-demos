print("About to import _02_what_is___main__support")

# noinspection PyProtectedMember
import ch_06_packages._02_what_is___main__support as s

print("Done importing _02_what_is___main__support")


def main():
    print()
    print("The variable value is {}.".format(s.var))
    print("The name of the executed python module is {}".format(__name__))


if __name__ == '__main__':
    main()
