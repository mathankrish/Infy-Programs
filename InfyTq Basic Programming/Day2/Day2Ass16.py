# Exact Coins change for the given amount
#PF-Assgn-16
def make_amount(rupees_to_make ,no_of_five ,no_of_one):
    five_needed=0
    one_needed=0

    five = no_of_five * 5
    one = no_of_one
    total = five + one

    if(rupees_to_make > total):

       print(-1)

    else:
        five_needed = int(rupees_to_make / 5)
        if(five_needed <= no_of_five):
            exact_five = five_needed
        else:
            exact_five = no_of_five
        one_needed = rupees_to_make - (exact_five * 5)

        print("No. of Five needed : {0}".format(exact_five))

        print("No. of One needed : {0}".format(one_needed))

        return 1




  #Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(105,21,8)