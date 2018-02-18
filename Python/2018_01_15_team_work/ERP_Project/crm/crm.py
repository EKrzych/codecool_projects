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
        file_name = "crm/customers.csv"    
        table = data_manager.get_table_from_file(file_name)

        title = "You are in CRM Module. What would you like to do?"
        list_options = ["Display a table", 
                        "Add new record", 
                        "Remove a record", 
                        "Update specified record", 
                        "Check what is the id of the customer with the longest name", 
                        "Check which customers has subscribed to the newsletter"]
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
            result = get_longest_name_id(table)
            label = "The id of the customer with the longest name is: "
            ui.print_result(result, label)
        elif option == "6":
            label = "Customers that has subscribed to the newsletter"
            result = get_subscribed_emails(table)
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

    title_list = ["ID", "Name", "Email", "Subscribed"]
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
    list_labels = ["Name:","Email:", "Are you subscribed to the newsletter? 1/0 = yes/not:"]
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
    list_labels = ["Name:","Email:", "Are you subscribed to the newsletter? 1/0 = yes/not:"]
    inputs = ui.get_inputs(list_labels, title)
    table = common.update_line_in_table(table, id_, inputs)
    return table


def get_longest_name_id(table):

    """

        Function which returning customer with the 
        longest name if there are more than one 
        longest name, return the first by descending 
        alphabetical order

        """

    list_of_names = []
    sorted_list_of_names = []
    name_lenght_list = []

    for line in table:
        list_of_names.append(line[1])
    
    while list_of_names:
        sorted_list_of_names.append(max(list_of_names))
        list_of_names.remove(max(list_of_names))
    
    for line in table:
        name_lenght_list.append(len(line[1]))

    number_of_letters_in_longest_name = max(name_lenght_list)

    for line in sorted_list_of_names:
        if len(line) == number_of_letters_in_longest_name:
            longest_sorted_name = line

    for line in table:
        if line [1] == longest_sorted_name:
            return line[0]



def get_subscribed_emails(table):

    """
        Function which returning list of strings 
        (where string is like 
        email+separator+name, separator=";")

        """

        
    customer_subscribed = []
    for line in table:
        if line[3] == "1":
            customer_subscribed.append("{};{}".format(line[2],line[1]))
    return customer_subscribed
