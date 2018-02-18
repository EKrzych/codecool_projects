def get_albums_by_genre(albums, genre):
    """
    Get albums by genre

    :param list albums: albums' data
    :param str genre: genre to filter by


    :returns: all albums of given genre
    :rtype: list
    """

    genre_list = [row for row in albums if row[3] == genre]

    if len(genre_list) == 0:
        raise ValueError("Wrong genre does not match")

    return genre_list


def get_genre_stats(albums):
    """
    Get albums' statistics showing how many albums are in each genre
    Example: { 'pop': 2, 'hard rock': 3, 'folk': 20, 'rock': 42 }

    :param list albums: albums' data
    :returns: genre stats
    :rtype: dict
    """
    genre_dict = {}
    for row in albums:
        genre_dict.setdefault(row[3],0)
        genre_dict[row[3]] += 1

    return genre_dict


def get_oldest(albums):
    oldest = int(albums[0][2])
    for counter, row in enumerate(albums[1:]):
        if int(oldest) > int(row[2]):
            oldest = int(row[2])
    return oldest


def get_last_oldest(albums):
    """
    Get last album with earliest release year.
    If there is more than one album with earliest release year return the last
    one of them (by original list's order)

    :param list albums: albums' data
    :returns: last oldest album
    :rtype: list
    """
    oldest = get_oldest(albums)
    oldest_list = [record for record in albums if int(record[2]) == int(oldest)]
    return oldest_list[-1]


def get_last_oldest_of_genre(albums, genre):
    """
    Get last album with earliest release year in given genre

    :param list albums: albums' data
    :param str genre: genre to filter albums by
    :returns: last oldest album in genre
    :rtype: list
    """
    genre_list = get_albums_by_genre(albums, genre)
    oldest = get_last_oldest(genre_list)
    return oldest


def get_longest_album(albums):
    """
    Get album with biggest value in length field

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """
    time_list = []
    for counter, row in enumerate(albums):
        temp_time = row[4].split(":")
        time_list.append(int(temp_time[0])*60 + int(temp_time[1]))
    
    longest = max(time_list)
    for counter, row in enumerate(time_list):
        if time_list[counter] == longest:
            longest_index = counter
    
    return albums[longest_index]


def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18

    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """
    time_list = []

    for counter, row in enumerate(albums):
        temp_time = row[4].split(":")
        time_list.append(int(temp_time[0])*60 + int(temp_time[1]))

    total_time_sec = sum(time_list)
    time_min = round(total_time_sec/60,2)

    return time_min