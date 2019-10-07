# PF-Prac-11
def find_upper_and_lower(sentence):
    # start writing your code here
    sen = sentence.split(" ")
    upper = 0
    lower = 0
    for i in range(len(sen)):
        for j in sen[i]:
            if j.isupper():
                upper += 1
            elif j.islower():
                lower += 1
    result_list = [upper,lower]


    return result_list


sentence = "Come Here"
print(find_upper_and_lower(sentence))