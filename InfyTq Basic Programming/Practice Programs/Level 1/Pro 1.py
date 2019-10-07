# PF-Prac-1
def add_string(str1):
    # start writing your code here

    if (str1[-3:] == "ing"):
        str1 = "{}ly".format(str1)

    elif (len(str1) >= 3):
        str1 = "{}ing".format(str1)

    elif (len(str1) < 3):
        str1 = str1

    return str1


str1 = "com"
print(add_string(str1))