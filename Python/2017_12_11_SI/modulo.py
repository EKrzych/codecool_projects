# Write a program which prints the top 25 three-digit 
# natural numbers divisible by 7 or by 9. 
# Each number should be displayed in a separate line.

list =[]

for i in reversed(range(100, 1000)):
    if (i % 7 == 0) or (i % 9 == 0):
	    list.append(i)
    if len(list) == 25:
        break
for number in list:
    print (number) 
