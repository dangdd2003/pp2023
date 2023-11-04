from domains.Student import Student
from domains.Course import Course
from domains.Mark import Mark
from domains.GPA import GPA
from input import Data


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
        Student.__init__(self)
        temp_std = []
        temp_std.append([f"Name: {Student.get_name(self)}",
                         f"ID: {Student.get_id(self)}",
                         f"Dob: {Student.get_dob(self)}"])
        print("***********")
        return temp_std

    def set_courses(self):
        Course.__init__(self)
        temp_crs = []
        temp_crs.append((f"Name: {Course.get_name(self)}",
                         f"ID: {Course.get_id(self)}"))
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