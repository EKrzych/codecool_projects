#You have 100 doors in a hallway in a row that are all initially closed. 
# You make 100 passes by the doors. 
# The first time through, you visit every door and toggle the door 
# (if the door is closed, you open it; if it is open, you close it). 
# The second time you only visit every 2nd door (door #2, #4, #6, ...). 
# The third time, every 3rd door (door #3, #6, #9, ...), 
# etc, until you only visit the 100th door.
# Script that lists the number (the name) of the open doors 
# after you visited all the 100 doors 100 a times.

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
    