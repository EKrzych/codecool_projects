def dec_to_bin():
    binary_num = ""
    number_to_change = int(input("Which number would you like to change?"))
    print("z format bin {0:b}".format(number_to_change))
    while number_to_change > 1:
        binary_num += str(number_to_change % 2)
        number_to_change = number_to_change // 2

    if number_to_change == 1:
                binary_num += "1" 
    if number_to_change == 0:
                binary_num += "0"

    binary_num = binary_num[::-1]
    print("(bin) ",binary_num)
    print("bin {0:b}".format)

def bin_to_dec():
    dec_num = 0
    number_to_change = input("Which number would you like to change?")
    number_to_change = number_to_change[::-1]
    
    list_of_values=[2**i for i in range (0,len(number_to_change))]
    for counter, letter in enumerate(number_to_change):
        dec_num += int(letter) * list_of_values[counter]
    print(dec_num)

    
        

dec_to_bin()
bin_to_dec()


