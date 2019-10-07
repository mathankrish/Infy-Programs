def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    # eligible_loan_amount=0
    # bank_emi_expected=0
    # eligible_loan_amount=0

    first_digit = int(str(account_number)[0])

    if(len(str(account_number)) == 4 and first_digit == 1):

        if (account_balance >= 100000):

            if (loan_type == "Car" and salary > 25000):
                eligible_loan_amount = 50000
                bank_emi_expected = 36

                if (loan_amount_expected <= eligible_loan_amount and customer_emi_expected <= bank_emi_expected):
                    print("Account number:", account_number)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:", customer_emi_expected)
                    exit()

                else:
                    print("The customer is not eligible for the loan")
                    exit()

            else:
                print("Invalid loan type or salary")
                exit()



            if (loan_type == "House" and salary > 50000):
                eligible_loan_amount = 6000000
                bank_emi_expected = 60

                if (loan_amount_expected <= eligible_loan_amount and customer_emi_expected <= bank_emi_expected):
                    print("Account number:", account_number)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:", customer_emi_expected)
                    exit()
                else:
                    print("The customer is not eligible for the loan")
                    exit()

            else:
                print("Invalid loan type or salary")
                exit()


            if (loan_type == "Business" and salary > 75000):
                eligible_loan_amount = 7500000
                bank_emi_expected = 84

                if (loan_amount_expected <= eligible_loan_amount and customer_emi_expected <= bank_emi_expected):
                    print("Account number:", account_number)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:", customer_emi_expected)
                    exit()
                else:
                    print("The customer is not eligible for the loan")
                    exit()

            else:
                print("Invalid loan type or salary")
                exit()

        else:
            print("Insufficient account balance")
            exit()


    else:
        print("Invalid account number")





calculate_loan(1000,40000,250000,"Car",300000,30)