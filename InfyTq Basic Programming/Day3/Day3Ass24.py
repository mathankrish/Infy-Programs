# Program to find the wheather the given siides form a triangle


#PF-Assgn-24
def form_triangle(num1,num2,num3):
    success = "Triangle can be formed"
    failure = "Triangle can't be formed"

    if (num1 + num2 >= num3) and (num2 + num3 >= num1) and (num1 + num3 >= num2):
        return success
    else:
        return failure

num1=3
num2=3
num3=5
print(form_triangle(num1, num2, num3))