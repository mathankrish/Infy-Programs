
def calculate_net_amount(trans_list):
    net_amount = 0
    for i in trans_list:
        l = i.split(":")
        deposit = l[0]
        amount = l[1]

        if deposit == "D":

            net_amount += int(amount)

        elif deposit == "W":
            net_amount -= int(amount)

    return net_amount


trans_list = ["D:300", "D:200", "W:200", "D:100"]


print(calculate_net_amount(trans_list))
