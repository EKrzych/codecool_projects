import data_manager

def print_introduction_screen():
    table = data_manager.get_table_from_file('start_screen.txt')
    for item in table:
        print('\033[38;5;144m',' '.join(item),'\033[0m')

def print_menu():
    table = data_manager.get_table_from_file('start_menu_screen.txt')
    for item in table:
        print(' '.join(item))


def print_rules():
    print("""RULES:

1. You have only 5 lives.

2. Move your character with letters: WSAD.

3. You lose one life if you step on the trap: ♒ ♨ ☠ or reset level.

4. Watch out when you walk. There is no way back!

5. You need 4 stars to grab flag.

""")


def choose_submenu():
    print_menu()
    answer = input("Press the number: ")
    return answer


def print_highscore():
    highscore_table = [["NICKNAME", "LEVEL", "TIME", "SCORE"]] + data_manager.get_table_from_file("highscore.txt")
    for item in highscore_table:
        print('{:-^58}'.format(''))
        print("| {:^15} | {:^10} | {:^10} | {:^10} |".format(*item))
    print('{:-^58}'.format(''))


def print_screen(screen):
    special_sign = ['⚝','✿','♨','❀','⚑','.','▤','♘','♒','♞','▦','♪','☠','♫','▨','ᛜ']
    colour_sign =['\033[38;5;226m', '\033[38;5;175m', '\033[38;5;196m',
                   '\033[38;5;215m', '\033[38;5;28m', '\033[38;5;187m',
                   '\033[38;5;138m', '\033[38;5;15m', '\033[38;5;196m',
                   '\033[38;5;215m', '\033[38;5;166m', '\033[38;5;225m',
                   '\033[38;5;196m', '\033[38;5;229m', '\033[38;5;172m',
                   '\033[38;5;223m']
    colour_end = "\033[0m"
    for row in screen:
        for item in row:
            for counter, sign in enumerate(special_sign):
                if item == sign:
                    item = colour_sign[counter] + sign + colour_end
            print(item, end =" ")
        print()


def print_dragon():
    table = data_manager.get_table_from_file('boss_screen.txt')
    for item in table:
        print('\033[38;5;150m',' '.join(item),'\033[0m')


def print_game_over_lost():
    table = data_manager.get_table_from_file('game_over_lost.txt')
    for item in table:
        print('\033[38;5;160m',' '.join(item),'\033[0m')


def print_game_over_won():
    table = data_manager.get_table_from_file('game_over_won.txt')
    for item in table:
        print('\033[38;5;132m',' '.join(item),'\033[0m')

def print_inventory(level, inventory):
    print("Level:", inventory['⚑'] + 1, "Points:", inventory['.'],)
    trap = ["♒","♨","☠"]
    for k,v in inventory[level].items():
        if k not in trap:
            print (k, ":", v, end =", ")
    print()
