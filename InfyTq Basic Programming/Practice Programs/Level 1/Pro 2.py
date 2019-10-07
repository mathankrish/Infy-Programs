#PF-Prac-2
def bracket_pattern(input_str):
    # Remove pass and write your code here
    coun1 = 0
    coun2 = 0

    l1 = []
    for j in input_str:
        l1.append(j)


    for k in l1:

        if k == "(":
            if k == l1[-1]:
                return False
            coun1 += 1
        elif k == ")":
            if k == l1[0]:
                return False
            coun2 += 1



    if coun1 == coun2 :
        return True
    else:
        return False




input_str = "()()"
print(bracket_pattern(input_str))