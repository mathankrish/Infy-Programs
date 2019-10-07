# PF-Tryout
def generate_schedule(module_list, duration_list, start_date):

    for i in range(len(module_list)):
        if (duration_list[i] < 10):
            a = start_date
            l1 = start_date.split("-")
            l1[0] = str((int(l1[0])+duration_list[i])-1)
            start_date = "-".join(l1)
            print(module_list[i]+" - "+" Start Date: "+a+" End Date: "+start_date)
            l1[0] = str(int(l1[0])+1)
            start_date = "-".join(l1)

        else:
            print(-1)



module_list = ["PF", "OOP"]
duration_list = [7, 80]
start_date = "01-03-2016"
generate_schedule(module_list, duration_list, start_date)



