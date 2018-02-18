with open ("table.txt", "r") as f:
    table = []
    for line in f:
        table.append(line.strip("\n").strip(",").split(","))
    print(table)
    table.append(['nine', 'ten', 'eleven'])
    print(table)

with open ("table.txt", "+w") as f:
    for record in table:
        line = ",".join(record)
        f.write(line + "\n")

with open ("table.txt", "r") as f:
    table =[]
    for line in f:
        record = line.strip("\n").split(",")
        for element in record:
            table.append(element)
    print(table)

new_table = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
with open("table.txt", "+w") as f:
    string = ""
    for line in new_table:
        string += str(line[0])+","
    f.write(string + "\n")
