import data_manager
import play
import terminal_print
import sys
import time
import os
import highscore


def main ():
    os.system('clear')
    terminal_print.print_introduction_screen()
    input("Press enter when you're ready!")
    while True:
        os.system('clear')
        choice = terminal_print.choose_submenu()
        inventory = play.create_inventory()

        if choice == "1":
            character = play.create_character()
            start_time = highscore.get_time_start()
            file_name = play.change_levels(inventory)
            screen = data_manager.get_table_from_file(file_name)
            play.play_game(screen, character,inventory, start_time)

        elif choice == "2":
            terminal_print.print_highscore()
            input("Press enter when you're ready!")
        elif choice == "3":
            terminal_print.print_rules()
            input("Press enter when you're ready!")
        elif choice == "0":
            sys.exit()
        else:
            print("Please choose number from 0 to 3!")





if __name__ == '__main__':
    main()
