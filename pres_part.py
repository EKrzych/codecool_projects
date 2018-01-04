MyList = (input("Give me your verbs separated by comas:")) 
MyList = MyList.split(",")
for item in MyList:
    if (len(item)>=3 and (item [-3] not in "a, e, i, o, u, y") and (item [-2] in "a, e, i, o, u, y") and (item [-1] not in "a, e, i, o, u, y")):
        item = item + item[-1]
    elif item.endswith("e"):
        if (item.endswith("ee")) or item == "be":
            item = item
        elif item.endswith("ie"):
            item = (str(item [:-2]) + "y")
        else:
            item = item [:-1]
    print (item + "ing")

