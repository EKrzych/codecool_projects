# implement commonly used functions here

import random
import data_manager
import os

# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
# @table: list of lists
# @generated: string - randomly generated string (unique in the @table)

def generate_random(table):

    """
    Generates random and unique string. 
    Used for id/key generation.

    Args:
        table: list containing keys. 
        Generated string should be different then all of them

    Returns:
        Random and unique string
    """
    generated = ''
    is_in_table = True

    while is_in_table == True:
        is_in_table = False
        chars_table = "abcdefghijklmnopqrstuwvxyz"
        numbers = "12345678901234567890123456"
        special_signes = "!@$%^&*!@$%^&*!!@$%^&*!@$%"
        generated = (chars_table[random.randint(0,25)]
                        + chars_table[random.randint(0,25)].upper()
                        + numbers[random.randint(0,25)]
                        + numbers[random.randint(0,25)]
                        + chars_table[random.randint(0,25)].upper()
                        + chars_table[random.randint(0,25)]
                        + special_signes[random.randint(0,25)]
                        + special_signes[random.randint(0,25)])                          
        for row in table:
            if row[0] == generated:
                is_in_table == True

    return generated

def uploading_table(file_name):

    """ 
    
        Function for getting file after changes 
        made through working on program

        """


    data_manager.get_table_from_file(file_name)

def adding_new_line_to_table(inputs,table):

    """

        Function for adding line to table from file
        to name columns containing info about 
        interested in data. 

        Additionally it also generating unique ID.

        """

    new_line = []
    id_string = [generate_random(table)]
    new_line = id_string + inputs
    table.append(new_line)
    return table

def remove_line_from_table(table, id_):

    """

        Function which removes changes made in function
        adding_new_line_to_table(inputs,table)

        """

    for index, line in enumerate(table[::]):
        if line[0] == id_:
            del table[index]
    return table
    

def update_line_in_table(table, id_, inputs):

    """

        function which uptdates chages made in
        update (update changes made in a given row)
        options in program

        """

    for index, line in enumerate(table[::]):
        if line[0] == id_:
            table[index] = [id_] + inputs
    return table
