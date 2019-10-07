# PF-Prac-45

def longest_common_substring(string1, string2):
    # start writing your code here

    l1 = [string2[i2:j2] for i2 in range(len(string2)) for j2 in range(i2+1, len(string2)+1)]
    l2 = [string1[i1:j1] for i1 in range(len(string1)) for j1 in range(i1+1, len(string1)+1)]

    l3, l4 = sorted(l2, key=len), sorted(l1, key=len)

    l5 = [i for i in l3 if i in l4]
    return l5[-1]



output = longest_common_substring("discatenation", "concatenation")
print("The longest overlap of characters between string1 and string2:", output)
output1 = longest_common_substring("assured", "measured")
print("The longest overlap of characters between string1 and string2:", output1)