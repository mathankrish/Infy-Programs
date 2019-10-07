# PF-Prac-15
def check_22(num_list):
    str_l1 = [str(i) for i in num_list]
    str_l2 = ''.join(str_l1)
    #print(str_l2)
    sub = '22'
    if sub in str_l2:
        return True
    else:
        return False


# start writing your code here

print(check_22([3, 2, 5, 1, 2, 1, 2, 2]))