import highscore

def get_table_from_file(file_name):
    '''
    Reads txt file and returns it as a list of lists.
    Lines are rows columns are separated by " "
    '''

    with open(file_name, "r", encoding='utf-8') as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(" ") for element in lines]
    return table



def write_screen_to_file(screen):
    with open('current_screen.txt', "+w", encoding='utf-8') as file:
        for record in screen:
            row = ' '.join(record)
            file.write(row + "\n")


def write_score_to_file(inventory, level, start_time, end_time):
    new_scores_record = highscore.get_new_scores_record(inventory, level, start_time, end_time)
    new_scores_record[2] = round(new_scores_record[2])
    for i in range(len(new_scores_record)):
        new_scores_record[i] = str(new_scores_record[i])
    with open("highscore.txt", "a") as file:
        file.write(' '.join(new_scores_record) + "\n")
