door = 0
hall = [0]*100
open_door = []
i=1
while i < 101:
        for nr in range (0,100,i):
            if hall[nr] == 1:
                hall[nr] = 0
            elif hall[nr] == 0:
                hall[nr] = 1
        i=i+1
print ("sprawdzmy:")
for nr, door in enumerate (hall):
    if door == 1:
        open_door.append(nr)
print("Otwarte sa drzwi:", open_door)
    