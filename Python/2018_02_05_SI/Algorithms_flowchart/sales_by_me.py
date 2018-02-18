def get_table():
    table = []
    with open ("sales.csv", "r") as f:
        for line in f:
            table.append(line.strip().split(";"))
    return table

def get_date_from_user():
    answer_from = []
    answer_to = []
    date_from = ["year_from ","month_from ", "day_from "]
    date_to = ["year_to ", "month_to ", "day_to "]
    print("Give me range of dates which you would like to check: ")
    for item in date_from:
        answer_from.append(input(item))
    for item in date_to:
        answer_to.append(input(item))
    return answer_from, answer_to 

def merge_dates(answer):
    merged_answer = ""
    for counter, item in enumerate(answer):
        if len(item) < 2:
            answer[counter] = "0" + answer[counter]
    for item in answer: 
        merged_answer += "".join(item)
    return merged_answer


#sales.csv
#"ID", "Title", "Price", "Month", "Day", "Year"
def get_items_sold_between(table, answer_from, answer_to):
    choosen_items = [item for item in table if int(merge_dates(answer_from)) < int(merge_dates([item[5],item[3],item[4]])) < int(merge_dates(answer_to)) ]
    print(choosen_items)


def main():
    table = get_table()
    answer_from, answer_to = get_date_from_user()
    get_items_sold_between(table, answer_from, answer_to)


if __name__ == "__main__":
    main()
