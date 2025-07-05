from os import system
#system is used to execute command in terminal
system('pwd') #Here we execute command pwd

#Exercise Solution for mac os
names = ["Rahul", "Rohan", "Javed", "John", "Shah Rukh Khan", "Ritika"]
for name in names:
    system(f"say Shoutout to {name}")
    
#You can use win32 module for window os