f = open("Myfile0.1.txt", 'w')
lines = ['line 1\n','line 2\n','line 3\n']
f.writelines(lines)
f.close()

rt = open("Myfile0.1.txt", 'r')
while True:
    rd = rt.readline()
    if not rd:
        break
    print(rd)