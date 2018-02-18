# Write the anagram recogniser that accepts a file name from the user provided as the command line argument 
# of the script, reads each line of that file, 
# and displays in separated lines those pairs of word which are anagrams.

import sys
file_object = open (sys.argv[1], "r")
MyList=[]
MyList = (file_object.readlines())
MyList = sorted(MyList)
i=0
for word in MyList:
    a=i+1
    while (a < (len(MyList))):
        if(word) != MyList[a]:
            if (sorted(word)) == (sorted(MyList[a])):
                print (word [:-1], "-", (MyList[a]))
        a=a+1
i=i+1
