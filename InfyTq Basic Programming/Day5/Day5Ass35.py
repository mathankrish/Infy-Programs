# Marks allocation

list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    count = 0
    Total_marks = sum(list_of_marks)
    Average_mark_of_all = Total_marks / len(list_of_marks)

    for Each_student in list_of_marks:
        if Average_mark_of_all <= Each_student:
            count += 1
    Stu_more_than_avg = (count / len(list_of_marks)) * 100

    return Stu_more_than_avg

def sort_marks():

    Sorted_marks = sorted(list_of_marks)
    return Sorted_marks

def generate_frequency():
    freq_list = list(max(list_of_marks) * [0])

    for i in list_of_marks:
        freq_list[i] = 1 + freq_list[i]

    return freq_list

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())