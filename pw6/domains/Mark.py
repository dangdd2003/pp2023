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