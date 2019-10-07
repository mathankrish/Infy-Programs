# Find the pairs of numbers

def find_pairs_of_numbers(num_list,n):
    count = 0
    for i in range(0,len(num_list)+1):
        for j in range(i+1, len(num_list)):
            if(num_list[i] + num_list[j] == n):

                count += 1
    return count

num_list=[1, 2, 4, 5, 6, 3,7,4]
n=8
print(find_pairs_of_numbers(num_list,n))