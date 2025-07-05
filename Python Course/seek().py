with open('seekfile.txt', 'r') as f:
    f.seek(10) #seek function is used to move the current position within a file to specific poin. #here I move 10 character/bytes
    data = f.read(5)
    print(data)