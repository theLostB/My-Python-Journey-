#This is all about how to use if else with for loop

for i in range(5):
    print(i)
else:
    print("Sorry no i")
    
for r in [ ]:
    print(r)
else:
    print("Sorry no r")

for a in range(6):
    print(a)
    if a == 4:
        break
else:
    print("Sorry no a")
    
#This is all about how to use if else with while loop
l = 1
while l<7:
    print(l)
    l = l+1
    if l == 4:
        break
else:
    print("Sorry no l")