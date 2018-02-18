import random
def choose_number():
    return random.randint(1,6)

def create_count_def_and_att():
    is_valid_a = True
    while is_valid_a:
        is_valid_a = False
        answer_a = input("How many units attack:(1,2,3)? ")
        if answer_a == "1" or answer_a == "2" or answer_a == "3":
            pass
        else:
            is_valid_a = True
    is_valid_d = True
    while is_valid_d:
        is_valid_d = False
        answer_d = input("How many units defend:(1,2)? ")
        if answer_d == "1" or answer_d == "2":
            pass
        else:
            is_valid_d = True
    return int(answer_a), int(answer_d)

def create_players(attacker_count,defender_count):
    attacker = []
    defender = []
    for i in range(attacker_count):
        attacker.append(choose_number())
    for i in range(defender_count):
        defender.append(choose_number())
    return sorted(attacker, reverse=True),sorted(defender, reverse=True)

def check_who_won(attacker,defender):
    atacker_loses = 0
    defender_loses = 0 
    for a,d in zip(attacker,defender):
        if a > d:
            defender_loses += 1
        else:
            atacker_loses += 1
    return atacker_loses, defender_loses

def change_into_str(attacker,defender):
    attacker_str = [str(item) for item in attacker]
    defender_str = [str(item) for item in defender]
    return attacker_str, defender_str

def print_output(attacker_str,defender_str):
    print("Dice: ")
    print("\tAttacker:", "-".join(attacker_str))
    print("\tDefender:", "-".join(defender_str))

def print_outcom(atacker_loses, defender_loses):
    print("Outcome: ")
    print("\tAttacker: Lost {} units".format(atacker_loses))
    print("\tDefender: Lost {} units".format(defender_loses))

def main():
    attacker_count,defender_count = create_count_def_and_att()
    attacker,defender = create_players(attacker_count,defender_count)
    attacker_str,defender_str = change_into_str(attacker,defender)
    print_output(attacker_str,defender_str)
    atacker_loses, defender_loses = check_who_won(attacker,defender)
    print_outcom(atacker_loses, defender_loses)


if __name__ == "__main__":
    main()


