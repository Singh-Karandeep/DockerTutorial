import sys
from time import sleep, strftime
import os


def make_directories():
    artifact_directory = "Artifacts"
    artifact_file = "File_{}.txt".format(strftime("%Y_%m_%d-%H_%M_%S"))
    os.makedirs(artifact_directory, exist_ok=True)
    file_obj = open(os.path.join(artifact_directory, artifact_file), 'w')
    return file_obj


def write_to_file(row, file_obj):
    print(row)
    file_obj.writelines(row + '\n')


def print_table(num_list):
    if not num_list:
        print("No Arguments Supplied...!!!")
        return

    file_obj = make_directories()

    for num in num_list:
        num = int(num)
        write_to_file("Table for {}...".format(num), file_obj)
        for i in range(1, 11):
            row = "{} x {} = {}".format(num, i, num * i)
            write_to_file(row, file_obj)
            sleep(0.1)
        write_to_file('\n', file_obj)

    file_obj.close()
    sleep(200)


if __name__ == '__main__':
    args = sys.argv
    print_table(args[1:])
