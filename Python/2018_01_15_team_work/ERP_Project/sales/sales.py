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
        file_name = "sales/sales.csv"
        table = data_manager.get_table_from_file(file_name)

        title = "You are in Sales Module. What would you like to do?"
        list_options = ["Display a table", 
                        "Add new record", 
                        "Remove a record", 
                        "Update specified record", 
                        "Check what is the id of the item that was sold for the lowest price", 
                        "Check which items are sold between two given dates"]
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
            label = "The id of the item that was sold for the lowest price is: "
            result = get_lowest_price_item_id(table)
            ui.print_result(result, label)
        elif option == "6":
        
            title = "Provide data: "
            list_labels = ["Month from :", "Day from :", "Year from :", "Month to :", "Day to :", "Year to :"]
            inputs = ui.get_inputs(list_labels, title)
    
            for i in range(len(inputs)):
                inputs[i] = int(inputs[i])

            month_from = inputs[0]
            day_from = inputs[1]
            year_from = inputs[2]
            month_to = inputs[3]
            day_to = inputs[4]
            year_to = inputs[5]

            result = get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
            label = "Data for item in between {}.{}.{} to {}.{}.{} :".format(day_from,month_from,year_from,day_to,month_to,year_to)
            
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
    title_list = ["ID", "Title", "Price", "Month", "Day", "Year"]
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
    list_labels = ["Title:", "Price(in $):", "Month:", "Day:", "Year:"]
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
    list_labels = ["Title:", "Price(in $):", "Month:", "Day:", "Year:"]
    inputs = ui.get_inputs(list_labels, title)
    table = common.update_line_in_table(table, id_, inputs)
    return table


def get_lowest_price_item_id(table):

    """
        id of the item that was 

        sold for the lowest price   
        
        """
    
    list_of_names = []
    sorted_list_of_names = []
    lowest_price = table[0][2]
    whole_list_sorted = []

    for line in table:
        list_of_names.append(line[1])

    while list_of_names:
        sorted_list_of_names.append(max(list_of_names))
        list_of_names.remove(max(list_of_names))
    
    for element in sorted_list_of_names[::]:
        for item in table:
            if element == item[1]:
                whole_list_sorted.append(item)

    for line in table:
        if line[2] <= lowest_price:
            lowest_price = line[2]

    for line in whole_list_sorted:
        if str(line[2]) == str(lowest_price):
            return (line[0])
        

def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    
    """
        function to pick all data 

        from table (initialized from file) 

        for items between given date    
        
        """

    from_date = string_merger(year_from, day_from, month_from)
    to_date = string_merger(year_to, day_to, month_to)

    sale_month = ""
    sale_day = ""
    sale_year = ""
    result = []

    for row in table:

        month = str(row[3])
        day = str(row[4])
        year = str(row[5])

        whole_date = string_merger(year, day, month)

        if from_date < whole_date < to_date:

            result.append(row) 

    return result


def string_merger(year, day, month):

    """ function to merge 3 parts od date into one string
        to make compare easier in function above """

    year = str(year)
    day = str(day)
    month = str(month)

    merged_data = year

    if len(day) < 2:

        day = "0" + day
        
    if len(month) < 2:

        month = "0" + month

    merged_data += month
    merged_data += day

    return int(merged_data)
        
