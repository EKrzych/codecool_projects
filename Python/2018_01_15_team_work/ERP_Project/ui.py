import data_manager

"""
    Prints table with data. Sample output:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table: list of lists - table to display
        title_list: list containing table headers

    Returns:
        This function doesn't return anything it only prints to console.
    """

def print_table(table, title_list):

    """ 
    
        Function for printing frame for table

        appended from file connected to module

        """

    if table[0] != title_list:
        table.insert(0, title_list)
    
    titles_row = table[0]
    number_of_columns = len(table[0])
    # Transposition of the list appended from file (table lookalike) and 
    # initializing list max_columns_width containing lengths of 
    # the longest element of column (row[i])
    max_columns_width = []
    max_columns_width_in_number = 0
    for i in range(number_of_columns):
        column = [row[i] for row in table]
        max_columns_width.append(len(max(column, key=len)))
        max_columns_width_in_number += max_columns_width[i]
    table_width = max_columns_width_in_number + len(titles_row)*3 - 1


    TOP = "+{}++".format(table_width*"=") + "\n"
    BOTTOM = "++{}+".format(table_width*"=")
    HEADER_INTERLUDE = "|{}|".format(table_width*"=") + "\n"
    ROWS_INTERLUDE = "|{}|".format(table_width*"=") + "\n"
    final_table_builder = TOP

    for row in table:
        rows_for_table = ""
        
        for i in range(number_of_columns):
            text_for_cell = row[i]
            current_column_width = max_columns_width[i] + 2

            spacing = (current_column_width - len(text_for_cell))
            side_spacing = int(spacing / 2)
            missing_blank_space = current_column_width - (2 * side_spacing + len(text_for_cell))

            rows_for_table += "{}{}{}{}{}{}".format("|",
                                                  side_spacing * " ",
                                                  text_for_cell,
                                                  side_spacing * " ",
                                                  " " if missing_blank_space == 1 else "",
                                                  "|" if i == number_of_columns - 1 else "")

 
        final_table_builder += rows_for_table + "\n"

        titles_row = table[0]
        bottom_row = table[-1]

        if row == titles_row:
            final_table_builder += HEADER_INTERLUDE

        elif row != bottom_row:
            final_table_builder += ROWS_INTERLUDE

    final_table_builder += BOTTOM

    print(final_table_builder)

    table.pop(0)



def print_result(result, label):

    """
    Displays results of the special functions.

    Args:
        result: string, list or dictionary - result of the special function
        label: label of the result

    Returns:
        This function doesn't return anything it only prints to console.
    """
    print ()
    print(label)
    print ()
    if type(result) is list:
        for item in result:
            print("\t{}".format(item))
    else: print("\t{}".format(result))
    print()
    


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        This function doesn't return anything it only prints to console.
    """
    print(title, ":")
    for index, item in enumerate(list_options, 1):
        print ("\t", "(",index,") ", item)
    print ("\t", "(",0,") ", exit_message)

def get_inputs(list_labels, title):

    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels: list of strings - labels of inputs
        title: title of the "input section"

    Returns:
        List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    
    list_of_answers = []
    i=0
    print(title)
    for item in list_labels:
        question = list_labels[i]
        answer = input (question)
        list_of_answers.append(answer)
        i += 1
    return list_of_answers


def print_error_message(message):
         
        
    """
    Displays an error message

    Args:
        message(str): error message to be displayed

    Returns:
        This function doesn't return anything it only prints to console.
    """
    print(message)



