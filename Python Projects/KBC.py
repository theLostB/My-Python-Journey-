questions = [
    ["Who is the father of python","Tim berners lee","Bill Gates","Guido Van Rossum","Mark Zuckerberg"],
    ["Who is the father of python","Tim berners lee","Bill Gates","Guido Van Rossum","Mark Zuckerberg"],["Who is the father of python","Tim berners lee","Bill Gates","Guido Van Rossum","Mark Zuckerberg"],
    ["Who is the father of python","Tim berners lee","Bill Gates","Guido Van Rossum","Mark Zuckerberg"],["Who is the father of python","Tim berners lee","Bill Gates","Guido Van Rossum","Mark Zuckerberg"],
        ["Who is the father of python","Tim berners lee","Bill Gates","Guido Van Rossum","Mark Zuckerberg"],
    ["Who is the father of python","Tim berners lee","Bill Gates","Guido Van Rossum","Mark Zuckerberg"],["Who is the father of python","Tim berners lee","Bill Gates","Guido Van Rossum","Mark Zuckerberg"],
    ["Who is the father of python","Tim berners lee","Bill Gates","Guido Van Rossum","Mark Zuckerberg"],["Who is the father of python","Tim berners lee","Bill Gates","Guido Van Rossum","Mark Zuckerberg"]]

levels = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
i = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\nQuestion for Rs. {levels[i]}")
    print(question[0])
    print(f"a. {question[1]}          b. {question[2]}")
    print(f"c. {question[3]}          d. {question[4]}")
    reply = int(input("Enter your answer (1-4) or 0 for quit "))
    if (reply == 0):
        money = levels[i-1]
        break
    if (reply == 3):
        print(f"Correct answer, you have won {levels[i]}")
        if (i == 4):
            money = 10000
        elif (i == 9):
            money = 320000
        elif (i == 14):
            money = 1000000
    else:
         print("Wrong answer!")
print(f"Your take home money is {money}")