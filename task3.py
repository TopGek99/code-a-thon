task2file = open("task2.txt","r")
p1_names = []
p2_names = []
p3_names = []
r_names = []
exec(task2file.read())
option = input("1. Present all P1\n2. Present all P2\n3. Present all P3\n4. Present all R\n5. How many businesses do you want to invest in\n6. Terminate\nWhich option do you want to see: ")
while option != '6':
    if option == '1':
        if len(p1_names) != 0:
            print(*p1_names, sep='\n')
        else:
            print("No startup satisfied requirement for P1 ratings.")
    elif option == '2':
        if len(p2_names) != 0:
            print(*p2_names, sep='\n')
        else:
            print("No startup satisfied requirement for P2 ratings.")
    elif option == '3':
        if len(p3_names) != 0:
            print(*p3_names, sep='\n')
        else:
            print("No startup satisfied requirement for P3 ratings.")
    elif option == '4':
        if len(r_names) != 0:
            print(*r_names, sep='\n')
        else:
            print("No startup satisfied requirement for R ratings.")
    elif option == '5':
        if len(p1_names) != 0:
            print(*p1_names, sep=',P1\n', end=',P1\n')
        elif len(p2_names) != 0:
            print(*p2_names, sep=',P2\n', end=',P2\n')
        elif len(p3_names) != 0:
            print(*p3_names, sep=',P3\n', end=',P3\n')
        else:
            print("No startup worth investing in.")
    option = input("1. Present all P1\n2. Present all P2\n3. Present all P3\n4. Present all R\n5. How many businesses do you want to invest in\n6. Terminate\nWhich option do you want to see: ")