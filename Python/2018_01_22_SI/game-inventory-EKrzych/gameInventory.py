import game
import os


def display_inventory(inventory):
    print ("Inventory: ")

    for k, v in inventory.items():
        print ("\t", v, k)
    items_count = counting_items(inventory)
    print ("Total number of items: ",  items_count)


def counting_items(inventory):
    items_count = 0

    for k, v in inventory.items():
        items_count += int(v)

    return items_count


def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""

    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    
    return inventory


def print_header(inventory_list_header, max_lenght_list):
    additional_space = 3
    width_of_table = sum(max_lenght_list) + additional_space

    for item in inventory_list_header:
        for index, element in enumerate(item):
            print (" "*(max_lenght_list[index] - len(item[index])),"{}".format(item[index]), sep=" ", end=" ")
    
    print()
    print ("-"*width_of_table)


def sorting_inventory(inventory_list,order):
    """ 
    "count,desc" means the table is ordered by count 
    (of items in the inventory)in descending order.
    "count,asc" means the table is ordered by count in ascending order
    """

    if order == "count,desc":
        inventory_list = sorted(inventory_list, key = lambda item: int(item[0]), reverse = True)
    elif order == "count,asc":
        inventory_list = sorted(inventory_list, key = lambda item: int(item[0]), reverse = False)

    return inventory_list


def print_table(inventory, inventory_list_header, max_lenght_list, order=None):
    print()
    additional_space = 3
    inventory_list = change_inventory_dict_into_list(inventory)
    width_of_table = sum(max_lenght_list) + additional_space

    if order != None:
        inventory_list = sorting_inventory(inventory_list,order)

    print("Inventory: ")
    print_header(inventory_list_header, max_lenght_list)

    for item in inventory_list:
        for index, element in enumerate(item):
            print (" "*(max_lenght_list[index] - len(item[index])),"{}".format(item[index]), sep=" ", end=" ")
        print()

    print ("-"*width_of_table)
    print ("Total number of items: ",  counting_items(inventory))


def change_inventory_dict_into_list(inventory):
    """change_inventory_dict_into_list and reverse key with value"""
    inventory_list = []
    for k, v in inventory.items():
        inventory_list.append([str(v), str(k)])

    return inventory_list


def find_max_lenght_of_column(inventory, inventory_list_header):
    max_lenght_list = []
    inventory = change_inventory_dict_into_list(inventory)

    for i in range(len(inventory_list_header[0])):
        max_lenght_inventory = max(inventory, key = lambda item: len(item[i]))
        max_lenght_header = max(inventory_list_header, key = lambda item: len(item[i]))
        max_lenght_inventory_header = max(len(max_lenght_inventory[i]),len(max_lenght_header[i]))
        max_lenght_list.append(max_lenght_inventory_header)

    return max_lenght_list


def import_inventory(inventory, filename="import_inventory.csv"):
    """Imports new inventory items from a file and merges it with given one"""
    with open (filename, "r") as f:
        for line in f:
            added_items = line.split(",")

        return add_to_inventory(inventory, added_items) 


def changeing_dict_into_string(inventory):
    inventory_list = change_inventory_dict_into_list(inventory)
    string = ""

    for item in inventory_list:
        string += (item[1]+",") * int(item[0])

    return string.strip(",").replace("\t", "   ").replace("\n", "\\n").replace("\32", " ")


def export_inventory(inventory, filename="export_inventory.csv"):
    inventory_string = changeing_dict_into_string(inventory)
    with open (filename, "+w") as f:
        f.write(inventory_string)


def prepare_inventory_for_new_game(inventory):
    """
        Import inventory from file "import_inventory.csv",
        join it with given in main function 
        and export to file: "export_inventory.csv"
    """
    inventory = import_inventory(inventory, filename="import_inventory.csv")
    export_inventory(inventory, filename="export_inventory.csv")
    return inventory


def main():
    os.system('clear')
    game.print_intro()
    inventory_list_header =[["count", "item name"]]
    inventory = {'rope': 1, 'ruby': 6, 'gold coin': 20, 'dagger': 1, 'arrow': 12, 'trouvé': 12} 
    inventory = prepare_inventory_for_new_game(inventory)

    wounded = False
    dragon_alive = True

    while dragon_alive == True or wounded == True:

        inventory = game.import_inventory_game(filename="export_inventory.csv")
        max_lenght_list = find_max_lenght_of_column(inventory, inventory_list_header)
        print_table(inventory, inventory_list_header, max_lenght_list)
        answer = int(game.choose_NPC_to_meet())
        print()

        if answer == 1:
            dragon_alive = game.handle_dragon()
            if dragon_alive == False:
                wounded = True
                inventory = game.handle_dragon_loot(inventory) 
            else: 
                inventory = game.teasing_dragon(inventory)
            export_inventory(inventory, filename="export_inventory.csv")

        elif answer == 2:
            inventory = game.handle_blacksmith()
            export_inventory(inventory, filename="export_inventory.csv")

        elif answer ==3:
            inventory = game.handle_doctor()
            if "magic cure" in inventory:
                wounded = False
            export_inventory(inventory, filename="export_inventory.csv")

        else:
            print("There is no such person in town. Try again")
    
    print("You have killed the dragon and healed your wounds. Game over")
    
        
if __name__ == '__main__':
    main()