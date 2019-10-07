# PF-Prac-6
def list123(nums):

    sub = '123'
    l1 = [str(i) for i in nums]
    s = ''.join(l1)
    if sub in s:
        return True
    else:
        return False

nums = [0, 1, 1, 2, 3]
print(list123(nums))