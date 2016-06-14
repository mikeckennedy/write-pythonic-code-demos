import time
import sys


def main():
    confirm = input("Are you sure you want to format drive C: [yes, NO]? ")
    if not confirm or confirm.lower() != 'yes':
        print("Format cancelled!")
        sys.exit(1)

    for _ in range(40):
        time.sleep(.15)
        print('.', end='')
        sys.stdout.flush()
    print()
    print("Format completed successful. Enjoy the new hard drive space.")

main()

