# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_table():
    with open ("persons.csv", "r") as f:
        table = []
        for line in f:
            table.append(line.strip("\n").split(";"))
    return table

def find_max(table):
    max = table[0][2]
    row_index = 0
    for counter, record in enumerate(table):
        if max < record[2]:
            max = record[2]
            row_index = counter
    return row_index

def get_oldest_person(table):
    oldest_person_index = find_max(table)
    oldest_person = [row[1] for row in table if row[2] == table[oldest_person_index][2]]
    print(oldest_person)
    return oldest_person

# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_average(table):
    current_year = 2018
    total = 0
    for record in table:
        record.append(current_year - int(record[2]))
        total += record[3]
    return table, total / len(table)

def find_min(table,column):
    min = table[0][column]
    row_index = 0
    for counter, record in enumerate(table):
        if min > record[column]:
            min = record[column]
            row_index = counter
    return row_index

def sort_table(table):
    sorted_table = []
    while table:
        sorted_table.append(table.pop(find_min(table,3)))
    print(sorted_table)


def get_persons_closest_to_average(table):
    table, average = get_average(table)
    print(table)
    print(average)
    for record in table:
        record.append(abs(average - record[3]))
    print("______")
    closest = find_min(table,4)
    print(closest)
    closest_list = [row[1] for row in table if row[4] == table[closest][4]]
    print(table)
    print(closest_list)
    return closest_list


def main():
    table = get_table()
    get_oldest_person(table)
    get_persons_closest_to_average(table)
    
            

if __name__ == "__main__":
    main()