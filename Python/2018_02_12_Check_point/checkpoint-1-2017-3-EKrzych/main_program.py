"""
The main program should use functions from music_reports and display modules
"""
import file_handling
import display
import music_reports
import sys

def delete_album_by_artist_and_album_name(albums, artist, album_name):
    """
    Deletes album of given name by given artist from list and updates data file

    :param list albums: currently existing albums
    :param str artist: artist who recorded the album
    :param str album_name: name of album to be deleted

    :returns: updated albums' list
    :rtype: list
    """
    for counter, record in enumerate(albums):
        if record[0] == artist and record[1] == album_name:
            del albums[counter]
    file_handling.export_data(albums, filename='albums_data.txt', mode='w')
    return albums

def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should repeat displaying menu and asking for
    input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """
    menu_commands = ["Delete album", 
                    "Get albums by genre",
                    "How many albums are in each genre",
                    "Get last album with earliest release year",
                    "Get last album with earliest release year in given genre",
                    "Get longest album",
                    "Get sum of lengths of all albums in minutes",
                    "Quit program"]

    while True:
        albums_data = file_handling.import_data(filename='albums_data.txt')
        display.print_command_result("Choose your option:")
        display.print_program_menu(menu_commands)
        choice = input("What would you like to do? ")
        if choice == "0":
            display.print_albums_list(albums_data)
            artist = input("Which artist would you like to remove?")
            album_name = input("Which album would you like to remove?")
            delete_album_by_artist_and_album_name(albums_data, artist, album_name)
        elif choice == "1":
            genre = input("Which genre would you like to check?")
            try:
                genre_list = music_reports.get_albums_by_genre(albums_data, genre)
                display.print_albums_list(genre_list)
            except ValueError:
                display.print_command_result("Wrong genre does not match")

        elif choice == "2":
            message = str(music_reports.get_genre_stats(albums_data))
            display.print_command_result(message)

        elif choice == "3":
            oldest = music_reports.get_last_oldest(albums_data)
            display.print_album_info(oldest)

        elif choice == "4":
            genre = input("Which genre would you like to check?")
            try:
                oldest_from_genre = music_reports.get_last_oldest_of_genre(albums_data, genre)
                display.print_album_info(oldest_from_genre)
            except ValueError:
                display.print_command_result("Wrong genre does not match")

        elif choice == "5":
            longest = music_reports.get_longest_album(albums_data)
            display.print_album_info(longest)

        elif choice == "6":
            message = str(music_reports.get_total_albums_length(albums_data))
            display.print_command_result(message)

        elif choice == "7":
            sys.exit()
            
        else:
            display.print_command_result("There's no such option. Try again.")


if __name__ == '__main__':
    main()
