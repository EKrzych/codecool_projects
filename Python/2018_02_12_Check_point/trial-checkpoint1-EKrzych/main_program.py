"""
The main program should use functions from data and display modules
"""
import data
import display
import sys

def add_new_student(students, new_student):
    """
    ADDITIONAL REQUIREMENT - BONUS

    Creates id for new student, adds it at the beginning of new student data,
    adds new student to students list and appends it to data file.

    :param list students: currently existing students
    :param list new_student: new student data without id. Format:
        name,surname,year of birth,class,average grade,average presence

    :returns: updated students list
    :rtype: list
    """
    current_ids = [item[0] for item in students]
    uid = data.generate_id(current_ids)
    complete_student = [uid] + new_student
    data.export_to_file(complete_student, filename='class_data.txt', mode='a')

def update_student(students, uid, new_student):
    for counter, item in enumerate(students):
        if item[0] == uid:
            students[counter] = [uid] + new_student
    data.export_to_file(students, filename='class_data.txt', mode='w')


def delete_student_by_id(students, uid):
    """
    Deletes student from list by given unique id and updates data file

    :param list students: currently existing students
    :param str uid: unique id of student to be deleted

    :returns: updated students list
    :rtype: list
    """
    for counter, row in enumerate(students):
        if row[0] == uid:
            del students[counter]
            data.export_to_file(students, filename='class_data.txt', mode='w')
            return students

def get_class_from_user():
    is_A_or_B = True
    while is_A_or_B:
        is_A_or_B = False
        class_name = input("Which class would you like to check (A/B)? ")
        if class_name != "A" and class_name != "B":
            is_A_or_B = True
    return class_name
    

def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should have main loop of program that will end only
    when user choose an option from menu to close the program. It should repeat
    displaying menu and asking for input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """
    menu_commands = ["Delete student.", 
                    "Get student by unique id.", 
                    "Get all students from given class.",
                    "Get youngest student from all classes.",
                    "Get youngest student from given class",
                    "Get oldest student from all classes",
                    "Get oldest student from given class",
                    "Calculate average grade of all students",
                    "Calculate average presence of all students",
                    "Add new student.",
                    "Get all students with given gender",
                    "Sorts student list by age",
                    "Update student",
                    "Exit program."]
    while True:
        table = data.import_data_from_file(filename='class_data.txt')
        display.print_command_result("")
        display.print_program_menu(menu_commands)
        answer = input("Hello to JERZYBOT. Please selcect your option:")
        if answer == "0":
            display.print_students_list(table)
            is_in_table = True
            while is_in_table:
                uid = input("Which student would you like to erase(id)? ")
                for row in table:
                    if row[0] == uid:
                        is_in_table = False
            delete_student_by_id(table, uid)
        elif answer == "1":
            display.print_students_list(table)
            uid = input("Which student would you like to check? ")
            try:
                student_data = data.get_student_by_id(uid, table)
                display.print_student_info(student_data)
            except ValueError:
                display.print_command_result('Student does not exist')
        elif answer == "2":
            class_name = get_class_from_user()
            student_data = data.get_students_of_class(table, class_name)
            display.print_students_list(student_data)
        elif answer == "3":
            student_data = data.get_youngest_student(table)
            display.print_student_info(student_data)
        elif answer == "4":
            class_name = get_class_from_user()
            student_data = data.get_youngest_student_of_class(table, class_name)
            display.print_student_info(student_data)
        elif answer == "5":
            student_data = data.get_oldest_student(table)
            display.print_student_info(student_data)
        elif answer == "6":
            class_name = get_class_from_user()
            student_data = data.get_oldest_student_of_class(table, class_name)
            display.print_student_info(student_data)
        elif answer == "7":
            message = str(data.get_average_grade_of_students(table))
            display.print_command_result(message)
        elif answer == "8":
            message = str(data.get_average_presence_of_students(table))
            display.print_command_result(message)
        elif answer == "9":
            new_student = []
            question =["name: ","surname: ","year of birth: ","class: ","average grade: ","average presence: "]
            display.print_command_result("Please provide:")
            for item in question:
                new_student.append(input(item))   
            add_new_student(table, new_student)
        elif answer == "10":
            try:
                gender = input("Which gender would you like to check (female/male)?")
                student_data = data.get_all_by_gender(table, gender)
                display.print_students_list(student_data)
            except ValueError:
                print('Wrong gender')
        elif answer == "11":
            try:
                order = input("Which order you choose(asc, desc, None)? ")
                if len(order) == 0:
                    order = None
                student_data = data.sort_students_by_age(table, order)
                display.print_students_list(student_data)
            except ValueError:
                display.print_command_result("Wrong order")
        elif answer == "12":
            display.print_students_list(table)
            is_in_table = True
            while is_in_table:
                uid = input("Which student would you like to update(id)? ")
                for row in table:
                    if row[0] == uid:
                        is_in_table = False
            new_student = []
            question =["name: ","surname: ","year of birth: ","class: ","average grade: ","average presence: "]
            display.print_command_result("Please provide:")
            for item in question:
                new_student.append(input(item))
            update_student(table, uid, new_student)

        elif answer == "13":
            sys.exit()
        else:
            display.print_command_result("There's no such option. Try again.")








if __name__ == '__main__':
    main()
