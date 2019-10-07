# create the largest number from the given list


def create_largest_number(number_list):
    
    return int("".join([str(i) for i in number_list][::-1]))

number_list = [23,34,55]
largest_number = create_largest_number(number_list)
print(largest_number)