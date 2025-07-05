with open('SampleFile.txt', 'w') as f:
    data = f.write('Hello World!')
    f.truncate(5) #truncate specifies that how many characters should be in a file , here we specify 5 character so if we print we will get only 5 characters of the start
    
with open('SampleFile.txt', 'r') as f:
    data = f.read()
    print(data)