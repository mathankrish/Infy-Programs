# Billing systems

#PF-Assgn-23
def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount= 0
    Total_bill =[]

    for i in range(len(reqd_gems)):
        for j in reqd_gems:
            if j in  gems_list:

                if reqd_gems[i] == gems_list[0]:
                    bill_amount = reqd_quantity[i] * price_list[0]
                    Total_bill.append(bill_amount)

                elif reqd_gems[i] == gems_list[1]:
                    bill_amount = reqd_quantity[i] * price_list[1]
                    Total_bill.append(bill_amount)

                elif reqd_gems[i] == gems_list[2]:
                    bill_amount = reqd_quantity[i] * price_list[2]
                    Total_bill.append(bill_amount)

                elif reqd_gems[i] == gems_list[3]:
                    bill_amount = reqd_quantity[i] * price_list[3]
                    Total_bill.append(bill_amount)

                elif reqd_gems[i] == gems_list[4]:
                    bill_amount = reqd_quantity[i] * price_list[4]
                    Total_bill.append(bill_amount)

            else:
                return -1

    if sum(Total_bill) >= 30000:
        bill_amount = 30000-((5/100)*30000)
    else:
        bill_amount = sum(Total_bill)

    return bill_amount

#List of gems available in the store
gems_list=['Amber', 'Aquamarine', 'Opal', 'Topaz']

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[4316, 1342, 8734, 6421]

#List of gems required by the customer
reqd_gems=['Amber', 'Topaz']

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[1, 4]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)