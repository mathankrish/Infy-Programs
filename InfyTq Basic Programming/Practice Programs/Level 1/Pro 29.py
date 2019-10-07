# PF-Prac-29
def exchange_list(number_list):

    number_list1 = number_list[0:int(len(number_list)/2)]
    number_list2 = number_list[int(len(number_list)/2):]
    number_list = number_list2 + number_list1
    return number_list


number_list = [1, 2, 3, 4, 5, 6]
print(exchange_list(number_list))
# print(number_list[int(len(number_list)/2):])