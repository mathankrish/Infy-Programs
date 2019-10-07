#Palindrome

def check_palindrome(word):
    a ="".join(reversed(word))
    print(a)
    print(word)
    if(a==word):
        return True
    else:
        return False

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")