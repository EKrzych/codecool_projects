#It's a game where a player can six time try guess a number from range 1 - 20.
import random #import module random

guesses_taken = 0 #Assign 0 to guesses_taken variable

print('Hello! What is your name?') #function that write string into the standard output
myName = input() #function that waits for answer from user and return string it into myName variable

number = random.randint(1, 20) #function that return a random integer (N such that 1 <= N <= 20) to number variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') #concatenate strings and writes it into the standard output

while guesses_taken < 6: #sets condition for while loop
    print('Take a guess.') #function that write string into the standard output
    guess = input() #function that waits for answer from user and return string it into guess variable
    guess = int(guess) #change guess variable type to integer

    guesses_taken += 1 #adds 1 to the guesses_taken variable value and assigns the new value to the variable.

    if guess < number: #sets conditional expresion for if statement and checks wheather is True
        print('Your guess is too low.') # a code that executes if the conditional expression is True: function that write string into the standard output

    if guess > number:#sets conditional expresion for if statement and checks wheather is True
        print('Your guess is too high.')# a code that executes if the conditional expression is True: function that write string into the standard output

    if guess == number:#sets conditional expresion for if statement and checks wheather is True
        break #terminates the while loop

if guess == number:#sets conditional expresion for if statement and checks wheather is True
    guesses_taken = str(guesses_taken) #change guesses_taken variable type to string
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!')#concatenate strings and writes it into the standard output

if guess != number:#sets conditional expresion for if statement and checks wheather is True
    number = str(number) #change number variable type to string
    print('Nope. The number I was thinking of was ' + number)#concatenate strings and writes it into the standard output
