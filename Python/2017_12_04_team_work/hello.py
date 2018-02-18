# Create a script file that welcomes the user given to it. 
# If no name was given, then it welcomes the whole world.
# Name is provided as the command line argument of the script.

import sys
if((len(sys.argv))>1):
    print ("Hello", sys.argv[1])
else:
    print ("Hello world")
