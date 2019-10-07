def rotate_list(input_list, n):

    l1 = input_list[0:len(input_list)-n]
    l2 = input_list[len(input_list)-n:]
    output_list = l2 + l1
    return output_list

input_list = [1, 2, 3, 4, 5, 6]
output_list = rotate_list(input_list, 4)
print(output_list)