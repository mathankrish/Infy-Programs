# Maximum of two numbers with the conditions

def find_max(num1, num2):
    max_num=-1
    num_list = []

    if(num1 < num2):
        if((num1 + num2) % 3 == 0 and len(str(num1)) == 2 and len(str(num2)) == 2 and num1 % 5 == 0 and num2 % 5 == 0):
            num_list.append(num1)
            num_list.append(num2)
            max_num = max(num1, num2)

        elif(num_list is []):
            return max_num
    else:
        return max_num


    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(15,45)
print(max_num)