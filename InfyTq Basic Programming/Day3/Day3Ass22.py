# To display the List of next 15 leap year from the given year

def find_leap_years(given_year):

    list_of_leap_years = []
    count = 0

    while(True):



        if (given_year % 400 == 0):
            list_of_leap_years.append(given_year)
            count = count + 1
            given_year += 1
        elif (given_year % 4 == 0):
            list_of_leap_years.append(given_year)
            count = count + 1
            given_year += 1
        elif (given_year % 100 != 0):
            given_year += 1
        else:
            given_year += 1

        if count == 15:
            print(list_of_leap_years)
            exit()

list_of_leap_years = find_leap_years(2002)
print(list_of_leap_years)