"""
This module should use random module to generate_id
"""
import random

def import_data_from_file(filename='class_data.txt'):
    """
    Import data from file to list. Expected returned data format:
        [['M9@p', 'Ela', 'Opak', '1988', 'A', '60', '69'],
        ['E4)i', 'Barbara', 'Loremska', '1991', 'B', '76', '61'],
        ...]

    :param str filename: optional, name of file to be imported

    :returns: list of lists representing students' data
    :rtype: list
    """
    with open(filename, "r") as f:
        table = []
        for line in f:
            table.append(line.strip().split(","))
    return table


def export_to_file(data, filename='class_data.txt', mode='a'):
    """
    Export data from list to file. If called with mode 'w' it should overwritte
    data in file. If called with mode 'a' it should append data at the end.

    :param list data: students' data
    :param str filename: optional, name of file to export data to
    :param str mode: optional, file open mode with the same meaning as\
    file open modes used in Python. Possible values: only 'w' or 'a'

    :raises ValueError: if mode other than 'w' or 'a' was given. Error message:
        'Wrong write mode'
    """
    with open (filename, mode) as f:
        if mode == "w":
            for record in data:
                line = ",".join(record)
                f.write(line + "\n")
        elif mode == "a":
            line = ",".join(data)
            f.write(line + "\n")
        else:
            raise ValueError('Wrong write mode')





def get_student_by_id(uid, students):
    """
    Get student by unique id

    :param str uid: student unique id
    :param list students: students' data

    :raises ValueError: if student's uid not found in class data.
        Error message: 'Student does not exist'

    :returns: specific student's data
    :rtype: list
    """
    for row in students:
        if row[0] == uid:
            return row
    raise ValueError('Student does not exist')
        


def get_students_of_class(students, class_name):
    """
    Get all students from given class

    :param list students: list of nested list imported from file
    :param str class_name: string representing class name that student\
        attends to

    :returns: students from given class only
    :rtype: list
    """
    for row in students:
        class_list = [row for row in students if row[4]== class_name]
    return class_list


def get_youngest_student(students):
    """
    Get youngest student from all classes

    IMPORTANT:
        Implement this function without built-in functions like max(), min()
        or similar

    :param list students:  students' data

    :returns: youngest student
    :rtype: list
    """
    youngest_index = 0 
    youngest = students[0][3]
    for counter, row in enumerate(students[1:], 1):
        if int(row[3]) > int(youngest):
            youngest = students[counter][3]
            youngest_index = counter 
    return students[youngest_index]




def get_youngest_student_of_class(students, class_name):
    """
    Get youngest student from given class

    IMPORTANT:
        Implement this function without built-in functions like max(), min()
        or similar

    :param list students:  students' data
    :param str class_name: string representing class name that student\
        attends to

    :returns: youngest student from given class
    :rtype: list
    """
    students_from_class = get_students_of_class(students, class_name)
    youngest_from_class = get_youngest_student(students_from_class)
    return youngest_from_class


def get_oldest_student(students):
    """
    Get oldest student from all classes

    IMPORTANT:
        Implement this function without built-in functions like max(), min()
        or similar

    :param list students:  students' data

    :returns: oldest student
    :rtype: list
    """
    oldest_index = 0 
    oldest = students[0][3]
    for counter, row in enumerate(students[1:], 1):
        if int(row[3]) < int(oldest):
            oldest = students[counter][3]
            oldest_index = counter 
    return students[oldest_index]

def get_oldest_student_of_class(students, class_name):
    """
    Get oldest student from given class

    IMPORTANT:
        Implement this function without built-in functions like max(), min()
        or similar

    :param list students:  students' data
    :param str class_name: string representing class name that student\
        attends to

    :returns: oldest student
    :rtype: list
    """
    students_from_class = get_students_of_class(students, class_name)
    oldest_from_class = get_oldest_student(students_from_class)
    return oldest_from_class

def get_average_grade_of_students(students):
    """
    Calculate average grade of all students

    IMPORTANT:
        Implement this function without built-in functions like sum()
        or similar

    :param list students:  students' data

    :returns: average grade of students value
    :rtype: float
    """
    total_grade = 0
    for row in students:
        total_grade += int(row[5])
    return total_grade/len(students)

def get_average_presence_of_students(students):
    """
    Returns rounded average presence of all students. For instance,
    if average presence is 35.4912, returned value should be 35,
    if average presence is 41.5, returned value should be 42,

    IMPORTANT:
        Implement this function without built-in functions like sum(), round()
        or similar

    :param list students:  students' data

    :returns: average presence of students rounded to int
    :rtype: int
    """
    total_presence = 0
    for row in students:
        total_presence += int(row[6])
    average_presence = str(total_presence/len(students))
    if average_presence.find(".5") != -1:
        average_presence = float(average_presence) + 1
    else: 
        average_presence = float(average_presence)

    return int(average_presence)


def generate_id(current_ids):
    """
    ADDITIONAL REQUIREMENT - BONUS

    Generate unique id. It should be unique in all existing students list. If
    generated id was already used, function should regenerate it untill it is
    totaly new. Newly generated unique id should be added to current_ids

    REQUIREMENTS:
        - All ids must be 4-characters long
        - Characters should appear in given order:
            1. Upper letter
            2. Digit from 0 to 9
            3. Special character from this list: !@#$%^&*()_+
            4. Lower letter

            Example ids:
                W1&p
                M9@p
                P1!n

    :param list current_ids: list of all ids. It's used to check if
            generated id is unique or not. If new id is unique, current_ids
            should be extended to include this new id.

    :returns: unique id
    :rtype: str
    """
    is_in_current_ids = True
    while is_in_current_ids:
        uid = ""
        is_in_current_ids = False
        chars_table = "abcdefghijklmnopqrstuwvxyz"
        digit = "0123456789" 
        special_char = "!@#$%^&*()_+"
        uid = (chars_table[random.randint(0,len(chars_table)-1)].upper()
                + digit[random.randint(0,len(digit)-1)]
                + special_char[random.randint(0,(len(special_char)-1))]
                + chars_table[random.randint(0,(len(chars_table)-1))])
        if uid in current_ids:
            is_in_current_ids = True
        current_ids.append(uid)
    return uid



def get_all_by_gender(students, gender):
    """
    ADDITIONAL REQUIREMENT - BONUS

    Get all students with given gender. As someone forgot to ask students about
    it, the only way JERZYBOT can find out if someone is female is her name.
    Treat all students with name ending with 'a' as female (Maria, Anna, etc).
    (we're sorry Miriam, we'll update JERZYBOT as soon as possible)

    :param list students:  students' data
    :param str gender: gender to filter by. 'female' will return female
        students, 'male' will return list of male students

    :raises ValueError: if gender other than 'female' or 'male' was given.
        Error message: 'Wrong gender'

    :returns: list of students filtered by given gender
    :rtype: list
    """
    if gender == "female":
        gender_list = [student for student in students if student[1].endswith("a")]
        return gender_list
    elif gender == "male":
        male_list = []
        for counter, student in enumerate(students):
            if student[1].endswith("a"):
                pass
            else: 
                male_list.append(students[counter])
        return male_list

    else:
        raise ValueError('Wrong gender')


def get_youngest(students):
    youngest_index = 0 
    youngest = students[0][3]
    for counter, row in enumerate(students[1:], 1):
        if int(row[3]) < int(youngest):
            youngest = students[counter][3]
            youngest_index = counter
    return youngest_index


def get_oldest(students):
    oldest_index = 0 
    oldest = students[0][3]
    for counter, row in enumerate(students[1:], 1):
        if int(row[3]) > int(oldest):
            oldest = students[counter][3]
            oldest_index = counter
    return oldest_index


def sort_students_by_age(students, order=None):
    """
    ADDITIONAL REQUIREMENT - BONUS

    Sorts student list by age. User can choose sorting order by passing
    'desc' for descending order or 'asc' for ascening order.
    If order is None returns empty list

    IMPORTANT:
        Implement this function without using sorted() or similar built-in
        functions

    :param list students:  students' data
    :param str order: optional, sorting order

    :raises ValueError: if order other than 'asc', 'desc' or None
        was given

    :returns: sorted students or empty list
    :rtype: list
    """
    sorted_list=[]
    if order == "asc":
        while students:
           sorted_list.append(students.pop(get_youngest(students)))
    elif order == "desc":
        while students:
           sorted_list.append(students.pop(get_oldest(students)))
    elif order == None:
        sorted_list=[]
    else:
        raise ValueError("Wrong order")
    return sorted_list
