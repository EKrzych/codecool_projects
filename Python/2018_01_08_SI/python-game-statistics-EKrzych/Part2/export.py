import reports
file_name = "game_stat.txt"
title = "Diablo II"

def writing_get_most_played(file_name):
    """writes down the title of the most played game"""
    result = str(reports.get_most_played(file_name))
    with open ("report_for_judy_part2.txt", "+a") as f:
        f.write(result)
        f.write("\n")
    
def writing_sum_sold(file_name):
    """writes total number of copies sold"""
    result = str(reports.sum_sold(file_name))
    with open ("report_for_judy_part2.txt", "+a") as f:
        f.write(result)
        f.write("\n")

def writing_get_selling_avg(file_name):
    """writes average selling"""
    result = str(reports.get_selling_avg(file_name))
    with open ("report_for_judy_part2.txt", "+a") as f:
        f.write(result)
        f.write("\n")

def writing_count_longest_title(file_name):
    """writes number of characters in the longest title"""
    result = str(reports.count_longest_title(file_name))
    with open ("report_for_judy_part2.txt", "+a") as f:
        f.write(result)
        f.write("\n")

def writing_get_date_avg(file_name):
    """writes average selling date"""
    result = str(reports.get_date_avg(file_name))
    with open ("report_for_judy_part2.txt", "+a") as f:
        f.write(result)
        f.write("\n")

def writing_get_game(file_name, title):
    """writes properties of choosen game"""
    result = str(reports.get_game(file_name, title))
    with open ("report_for_judy_part2.txt", "+a") as f:
        f.write(result)
        f.write("\n")
    
def writing_count_grouped_by_genre(file_name):
    """writes a dictionary where each genre is associated 
    with the count of the games of its genre"""
    result = str(reports.count_grouped_by_genre(file_name))
    with open ("report_for_judy_part2.txt", "+a") as f:
        f.write(result)
        f.write("\n")

def writing_get_date_ordered(file_name):
    """returns date ordered list of the titles"""
    result = str(reports.get_date_ordered(file_name))
    with open ("report_for_judy_part2.txt", "+a") as f:
        f.write(result)
        f.write("\n")

def cleaning_file():
    """cleans the content of report_for_judy.txt"""
    f = open ("report_for_judy_part2.txt", "w")
    f.close()

def main():
    cleaning_file()
    writing_get_most_played(file_name)
    writing_sum_sold(file_name)
    writing_get_selling_avg(file_name)
    writing_count_longest_title(file_name)
    writing_get_date_avg(file_name)
    writing_get_game(file_name, title)
    writing_count_grouped_by_genre(file_name)
    writing_get_date_ordered(file_name)


if __name__ == '__main__':
    main()
