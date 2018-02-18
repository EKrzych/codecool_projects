"""Check how many passphrases are valid"""


def get_data():
    my_list = []
    with open("input_day_4.txt", "r") as f:
        for line in f:
            my_list.append(line.strip().split(" "))
    return my_list


def sort_letters_in_words(my_list):
    for item in my_list:
        for counter, element in enumerate(item):
            item[counter] = "".join(sorted(item[counter]))


def check_if_valid(my_list):
    valid_count = 0
    for item in my_list:
        if len(item) == len(set(item)):
            valid_count += 1
    print(valid_count)


def main():
    my_list = get_data()
    check_if_valid(my_list) #valid passphrase contain no duplicate words
    sort_letters_in_words(my_list)
    check_if_valid(my_list) #valid passphrase contain no duplicate words nor anagrams

if __name__ == "__main__":
    main()
