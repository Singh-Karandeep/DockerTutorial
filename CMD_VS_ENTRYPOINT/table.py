import sys
from time import sleep


def print_table(num_list):
    if not num_list:
        print("No Arguments Supplied...!!!")
    for num in num_list:
        num = int(num)
        print("Table for {}...".format(num))
        for i in range(1, 11):
            print("{} x {} = {}".format(num, i, num * i))
            sleep(0.1)
        print()


if __name__ == '__main__':
    args = sys.argv
    print_table(args[1:])
