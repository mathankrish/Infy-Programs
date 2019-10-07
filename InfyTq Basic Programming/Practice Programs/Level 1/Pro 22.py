#PF-Tryout
def diagonal_stars(number):
   for i in range(number):
       for j in range(i):
           if  j == i-1:
               print("*", end="")
           else:
               print(".",end="")
       print()


number=6
diagonal_stars(number)