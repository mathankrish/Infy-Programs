#PF-Prac-43

def find_promoted_vp(presidents_dict):
    #start writing your code here
    pre = []
    vp = []

    for k in range(len(presidents_dict)):
        pre.append(presidents_dict[k]['name'])
        vp.append(presidents_dict[k]['vp'])


    promoted_vp_list = [i for i in vp if i in pre]
    return promoted_vp_list

def find_presidents_vp(presidents_dict,duration):
    vice, pre = [], []
    rstarrt, rend = duration.split('-')
    for i in range(len(presidents_dict)):
        start, end = presidents_dict[i]['period'].split('-')
        if (int(start) >= int(rstarrt) and int(end) <= int(rend)):
            vice.append(presidents_dict[i]['vp'])
            pre.append(presidents_dict[i]['name'])
    promoted_vp = [i for i in vice if i in pre]
    return promoted_vp

presidents_dict=[{'name':'George Washington', 'vp':'John Adams', 'period':'1990-1993'},
                 {'name':'John Adams', 'vp':'Thomas Jefferson', 'period':'1994-1996'},
                 {'name':'Zachary Taylor', 'vp':'Millard Fillmore', 'period':'1997-1999'},
                 {'name':'Dwight D. Eisenhower', 'vp':'Richard Nixon', 'period':'1999-2001'},
                 {'name':'Richard Nixon', 'vp':'Spiro Agnew', 'period':'2001-2002'},
                 {'name':'Richard Nixon', 'vp':'Gerald Ford', 'period':'2002-2004'}]

print("The president and vice president details:",presidents_dict)
output=find_promoted_vp(presidents_dict)
print("The list of vice presidents who also got promoted as presidents:",output)
duration='1999-2005'
print("The president and vice president details:",presidents_dict)
print("Given duration:",duration)
output1=find_presidents_vp(presidents_dict, duration)

print("The list of vice presidents who also got promoted as presidents in the given duration:",output1)
