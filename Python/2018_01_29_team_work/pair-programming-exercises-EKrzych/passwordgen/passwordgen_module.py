import random


def passwordgen():
    chars_table = "abcdefghijklmnopqrstuwvxyz"
    numbers = "12345678901234567890123456"
    special_signes = "!@$%^&*!@$%^&*!!@$%^&*!@$%"
    generated = (chars_table[random.randint(0,25)]
                    + chars_table[random.randint(0,25)].upper()
                    + numbers[random.randint(0,25)]
                    + numbers[random.randint(0,25)]
                    + chars_table[random.randint(0,25)].upper()
                    + chars_table[random.randint(0,25)]
                    + special_signes[random.randint(0,25)]
                    + special_signes[random.randint(0,25)])     

    return generated


def main():
    passwordgen()


if __name__ == '__main__':
    main()
