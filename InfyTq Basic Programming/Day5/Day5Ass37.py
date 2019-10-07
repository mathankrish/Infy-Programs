# Rewarding the child with Extra Chocolates

child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

def calculate_total_chocolates():

    Total_choci = sum(chocolates_received)
    return  Total_choci

def reward_child(child_id_rewarded, extra_chocolates):

    if child_id_rewarded in child_id:

        if extra_chocolates < 1:
            print("Extra chocolates is less than 1")

        else:
            for i in child_id:
                if i == child_id_rewarded:
                    reward_child_index = child_id.index(child_id_rewarded)
                    chocolates_received[reward_child_index] += extra_chocolates

            print(chocolates_received)
    else:
        print("Child id is invalid")


print(calculate_total_chocolates())

reward_child(20,2)