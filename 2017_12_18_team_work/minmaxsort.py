list =[-5, 23, 0, "dupa", -9, 12, 99, [2, 44], none, 105, -43]

def create_list_int(list):
    for ii

#Numbers = [-5, 23, 0, -9, 12, 99, 105, -43]
def min_max(Numbers):
    i=1
    while i < len(Numbers):
        j=0
        while j<=(len(Numbers)-2):
            if Numbers[j] > Numbers[j+1]:
                temp = Numbers[j+1]
                Numbers[j+1] = Numbers[j]
                Numbers[j] = temp
            j=j+1
        i=i+1

def avg (Numbers):
    suma = 0
    i=0
    while i<len(Numbers):
        suma=+Numbers[i]
        i+=1
    return suma/len(Numbers)
    

print(Numbers)
min_max(Numbers)
print ("Min value in Numbers is ", Numbers[0], "Max value in Numbers is ", Numbers[len(Numbers)-1])
average = avg(Numbers)
print ("Avarage in Numbers is ", average)
