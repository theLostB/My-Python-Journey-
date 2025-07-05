a = input("Enter the number: ")
print(f"Multiplication table of {a} is")
try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)    
#if we give any word or alphabet this program throws error and the code below the multiplication table will not execute
#So by using try except code program will not throws error and code which is written after error will execute as well as
a = input("Enter the number: ")
print(f"Multiplication table of {a} is")
try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Invalid Input")    
print("Some important line of code")
print("End of program")