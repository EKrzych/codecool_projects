# Create a script that has a list of European capitals, 
# pick one of them randomly and let the user guess it.

import sys
import random
import time
import datetime
import os

def hangman(life, max_life):
    """Prints hangman picture"""
    with open ("pict_hangman.txt", "r") as f:
        picture =[]
        for line in f:
            picture.append(line)
        number = [0, 9, 18, 27, 36, 45, 54]
        if life < 0:
            for item in picture[54:63]:
                print(item, end = "")  
        else:
            hangman_size = 9
            a = (number[max_life - life])
            for item in picture[a:a+hangman_size]:
                print(item, end = "")   

def date():
    """return date"""
    now = datetime.datetime.now()
    now_date = now.strftime("%Y-%m-%d")
    return str(now_date)

def take_countries_and_capitals():
    """return full content of file"""
    full_list =[]
    with open ("countries_and_capitals.txt", "r") as f:
        for line in f:
            full_list.append(line)
    return full_list


def create_country_capital_list(full_list):
    """return country (country_capital_list [0]) and capital (country_capital_list[1]"""
    pair = random.choice(full_list)
    country_capital_list = []
    country, capital = pair.split("|")
    country_capital_list.append(country.strip())
    country_capital_list.append(capital.strip().upper())
    return country_capital_list

def hide_capital(country_capital_list):
    """hide capital in hidden_word and add it to country_capital_list [2]"""
    hidden_word = []
    for i in range (len(country_capital_list[1])):
        hidden_word.append("_ ")
    country_capital_list.append(hidden_word)

def ask_for(word_or_letter):
    """return player's guess"""
    print ("Give me your", word_or_letter, end="")
    guess = input(":")
    return guess.upper()

def guess_letter(country_capital_list, life):
    user_won = False
    guess = ask_for("letter")
    if guess in country_capital_list[1]:
        for nr, char in enumerate (country_capital_list[1]):
            if guess == char:
                country_capital_list[2][nr]= guess
        if ''.join(country_capital_list[2]) == country_capital_list[1]: 
            user_won = True
    else:
        life = life - 1
        if guess not in country_capital_list[3]:
            country_capital_list[3].append(guess)
    return (life, user_won)

def guess_word(country_capital_list, life):
    user_won = False
    guess = ask_for("word")
    if guess == country_capital_list[1]:
        user_won = True
    else:
        life = life - 2
    return (life, user_won)

def take_score_list():
    """read and return score_list from file"""
    score_list =[]
    with open ("score_list.txt", "r") as f:
        for line in f:
            score_list.append(line)
    return score_list

def get_key_for_sorting_score_list (item):
    return item[2][0]

def sorting_score_list(score_list):
    scorelist_switched = []
    for item in score_list:
        item = item.split("|")
        item[2] = item[2].split(" ")
        item[2][0] = int(item[2][0])
        scorelist_switched.append(item)
    sorted_list = sorted(scorelist_switched, key=get_key_for_sorting_score_list)
    return sorted_list

def print_sorted_list(sorted_list):
    for item in sorted_list[0:10]:
        item[2][0] = str(item[2][0])
        for i in item[2]:
            item[2] = "".join(item[2])
        item = "|".join(item)
        print (item)

def gather_users_data(country_capital_list, game_time,  guess_tries):
    score_item = []
    name = input("What's your name?")
    score_item.append(name)
    score_item.append(date())
    score_item.append(game_time)
    score_item.append(guess_tries)
    score_item.append(country_capital_list[1])
    score_item = "|".join(score_item)
    print(score_item)
    return score_item
            
def game_over (life, user_won, country_capital_list, game_time, guess_tries, max_life):
    if user_won and life > 0:
        print("You Won!!!!!")
        
        answer = input("Would you like to save your score?(yes/no)")
        if answer == "yes":
            score_item = gather_users_data(country_capital_list, game_time,  guess_tries)
            with open ("score_list.txt", "+a") as f:
                f.write("%s\n" % score_item)

    hangman(life, max_life)
    print("GAME OVER")

def give_hint (country_capital_list, life):
    if life == 1:
        print("Hint: You are guessing capital of: ", country_capital_list[0])

def print_guess_not_in_word_list(country_capital_list):
    if len(country_capital_list[3]) > 0:
            print ("Letters not in word: ", country_capital_list[3]) 

def print_hidden_capital_name(country_capital_list):  
        for i in country_capital_list[2]:
            print(i, end="")
        print("\n")

def guessing_word_or_letter(country_capital_list, max_life):
    life = max_life
    user_won = False
    guess_tries = 0
    #create (list of guess not_in_word) in (country_capital_list[3])
    country_capital_list.append([])
    
    while life>0 and not user_won:
        _ = os.system('clear')
        hangman(life, max_life)
        start = time.time()
        print("\n"*2)
        print("Your life: ", life)

        print_guess_not_in_word_list(country_capital_list)

        print_hidden_capital_name(country_capital_list) 
        
        give_hint(country_capital_list, life)

        #ask user if he want to guess letter or word
        l_or_w = input("guess a letter (press L) or whole word (press W)")
        if l_or_w == "L" or l_or_w == "l":
            guess_tries +=1
            life, user_won = guess_letter(country_capital_list, life)
        elif l_or_w ==  "W" or l_or_w == "w":
            guess_tries +=1
            life, user_won = guess_word(country_capital_list, life)

    end = time.time()
    game_time = end - start
    game_time = str(int(game_time)) + " sec"

    print("Time:",game_time)
    print("You tried:", guess_tries, " times")
    guess_tries = str(guess_tries)

    return user_won, life, game_time, guess_tries   

def main():

    another_try = "yes"
    while another_try=="yes":
        max_life  = 6
        another_try = "no"
        full_list = take_countries_and_capitals()
        country_capital_list = create_country_capital_list(full_list)
        hide_capital(country_capital_list)
        user_won,life,game_time,guess_tries = guessing_word_or_letter(country_capital_list, max_life)
        game_over (life, user_won, country_capital_list, game_time, guess_tries, max_life)
        score_list = take_score_list()
        sorted_list = sorting_score_list(score_list)
        print_sorted_list(sorted_list)
        another_try = input("Would you like to try again?(yes/no)")  
main()