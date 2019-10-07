import math
def find_gcd(num1, num2):
    while(num2):
        num1, num2 = num2, num1 % num2
    return num1

num1 = 45
num2 = 9
print(find_gcd(num1, num2))