# PF-Tryout
def sing_99_bottles():

    for i in range(99, 0, -1):
        print("{} bottles of beer on the wall, {} bottles of beer.".format(i,i))
        print("Take one down, pass it around, {} bottles of beer on the wall.".format(i-1))


sing_99_bottles()