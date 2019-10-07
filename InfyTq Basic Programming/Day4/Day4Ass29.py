# profit problem
def calculate(distance, no_of_passengers):
    petrol = distance * 7
    ticket = no_of_passengers * 80
    if (petrol > ticket):

        return -1
    else:
        profit = ticket - petrol
        return profit


distance = 20
no_of_passengers = 50
print(calculate(distance, no_of_passengers))