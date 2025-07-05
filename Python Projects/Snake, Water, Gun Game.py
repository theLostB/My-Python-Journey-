import random
uscore = 0
cscore = 0
i = 0
n = 0
print('''\t\t\tWelcome to\n \t \t Snake, Gun, Water Game''')
print("  Rules:")
print('''\tSnake beats Water\n\tWater beats Gun\n\tGun beats Snake\n\t\t\tAll Rounds: 5''')
for i in range(1,6):
    print(f"\n Round {i}")
    print(" [S] for Snake, [G] for Gun, [W] for Water and [Q] for Quit!")
    ui = input(" Enter your choice: ")
    if (ui=="S"):
        usr_cho = "Snake"
    elif (ui=="G"):
        usr_cho = "Gun"
    elif (ui=="W"):
        usr_cho = "Water"
    elif (ui=="Q"):
        print("\n Bye!!!")
        break;
    else:
        usr_cho = ui
        print("\n Wrong Entry!")
    com_cho = random.choice(["Snake","Water","Gun"])
    if(usr_cho==com_cho):
        print("\n\t Draw!")
        n = n+1
    elif(usr_cho=="Snake" and com_cho=="Water"):
        print("\n\t You Win!")
        uscore += 1
    elif(usr_cho=="Gun" and com_cho=="Snake"):
       print("\n\t You Win!")
       uscore += 1
    elif(usr_cho=="Water" and com_cho=="Gun"):
        print("\n\t You Win!")
        uscore += 1
    else:
        print("\n\t You Loose!")
        cscore += 1
    print(f"\t You choose {usr_cho}, Computer choose {com_cho}")
print(f"\n Your Score is {uscore}\n Computer Score is {cscore}\n Draw Rounds {n}")
if(uscore>cscore):
    print("\n Yeah!!! You Win the Match")
elif(uscore==cscore):
    print(" Match Draw!!!")
else:
    print("\n You Loose!! Better luck next time")