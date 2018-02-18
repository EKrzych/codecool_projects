def get_data():
    my_list = []
    my_list_number = []
    
    with open ("input_day_2.txt", "r") as f:
        for line in f:
            my_list.append(line.strip().split("	"))

    for row in my_list:
        line=[]
        for item in row:
            line.append(int(item))
        my_list_number.append(line)

    return my_list_number

def get_check_sum(my_list):
    """Determine the difference between 
    the largest value and the smallest value.
    The checksum is the sum of all of these differences.
    """

    diff_list = []
    for row in my_list:
        max_row = max(row)
        min_row = min(row)
        diff_list.append(int(max_row)-int(min_row))
    check_sum_diff = sum(diff_list)
    return check_sum_diff

def get_sum_division(my_list):
    """Find two numbers in each row where the result of the division operation 
    is a whole number, divide them, and add up each line's result.
    """

    div_list = []
    
    for row in my_list:
        for i in range(0,len(row)):           
            position_to_check = i
            list_to_check = row[0:i]+row[i+1:]
            for counter, item in enumerate(list_to_check):
                if int(row[position_to_check]) % int(list_to_check[counter]) == 0:
                    div_list.append(int(row[position_to_check])/int(list_to_check[counter]))
                    
    check_sum_div = sum(div_list)
    return check_sum_div



def main():
    my_list_number = get_data()
    check_sum_diff = get_check_sum(my_list_number)
    print(check_sum_diff)
    check_sum_div = get_sum_division(my_list_number)
    print(check_sum_div)

if __name__ == "__main__":
    main()
    
        
