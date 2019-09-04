import sys
import string
def palindrome(x):

    s = str(x)
    z = ""
    n = False
    for i in s:
        if i in string.punctuation:
            n = True
        else:
            z = i + z
    if int(z) <= 2147483647 and int(z) >= -2147483647:
        if n == True:
            z = int(z) * -1
        elif z == "":
            z = "0" + z
        elif len(z)>1 and z[0]=="0":
            z = z[1:]
            z = "0" + z       
        else:
            pass
    else:
        return 0

    if z == s:
        return True
    else:
        return False


def main():
    x = 121
    test = palindrome(x)
    print test

if __name__ == '__main__':
    main()