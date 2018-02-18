import os
import ui
import data_manager
import common


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """
    is_input_correct = True

    while is_input_correct:
        file_name = "accounting/items.csv"    
        table = data_manager.get_table_from_file(file_name)
        
        title = "You are in Accounting Module. What would you like to do?"
        list_options = ["Display a table", 
                        "Add new record", 
                        "Remove a record", 
                        "Update specified record", 
                        "Check which year has the highest profit", 
                        "Check what is the average (per item) profit in a given year"]
        exit_message = "Go back to main menu"

        ui.print_menu(title, list_options, exit_message)
        inputs = ui.get_inputs(["Please enter a number from menu: "], "")
        option = inputs[0]

        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            show_table(table)
            answer = ui.get_inputs(["Which item would you like to remove: "], "")
            id_ = answer[0]
            remove(table, id_)
        elif option == "4":
            show_table(table)
            answer = ui.get_inputs(["Which item would you like to update: "], "")
            id_ = answer[0]
            update(table, id_)
        elif option == "5":

            show_table(table)
            label = "Highest profit was achieved in :"
            result = which_year_max(table)
            ui.print_result(result, label)
            
        elif option == "6":
            show_table(table)
            list_labels = ["Type year of Average profit you are interested in : "]
            title = ""
            answer = ui.get_inputs(list_labels, title)
            year = int(answer[0] )           

            result = avg_amount(table, year)      
            
            label = "The average profit (per) item in year {} is :".format(year)
            ui.print_result(result, label)
            
        elif option == "0":
            is_input_correct = False
        else: 
            ui.print_error_message("There is no such option.")

        data_manager.write_table_to_file(file_name, table)
        
def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    title_list = ["ID", "Month", "Day", "Year", "Type", "Amount"]
    os.system('clear')
    ui.print_table(table, title_list)

def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    title = "Provide data: "
    list_labels = ["Month:","Day:", "Year:", "Type(in = income, out = outcome):", "Amount:"]
    inputs = ui.get_inputs(list_labels, title)
    table = common.adding_new_line_to_table(inputs,table)
    
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table: table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        Table without specified record.
    """
    table = common.remove_line_from_table(table, id_)

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        table with updated record
    """
    title = "Provide data: "
    list_labels = ["Month:","Day:", "Year:", "Type(in = income, out = outcome):", "Amount:"]
    inputs = ui.get_inputs(list_labels, title)
    table = common.update_line_in_table(table, id_, inputs)

    return table


def which_year_max(table):

    """
    
        Returns year that has the highest profit
        
        """

    profit_by_year = {}

    for row in table:
        if row[3] not in profit_by_year:
            profit_by_year[row[3]] = 0
        if row[4] == "out":
            profit_by_year[row[3]] -= int(row[5])
        if row[4] == "in":
            profit_by_year[row[3]] += int(row[5])
        
    result = int(max(profit_by_year, key=lambda k: profit_by_year[k]))
    
    return result   

    
def avg_amount(table, year):

    """ 
        Returns the average (per item) 
        profit in a given year
        
        """


    data_for_given_year = [[row[4], row[5]] for row in table if row[3] == str(year)]

    profit = 0
    count = 0 

    for row in data_for_given_year: 
        
        if row[0] == "out":
            profit -= int(row[1])
        elif row[0] == "in":
            profit += int(row[1])
        count += 1
        
    result = profit / count

    return result
