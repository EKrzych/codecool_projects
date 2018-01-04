# Write a program which takes two numbers from a command line 
# and prints the greatest common divisor of them.

a = int (input("Your first number:"))
b = int (input("Your second number:"))

if a%b==0:
    print (b, "is our greatest common divisor")
else:
    while (a%b != 0):
        a,b=b,a%b 
print (b, "is our greatest common divisor")
    
