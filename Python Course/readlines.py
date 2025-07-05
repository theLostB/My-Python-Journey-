f = open('readlines.txt', 'r')
#Readlines helps us to print the content of file line by line 
while True:
    line = f.readline()
    if not line:
        break
    print(line)