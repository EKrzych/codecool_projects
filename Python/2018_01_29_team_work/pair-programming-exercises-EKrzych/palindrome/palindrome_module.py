def palindrome(str1):

    str1 = str1.replace(" ", "")
    print(str1)
    str2 = str1[::-1]
    print(str2)
    if str1.lower() == str2.lower():
        return True
    else:
        return False


def main():
    palindrome("A nut for a jar of tuna")


if __name__ == '__main__':
    main()
