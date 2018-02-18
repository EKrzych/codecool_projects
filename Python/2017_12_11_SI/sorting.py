#This is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order.
# Implement the algorithm described by the flowchart in Python!
# Structure your code: separate some logic into functions.
# Modify your program so ask the user to give the list of numbers.

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