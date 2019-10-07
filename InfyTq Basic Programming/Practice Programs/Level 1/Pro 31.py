l1 = list(map(int, input().split()))
number = int(input())

l2 = [j for j in range(0,len(l1)-1) if l1[j] == number and l1[j+1] == number]

l3 = [ele for index, ele in enumerate(l1) if index not in l2]
print(l3)

for o in range(0,len(l3)):
  if(o == 0 and l1[0] == number):
    l3[o+1] = 0
    l3[o] = 0

  elif (o>0 and o<len(l3)-1 and l3[o] == number):
    for i in range(0, len(l3)-1):
      if (l3[i] == number):
        l3[i+1] = 0
        l3[i-1] = 0
        l3[i] = 0

  elif (o == len(l3)-1 and l3[o] == number):
    l3[o-1] = 0
    l3[o] = 0

print(sum(l3))