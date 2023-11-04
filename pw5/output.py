import base64
import zlib

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
        temp_std = [[f"Name: {Student.get_name(self)}",
                     f"ID: {Student.get_id(self)}",
                     f"Dob: {Student.get_dob(self)}"]]

        with open("data\\students.txt", "a") as student_file:
            student_file.write(f"Name: {Student.get_name(self)}\n"
                               f"ID: {Student.get_id(self)}\n"
                               f"Dob: {Student.get_dob(self)}\n\n")

        print("***********")
        return temp_std

    def set_courses(self):
        Course.__init__(self)
        temp_crs = [(f"Name: {Course.get_name(self)}",
                     f"ID: {Course.get_id(self)}")]
        with open("data\\courses.txt", "a") as course_file:
            course_file.write(f"Name: {Course.get_name(self)}\n"
                              f"ID: {Course.get_id(self)}\n\n")
        return temp_crs

    # create the student mark list
    def create_list(self):
        # open and read file
        with open("data\\students.txt", "w") as file1:
            file1.write("Students information:\n----------\n")
        with open("data\\courses.txt", "w") as file2:
            file2.write("Courses information:\n----------\n")
        with open("data\\marks.txt", "w") as file3:
            file3.write("Marks information:\n----------\n")

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
                with open("data\\marks.txt", "a") as mark_file:
                    mark_file.write(f"Course {Course.get_name(self)}:\n"
                                    f"Mark: {Mark.get_mark(self)}\n"
                                    f"Credit: {Mark.get_credit(self)}\n\n")
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


def data_syncing():
    try:
        with open("students.dat", "r") as file:
            content = file.read().encode('utf-8')
            compressed_content = base64.b64decode(content)
            decompressed_content = zlib.decompress(compressed_content)
            content = decompressed_content.decode('utf-8')

            print("\n__________LAST SAVED DATA__________\n")
            print(content)

    except IOError:
        print("\nERROR: File students.dat does not exit!\nCreating a new file students.dat.......")

    finally:
        with open("data\\students.txt", "r") as file1:
            text1 = file1.read()
        with open("data\\courses.txt", "r") as file2:
            text2 = file2.read()
        with open("data\\marks.txt", "r") as file3:
            text3 = file3.read()

        text = text1 + text2 + text3
        encode_file = base64.b64encode(zlib.compress(text.encode('utf-8'),6))
        content = encode_file.decode('utf-8')

        with open("students.dat", "w") as file:
            file.write(content)
        print("Save new data to students.dat file.......\nSaved Successfully !")