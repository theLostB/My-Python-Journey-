import time

def usingWhile():
    i = 0
    while i<50000:
        i += 1
        print(i)
        
def usingFor():
    for i in range(50000):
        print(i)
       
time.sleep(5)
#This all will print after 5 second   
init = time.time()
usingFor()
t1 = time.time() - init
init = time.time()
usingWhile()
print(time.time() - init)
print(t1)

#For printing our time we can write
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)