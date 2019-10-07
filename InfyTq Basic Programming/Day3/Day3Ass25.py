#PF-Tryout

#debug the below code
counter1 = 0
counter2 = 5
for i in range(counter1, counter2):
    for j in range(counter2, i, -1):
        print("* ", end="")
    print()
