#Write a program which takes 6 integers a, b, c, d, e, f 
# - the coordinates of the vertices of the triangle (a, b), (c, d) and (e, f), 
# and prints the value of its area. 
# The coordinates of the vertices of the triangle are numbers in the range from -100 to 100. 

Coordinates = input("Give me 6 intigers divided by comas - coordinates of 3 verticles: x1,y1,x2,y2,x3,y3) ")
Coordinates = Coordinates.split(",")
Coordinates = [int (i) for i in Coordinates]
A = Coordinates[2] - Coordinates[0]
B = Coordinates[3] - Coordinates[1]
C = Coordinates[4] - Coordinates[0]
D = Coordinates[5] - Coordinates[1]

P2 = abs(A*D-C*B)
P=(P2)/2

if(P % round(P)):
    print ("P=", P) 
else:
    print ("P=", round(P))