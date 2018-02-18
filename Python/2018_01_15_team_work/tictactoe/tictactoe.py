import random

def check_if_win(board, winners):
    stringX = "XXX"
    stringO = "OOO"

    for item in winners:
        test_string = ""
        for position in item:
            test_string += board[position-1]
        if test_string == stringO or test_string == stringX:
            return True

def block_human(winners, board, dict_players_mark):
    shoot = None
    for item in winners:
        count_in_row = 0
        for position in item:
            if board[position-1] == dict_players_mark["human"]:
                count_in_row += 1
            elif board[position-1] != dict_players_mark["machine"] and board[position-1] != dict_players_mark["human"]:
                shoot = position-1
        if count_in_row == 2:
            return shoot


def who_is_first():
    players = ["machine","human"]
    first_player_index = random.randint(0,1)
    second_player_index = abs(first_player_index-1)

    return players[first_player_index], players[second_player_index]


def show(board):
    print("\n", board[0], board[1], board[2], "\n",
                board[3], board[4], board[5], "\n",
                board[6], board[7], board[8], "\n")

    
def game(board, first_player, second_player,dict_players_mark,winners):
    player = None
    while set(board) != {"O","X"}:
        if first_player == "machine" or player == "machine":
            print("Computer move, he plays '{}'.".format(dict_players_mark["machine"]))
            is_free = True
            block = block_human(winners, board, dict_players_mark)
            if block:
                board[block] = dict_players_mark["machine"]         
            else:
                while is_free:
                    place_to_change = random.randint(0,8)
                    if board[place_to_change] != "X" and board[place_to_change] != "O":
                        board[place_to_change] = dict_players_mark["machine"]
                        is_free = False
            show(board)
            player = "human"
            if check_if_win(board, winners):
                print("Computer won!")
                break
            
        if set(board) == {"O","X"}:
            break

        if first_player == "human" or player == "human":
            print("Human move, you are playing '{}'.".format(dict_players_mark["human"]))
            
            is_free = True
            while is_free:
                place_to_change = int(input("Which place would you like to change ??: "))
                if board[place_to_change-1] != "X" and board[place_to_change-1] != "O":
                        board[place_to_change-1] = dict_players_mark["human"]
                        is_free = False
                        player = "machine"
                else:
                    print("This place is already taken!")
            show(board)
            if check_if_win(board, winners):
                print("You won!")
                break

def main():
    winners = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    first_player, second_player = who_is_first()
    dict_players_mark = {first_player : "X", second_player : "O"}
    show(board)
    game(board, first_player, second_player,dict_players_mark, winners)

if __name__ == '__main__':
    main()

# \033[91m\033[1m  \033[0m
# \033[92m\033[1m \033[0m