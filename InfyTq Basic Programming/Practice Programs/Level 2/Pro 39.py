# PF-Prac-39
def max_populated_state(cities_dict, state):
    # start writing your code here
    l1 = []
    l2 = []
    for dictt in cities_dict:
        if dictt['State'] == state:
            l2.append(cities_dict.index(dictt))
            l1.append(dictt['Population'])

    num = l1.index(max(l1))

    return cities_dict[l2[num]]


cities_dict = [
    {'Name': 'Vancouver', 'State': 'WA', 'Population': 161791},
    {'Name': 'Salem', 'State': 'OR', 'Population': 154637},
    {'Name': 'Seattle', 'State': 'WA', 'Population': 80885},
    {'Name': 'Bellingham', 'State': 'WA', 'Population': 608660},
    {'Name': 'Spokane', 'State': 'WA', 'Population': 208916},
    {'Name': 'Bellevue', 'State': 'WA', 'Population': 608660},
    {'Name': 'Portland', 'State': 'OR', 'Population': 583776}
]
state = "OR"
print("The city details are:", cities_dict)
print("State:", state)
output = max_populated_state(cities_dict, state)
print("The highest populated city in the given state is:", output)