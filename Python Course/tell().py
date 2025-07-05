with open('seekfile.txt', 'r') as f:
    f.seek(2)
    current_position = f.tell() 
    #tell() function return the current position within the file OR we can say it returns how many time seek is there 
    print(current_position)