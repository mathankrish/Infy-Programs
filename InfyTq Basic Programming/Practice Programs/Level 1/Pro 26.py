# PF-Prac-26
def check_occurence(string):

    string1 = string.lower()
    count1 = string1.count("mat")
    count2 = string1.count("jet")
    if count1 == count2:
        return True
    else:
        return False

string = "Jet on the Mat but mat is too long"
print(check_occurence(string))