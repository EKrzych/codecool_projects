def fibonacci():
    a = 0
    b = 1
    count_fib = int(input("How many fib numbers would you like to print?"))
    fib_list = ["0","1"]
    for i in range(count_fib-2):
        a, b = b, a+b
        fib_list.append(str(b))
    spaces = len(fib_list[count_fib-2])
    for counter, item in enumerate(fib_list,1):
        print("{:>3}.".format(counter)+(" "*(spaces-len(item)))+item)
      
fibonacci()