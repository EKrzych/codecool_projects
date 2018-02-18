import sys

def get_input():
    new_idea = input("What is your new idea: ")
    return new_idea

def write_into_file(new_idea):
    with open("Ideabank.txt", "a") as f:
        f.write(new_idea + "\n")

def get_data():
    idea_list = []
    with open("Ideabank.txt", "r") as f:
        for line in f:
            idea_list.append(line.strip())
    return idea_list

def print_list(idea_list):
    print("Your ideabank:")
    for counter, item in enumerate(idea_list,1):
        print(counter,".", item)

def write_list_into_file(idea_list):
    with open("Ideabank.txt", "w") as f:
        f.write("\n".join(idea_list))



def main():
    if len(sys.argv)>1 and sys.argv[1] == "--list":
        idea_list = get_data()
        print_list(idea_list)
    elif len(sys.argv)>1 and sys.argv[1] == "--delete":
        idea_list = get_data()
        del idea_list[int(sys.argv[2])-1]
        write_list_into_file(idea_list)
        idea_list = get_data()
        print_list(idea_list)
    else:
        new_idea = get_input()
        write_into_file(new_idea)
        idea_list = get_data()
        print_list(idea_list)

if __name__ == "__main__":
    main()

