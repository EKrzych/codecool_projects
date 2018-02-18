import random

def choose_no_to_guess():
    while True:
        number_to_guess = str(random.randint(100, 999))

        if (number_to_guess[0] != number_to_guess[1]) and (number_to_guess[1] != number_to_guess[2]) and (number_to_guess[0] != number_to_guess[2]):
            return number_to_guess 


def main():
    number_to_guess = choose_no_to_guess()
    print(number_to_guess)
    tries = 6

    while tries:
        guess = input('What is your guess?')
        if guess == number_to_guess:
            print ("Hot Hot Hot", "\nYou have won")
            break
        for nr, digit in enumerate(guess):
            if digit in number_to_guess:
                if guess[nr] == number_to_guess[nr]:
                    print("Hot", end=" ")
                else:
                    print("Warm", end=" ")
            else: 
                print("Cold", end=" ")
        print("\n")
        tries -= 1
        if tries == 0:
            print("Game Over")

if __name__ == '__main__':
    main()


