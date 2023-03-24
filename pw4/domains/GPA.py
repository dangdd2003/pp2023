import numpy as np
import math

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