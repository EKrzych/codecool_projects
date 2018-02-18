def get_table():
    table = []
    with open("items.csv", "r") as f:
        for line in f:
            table.append(line.strip("\n").split(";"))
    return table
    
def find_max_dict(year_dict):
    years = list(year_dict.keys()) 
    max = year_dict[years[0]]
    year = years[0]
    for item in years[1:]:
        if year_dict[item] > max:
            max = year_dict[item]
            year = item
    return year

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def profit_per_year_dict(table):
    """Returns profit per year dict"""
    year_dict ={}
    for record in table:
        year_dict.setdefault(record[3],0)
        if record[4] == "in":
            year_dict[record[3]] += int(record[5])
        elif record[4] == "out":
            year_dict[record[3]] -= int(record[5])
    return year_dict
    

def count_item_in_year(table):
    item_per_year = {}
    for record in table:
        item_per_year.setdefault(record[3],0)
        item_per_year[record[3]] +=1
    print(item_per_year)
    return item_per_year


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):
    """Returns the average (per item) profit in a given year"""
    profit_per_year = profit_per_year_dict(table)
    item_in_year = count_item_in_year(table)
    average = profit_per_year[year] / item_in_year[year]
    print(average)
    return average


def main():
    table = get_table()
    profit_per_year = profit_per_year_dict(table)
    max_profit = find_max_dict(profit_per_year)
    year = input("Profit per which year would you like to check?")
    avg_amount(table, year)

if __name__ == "__main__":
    main()
