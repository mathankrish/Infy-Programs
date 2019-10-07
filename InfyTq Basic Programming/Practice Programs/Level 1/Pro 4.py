# PF-Prac-5
def count_digits_letters(sentence):
    # start writing your code here
    num = 0
    alpha = 0


    for j in sentence:
            if j.isdigit() == True:
                num += 1
            elif j.isalpha() == True:
                alpha += 1

    result_list = [alpha, num]
    return result_list


sentence = "Infosys Mysore 570027"
print(count_digits_letters(sentence))