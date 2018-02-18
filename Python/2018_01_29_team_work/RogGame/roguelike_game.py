import os
import sys

def create_game_board(lenght, width):
    playboard=[[] for i in range(lenght)]
    for counter, row in enumerate(playboard):
        if counter == 0 or counter == lenght-1:
            for i in range(width+2):
                row.append("# ")
        else:
            row.append("# ")
            for i in range(width):
                row.append(". ")
            row.append("# ")
    return playboard

def print_game_board(playboard):
    os.system('clear')
    for element in playboard:
        for item in element:
            print (item, end ="")
        print()
    
    
def create_character():
    while True:
        try:
            print("Which character would you like to play?(choose number)")
            counter = int(input("1:@, 2:!, 3:&, 4:☠, 5:㋡"))
            character_list =["@ ", "! ", "& ", "☠ ", "㋡"]
            is_number = False
            return character_list[counter-1]
        except (ValueError, IndexError):
            print("Choose number from 1 to 5!")


def set_character_on_screen(playboard,x,y,character):
    playboard[y][x] = character
    return playboard


def getch():
    import sys, tty, termios #imports modules: sys, tty, termios
    fd = sys.stdin.fileno() #initialize variable fd with an intiger that represents file descriptor(in this case: 0)
    old_settings = termios.tcgetattr(fd)#initialize variable ols_settings with a result of termios.tcgetattr(fd) (list containing the tty attributes for file descriptor fd)
    try: #tries to execute:
        tty.setraw(sys.stdin.fileno())#change the mode of the file descriptor to raw
        ch = sys.stdin.read(1)#initialize variable ch with first sign from user input
    finally:#no matter what:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)#set the tty attributes for file descriptor to attributes written in old_settings
    return ch #return value assign to variable ch as a result of function


def game(lenght,width,x,y):
    move = getch()
    if move == "w":
        if y > 1:
            y -= 1
    if move == "s":
        if y < lenght - 2:
            y += 1
    if move == "a":
        if x > 1:
            x -= 1
    if move == "d":
        if x < width:
            x += 1
    if move == "q":
        sys.exit()
    return x,y


def main():
    x=10
    y=5
    lenght = 20
    width = 20
    playboard = create_game_board(lenght,width)
    character = create_character()
    set_character_on_screen(playboard,x,y,character)
    print_game_board(playboard)
    while True:
        x,y = game(lenght,width,x,y)
        playboard = create_game_board(lenght,width)
        set_character_on_screen(playboard,x,y,character)
        print_game_board(playboard)
        


if __name__ == '__main__':
    main()