# Write a program which takes a natural number 
# (written in Arabic numerals, greater than zero and less than 4000), 
# and then prints it in Roman form.

Number = int (input("What's your number?"))
RomanNumber = ""
Arabic = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
Symbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
a = 0
while Number != 0:
    while (Number) >= Arabic[a]:
        RomanNumber = RomanNumber+Symbols[a]
        Number = Number - Arabic[a]
    a=a+1
print (RomanNumber)
