# DATA
student = []
course = []
mark = []

# input function
def input_function():

    # input information of students
    std = int(input("number of students: "))

    for i in range (std):
        student.append((str(input("student id: ")), 
                       str(input("student name: ")), 
                       str(input("date of birth: "))
                        ))
        print("------")

    # input information of courses
    crs = int(input("number of courses: "))

    for i in range (crs):
        course.append((str(input("course id: ")),
                    str(input("course name: "))))
        print("------")

        # input information of courses' mark
        std_mark = []
        for c in course:
            std_mark.append(float(input(f"course {c[1]} mark: ")))
        mark.append(std_mark)
        print("------")

    # output funtion
def output_function():
    for i, std in enumerate(student):
        print(f"""
        Student {std[1]}:
        -------
        Student ID: {std[0]}
        Student Name: {std[1]}
        Student DoB: {std[2]}
        """)

        for i, crs in enumerate(course):
            print(f"""
            Course ID: {crs[0]}
            Course Name: {crs[1]}
            Course Mark: {mark[i][i]}
            """)
            print("------")

# main function
if __name__ == "__main__":
    print("the python language (practical session)")
    print("______Input information______")
    input_function()
    
    print("______Student information______")
    output_function()
