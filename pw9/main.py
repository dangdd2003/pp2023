import time
import threading

from output import Main
from output import data_syncing, save_data


def run():
    # create new object
    main = Main()
    # call object's method
    main.set_num_of_students()
    main.create_list()
    print("\n__________STUDENT'S LIST IN DESCENDING ORDER OF GPA__________\n")
    main.list_students()
    # write data to file txt
    data_syncing()


if __name__ == "__main__":
    p1 = threading.Thread(target=run)
    p2 = threading.Thread(target=save_data)

    p1.start()
    p1.join()

    p2.start()
    p2.join()