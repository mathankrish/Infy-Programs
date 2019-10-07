# PF-Prac-23
def divisible_by_sum(number):

    num = number
    a = sum([int(i) for i in str(number)])
    if num % a == 0:
        return True
    else:
        return False

number = 42
print(divisible_by_sum(number))