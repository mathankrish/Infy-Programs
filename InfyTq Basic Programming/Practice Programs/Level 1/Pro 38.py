row = int(input())
col = int(input())
l1 = []

l2 = [[str(i)+str(j) for j in range(0, col)]for i in range(0, row)]

print(l2)