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