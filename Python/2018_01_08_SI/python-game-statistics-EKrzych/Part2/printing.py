import reports
file_name = "game_stat.txt"
title = "Diablo II"

def printing_get_most_played(file_name):
    """prints the title of the most played game"""
    result = reports.get_most_played(file_name)
    print (result, "is the most played game.")
    print()

def printing_sum_sold(file_name):
    """prints total number of copies sold"""
    result = reports.sum_sold(file_name)
    print (result, "is the total number of copies sold.")
    print()

def printing_get_selling_avg(file_name):
    """prints average selling"""
    result = reports.get_selling_avg(file_name)
    print ("Average selling is", result)
    print()

def printing_count_longest_title(file_name):
    """prints number of characters in the longest title"""
    result = reports.count_longest_title(file_name)
    print ("Number of characters in the longest title is:", result)
    print()

def printing_get_date_avg(file_name):
    """prints average selling date"""
    result = reports.get_date_avg(file_name)
    print ("The average selling date is:", result)
    print()

def printing_get_game(file_name, title):
    """prints properties of choosen game"""
    result = reports.get_game(file_name, title)
    print("The properties of choosen game are:")
    for i in result:
        print(" ", i, end=", ")
    print("(title, total copies sold (million), release date, genre, publisher)")
    print()

def printing_count_grouped_by_genre(file_name):
    """prints a dictionary where each genre is associated 
    with the count of the games of its genre"""
    result = reports.count_grouped_by_genre(file_name)
    print ("The number of games in genres are:")
    for k in result:
        print(k, ":", result[k])
    print()

def printing_get_date_ordered(file_name):
    """returns date ordered list of the titles"""
    result = reports.get_date_ordered(file_name)
    print ("Date ordered (descending) list of titles:")
    for nr, game in enumerate(result, 1):
        print (nr, ".", game)
    print()


def main():
    print()
    printing_get_most_played(file_name)
    printing_sum_sold(file_name)
    printing_get_selling_avg(file_name)
    printing_count_longest_title(file_name)
    printing_get_date_avg(file_name)
    printing_get_game(file_name, title)
    printing_count_grouped_by_genre(file_name)
    printing_get_date_ordered(file_name)


if __name__ == '__main__':
    main()