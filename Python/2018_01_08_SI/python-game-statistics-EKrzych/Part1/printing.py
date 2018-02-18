import reports

file_name = "game_stat.txt"
year = 2000
title = "Minecraft"
genre = "RPG"

def printing_count_games(file_name):
    """prints number of games in file"""
    result = reports.count_games(file_name)
    print ("There are", result, "games listed in file", file_name)
    print()

def printing_decide(file_name, year):
    """prints answer for question: is there a game from a given year?"""
    result = reports.decide(file_name, year)
    if result:
        print ("There is a game from", year, "year.")
    else:
        print ("There is not a game from", year, "year.")
    print()

def printing_get_latest(file_name):
    """prints title of the latest game"""
    result = reports.get_latest(file_name)
    print (result, "is the latest game.")
    print()

def printing_count_by_genre(file_name, genre):
    """prints answer for question: How many games do we have by genre?"""
    result = reports.count_by_genre(file_name, genre)
    print ("We have", result, genre, "games.")
    print()

def printing_get_line_number_by_title(file_name, title):
    """prints line number of the given game (by title)"""
    try:
        result = reports.get_line_number_by_title(file_name, title)
        print ("The line number of", title, "is", result, ".")
    except ValueError:
            print("There's no such title in file.")
    print()

def printing_sort_abc(file_name):
    """prints alphabetical ordered list of the titles"""
    result = reports.sort_abc(file_name)
    print ("The ordred list of titles:")
    for nr, game in enumerate(result, 1):
        print ("    ", nr, game)
    print()

def printing_get_genres(file_name):
    """prints set of the genres (alphabetical order)"""
    result = reports.get_genres(file_name)
    print ("The ordred list of genres:")
    for nr, genre in enumerate(result, 1):
        print ("    ", nr, genre)
    print()

def printing_when_was_top_sold_fps(file_name):
    """prints year of the release top sold "First-person shooter game"""
    try:
        result = reports.when_was_top_sold_fps(file_name)
        print ("The year of release First-person shooter is: ", result)
    except ValueError:
        print ("There is no game with genre 'First-person shooter'")
    print()


def main():
    print()
    printing_count_games(file_name)
    printing_decide(file_name, year)
    printing_get_latest(file_name)
    printing_count_by_genre(file_name, genre)
    printing_get_line_number_by_title(file_name, title)
    printing_sort_abc(file_name)
    printing_get_genres(file_name)
    printing_when_was_top_sold_fps(file_name)

if __name__ == '__main__':
    main()