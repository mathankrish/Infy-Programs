# from math import gcd
# a = [12, 14]   #will work for an int array of any length
# lcm = a[0]
# for i in a[1:]:
#   lcm = lcm*i//gcd(lcm, i)
# print(lcm)


from math import gcd
from functools import reduce
def find_gcd(list):
    x = reduce(gcd, list)
    return x

print(find_gcd([2,4,6,8]))