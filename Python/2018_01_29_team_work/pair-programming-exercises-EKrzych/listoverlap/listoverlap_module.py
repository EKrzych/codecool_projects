def listoverlap(list1, list2):
    list3 = []
    for item in list1:
        if item in list2 and item not in list3:
            list3.append(item)
    print(list3)
    return list3


def main():
    list1= [1, 1]
    list2= [1, 0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 2]
    
    
    return listoverlap(list1, list2)


if __name__ == '__main__':
    main()
