from output import Main
from output import data_syncing

if __name__ == "__main__":
    # create new object
    main = Main()

    # call method's object
    main.set_num_of_students()

    main.create_list()

    print("\n__________STUDENT'S LIST IN DESCENDING ORDER OF GPA__________\n")
    main.list_students()

    data_syncing()