import math

def get_most_played(file_name):
    """returns the title of the most played game"""
    with open (file_name, "r") as f:
        games_list = []
        total_copies_sold = []
        for line in f:
            game = line.split("\t")
            games_list.append(game)
            total_copies_sold.append(float(game[1]))
        bestseller =  max(total_copies_sold)
        for game in games_list:
            if float(game[1]) == bestseller:
                return game[0]

def sum_sold(file_name):
    """returns total number of copies sold"""
    with open (file_name, "r") as f:
        copies_sold = []
        for line in f:
            game = line.split("\t")
            copies_sold.append(float(game[1]))
        return sum(copies_sold)

def get_selling_avg(file_name):
    """returns average selling"""
    with open (file_name, "r") as f:
        copies_sold = []
        for line in f:
            game = line.split("\t")
            copies_sold.append(float(game[1]))
        return sum(copies_sold)/len(copies_sold)

def count_longest_title(file_name):
    """returns number of characters in the longest title"""
    with open (file_name, "r") as f:
        title_lenght = []
        for line in f:
            game = line.split("\t")
            title_lenght.append(len(game[0]))
        return max(title_lenght)

def get_date_avg(file_name):
    """returns average selling"""
    with open (file_name, "r") as f:
        release_dates = []
        for line in f:
            game = line.split("\t")
            release_dates.append(int(game[2]))
        return int(math.ceil(sum(release_dates)/len(release_dates)))

def get_game(file_name, title):
    """returns properties of choosen game"""
    with open (file_name, "r") as f:
        choosen_game = []
        for line in f:
            game = line.split("\t")
            if game[0] == title:
                for element in game:
                    try:
                        element = float(element)
                        if (element % round(element) == 0):
                            choosen_game.append(int(element))
                        else:
                            choosen_game.append(float(element))
                    except ValueError:
                        choosen_game.append(element.strip("\n"))             
        return choosen_game
            
def count_grouped_by_genre(file_name):
    """return a dictionary where each genre is associated 
    with the count of the games in it"""
    with open (file_name, "r") as f:
        game_genres = []
        for line in f:
            game = line.split("\t")
            game_genres.append(game[3])
        genre_dict = dict.fromkeys(game_genres,0)
        for genre in game_genres:
            if genre in genre_dict.keys():
                genre_dict[genre] += 1
        return genre_dict

def get_date_ordered(file_name):
    """returns date ordered list of the titles"""
    with open (file_name, "r") as f:
        titles = []
        release_dates = []
        for line in f:
            game = line.split("\t")
            release_dates.append((game[0],game[2]))
            release_dates = sorted(sorted(release_dates), key = lambda release_dates: release_dates[1], reverse=True)
        for game in release_dates:
            titles.append(game[0])
    return titles