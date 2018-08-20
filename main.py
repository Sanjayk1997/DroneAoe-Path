
i = 0
while i == 0:
    choice = input("Use Video files or Assets file? (V/A) :")
    sel = choice.upper().strip().replace(" ","")
    if (sel == "A"):
        import poibased
    elif(sel == "V"):
        import dronebased
    else:
        print("Invalid Choice/n")

    tmp = input("Run Again? (Y/N) :")
    flag = tmp.upper().strip().replace(" ","")
    if (flag == "Y"):
        i = 0
    elif(flag == "N"):
        i = 1
    else:
        print("Invalid Choice/n")

print ("Terminated Successfully")
