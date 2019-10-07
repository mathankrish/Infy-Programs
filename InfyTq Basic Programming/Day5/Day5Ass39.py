# Hotel ordering system

# Global variables
menu = ('Veg Roll', 'Noodles', 'Fried Rice', 'Soup')
quantity_available = [2, 200, 3, 0]

customer_ordered_food = []
customer_ordered_Quantity = []


def place_order(*item_tuple):

    for i in range(0, len(item_tuple), 2):
        customer_ordered_food.append(item_tuple[i])

    for j in range(1, len(item_tuple), 2):
        customer_ordered_Quantity.append(item_tuple[j])


    for stock in customer_ordered_food:
        if stock in menu:
            if stock == menu[0]:
                quan_avail = check_quantity_available(menu.index(stock), customer_ordered_Quantity[customer_ordered_food.index(stock)])

                if quan_avail == False:
                    print("{0} stock is over".format(stock))
                    exit()

                print("{0} is available".format(stock))

            if stock == menu[1]:
                quan_avail = check_quantity_available(menu.index(stock), customer_ordered_Quantity[customer_ordered_food.index(stock)])

                if quan_avail == False:
                    print("{0} stock is over".format(stock))
                    exit()

                print("{0} is available".format(stock))

            if stock == menu[2]:
                quan_avail = check_quantity_available(menu.index(stock), customer_ordered_Quantity[customer_ordered_food.index(stock)])

                if quan_avail == False:
                    print("{0} stock is over".format(stock))
                    exit()

                print("{0} is available".format(stock))

            if stock == menu[3]:
                quan_avail = check_quantity_available(menu.index(stock), customer_ordered_Quantity[customer_ordered_food.index(stock)])

                if quan_avail == False:
                    print("{0} stock is over".format(stock))
                    exit()

                print("{0} is available".format(stock))


        else:
            print("{0} is not available".format(stock))



def check_quantity_available(index, quantity_requested):

    if quantity_requested <= quantity_available[index]:
        quantity_available[index] -= quantity_requested
        return True
    else:
        return False


place_order("Veg Roll", 2, "Noodles", 2)
#place_order("Soup", 1, "Veg Roll", 2, "Fried Rice", 1)
#place_order("Fried Rice", 2, "Soup", 1)