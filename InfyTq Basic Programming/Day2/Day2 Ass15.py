# Product if three numbers ingnoring 7

def find_product(num1, num2, num3):
    product = 0
    index = 3
    p = []
    p.extend([num1, num2, num3])

    for i in range(len(p)):
        if (p[i] == 7 and i == 0):
            index = 0
        elif (p[i] == 7 and i == 1):
            index = 1
        elif (p[i] == 7 and i == 2):
            index = 2

    if (index == 0):
        product = p[1]*p[2]

    elif (index == 1):
        product = p[2]

    elif (index == 2):
        product = -1

    elif(index == 3):
        product = None


    return product


product = find_product(7, 6, 8)
print(product)