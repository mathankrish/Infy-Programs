def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    b=[]
    countP=0
    countO=0
    countE=0
    for i in range(0,len(patient_medical_speciality_list),2):
        b.append(patient_medical_speciality_list[i+1])

    for j in range(len(b)):
        if(b[j]=="P"):
            countP=countP+1
        elif(b[j]=="E"):
            countE=countE+1
        elif(b[j]=="O"):
            countO=countO+1

    if (countP >= countO) and (countP >= countE):
        speciality=medical_speciality['P']

    elif (countO >= countP) and (countO >= countE):
         speciality=medical_speciality['O']
    else:
         speciality=medical_speciality['E']


    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)