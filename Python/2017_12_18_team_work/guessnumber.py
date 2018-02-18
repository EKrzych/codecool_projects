#The program will randomly set a secret number from 1 to parameter indicating max number 
# (i.e. python guess.py 50 => program will select number from 1 to 50)
# and user will be asked to guess that number. After each guess the program will be informing the user, 
# whether the guess is too low or too high, until user guesses the correct number.

import random
import sys
import time

def loading_max_value():
    max_value = int(sys.argv[1])
    return max_value

def ask_for_name():
    print("Welcome in *** Guess the Number game!")
    name = input("What is your name?")
    print("Well, " + name + ", I am thinking of a number.")
    return name

def guessing_number(number):
    guess = 0
    attempts = 0
    while guess != number:
        if attempts > 0:
            print("attempts:", attempts)
        attempts += 1
        guess = int(input("What is your guess?"))
        print()
        if number == guess:
            print("You have guessed in: ", attempts, " attempts")    
        elif guess>number:
            print(guess, " is too high")
        else:
            print(guess, "is too low")

def picking_number(max_value):
    number = random.randint(1,max_value)
    return number

def play_again():
    max_value = loading_max_value()
    play = True
    ask_for_name()
    start_time = time.time()
    while play:
        number = picking_number(max_value)
        guessing_number(number)
        end_time = time.time() - start_time
        print("It took you", int(end_time), "s")
        again = str(input("Do you want to play again, type yes or no "))
        if again == "no":
            play = False
def main():
    play_again()

if __name__ == '__main__':
    main()  