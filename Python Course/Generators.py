#Generators in python are special type of function that allow you to create an iterable sequence o value.

def my_generator():
    for i in range(5):
        yield i
        
gen = my_generator()

#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))

for j in gen:
    print(j)