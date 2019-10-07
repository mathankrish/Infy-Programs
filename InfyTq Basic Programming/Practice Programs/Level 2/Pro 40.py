#PF-Prac-40
def index_of_max_unique(num_list):
    #start writing your code here
    l2 = []
    for l1 in num_list:
        l2.append(len(set(l1)))

    index = l2.index(max(l2))

    return index

num_list = [[1, 3, 3], [12, 4, 12, 7, 4, 4], [41, 2, 4, 7, 1, 12], [1, 2, 3, 4, 5, 6]]

print("Number list:", num_list)
output=index_of_max_unique(num_list)
print("The index of sub list containing maximum unique elements is:", output)