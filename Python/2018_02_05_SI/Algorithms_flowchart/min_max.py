my_list = [-30000000,40000000,5,1000,0,-200,0,23,122,1333,-10111]
def find_min(my_list):
    my_min = my_list[0]
    index = 0
    for counter, item in enumerate(my_list):
        if my_min > item:
            my_min = my_list[counter]
            index = counter
    print(my_min)
    print(index)

def find_max(my_list):
    my_max = my_list[0]
    index = 0 
    for counter, item in enumerate(my_list):
        if my_max < item:
            my_max = my_list[counter]
            index = counter
    print(my_max)
    print(index)

def average_value(my_list):
    average_value = sum(my_list)/len(my_list)
    print(average_value)
    total = 0
    counter = 0
    for item in my_list:
        total += item
        counter += 1
    my_calc = total/counter
    print(my_calc)

find_min(my_list)
find_max(my_list)
average_value(my_list)
