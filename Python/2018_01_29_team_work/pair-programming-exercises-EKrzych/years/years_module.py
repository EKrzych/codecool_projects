import datetime

def years(age):
    currentYear = datetime.datetime().now().year
    return (100 - age + currentYear)


def main():
    age = int(input("How old are you? "))
    print(years(age))


if __name__ == '__main__':
    main()
