# To display the date of the nxt day from the current day

def generate_next_date(day,month,year):
    next_month = month
    next_day = day
    next_year = year

    if(next_year % 400 == 0 ):
        leap_year = True
    elif(year % 4 == 0):
        leap_year = True
    elif(year % 100 !=0):
        leap_year = False
    else:
        leap_year = False

    if next_month in [1,3,5,7,9,12]:
        month_length = 31
    elif next_month == 2:
        if (leap_year == True):
            month_length = 29
        else:
            month_length = 28
    else:
        month_length = 30


    if (next_day < month_length):
        next_day += 1

    else:
        next_day = 1
        if(next_month == 12):
            next_month = 1
            next_year += 1
        else:
            next_month += 1







    print(next_day, "-", next_month, "-", next_year)


generate_next_date(30, 6, 2015)