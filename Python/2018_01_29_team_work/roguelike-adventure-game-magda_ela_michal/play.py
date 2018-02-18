import terminal_print
import data_manager
import os
from random import randint
import time
import sys
import highscore



def getch():
    import tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def choose_caracter_sign():
    while True:
        try:
            print("Which character would you like to play?")
            counter = int(input('\n [1] ♥\n [2] ♛\n [3] ★\n [4] ✺\n [5] ♝\nPress the number: '))
            character_sign =["♥", "♛", "★", "✺", "♝"]
            return(character_sign[counter-1])

        except (ValueError, IndexError):
            print("Choose number from 1 to 5!")

def choose_caracter_colour():
    while True:
        try:
            print("Which colour would you like to play?")
            counter = int(input('\n [1] red\n [2] blue\n [3] green\n [4] black\n [5] yellow\nPress the number: '))
            character_colour =["red", "blue", "green", "black", "yellow"]
            return(character_colour[counter-1])

        except (ValueError, IndexError):
            print("Choose number from 1 to 5!")

def change_levels(inventory):
    """Return name of screen file for level"""
    screen_list = ["screen1.txt", "screen2.txt","screen3.txt", "boss_screen.txt"]
    return screen_list[inventory['⚑']]


def create_character():
    """Combine character sign with character colour"""
    os.system('clear')
    sign = choose_caracter_sign()
    os.system('clear')
    colour = choose_caracter_colour()
    colour_dict = {"red":'\033[31m', "blue":'\033[34m', "green":'\033[32m', "black":'\033[30m', "yellow":'\033[93m'}
    end_change = '\x1b[0m'
    character = colour_dict[colour] + sign + end_change
    return character


def move_character(key, screen,x, y):
    special_sign = ['⚝','✿','♨','❀','⚑','.','♘','♒','♞','♪','☠','♫']
    old_x_y = (x,y)
    if key == 'w':
        if screen[x-1][y] in special_sign:
            x -= 1
            return x, y, old_x_y
    if key == 's':
        if screen[x+1][y] in special_sign:
            x += 1
            return x, y, old_x_y
    if key == 'd':
        if screen[x][y+1] in special_sign:
            y += 1
            return x, y, old_x_y
    if key == 'a':
        if screen[x][y-1] in special_sign:
            y -= 1
            return x, y, old_x_y
    return x, y, old_x_y

def check_life_in_inventory(life, inventory, level):
    death_traps = ["♒","♨","☠"]
    for item in death_traps:
        if item in inventory[level]:
            if inventory[level][item] > 0:
                life -= inventory[level][item]
                inventory[level][item] -= 1
    return life, inventory


def guess_number():
    secret_num = str(randint(1, 9))
    random_number = randint(0, 9)

    for i in range(2):
        while str(random_number) in secret_num:
            random_number = randint(0, 9)
        secret_num += str(random_number)

    guess = ""
    repeats = 1
    while secret_num != guess:
        if repeats > 10:
            return False

        print (secret_num)
        hints = []
        guess = input("Enter your guess: ")
        if len(guess) == len(secret_num):

            for i in range(3):
                if guess[i] in secret_num:
                    if guess[i] == secret_num[i]:
                        hints.insert(0, "\033[1;31mHOT\033[0;0m")
                    else:
                        hints.append("\033[1;33mWARM\033[0;0m")
            if not hints:
                hints.append("\033[1;34mCOLD\033[0;0m")
            repeats += 1
            print(" ".join(hints))
        else:
            print('Please, write tree digital number.')

    return True


def fighting_with_dragon(inventory, level, start_time):
    is_won = guess_number()
    if is_won == True:
        terminal_print.print_game_over_won()
        time.sleep(1)
        end_time = highscore.get_time_end()

    else:
        terminal_print.print_game_over_lost()
        time.sleep(1)
        end_time = highscore.get_time_end()


def set_character_on_screen(screen,character, x,y):
    screen[x][y] = character
    return screen


def get_start_positions():
    return 1,1


def add_to_inventory(x,y,inventory, screen, level):
    max_star_count = 4
    if screen[x][y] != '⚑':
        if screen[x][y] in inventory:
            inventory[screen[x][y]]+= 1
        if screen[x][y] in inventory[level]:
            inventory[level][screen[x][y]]+= 1
    else:
        if inventory[level]['⚝'] == max_star_count:
            inventory[screen[x][y]]+= 1
    return inventory


def create_inventory():
    inventory = {'⚑':0, '.':0, 0:{'⚝':0,'✿':0, '♨':0, '❀':0}, 1: {'⚝':0,'♘':0, '♒':0, '♞':0}, 2:
   {'⚝':0,'♪':0, '☠':0, '♫': 0}}

    return inventory

def clear_the_path(screen, x, y, old_x_y):
    if old_x_y == (x,y):
        return screen
    screen[old_x_y[0]][old_x_y[1]] = "ᛜ"
    screen[x][y] = "ᛜ"
    return screen

def clear_inventory_level(inventory,level):
    for item in inventory[level]:
        inventory [level][item] = 0
    return inventory

def check_if_reset(key):
    if key == "r":
        return True
    else:
        return False


def take_life_when_reset(life,key):
    if check_if_reset(key) == True:
        life -= 1
    return life


def play_level(screen,character,x,y,inventory,level,life):
    key = None
    inventory = clear_inventory_level(inventory,level)
    while inventory['⚑'] == level and key != "r" and life > 0 and key != "q" :
        os.system('clear')
        life, inventory = check_life_in_inventory(life, inventory, level)
        screen = data_manager.get_table_from_file("current_screen.txt")
        screen_with_char = set_character_on_screen(screen,character, x,y)
        terminal_print.print_inventory(level, inventory)
        print("Life:", life)
        terminal_print.print_screen(screen_with_char)
        print("Press [R] to reset level.")
        key = getch()
        x, y, old_x_y = move_character(key, screen,x, y)
        inventory = add_to_inventory(x, y, inventory,screen, level )
        screen = clear_the_path(screen, x, y, old_x_y)
        data_manager.write_screen_to_file(screen)
        life = take_life_when_reset(life,key)

    return key,inventory,life


def play_game(screen, character,inventory, start_time):
    os.system('clear')
    x, y = get_start_positions()
    key = None
    life = 5

    while life > 0 and key != "q":
        os.system('clear')
        file_name = change_levels(inventory)
        screen = data_manager.get_table_from_file(file_name)
        data_manager.write_screen_to_file(screen)
        if file_name == "boss_screen.txt":
            terminal_print.print_dragon()
            print("To fight the dragon you have to guess number (100-999) of people he has eaten.")
            input("Prepare yourself to fight dragon. Press enter when you're ready!")
            fighting_with_dragon(inventory, level, start_time)
            key = "q"
        elif file_name == "screen1.txt":
            level = 0
            key,inventory,life = play_level(screen,character,x,y,inventory,level,life)
        elif file_name == "screen2.txt":
            level = 1
            key,inventory, life = play_level(screen,character,x,y,inventory,level,life)
        elif file_name == "screen3.txt":
            level = 2
            key,inventory, life = play_level(screen,character,x,y,inventory,level,life)
    os.system('clear')
    if life == 0:
        terminal_print.print_game_over_lost()
        time.sleep(1)

    end_time = highscore.get_time_end()
    data_manager.write_score_to_file(inventory, level, start_time, end_time)
