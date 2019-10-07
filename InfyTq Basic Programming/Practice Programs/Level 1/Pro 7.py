from functools import reduce



def seed_no(number, ref_no):
    l1 = [int(i) for i in str(number)]
    val = number * reduce(lambda x, y: x * y, l1)
    if val == ref_no:
        return True
    else:
        return False

number = 123
ref_no = 738
print(seed_no(number, ref_no))