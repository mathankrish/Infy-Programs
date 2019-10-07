# PF-Prac-13
def close_number(num1, num2, num3):

    if num1+1 == num2 or num1+1 == num3:
        if num2+2 == num1 or num2+2 == num3 or num3+2 == num1 or num3+2 == num2:
            return True
        return False
    elif num2+1 == num1 or num2+1 == num3:
        if num1+2 == num2 or num1+2 == num3 or num3+2 == num1 or num3+2 == num2:
            return True
        return False
    elif num3+1 == num2 or num3+1 == num1:
        if num2+2 == num1 or num2+2 == num3 or num1+2 == num2 or num1+2 == num3:
            return True
        return False

    # l1=[]
    # l1.append(num1)
    # l1.append(num2)
    # l1.append(num3)
    # for i in range(len(l1)):
    #     for j in range(i+1, len(l1)):
    #         if l1[i]+1 == l1[i+1]:
    #             if

# start writing your code here

print(close_number(1, 2, 3))