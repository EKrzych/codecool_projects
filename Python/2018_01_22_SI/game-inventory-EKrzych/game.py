def print_intro():
    print()
    print("You are a mighty warrior who wants to kill dragon.")
    print("You can buy things from blacksmith.")
    print("If you have lost all your gold maybe doctor can help.")


def handle_blacksmith():
    inventory = import_inventory_game(filename="export_inventory.csv")
    items_to_sell = {"magic sword": {"gold coin": 30, "dagger": 1}, "treasure bag" : {"gold coin": 15, "arrow": 3}}
    answer = input("Hello, I'm a blacksmith. Would you like to buy something?(y/n)")
    if answer.lower() == "y" or answer.lower() == "yes":
        answer = print_nested_dictionary(items_to_sell)
        if answer in items_to_sell:
            inventory = check_wheather_can_buy(answer, inventory, items_to_sell)  
        else: 
            print("I don't have it! Stop wasting my time!!")
    else: 
            print("Stop wasting my time!!")
    return inventory


def handle_dragon():
    inventory = import_inventory_game(filename="export_inventory.csv")
    if "magic sword" in inventory:
        return False
    else:
        return True

def handle_dragon_loot(inventory):
    dragon_loot = ['pot', 'dagger', 'gold coin', 'gold coin', 'ruby']
    print("You have killed the dragon!")
    print("But you are wounded go to doctor and buy some medicine!")
    inventory = add_to_inventory(inventory, dragon_loot)
    del inventory["magic sword"]
    return inventory


def teasing_dragon(inventory):
    print("Stop teasing the dragon. You need magic sword!")
    print("Dragon has stolen your 5 coins!")
    inventory["gold coin"] -= 10
    return inventory


def handle_doctor():
    inventory = import_inventory_game(filename="export_inventory.csv")
    items_to_sell = {"magic cure": {"pot": 1, "ruby": 1}, "hot wine": {"gold coin": 5}}
    answer = input("Hello, I'm a doctor. Would you like to buy something ?(y/n)")

    if answer.lower() == "y" or answer.lower() == "yes":
        answer = print_nested_dictionary(items_to_sell)
        if answer in items_to_sell:
            inventory = check_wheather_can_buy(answer, inventory, items_to_sell)  
        else: 
            print("I don't have it! Stop wasting my time!!")

    else: 
        answer = input("Would you like to sell me some blood fo 10 gold coins?(y/n)")
        if answer.lower() == "y" or answer.lower() == "yes":
            inventory["gold coin"] += 10
        else: 
            print("Stop wasting my time!!")
        
    return inventory
    
def check_wheather_can_buy(answer, inventory, items_to_sell):
    for inner_key in items_to_sell[answer]:
        if inner_key in inventory:
            if inventory[inner_key] >= items_to_sell[answer][inner_key]:
                inventory[inner_key] -= items_to_sell[answer][inner_key]  
            else: 
                print("You are to poor.")
                return inventory
        else: 
            print("You are to poor. Stop wasting my time!!")
            return inventory
    inventory[answer] = 1
    print("You have bought {}.".format(answer))
    return inventory


def print_nested_dictionary(items_to_sell):
    """Print items to sell and return answer 
    for question:which item would you like to buy?
    """

    print("Here's what I have and the price of it:")
    for item, price in items_to_sell.items():
        print (item,"will cost:")
        for k,v in price.items():
            print("\t", v, k)

    return input("Which item would you like to buy?")


def choose_NPC_to_meet():
    NPC = ["Dragon", "Blacksmith", "Doctor"]
    for index, item in enumerate(NPC, 1):
        print ("(", index, ")", item)

    return input("Who would you like to meet with(choose number)?")
    


def import_inventory_game(filename="export_inventory.csv"):
    with open (filename, "r") as f:
        for line in f:
            added_items = line.split(",")
        inventory ={}
        for item in added_items:
            inventory.setdefault(item, 0)
            inventory[item] += 1
        return inventory

def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""

    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    
    return inventory