# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
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
        file_name = "hr/persons.csv"    
        table = data_manager.get_table_from_file(file_name)

        title = "You are in Human Resources Module. What would you like to do?"
        list_options = ["Display a table", 
                        "Add new record", 
                        "Remove a record", 
                        "Update specified record", 
                        "Check who is the oldest person", 
                        "Check who is the closest to the average age"]
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
            result = get_oldest_person(table)
            label = "The oldest: "
            ui.print_result(result, label)
        elif option == "6":
            label = "Closest to average :"
            result = get_persons_closest_to_average(table)
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

    title_list = ["ID", "Name", "Birth Year"]
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
    list_labels = ["Name:", "Birth Year:"]
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

    common.remove_line_from_table(table, id_)

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

    title = "Provide data:"
    list_labels = ["Name:", "Birth Year:"]
    inputs = ui.get_inputs(list_labels, title)
    table = common.update_line_in_table(table, id_, inputs)
    
    return table


def get_oldest_person(table):


    """
    
        Returns list of the oldest people   
        
        """
    
    birthyears = [element[2] for element in table]
    oldest = min(birthyears)

    names = [element[1] for element in table if element[2] == oldest]
    result = names

    return result


def get_persons_closest_to_average(table):

    """

        Function returning list of people from table 
        whom birthyears are closest to the average 
        birthyear in given file.

        """

    birthyears = [int(element[2]) for element in table]
    
    sum_from_birthyears = 0
    for element in birthyears: 
        sum_from_birthyears += element
    
    avg_birthyear = sum_from_birthyears / len(birthyears)

    birthyears_sorted = []

    while birthyears:
        minimum = birthyears[0]  
        for y in birthyears: 
            if y < minimum:
                minimum = y
    
        birthyears_sorted.append(minimum)
        birthyears.remove(minimum)

    closest = str(min(birthyears_sorted, key=lambda x:abs(x-avg_birthyear)))

    result = [str(row[1]) for row in table if closest == row[2]]    

    return result
