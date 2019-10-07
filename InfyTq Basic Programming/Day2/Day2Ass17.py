# Salary Hike using Levels

def find_new_salary(current_salary,job_level):
    # write your logic here
    if(job_level == 3):
        percentage = current_salary * (15/100)
        new_salary = int(current_salary + percentage)

    elif(job_level == 4):
        percentage = current_salary * (7 / 100)
        new_salary = int(current_salary + percentage)

    elif (job_level == 5):
        percentage = current_salary * (5 / 100)
        new_salary = int(current_salary + percentage)


    return new_salary

# provide different values for current_salary and job_level and test yor program
new_salary = find_new_salary(20000 , 5)
print(new_salary)