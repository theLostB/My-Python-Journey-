f = open('Marks.txt', 'r')
i = 0
while True:
    i += 1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(',')[0])
    m2 = int(line.split(',')[1])
    m3 = int(line.split(',')[2])
    print(f"Marks of Student {i} in Maths is {m1*2}\n")   
    print(f"Marks of Student {i} in English is {m2*2}\n")   
    print(f"Marks of Student {i} in SST is {m3*2}\n")   