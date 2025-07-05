f = open('myfile.txt', 'r') #We have to give here two arguments first is the file name second is in which mode we want to open the file default is r means reading mode , and w for writing and similarly a for appending extra content in a existing content and x for creating new file and rb for opening the file in binary file. 
text = f.read()
print(text)
f.close()
#Write mode erase the all file content and write what we want to write And if the file is not exist in which we want to write than its creates the file.
w = open('Myfile.txt2', 'w')
wr = w.write('Heybro you are awesome yrr!!!')
w.close()#here we create new file by using w mode and also write some text

a = open('Myfile2.txt', 'a')
ap = a.write(" We append this text using a mode...")
a.close()

#Here we used with and as This statements doesn't need to close the file again after opening it, And this will exactly work fine
with open('Myfile2.txt', 'r') as o:
    op = o.read()
    print(op)
