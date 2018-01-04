
questions = ["would you like to use sauna(yes/no)?", "Are you a student?(yes/no)", "Are you a woman?(yes/no)"]
answers = ["You should pay: 1500 HUF","You should pay: 300 HUF", "You should pay: 500 HUF", "You should pay: 750 HUF"]
def checking_age():
    try:
        age = int(input ("how old are you?Please give me intiger!"))
    except ValueError:
        print("You were supposed to give me an int!!")
        
user_input = checking_age()
if user_input >= 14:
    a = 0
    question_number = len(questions)
    while a < question_number:
        user_input = input (questions[a])
        if user_input == "yes":
            print (answers[a])
            break
        a = a + 1  
    if a == question_number:
        print (answers[a])
else:
    print ("You are too young!")


