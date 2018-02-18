def count_games(file_name):
    """returns number of games in file"""
    with open (file_name, "r") as f:
        return (sum (1 for line in f))

def decide(file_name, year):
    """returns True if there is a game from a given year or False otherwise"""
    with open (file_name, "r") as f:
        games_list = []
        for line in f:
            game = line.split("\t")
            games_list.append(game)
        for game in games_list:
            if game[2] == str(year):
                return True
        return False
            
def get_latest(file_name):
    """returns title of the latest game as a string"""
    with open (file_name, "r") as f:
        games_list = []
        game_years = []
        for line in f:
            game = line.split("\t")
            games_list.append(game)
            game_years.append(game[2])
        latest =  max(game_years)
        for game in games_list:
            if game[2] == str(latest):
                return game[0]

def count_by_genre(file_name, genre):
    """returns number of games in given genre"""
    with open (file_name, "r") as f:
        game_number = 0
        for line in f:
            game = line.split("\t")
            if game[3] == genre:
                game_number += 1
        return game_number

def get_line_number_by_title(file_name, title):
    """returns line number of the given game title"""
    with open (file_name, "r") as f:
        for number_line, line in enumerate(f, 1):
            game = line.split("\t")
            if title == game[0]:
                return number_line
        raise ValueError ()
    
def sort_abc(file_name):
    """returns alphabetical ordered list of the titles"""
    with open (file_name, "r") as f:
        game_names = []
        for line in f:
            game = line.split("\t")
            game_names.append(game[0])
        return (sorted(game_names))

def get_genres(file_name):
    """returns sorted set of the genres (alphabetical order)"""
    with open (file_name, "r") as f:
        game_genres = []
        for line in f:
            game = line.split("\t")
            game_genres.append(game[3])
        return (sorted(set(game_genres),key=str.lower))

def when_was_top_sold_fps(file_name):
    """returns year of the release top sold "First-person shooter game"""
    with open (file_name, "r") as f:
        games_list = []
        copies_sold = []
        top_sold = 0
        for line in f:
            game = line.split("\t")
            games_list.append(game)
            if "First-person shooter" == game[3]:
                if float(game[1]) > top_sold:
                    top_sold = float(game[1])
        for game in games_list:
            if float(game[1]) == top_sold:
                return int(game[2])
        raise ValueError ()
