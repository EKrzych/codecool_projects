def factorial():
    number_to_check = int(input("For which number would you like to calculate factorial?"))
    factorial = 1
    while number_to_check >= 1:
        factorial *= number_to_check
        number_to_check -= 1
    print(factorial)

factorial()