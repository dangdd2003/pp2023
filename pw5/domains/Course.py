class Course:

    # initialize data
    def __init__(self):
        self.__name = str(input("Enter Course's Name: "))
        self.__id = str(input("Enter Course's ID: "))

    # encapsulation
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id