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
        file_name = "inventory/inventory.csv"    
        table = data_manager.get_table_from_file(file_name)

        title = "You are in Inventory Module. What would you like to do?"
        list_options = ["Display a table", 
                        "Add new record", 
                        "Remove a record", 
                        "Update specified record", 
                        "Check which items have not exceeded their durability yet", 
                        "Check what are the average durability times for each manufacturer"]
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
            result = get_available_items(table)
            label = "List of items that have not exceeded their durability: "
            ui.print_result(result, label)
            for row in result:
                row[3] = str(row[3])
                row[4] = str(row[4])
        elif option == "6":
            show_table(table)
            label = "Average durability by manufacturers :"
            result = get_average_durability_by_manufacturers(table)
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

    title_list = ["ID", "Name", "Manufacturer", "Purchase Year", "Durability"]
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
    list_labels = ["Name:", "Manufacturer:", "Purchase Year:", "Durability(year):"]
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
    list_labels = ["Name:", "Manufacturer:", "Purchase Year:", "Durability(year):"]
    inputs = ui.get_inputs(list_labels, title)
    table = common.update_line_in_table(table, id_, inputs)
    return table

#
def get_available_items(table):

    """ 
        Returns list of items that have not 
        exceeded their durability   
        
        """
    
    year = 2017

    production_durability = [row for row in table if int(row[3]) + int(row[4]) >= year]
    result = []

    for row in production_durability:
        row[3] = int(row[3])
        row[4] = int(row[4])
        result.append(row)
    
    return result


def get_average_durability_by_manufacturers(table):

    """

        Function returning dictionary with given 
        structure ({'manufacturer':avg}) which means
        key=str(manufacturer):value=float(average_durability)

        """

    manufacturer_durability = {}
    manufacturer_count = {}
    result = manufacturer_durability

    for item in table:
        
        if item[2] not in manufacturer_durability:
            manufacturer_durability[item[2]] = float(item[4])
            manufacturer_count[item[2]] = 1
        else:
            manufacturer_durability[item[2]] += float(item[4])
            manufacturer_count[item[2]] += 1
    
    for item in manufacturer_durability:

        manufacturer_durability[item] = float(manufacturer_durability[item]/manufacturer_count[item])

    return result