def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0

    if(distance_in_kms<=0 or quantity_ordered<1):
        bill_amount=-1
    else:
        if(food_type=="N"):
            if(distance_in_kms<=3):
                bill_amount=(150*quantity_ordered)+(0*distance_in_kms)
            elif(distance_in_kms>3 and distance_in_kms<=6):
                bill_amount=(150*quantity_ordered)+(3*(distance_in_kms-3))
            else:
                bill_amount=((150*quantity_ordered)+((distance_in_kms-6)*6+9))
        elif(food_type=="V"):
            if(distance_in_kms<=3):
                bill_amount=(120*quantity_ordered)+(0*distance_in_kms)
            elif(distance_in_kms>3 and distance_in_kms<=6):
                bill_amount=(120*quantity_ordered)+(3*(distance_in_kms-3))
            else:
                bill_amount=(120*quantity_ordered)+(9+6*(distance_in_kms-6))
        else:
            bill_amount=-1
    return bill_amount


bill_amount=calculate_bill_amount("N",2,8)
print(bill_amount)