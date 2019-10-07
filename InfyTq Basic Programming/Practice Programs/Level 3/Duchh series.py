import math
def ducci_sequence(test_list, n):
    # start writing your code here
    j = 0
    final_list =[]
    while (j < n + 1):
        b = test_list.copy()
        for i in range(len(test_list)):
            if i < len(test_list) - 1:
                test_list[i] = int(math.fabs(test_list[i] - test_list[i + 1]))
            elif i == len(test_list) - 1:
                test_list[i] = int(math.fabs(test_list[i] - b[0]))
        j += 1
        final_list.append(test_list)
    return final_list[n]
ducci_element = ducci_sequence([0, 653, 1854, 4063], 3)
print(ducci_element)