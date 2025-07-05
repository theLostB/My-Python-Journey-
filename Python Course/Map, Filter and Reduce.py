from functools import reduce 
# MAP

#def cube(x):
#    return x*x*x
#print(cube(2)) We can use this also

l = [82,8,2,91,10,7,9]
#nl = []
#for item in l:
#    nl.append(cube(item)) Map is shortcut for this all
nl = list(map(lambda x: x*x*x, l))
print(nl)

# FILTER

def filter_function(a):
    return a>10
    
newl = list(filter(filter_function, l))
print(newl)

# REDUCE
def mysum(x,y):
    return x+y

newnewl = reduce(mysum, l)
#Calculate sum using reduce function 
print(newnewl)