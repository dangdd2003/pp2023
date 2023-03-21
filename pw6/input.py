import math
import numpy as np


class Students:

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


class Courses:

    # initialize data
    def __init__(self):
        self.__name = str(input("Enter Course's Name: "))
        self.__id = str(input("Enter Course's ID: "))

    # encapsulation
    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id


class Mark:

    # initialize data
    def __init__(self):
        self.__mark = int(input("Enter Course's Mark: "))
        self.__credit = int(input("Enter Course's Credit: "))

    # encapsulation
    def get_mark(self):
        return self.__mark

    def get_credit(self):
        return self.__credit


# use for polymorphism data
class Data:

    # input data
    def input_data(args):
        return int(input(f"Enter number of {args}: "))

    # display data
    def display(data):
        for i, element in enumerate(data, 1):
            print(f"Student {i}:")
            print('\n'.join(element))
            print("**********")


class GPA:

    # initialize data
    def __init__(self, mark_list, credit_list):
        self.__mark_list = np.array(mark_list)
        self.__credit_list = np.array(credit_list)
        self.__gpa = 0

    # average of gpa
    def gpa_calculating(self):
        self.__gpa = np.divide(np.sum(np.multiply(self.__mark_list, self.__credit_list)), np.sum(self.__credit_list))

    # encapsulation
    def get_gpa(self):
        return math.floor(self.__gpa)
