import random
import sys


def ask_for_name():
    print("Welcome in *** Guess the Number game!")
    name = input("What is your name?")
    print("Well, " + name + ", I am thinking of a number between 1 and 30.")
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

def picking_number():
    number = random.randint(1,31)
    return number

def play_again():
    play = True
    ask_for_name()
    
    while play:
        number = picking_number()
        print(number)
        guessing_number(number)
        again=str(input("Do you want to play again, type yes or no "))
        if again == "no":
            play = False

def main():
    play_again()
main()
        