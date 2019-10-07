# PF-Prac-17
train_list = [
    {"train_no": 16453, "name": "Prasanti Express", "from": "SBC", "to": "BBS", "days_of_run": ['Mo', 'We', 'Th'],
     "sleeper_fare": 600, "ac_fare": 987},
    {"train_no": 25627, "name": "Karnataka Express", "from": "SBC", "to": "DEC", "days_of_run": ['Su', 'Tu'],
     "sleeper_fare": 1600, "ac_fare": 2500},
    {"train_no": 22642, "name": "Trivandrum SF Express", "from": "VSKP", "to": "TVM",
     "days_of_run": ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa'], "sleeper_fare": 800, "ac_fare": 1256},
    {"train_no": 22905, "name": "Okha Howrah Express", "from": "ST", "to": "KOAA", "days_of_run": ['We', 'Sa'],
     "sleeper_fare": 987, "ac_fare": 2879}]


def get_train_name(train_no):

    for dictt in train_list:
        if dictt['train_no'] == train_no:
            return dictt['name']
def get_trains_for_day(day_of_run):

    l1 =[]
    for dictt in train_list:
        if day_of_run in dictt['days_of_run']:
            l1.append(dictt['train_no'])
    return l1


def get_total_fare(train_no, passenger_dict):

    sum1 = 0
    for dictt in train_list:
        if train_no == dictt['train_no']:
            sl = passenger_dict['sleeper'] * dictt['sleeper_fare']
            ac = passenger_dict['ac'] * dictt['ac_fare']
            sum1 = sl + ac
    return sum1



# start writing your code here

print(get_train_name(25627))
print(get_trains_for_day("We"))
print(get_total_fare(25627, {"sleeper": 10, "ac": 10}))