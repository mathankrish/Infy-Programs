a = int(input())

while(True):
    if str(a)[::-1] != str(a):
        a += int(str(a)[::-1])
    else:
        print(a)
        break

