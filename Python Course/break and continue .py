for i in range(1, 11):
    print("5 X", i, "=", 5 * i)
    if (i == 5):
        break
        
print("Loop ko chod ke nikal gaya")

for a in range(12):
    if (a == 10):
        break
    print("5 X", a+1, "=", 5 * (a+1))
        
print("Loop ko chod ke nikal gaya")

for r in range(12):
    if(r == 10):
        print("Skip the iteration")
        continue
    print("5 X", r+1, "=", 5 * (r+1))
  
d = 0
while True:
    print(d)
    d = d+1
    if(d%100 == 0):
        break