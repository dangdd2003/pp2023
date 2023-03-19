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


class Main:

    # initialize data (number of elements)
    def __init__(self):
        self.__num_of_students = 0
        self.__num_of_courses = 0
        self.__students = []
        self.__courses = []

    # encapsulation
    # getter
    def get_num_of_students(self):
        return self.__num_of_students

    def get_num_of_courses(self):
        return self.__num_of_courses

    def get_students(self):
        return self.__students

    def get_courses(self):
        return self.__courses

    # setter
    def set_num_of_students(self):
        self.__num_of_students = Data.input_data("students")
        print("----------")

    def set_num_of_courses(self):
        self.__num_of_courses = Data.input_data("courses")
        print("----------")

    def set_students(self):
        Students.__init__(self)
        temp_std = []
        temp_std.append([f"Name: {Students.get_name(self)}",
                         f"ID: {Students.get_id(self)}",
                         f"Dob: {Students.get_dob(self)}"])
        print("***********")
        return temp_std

    def set_courses(self):
        Courses.__init__(self)
        temp_crs = []
        temp_crs.append((f"Name: {Courses.get_name(self)}",
                         f"ID: {Courses.get_id(self)}"))
        return temp_crs

    # create the student mark list
    def create_list(self):
        gpa_list = []  # list of all GPA

        for i in range(self.get_num_of_students()):
            std = self.set_students()
            self.set_num_of_courses()

            # create list of courses and mark
            mark_list = []
            credit_list = []
            self.__courses = []
            for j in range(self.get_num_of_courses()):
                self.__courses.append(self.set_courses())
                Mark.__init__(self)
                temp_mark = Mark.get_mark(self)
                temp_credit = Mark.get_credit(self)
                mark_list.append(temp_mark)
                credit_list.append(temp_credit)
                self.__courses.append(f"Credit: {Mark.get_credit(self)}, Mark: {Mark.get_mark(self)}")
                print("-----------")

            # calculating gpa
            GPA.__init__(self, mark_list, credit_list)
            GPA.gpa_calculating(self)

            # create list of students
            temp_list = [f"Student Info: {std}",
                         f"Course Info: {self.__courses}",
                         f"GPA: {GPA.get_gpa(self)}"]

            # sorting part
            if len(gpa_list) == 0:
                self.__students.append(temp_list)
                gpa_list.append(GPA.get_gpa(self))
            else:
                for k in range(len(gpa_list)):
                    if GPA.get_gpa(self) >= gpa_list[k]:
                        self.__students.insert(k, temp_list)
                        gpa_list.insert(k, GPA.get_gpa(self))
                        break
                    if GPA.get_gpa(self) <= gpa_list[len(gpa_list) - 1]:
                        self.__students.append(temp_list)
                        gpa_list.append(GPA.get_gpa(self))
                        break

    # display student mark management list
    def list_students(self):
        Data.display(self.__students)


if __name__ == "__main__":
    # create new object
    main = Main()

    # call method's object
    main.set_num_of_students()

    main.create_list()

    print("\n__________STUDENT'S LIST IN DESCENDING ORDER OF GPA__________\n")
    main.list_students()
