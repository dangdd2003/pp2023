class Student:

    # initialize data
    def __init__(self):
        self.__name = str(input("Enter Student's Name: "))
        self.__id = str(input("Enter Student's ID: "))
        self.__dob = str(input("Enter Student's Date of Birth: "))

    # encapsulation
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_dob(self):
        return self.__dob
