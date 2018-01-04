def sorting (List):
    i=1
    while i < len(List):
        j=0
        while j<=(len(List)-2):
            if List[j] > List[j+1]:
                temp = List[j+1]
                List[j+1] = List[j]
                List[j] = temp
            j=j+1
        i=i+1

Numbers = input("Give me your numbers (separated by comas):")
Numbers = Numbers.split(",")
Numbers = [int (i) for i in Numbers]
print (Numbers)
sorting (Numbers)
print (Numbers)