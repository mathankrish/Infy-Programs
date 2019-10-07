# Check for the digits in a double


def check_double(number):
    double = number * 2

    for i in str(double):
        if i in str(number):
            a = True

        else:
            return False

    if (a == True):
        return True


print(check_double(125874))