import reports

file_name = "game_stat.txt"
year = 1999
title = "Diablo III"
genre = "RPG"

def writing_count_games(file_name):
    """Writes down number of games in file"""
    result = str(reports.count_games(file_name))
    with open ("report_for_judy.txt", "+a") as f:
        f.write(result)
        f.write("\n")
        
def writing_decide(file_name, year):
    """Writes down answer for question: is there a game from a given year?"""
    result = str(reports.decide(file_name, year))
    with open ("report_for_judy.txt", "+a") as f:
        f.write(result)
        f.write("\n")

def writing_get_latest(file_name):
    """writes down title of the latest game as a string"""
    result = str(reports.get_latest(file_name))
    with open ("report_for_judy.txt", "+a") as f:
        f.write(result)
        f.write("\n")

def writing_count_by_genre(file_name, genre):
    """writes down answer for question: How many games do we have by genre?"""
    result = str(reports.count_by_genre(file_name, genre))
    with open ("report_for_judy.txt", "+a") as f:
        f.write(result)
        f.write("\n")

def writing_get_line_number_by_title(file_name, title):
    """writes down line number of the given game (by title)"""
    with open ("report_for_judy.txt", "a") as f:
        try:
            result = str(reports.get_line_number_by_title(file_name, title))
            f.write(result)
            f.write("\n")
        except ValueError:
                f.write("There's no such title in file.")
                f.write("\n")

def writing_sort_abc(file_name):
    """writes  down alphabetical ordered list of the titles"""
    result = str(reports.sort_abc(file_name))
    with open ("report_for_judy.txt", "a") as f:
        f.write(result)
        f.write("\n")

def writing_get_genres(file_name):
    """writes down list of the genres (without duplicates, in alphabetical order)"""
    result = str(reports.get_genres(file_name))
    with open ("report_for_judy.txt", "a") as f:
        f.write(result)
        f.write("\n")

def writing_when_was_top_sold_fps(file_name):
    """writes down year of the release top sold "First-person shooter game"""
    with open ("report_for_judy.txt", "a") as f:
        try:
            result = str(reports.when_was_top_sold_fps(file_name))
            f.write(result)
            f.write("\n")
        except ValueError:
            f.write ("There is no game with genre 'First-person shooter'")
            f.write("\n")

def cleaning_file():
    """cleans the content of report_for_judy.txt"""
    f = open ("report_for_judy.txt", "w")
    f.close()

def main():
    cleaning_file()
    writing_count_games(file_name)
    writing_decide(file_name, year)
    writing_get_latest(file_name)
    writing_count_by_genre(file_name, genre)
    writing_get_line_number_by_title(file_name, title)
    writing_sort_abc(file_name)
    writing_get_genres(file_name)
    writing_when_was_top_sold_fps(file_name)

if __name__ == '__main__':
    main()
