state = input ("Would you like to use todo list? (yes/no)")
todo_list =[]
brack_list =[]
i = 0

while state == "yes":
    answer = input ("Please specify a command [list, add, mark, archive]:")
    
    if answer == "add":
        item = input ("Add an item:")
        todo_list.append (item)
        new_item = '[ ]'+ todo_list [i]
        i=i+1
        brack_list.append (new_item)
        print ("Item added.")
    if answer == "list" :
        print ("You saved the following to-do items:")
        for nr, new_item in enumerate (brack_list):
            print (nr+1, new_item)     
    if answer == "mark":
        print ("You saved the following to-do items:")
        for nr, new_item in enumerate (brack_list):
            print (nr+1, new_item)
        i_mark = int(input("Which one you want to mark as completed?"))
        new_item = ('[x]' + todo_list [int(i_mark)-1])
        brack_list[(i_mark)-1] = new_item
        print(todo_list[int(i_mark)-1], "is completed.")
    if answer == "archive":
        for new_item in brack_list[:]:
                if new_item [1] =='x':
                    brack_list.remove(new_item)
        print("All completed tasks got deleted.") 

print ("Have a nice day")