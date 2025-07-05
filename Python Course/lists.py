marks = [3, 5, 6, "Rishaank"]
print(marks)
print(type(marks))
print((marks[0]))

print(marks[-2])#negative index
print(marks[len(marks)-2])
print(marks[3-2])
print(marks[1])#positive index

if 4 in marks:
    print("Yes")
else:
    print("No")
    
if "Rishaank" in marks:
    print("Yes")
else:
    print("No")
 
if "ank" in "Rishaank":
    print("Yes")
else:
    print("No")