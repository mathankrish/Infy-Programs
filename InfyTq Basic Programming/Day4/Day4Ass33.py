#Common Characters

def find_common_characters(msg1,msg2):
    a1=msg1.replace(" ","")
    b1=msg2.replace(" ","")
    a=list(set(a1)&set(b1))
    a11 = list(set(a)&set(a1))

    if(a!=" "):
        b=' '.join(a)
        return b
    else:
        return a11

msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)