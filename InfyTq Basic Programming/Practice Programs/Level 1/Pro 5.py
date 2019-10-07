# PF-Prac-4
def find_nine(nums):
    # Remove pass and write your code here
    if 9 in nums:
        if nums.index(9) <= 3:
            return True
    return False


nums = [1, 0, 9]
print(find_nine(nums))