import sys
import string
def palindrome(x):
    """
    """

    number = str(x)
    reverse = ""
    n = False
    for i in number:
        if i in string.punctuation:
            n = True
        else:
            reverse = i + reverse
    if int(reverse) <= 2147483647 and int(reverse) >= -2147483647:
        if n == True:
            reverse = int(reverse) * -1
        elif reverse == "":
            reverse = "0" + reverse
        elif len(reverse)>1 and reverse[0]=="0":
            reverse = reverse[1:]
            reverse = "0" + reverse       
        else:
            pass
    else:
        return 0

    if reverse == number:
        return True
    else:
        return False


def main():
    x = 262
    test = palindrome(x)
    print(test)

if __name__ == '__main__':
    main()