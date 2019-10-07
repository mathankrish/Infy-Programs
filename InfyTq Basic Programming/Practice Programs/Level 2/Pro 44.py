# def maxDepth(S):
#
# 	current_max = 0
# 	max = 0
# 	n = len(S)
#
# 	# Traverse the input string
# 	for i in range(n):
# 		if (S[i] == '('):
# 			current_max += 1
#
# 			if (current_max > max):
# 				max = current_max
# 		elif (S[i] == ')'):
# 			if(current_max > 0):
# 				current_max -= 1
# 			else:
# 				return -1
#
# 	# finally check for unbalanced string
# 	if current_max != 0:
# 		return -1
#
# 	return max
#
# # Driver program
# s = "((2))"
# print(maxDepth(s))


a = "((2)((3)))"
