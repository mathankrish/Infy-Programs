#PF-Prac-41
# Part-1
def get_edges(pollsters_stateedge_dict,state):
    l1 = []
    l2 = []
    for key, values in pollsters_stateedge_dict.items():

        if state in values.keys():
            l1.append(values[state])
        else:
            l1.append(None)
        l2.append(key)

    result_list = list(zip(l2, l1))
    return result_list

# Part-2
def find_pollster_states(pollsters_stateedge_dict):

    l1 = []
    l2 = []
    for key, value in pollsters_stateedge_dict.items():
        l1.append(key)
        l2.append(list(value.keys()))

    result_dict = dict(zip(l1, l2))
    return result_dict

pollsters_stateedge_dict = {
              "Gallup": { "WA": 7, "CA": 15, "UT": -30 },
              "SurveyUSA": { "CA": 14, "CO": 2, "CT": 13, "FL": 0 },
              "Omniscient": { "AK": -14.0, "WA": -2.3, "CA": 20.9 }
             }
state='WA'
print("Pollsters, States and its edge details:", pollsters_stateedge_dict)
print("Given State:", state)
output = get_edges(pollsters_stateedge_dict,state)
print("Pollster Edge details for the given state:", output)

output1 = find_pollster_states(pollsters_stateedge_dict)
print("Pollster and their entire state details:", output1)