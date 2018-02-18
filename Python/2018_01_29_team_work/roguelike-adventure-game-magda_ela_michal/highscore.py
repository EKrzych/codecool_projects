import time

def get_name():
    name = input("Enter your name: ")
    return name


def get_time_start():
    start = time.time()
    return start


def get_time_end():
    end = time.time()
    return end


def get_time(start, end):
    return end - start


def get_score(inventory):
    score = inventory['.']
    elements_list = ['✿','❀','♘','♞','♪','♫']
    how_much_worth_element = [2,5,10,5,3,10]
    for i in range(3):
        for number, item in enumerate(elements_list):
            if item in inventory[i].keys():
                score += inventory[i][item]*how_much_worth_element[number]
    return score

def get_new_scores_record(inventory,level, start_time, end_time):
    time = get_time(start_time, end_time)
    name = get_name()
    level += 1
    score = get_score(inventory)
    return [name, level, time, score]
